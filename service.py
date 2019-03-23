import time
import socket
import win32serviceutil
import servicemanager
import win32event
import win32service

"""
This base class is used to create windows services
Ensure that you overwrite the required methods:
https://pbaumgarten.com/python/windows-service-howto.pdf
"""
class SMWinservice(win32serviceutil.ServiceFramework):
    """
    Base class to create winservice in python 
    """
    _svc_name_ = 'pythonService'
    _svc_display_name_ = 'Python Service'
    _svc_description_ = 'Python service description'

    @classmethod
    def parse_command_line(cls):
        """
        Class method to parse the command line
        """
        win32serviceutil.HandleCommandLine(cls)

    def __init__(self, args):
        """
        ctor of the windows service
        """
        win32serviceutil.ServiceFramework.__init__(self, args)
        self.hWaitStop = win32event.CreateEvent(None, 0, 0, None)
        socket.setdefaulttimeout(60)

    def SvcStop(self):
        """
        This method is called when the service is asked to stop
        """
        self.stop()
        self.ReportServiceStatus(win32service.SERVICE_STOP_PENDING)
        win32event.SetEvent(self.hWaitStop)

    def SvcDoRun(self):
        """
        This method is called when the service is asked to start
        """
        self.start()
        servicemanager.LogMsg(servicemanager.EVENTLOG_INFORMATION_TYPE,
                              servicemanager.PYS_SERVICE_STARTED,
                              (self._svc_name_, ''))
        self.main()

    def start(self):
        """
        Override to add logic before the start
        """
        pass

    def stop(self):
        """
        Override to add logic to before the stop
        """
        pass

    def main(self):
        """
        Main method, override this to add logic to your service
        """
        pass


if __name__ == "__main__":
    SMWinservice.parse_command_line()
