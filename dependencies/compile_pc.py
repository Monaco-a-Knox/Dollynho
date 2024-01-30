from subprocess import run
from distutils.dir_util import copy_tree
import os, shutil, shlex
from sys import exit

# Nome da pasta onde os arquivos do patch serão enviados
output_folder = "[KT]Umineko.Dolly.PT-BR"

def prepareFiles():

    try:
        os.mkdir(output_folder)
    except:
        pass

    # Lista de ARQUIVOS (não pastas!) que são necessários para montar o patch 
    # (atenção: não incluir o nscript.dat ou arc.nsa que são compilados por esse script posteriormente)
    dependencies = [
        "onscripter-en.exe",
        "default.ttf",
        "0.txt"
    ]

    for files in dependencies:
        try:
            shutil.copy(f"[KT] Umineko Dolly/{files}", output_folder)
        except:
            print(f"Couldn't copy {files}")
            pass
    
    # copia a pasta web. Para copiar outras pastas, reuse este bloco de código
    # tradução do que está sob o TRY: copy_tree('pasta que você quer copiar', f'{output_folder}/para onde ela vai' << pode ser para dentro dela mesmo, como no caso abaixo)
    folders = [
        'system',
        'e1'
    ]
    
    for folders in folders:
        try:
            copy_tree(f"[KT] Umineko Dolly/{folders}", f"{output_folder}/{folders}")
        except FileNotFoundError:
            print("Couldn't find the system folder. Skipping.")
            pass
         
    # este bloco de código deleta a pasta bmp/background
    # try:
    #     shutil.rmtree('bmp/background')
    # except FileNotFoundError:
    #     print("Couldn't find the backgrounds folder. Skipping.")
    
    # este bloco copia a pasta legacy_extra/bmp para dentro da pasta bmp
    # try:
    #     copy_tree('legacy_extra/bmp', f'bmp')
    # except FileNotFoundError:
    #     print("Couldn't find the legacy_extra folder. Skipping.")

def compile():
    # try:
    #     os.remove('nscript.dat')
    # except FileNotFoundError:
    #     pass
    
    # caso precise modificar o caminho ou o nome do script, editar ele abaixo
    # IMPORTANTE: o nome do arquivo, caso modificado, precisa também ser modificado nos scripts do Github Actions, sob a pasta .github/workflows neste repositório
    #nscript_args = '-o pscript.dat SCRIPT/0.txt'
    # shutil.copy('SCRIPTS/PC/hane_pc.txt', '0.txt')
    #run(['dependencies/nscmake.exe'] + shlex.split(nscript_args))
    #shutil.move('pscript.dat', output_folder)

    #nsa_args = 'arc.nsa bmp'
    #run(['dependencies/nsamake.exe'] + shlex.split(nsa_args))
    #shutil.move('arc.nsa', output_folder)

    # nome do arquivo de destino
    # IMPORTANTE: o nome do arquivo, caso modificado, precisa também ser modificado nos scripts do Github Actions, sob a pasta .github/workflows neste repositório
    zip_args = f"[KT]Umineko.Dolly.PT-BR.7z {output_folder}"
    run([r'dependencies/7za.exe', 'a'] + shlex.split(zip_args))

def cleanup():
    shutil.rmtree(output_folder)

prepareFiles()
compile()
cleanup()