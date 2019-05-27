import socket
import time
from week6_asyncio_server import HOST, PORT


class ClientError(Exception):
	pass


class ClientSocketError(ClientError):
	pass


class ClientProtocolError(ClientError):
	pass


class Client:
	def __init__(self, host, port, timeout=None):
		self.connection = socket.create_connection((host, port), timeout)  # connect to server
		if not self.connection:
			raise ClientSocketError

	def put(self, key, metric, timestamp=None):
		timestamp = timestamp or str(int(time.time()))  # if timestamp is not exist
		metric = float(metric)
		message = f"put {key} {metric} {timestamp}\n"
		try:
			self.connection.sendall(message.encode())  # send data to server
			data = self.connection.recv(50).decode()  # get data from server
			if not data:
				raise ClientError
			# task: Метод put не возвращает ничего в случае успешной отправки
		except socket.error:
			self.connection.close()
			raise ClientError  # task: # и выбрасывает исключение ClientError в случае неуспешной

	def get(self, key):
			message = f'get {key}\n'
			self.connection.send(message.encode())  # send data to server
			data = self.connection.recv(1024).decode()  # get data from server
			if key in data or key == '*':  # write key or all keys
				data = data.split('\n')
				len_data = len(data)
				data_metric = dict()
				if len_data > 2 and data[0] == 'ok' and data[len_data - 2] == '' and data[len_data - 1] == '':
					if len_data > 3:
						for i in range(2, len_data - 2):  # get all keys from data
							_key, _value, _timestamp = data[i].split()
							_timestamp = int(_timestamp)
							_value = float(_value)
							if key == _key or key == "*":
								if data_metric.get(_key):
									data_metric[_key].append((_timestamp, _value))
								else:
									data_metric[_key] = [(_timestamp, _value)]
				return data_metric
			else:
				if data == "ok\n\n":
					print('{}')
				else:
					raise ClientError


def _main():
	# check test
	client = Client(HOST, PORT, timeout=5)
	client.put("test", 0.5, timestamp=1)
	client.put("test", 2.0, timestamp=2)
	client.put("test", 0.5, timestamp=3)
	client.put("load", 3, timestamp=4)
	client.put("load", 4, timestamp=5)
	print(client.get("*"))


def _main2():
	# check test #2
	client = Client(HOST, PORT, timeout=15)
	client.put("palm.cpu", 0.5, timestamp=1150864247)
	client.put("palm.cpu", 2.0, timestamp=1150864248)
	client.put("palm.cpu", 0.5, timestamp=1150864248)
	client.put("eardrum.cpu", 3, timestamp=1150864250)
	client.put("eardrum.cpu", 4, timestamp=1150864251)
	client.put("eardrum.memory", 4200000)
	print(client.get("palm.cpu"))
	print(client.get("eardrum.memory"))
	print(client.get('*'))


if __name__ == "__main__":

	# _main()
	_main2()

"""
_main() 
>>	{'test': [(1, 0.5), (2, 2.0), (3, 0.5)], 'load': [(4, 3.0), (5, 4.0)]}

_main2()
>> {'palm.cpu': [(1150864247, 0.5), (1150864248, 2.0), (1150864248, 0.5)]}
>> {'eardrum.memory': [(1558950420, 4200000.0)]}
>> {'palm.cpu': [(1150864247, 0.5), (1150864248, 2.0), (1150864248, 0.5)], 'eardrum.cpu': [(1150864250, 3.0)
>> , (1150864251, 4.0)], 'eardrum.memory': [(1558950420, 4200000.0)]}

"""