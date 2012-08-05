import imaplib

from imapclient import IMAPClient

class mail():
    _mail=None
    _currentFolder=None
    
    @property
    def name(self):
        return self._name
    @name.setter
    def name(self, arg=None):
        self._name = arg
        
    @property
    def server(self):
        return self._server
    @server.setter
    def server(self, arg=None):
        self._server = arg
        
    @property
    def username(self):
        return self._username
    @username.setter
    def username(self, arg=None):
        self._username = arg
        
    @property
    def password(self):
        return self._password
    @password.setter
    def password(self, arg=None):
        self._password = arg
    
    @property
    def folders(self):
        _folders = []
        
        for flags, delimiter, name in self._mail.list_folders():
            _folders.append(name)
        
        return _folders
    
    @property
    def currentFolder(self):
        return self._currentFolder
    
    def select_folder(self, folderName):
        self._mail.select_folder(folder=folderName, readonly=False)
        self._currentFolder=folderName
        
    def close_folder(self, folderName):
        self._currentFolder=None
        
    @property
    def MessageCount(self):
        if self.currentFolder == None:
            pass
        else:
            return int(self._mail.folder_status(folder=self.currentFolder, what='MESSAGES')['MESSAGES'])
    
    @property
    def UnreadCount(self):
        if self.currentFolder == None:
            pass
        else:
            return int(self._mail.folder_status(folder=self.currentFolder, what='UNSEEN')['UNSEEN'])
        
    def logout(self):
        self._mail.logout()

    def __init__(self, name=None, server=None, username=None, password=None):
        self._name = name
        self._server = server
        self._username = username
        self._password = password

        self._mail=IMAPClient(host=self._server, ssl=True)
        self._mail.login(username=self._username, password=self._password)