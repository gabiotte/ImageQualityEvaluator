import os
import argparse
import csv

def remove(main_dir):
    for camera in os.listdir(main_dir):
        camera_path = os.path.join(main_dir, camera)

        if not os.path.isdir(camera_path) or camera.startswith("."):
            continue

        file_path = os.path.join(camera_path, "comparacao.csv")
        try:
            if os.path.isfile(file_path):
                os.remove(file_path)
                print(f"[✔] Removido: {file_path}")
            else:
                print(f"[!] Não encontrado: {file_path}")
        except Exception as e:
            print(f"[✘] Erro ao remover {file_path}: {e}")


def atualizar_cabecalho_csvs(diretorio_raiz):
    for dir_caminho, _, arquivos in os.walk(diretorio_raiz):
        if "tempo.csv" in arquivos:
            caminho_csv = os.path.join(dir_caminho, "tempo.csv")

            try:
                with open(caminho_csv, mode='r', newline='', encoding='utf-8') as f:
                    leitor = csv.reader(f)
                    linhas = list(leitor)

                cabecalho = linhas[0]
                if "Foto" in cabecalho:
                    indice = cabecalho.index("Foto")
                    cabecalho[indice] = "Imagem"

                    with open(caminho_csv, mode='w', newline='', encoding='utf-8') as f:
                        escritor = csv.writer(f)
                        escritor.writerows(linhas)
                    
                    print(f"[✔] Cabeçalho atualizado em: {caminho_csv}")
                else:
                    print(f"[!] Cabeçalho já está correto ou não contém 'Foto': {caminho_csv}")
            except Exception as e:
                print(f"[✘] Erro ao processar {caminho_csv}: {e}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Remove arquivos comparacao.csv ou atualiza cabeçalhos de tempo.csv")
    parser.add_argument("--diretorio", type=str, required=True, help="Diretório principal do projeto")
    parser.add_argument("--action", type=str, required=True, choices=["remove", "header"],
                        help="Ação a ser executada: 'remove' para excluir comparacao.csv, 'header' para atualizar o cabeçalho de tempo.csv")
    args = parser.parse_args()

    if args.action == "remove":
        remove(args.diretorio)
    elif args.action == "header":
        atualizar_cabecalho_csvs(args.diretorio)