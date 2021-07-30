# -*-coding: utf-8-*-

# 최신 python3 문법을 사용하여, python3를 이용해 실행시켜야 합니다.

import argparse
import operator
import os
import subprocess


class GitWorker():
    def __init__(self):
        self.work = ''
        self.remoteUrl = ''
        self.app = ''
        self.showLogo()
        self.parser()
        self.checkArgs()
        self.checkContinue()

    def showLogo(self):
        print('\n@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@')
        print('@@@@@@@@@@@@@####@@@@@@@@@@@@@@@####@@@@@@@@@@@@@@')
        print('@@@@@@@@@@@@@######@@@######@@######@@@@@@@@@@@@@@')
        print('@@@@@@@@@@@@@#######################@@@@@@@@@@@@@@')
        print('@@@@@@@@@@@@@#######################@@@@@@@@@@@@@@')
        print('@@@@@@@@@@@@@#######################@@@@@@@@@@@@@@       할 수 있는 작업의 목록 입니다.')
        print('@@@@@@@@@@@@@########################@@@@@@@@@@@@@       원격 저장소 리모트 url 등록하기 : work를 addUrl로 설정하세요')
        print('@@@@@@@@@@@@#########################@@@@@@@@@@@@@       원격 저장소 리모트 url 삭제하기 : work를 rmUrl로 설정하세요')
        print('@@@@@@@@@@@@##########################@@@@@@@@@@@@       서브 모듈 초기화 : work를 initModule로 설정하세요')
        print('@@@@@@@@@@@###########################@@@@@@@@@@@@       서브 모듈 등록 : work를 addModule로 설정하세요')
        print('@@@@@@@@@@@############################@@@@@@@@@@@       서브 모듈 삭제 : work를 rmModule로 설정하세요')
        print('@@@@@@@@@@@######=------;:------#######@@@@@@@@@@@       모든 서브 모듈 백업 : work를 backupModule로 설정하세요')
        print('@@@@@@@@@@@#####                 -#####@@@@@@@@@@@')
        print('@@@@@@@@@@@####                   ;####@@@@@@@@@@@')
        print('@@@@@@@@@@@###$    ~          ~    ####@@@@@@@@@@@')
        print('@@@@@@@@@@@###.    ~~        ~,~   ####@@@@@@@@@@@')
        print('@@@@@@@@@@@###.   ~~~        ~~~   ###@@@@@@@@@@@@')
        print('@@@####@@@@###;   ~~,        ,~~   ###@@@@#####@@@')
        print('@@@@@@@########         ,          ########@@@@@@@')
        print('@@##@@@@@@@@@##.                  *##@@@@@@@@@##@@')
        print('@@@@@@@@@@@@@@##.        .       .##@@@@@@@@@@@@@@')
        print('@@@@@@@@@@@@@@@###,             ###@@@@@@@@@@@@@@@')
        print('@@@@@@@@@@##@@@@@################@@@@@@@@@@@@@@@@@')
        print('@@@@@@@@@@##.@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@')
        print('@@@@@@@@@@ @#!@@@@@@#########@@@@@@@@@@@@@@@@@@@@@')
        print('@@@@@@@@@@@@###@@@@###########@@@@@@@@@@@@@@@@@@@@')
        print('@@@@@@@@@@@@@##=$##############@@@@@@@@@@@@@@@@@@@')
        print('@@@@@@@@@@@@@@#################@@@@@@@@@@@@@@@@@@@')
        print('@@@@@@@@@@@@@@@@###############@@@@@@@@@@@@@@@@@@@')
        print('@@@@@@@@@@@@@@@@@@@############@@@@@@@@@@@@@@@@@@@')
        print('@@@@@@@@@@@@@@@@@@@############@@@@@@@@@@@@@@@@@@@')
        print('@@@@@@@@@@@@@@@@@@@##*########=@@@@@@@@@@@@@@@@@@@')
        print('@@@@@@@@@@@@@@@    ##*########!    @@@@@@@@@@@@@@@')
        print('@@@@@@@@@@@@@      ##:######$##      @@@@@@@@@@@@@')
        print('@@@@@@@@@@@@      ### ###### ##$      @@@@@@@@@@@@')
        print('@@@@@@@@@@@@      ,.. ##.*## ..,      @@@@@@@@@@@@')
        print('@@@@@@@@@@@@       ..##;  $#$..       @@@@@@@@@@@@')
        print('@@@@@@@@@@@@@      ..... ......      @@@@@@@@@@@@@')
        print('@@@@@@@@@@@@@@@    ............     @@@@@@@@@@@@@@')
        print('@@@@@@@@@@@@@@@@@@ ............ .@@@@@@@@@@@@@@@@@\n')

    def parser(self):
        parser = argparse.ArgumentParser(
            description='Parser')
        parser.add_argument('--work', dest='work',
                            required=True, help='진행할 작업의 이름')
        parser.add_argument('--url', dest='url',
                            help='원격 저장소 url')
        parser.add_argument('--app', dest='app',
                            help='어플리케이션 이름')

        args = parser.parse_args()
        self.work = args.work
        self.remoteUrl = args.url
        self.app = args.app

    def checkArgs(self):
        print("\n*********************************************\n")
        print("입력된 인자들 목록입니다. 제대로 입력되었는지 확인해주세요!\n")
        print(f"work : {self.work}")
        print(f"url : {self.remoteUrl}")
        print(f"app : {self.app}")
        print("\n*********************************************\n")

    def checkContinue(self):
        while(True):
            option = input("계속 진행하시겠습니까? [y/n] >> ")
            if (operator.eq(option, 'y')):
                break
            elif(operator.eq(option, 'n')):
                exit()
            else:
                print('비유효 옵션 입니다. y나 n 중 하나를 다시 입력해주세요\n')
                continue

    def initModule(self):
        os.system('git submodule update --init --recursive')

    def registUrl(self):
        os.system(f'git remote add origin {self.remoteUrl}')

    def removeUrl(self):
        os.system(f'git remote remove origin')

    def registModule(self):
        os.system(f' git submodule add {self.remoteUrl}')

    def removeModule(self):
        os.system(f'git submodule deinit -f {self.app}')
        os.system(f'rm -rf .git/modules/{self.app}')
        os.system(f'git rm -f {self.app}')

    def backupModule(self):
        path = os.getcwd()
        subdirs = [subdir.name for subdir in os.scandir(
            path) if not subdir.name.startswith('.')]
        subdirs = [subdir for subdir in subdirs if os.path.isdir(
            os.path.join(path, subdir))]
        total_works = len(subdirs)
        count = 0
        for subdir in subdirs:
            count += 1
            print(f'진행도 : {count} / {total_works}')
            print(f'{subdir} 디렉토리의 백업을 진행합니다.')
            option = input('계속 진행하시겠습니까? [y/n] >>> ')
            if(operator.eq(option, 'n')):
                continue
            subdir_path = os.path.join(path, subdir)
            os.chdir(subdir_path)
            origin_url = subprocess.getoutput(
                "git remote get-url --push origin")
            if not "Itsbeenalongday@" in origin_url:
                print("origin remote push 권한 부여")
                origin_url = origin_url[:8] + \
                    "Itsbeenalongday@" + origin_url[8:]
                os.system(f"git remote set-url origin {origin_url}")
            if os.path.exists('git.sh'):
                os.system('sh git.sh')
            else:
                print(f"{subdir}디렉토리에 git.sh가 존재하지 않습니다. 상위 디렉토리에서 복사합니다.")
                os.system('cp ../git.sh .')
                os.system('sh git.sh')
            os.chdir(path)

    def load(self):
        if(operator.eq(self.work, 'addUrl')):
            self.registUrl()
        elif(operator.eq(self.work, 'rmUrl')):
            self.removeUrl()
        elif(operator.eq(self.work, 'initModule')):
            self.initModule()
        elif(operator.eq(self.work, 'addModule')):
            self.registModule()
        elif(operator.eq(self.work, 'rmModule')):
            self.removeModule()
        elif(operator.eq(self.work, 'backupModule')):
            self.backupModule()


if __name__ == "__main__":
    worker = GitWorker()
    worker.load()
