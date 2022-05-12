import ftplib
from re import S
import config as co
class FileUpload:
    def __init__(self) -> None:
        pass

    def UploadFunc(self) -> None:
        session = ftplib.FTP()
        session.connect(co.ftpweb, co.port) # 두 번째 인자는 port number
        session.login(co.ftpid, co.ftppwd)   # FTP 서버에 접속
    
        mlist = open('./' + co.listFilename ,mode='rb')
        rank = open('./' + co.rankFilename ,mode='rb')
        tobe = open('./' + co.openFilename, mode='rb')
        
        session.encoding='utf-8'
        session.storbinary('STOR ' + '/html/' + co.listFilename, mlist)
        session.storbinary('STOR ' + '/html/' + co.rankFilename, rank)
        session.storbinary('STOR ' + '/html/' + co.openFilename, tobe)

        mlist.close()
        rank.close()
        tobe.close()
    
        session.quit()
        print('파일전송함')