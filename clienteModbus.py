from pyModbusTCP.client import ModbusClient
from time import sleep


class ClienteMODBUS():
    """
    Classe Cliente MODBUS
    """
    def __init__(self,server_ip,porta,device_id=1,scan_time=0.1,valor=0):
        """
        Construtor
        """
        self._scan_time = scan_time
        self._server_ip = server_ip
        self._device_id = device_id
        self._port = porta
        self._cliente = ModbusClient(host=server_ip, port=porta, unit_id=device_id)

    def atendimento(self):
        """
        Método para atendimento do usuário
        """
        try:
            self._cliente.open()
            print('\n\033[33m --> Cliente Modbus conectado..\033[m\n')

        except Exception as e:
            print('\033[31mERRO: ', e.args, '\033[m')

        try:
            atendimento = True
            while atendimento:
                print('-' * 100)
                print('\033[34mCliente Modbus TCP\033[m'.center(100))
                print('-' * 100)
                sel = input("Qual serviço? \n1- Leitura \n2- Escrita \n3- Configuração \n4- Sair \nNº Serviço: ")
                if sel == '1':
                    print('\nQual tipo de dado deseja ler?')
                    print("1- Coil Status \n2- Input Status \n3- Holding Register \n4- Input Register")
                    while True:
                        tipo = int(input("Type: "))
                        if tipo > 4:
                            print('\033[31mDigite um tipo válido..\033[m')
                            sleep(0.5)
                        else:
                            break

                    if tipo == 3 or tipo == 4: 
                        while True:
                            print('\nQual tipo de display?')
                            val = int(input("1- Decimal \n2- Floating Point \n3- Float Swapped \nDisplay: "))
                            if val > 3:
                                print('\033[31mDigite um tipo válido..\033[m')
                                sleep(0.5)
                            else:
                                break
                        if val == 1: #valores decimais
                            addr = int(input(f'\nAddress: '))
                            leng = int(input(f'Length: '))
                            nvezes = input('Quantidade de leituras: ')
                            print('\nComeçando leitura Decimal..\n')
                            sleep(0.5)
                            try:
                                for i in range(0,int(nvezes)):
                                    print(f'\033[33mLeitura {i+1}:\033[m', end='')
                                    print(self.lerDado(int(tipo),int(addr),leng))
                                    sleep(self._scan_time)
                                print('\nValores lidos com sucesso!!\n')
                                sleep(0.5)
                            except Exception as e:
                                print('\033[31mERRO: ', e.args, '\033[m')
                                try:
                                    sleep(0.5)
                                    print('\033[33m\nTentando novamente..\033[m')
                                    if not self._cliente.is_open():
                                        self._cliente.open()
                                    sleep(0.5)
                                    for i in range(0, int(nvezes)):
                                        print(f'\033[33mLeitura {i + 1}:\033[m', end='')
                                        print(self.lerDado(int(tipo), int(addr), leng))
                                        sleep(self._scan_time)
                                    print('\nValores lidos com sucesso!!\n')
                                    sleep(0.5)
                                except Exception as e:
                                    print('\033[31mERRO: ', e.args, '\033[m')
                                    print('\nO Cliente não conseguiu receber uma resposta.. \nVoltando ao menu..\n\n')
                                    sleep(1.5)

                        elif val == 2: #valores FLOAT
                            addr = input(f'\nAddress: ')
                            leng = int(input(f'Length: '))
                            nvezes = input('Quantidade de leituras: ')
                            print('\nComeçando leitura FLOAT..\n')
                            sleep(0.5)
                            try:
                                for i in range(0, int(nvezes)):
                                    print(f'\033[33mLeitura {i + 1}:\033[m', end='')
                                    print(self.lerDadoFloat(int(tipo), int(addr), leng))
                                    sleep(self._scan_time)
                                print('\nValores lidos com sucesso!!\n')
                                sleep(0.5)
                            except Exception as e:
                                print('\033[31mERRO: ', e.args, '\033[m\n')
                                print('O Cliente não conseguiu receber uma resposta.. \nVoltando ao menu..\n\n')
                                sleep(1.5)

                        elif val == 3: #valores FLOAT SWAPPED 
                            addr = input(f'\nAddress: ')
                            leng = int(input(f'Length: '))
                            nvezes = input('Quantidade de leituras: ')
                            print('\nComeçando leitura FLOAT SWAPPED..\n')
                            sleep(0.5)
                            try:
                                for i in range(0, int(nvezes)):
                                    print(f'\033[33mLeitura {i + 1}:\033[m', end='')
                                    print(self.lerDadoFloatSwapped(int(tipo), int(addr), leng))
                                    sleep(self._scan_time)
                                print('\nValores lidos com sucesso!!\n')
                                sleep(0.5)
                            except Exception as e:
                                print('\033[31mERRO: ', e.args, '\033[m\n')
                                print('O Cliente não conseguiu receber uma resposta.. \nVoltando ao menu..\n\n')
                                sleep(1.5)

                        else:
                            print('\033[31mSeleção inválida..\033[m\n')
                            sleep(0.7)

                    else:
                        addr = input(f'\nAddress: ')
                        leng = int(input(f'Length: '))
                        nvezes = input('Quantidade de leituras: ')
                        print('\nComeçando leitura..\n')
                        sleep(0.5)
                        try:
                            for i in range(0, int(nvezes)):
                                print(f'\033[33mLeitura {i + 1}:\033[m', end='')
                                print(self.lerDado(int(tipo), int(addr), leng))
                                sleep(self._scan_time)
                            print('\nValores lidos com sucesso!!\n')
                            sleep(0.5)
                        except Exception as e:
                            print('\033[31mERRO: ', e.args, '\033[m\n')
                            print('O Cliente não conseguiu receber uma resposta.. \nVoltando ao menu..\n\n')
                            sleep(1.5)

                elif sel == '2':
                    print('\nQual tipo de dado deseja escrever? \n1- Coil Status \n2- Holding Register')
                    while True:
                        tipo = int(input("Tipo: "))
                        if str(tipo) not in '1' and str(tipo) not in '2':
                            print('\033[31mDigite um tipo válido..\033[m')
                            sleep(0.5)
                        else:
                            break
                    addr = input(f'Digite o endereço: ')
                    valor = int(input(f'Digite o valor que deseja escrever: '))
                    try:
                        print('\nEscrevendo..')
                        sleep(0.5)
                        self.escreveDado(int(tipo), int(addr), valor)
                    except Exception as e:
                        print('\033[31mERRO: ', e.args, '\033[m')
                        print('\nO Cliente não conseguiu escrever.. \nVoltando ao menu..\n\n')
                        sleep(1.5)

                elif sel == '3':
                    print('')
                    print('-' * 100)
                    print('Configurações de Leitura'.center(100))
                    print(f'\n\033[32m->\033[m Configuração atual: - IP Addrs: \033[35m{self._server_ip}\033[m - TCP Port: \033[35m{self._port}\033[m - Device ID: \033[35m{self._device_id}\033[m - Scan_Time: \033[35m{self._scan_time}\033[ms')
                    print('\nQual tipo de configuração deseja fazer? \n1- Endereço IP \n2- Porta TCP \n3- Device ID \n4- ScanTime \n5- Voltar')
                    config = int(input("Configuração: "))
                    if config == 1:
                        ipserv = str(input(' Novo endereço IP: '))
                        try:
                            self._cliente.close()
                            self._server_ip = ipserv
                            self._cliente = ModbusClient(host=self._server_ip)
                            self._cliente.open()
                            print(f'\nServer IP alterado para {ipserv} com sucesso!!\n')
                            sleep(0.5)
                        except Exception as e:
                            print('\033[31mERRO: ', e.args, '\033[m')
                            print('\nNão foi possível alterar o endereço IP.. \nVoltando ao menu..\n\n')
                            sleep(0.5)
                    elif config == 2:
                        porttcp = input(' Nova porta TCP: ')
                        try:
                            self._cliente.close()
                            self._port = int(porttcp)
                            self._cliente = ModbusClient(port=self._port)
                            self._cliente.open()
                            print(f'\nTCP port alterado para {porttcp} com sucesso!!\n')
                            sleep(0.5)
                        except Exception as e:
                            print('\033[31mERRO: ', e.args, '\033[m')
                            print('\nNão foi possível alterar a porta.. \nVoltando ao menu..\n\n')
                            sleep(0.5)
                    elif config == 3:
                        while True:
                            iddevice = input(' Novo device ID: ')
                            if 0 <= int(iddevice) < 256:
                                break
                            else:
                                print('\033[31mDevice ID deve ser um número inteiro entre 0 e 256.\033[m', end='')
                                sleep(0.5)
                        try:
                            self._cliente.close()
                            self._device_id = int(iddevice)
                            self._cliente = ModbusClient(unit_id=self._device_id)
                            self._cliente.open()
                            print(f'\nDevice ID alterado para {iddevice} com sucesso!!\n')
                            sleep(0.5)
                        except Exception as e:
                            print('\033[31mERRO: ', e.args, '\033[m')
                            print('\nNão foi possível alterar o ID do device.. \nVoltando ao menu..\n\n')
                            sleep(0.5)
                    elif config == 4:
                        scant = input(' Novo tempo de varredura [s]: ')
                        try:    
                            self._scan_time = float(scant)
                            print(f'\nScan_time alterado para {scant}s com sucesso!!\n')
                        except Exception as e:
                            print('\033[31mERRO: ', e.args, '\033[m')
                            print('\nNão foi possível alterar o tempo de varredura.. \nVoltando ao menu..\n\n')
                            sleep(0.5)
                    elif config == 5:
                        print('\nVoltando ao menu inicial..\n')
                        sleep(0.5)
                    else:
                        print('\033[31mSeleção inválida..\033[m\n')
                        sleep(0.7)
                
                elif sel == '4':
                    sleep(0.2)
                    print('\n\033[32mFechando sistema..\033[m')
                    sleep(0.5)
                    self._cliente.close()
                    atendimento = False

                else:
                    print('\033[31mSeleção inválida..\033[m\n')
                    sleep(0.7)
        except Exception as e:
            print('\033[31mERRO: ', e.args, '\033[m')


    def lerDado(self, tipo, addr, leng=1):
        """
        Método para leitura MODBUS
        """
        if tipo == 1:
            co = self._cliente.read_coils(addr - 1, leng)
            ic = 0
            while ic <= leng:
                if ic == leng:
                    break
                else:
                    value = co[0 + ic]
                    ic += 1
                    # print(value)
                    if value == True:
                        value = 1
                    else:
                        value = 0
            return co

        elif tipo == 2:
            di = self._cliente.read_discrete_inputs(addr - 1, leng)
            idi = 0
            while idi <= leng:
                if idi == leng:
                    break
                else:
                    value = di[0 + idi]
                    idi += 1
            return di

        elif tipo == 3:
            hr = self._cliente.read_holding_registers(addr - 1, leng)
            ihr = 0
            while ihr <= leng:
                if ihr == leng:
                    break
                else:
                    value = hr[0+ihr]
                    ihr += 1
            return hr

        elif tipo == 4:
            ir = self._cliente.read_input_registers(addr - 1, leng)
            iir = 0
            while iir <= leng:
                if iir == leng:
                    break
                else:
                    value = ir[0 + iir]
                    iir += 1
            return ir

        else:
            print('Tipo de leitura inválido..')


    def lerDadoFloat(self, tipo, addr, leng):
        """
        Método para leitura FLOAT MODBUS
        """
        i = 0
        g = 0
        e1 = []
        listfloat = []
        while i < leng:
            if tipo == 3:
                i1 = self._cliente.read_holding_registers(addr - 1 + g, 2)
            elif tipo == 4:
                i1 = self._cliente.read_input_registers(addr - 1 + g, 2)
            else:
                print('Tipo inválido..')
            for x in i1:
                x = bin(x).lstrip("0b")
                e1.insert(0 + g, x)
            i += 1
            g += 2
        e = 0
        while e <= leng:
            e2 = ''
            for x in e1:
                e2 = str(f'{e2}{x.rjust(16, "0")} ')
            e += 1
        b2 = str(f'{e2}')
        e3 = b2.split()
        y = 0
        while y < len(e3):
            ieee = f'{e3[0+y]}{e3[1+y]}'
            sign = int(ieee[0])
            expo = str(ieee[1:9])
            expodec = 0
            expopot = 7
            for i in range(8):
                expodec = expodec + (int(expo[i]) * (2**expopot))
                expopot -= 1
            mant = str(ieee[9:])
            mantdec = 0
            mantpot = -1
            for i in range(23):
                mantdec = mantdec + (int(mant[i]) * (2 ** mantpot))
                mantpot -= 1
            value = ((-1)**sign)*(1+mantdec)*2**(expodec-127)
            listfloat.append(round(value, 3))
            y += 2
        return listfloat


    def lerDadoFloatSwapped(self, tipo, addr, leng):
        """
        Método para leitura FLOAT SWAPPED MODBUS
        """
        i = 0
        g = 0
        e1 = []
        listfloatsp = []
        while i < leng:
            if tipo == 3:
                i1 = self._cliente.read_holding_registers(addr - 1 + g, 2)
            elif tipo == 4:
                i1 = self._cliente.read_input_registers(addr - 1 + g, 2)
            else:
                print('Tipo inválido..')
            i2 = i1[::-1]
            for x in i2:
                x = bin(x).lstrip("0b")
                e1.insert(0 + g, x)
            i += 1
            g += 2
        e = 0
        while e <= leng:
            e2 = ''
            for x in e1:
                e2 = str(f'{e2}{x.rjust(16, "0")} ')
            e += 1
        b2 = str(f'{e2}')
        e3 = b2.split()
        y = 0
        while y < len(e3):
            ieee = f'{e3[0+y]}{e3[1+y]}'
            sign = int(ieee[0])
            expo = str(ieee[1:9])
            expodec = 0
            expopot = 7
            for i in range(8):
                expodec = expodec + (int(expo[i]) * (2**expopot))
                expopot -= 1
            mant = str(ieee[9:])
            mantdec = 0
            mantpot = -1
            for i in range(23):
                mantdec = mantdec + (int(mant[i]) * (2 ** mantpot))
                mantpot -= 1
            value = ((-1)**sign)*(1+mantdec)*2**(expodec-127)
            listfloatsp.append(round(value, 3))
            y += 2
        return listfloatsp


    def escreveDado(self, tipo, addr, valor):
        """
        Método para escrita MODBUS
        """
        try:
            if tipo == 1:
                print(f'\033[33mValor {valor} escrito no endereço {addr}\033[m\n')
                return self._cliente.write_single_coil(addr - 1, valor)
            elif tipo == 2:
                print(f'\033[33mValor {valor} escrito no endereço {addr}\033[m\n')
                return self._cliente.write_single_register(addr - 1, valor)
            else:
                print('Tipo de escrita inválido..\n')

        except Exception as e:
            print('\033[31mERRO: ', e.args, '\033[m')