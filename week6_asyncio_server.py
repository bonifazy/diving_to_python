import asyncio


HOST = '127.0.0.1'
PORT = '8888'


class MetricsServer(asyncio.Protocol):
    def connection_made(self, transport):  # connect asyncio.Protocol, overrides method from asyncio
        self.transport = transport
        sock = self.transport.get_extra_info('socket')
        sock.settimeout(1)

    def data_received(self, data):  # receive data from client, overrides from asyncio
        if data:
            resp = self.process_data(data.decode("utf8"))  # process client data
            self.transport.write(resp.encode('utf8'))  # send answer to client

    storage = dict()

    def process_data(self, data):
        if data.startswith('get'):
            return self.get_from_storage(data.split()[1])
        elif data.startswith('put'):
            return self.put_to_storage(data.split('\n')[0])
        else:
            return 'error\nwrong command\n\n'

    def put_to_storage(self, values_list):
        _, key, value, timestamp = values_list.split()
        if self.storage.get(key):
            if not (value, timestamp) in self.storage.get(key):
                self.storage[key].append((value, timestamp))  # write new data for existing key
        else:
            self.storage[key] = [(value, timestamp)]  # write new key
        return 'ok\n\n'

    def get_from_storage(self, key):
        data = 'ok\n\n'  # start pattern answer
        if key in self.storage.keys():
            for value in self.storage[key]:  # keys of client data
                data = data + f'{key} {str(value[0])} {str(value[1])}\n'
        if key == '*':
            for key_ in self.storage.keys():
                for value in self.storage[key_]:
                    data += f'{key_} {str(value[0])} {str(value[1])}\n'
        default = '{}'
        data += '\n'
        return data if data != 'ok\n\n' else default


def run_server(host, port):
    loop = asyncio.get_event_loop()
    coro = loop.create_server(MetricsServer, host, port)
    # then: MetricsServer.connection_made(self, transport)
    # then: MetricsServer.data_received(self, data)
    server = loop.run_until_complete(coro)
    try:
        loop.run_forever()
    except KeyboardInterrupt:
        pass
    server.close()
    loop.run_until_complete(server.wait_closed())
    loop.close()


if __name__ == '__main__':
    run_server(host, port)

# after run this, you maybe run wee5_client_TCP.py
