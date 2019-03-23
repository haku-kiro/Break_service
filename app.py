import webbrowser
import time
import ctypes
from service import SMWinservice

# Just keeping track of the breaks :shrug:


def break_process():
    pass


class PythonTakeBreakService(SMWinservice):
    _svc_name_ = "TakeBreakPy"
    _svc_display_name_ = "Take Break Py"
    _svc_description_ = "Windows service to monitor 30 minute intervals"

    def start(self):
        self.isrunning = True

    def stop(self):
        self.isrunning = False

    def main(self):
        if self.isrunning:
            x = 0
            MessageBox = ctypes.windll.user32.MessageBoxW

            # print("The program has started, it started at: " + time.ctime())
            while(self.isrunning):
                # Run every 30 minutes
                time.sleep(60 * 30)
                # website just for this
                webbrowser.open("https://takeabreak.azurewebsites.net/")

                MessageBox(
                    None,
                    f"Stretch your legs mah dude, current time is: {time.ctime()}",
                    f"There have been {x} breaks...",
                    0
                )
                x += 1


if __name__ == "__main__":
    PythonTakeBreakService.parse_command_line()
