import subprocess

def nslookup_server(host):
    try:
        # Executa o comando nslookup no sistema operacional
        process = subprocess.Popen(['nslookup', host], stdout=subprocess.PIPE, stderr=subprocess.PIPE)

        # Aguarda até que o processo termine e captura a saída e o erro, se houver
        output, error = process.communicate()

        # Decodifica a saída e o erro, lidando com exceções caso ocorram
        output_str = output.decode('utf-8', errors='ignore').strip() if output else ""
        error_str = error.decode('utf-8', errors='ignore').strip() if error else ""

        # Verifica se houve erro durante o processo
        if error_str:
            print(f"Ocorreu um erro ao executar o nslookup para o servidor {host}: {error_str}")
        else:
            print(f"Endereço IP do servidor {host}:")
            print(output_str)
    except Exception as e:
        print(f"Ocorreu um erro: {e}")

# Solicitar ao usuário que insira o endereço IP ou URL do servidor
try:
    server_host = input("Insira o endereço IP ou URL do servidor para nslookup: ")
    nslookup_server(server_host)
except KeyboardInterrupt:
    print("\nOperação interrompida pelo usuário.")
except Exception as e:
    print(f"Ocorreu um erro: {e}")
 