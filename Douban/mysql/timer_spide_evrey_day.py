import datetime, os, platform, time

def run_Task():
    os_platform = platform.platform()
    if os_platform.startswith('Darwin'):
        print("this is mac")
        os.system("ls")
    elif os_platform.startswith('Window'):
        print('this is win')
        os.system('dir')


def timerFun(sched_Timer):
    flag = True
    while flag:
        now = datetime.datetime.now()
        if (sched_Timer - now).seconds == 0 & (sched_Timer - now).days == 0:
            run_Task()  
            time.sleep(1)
        elif (sched_Timer - now).days < 0:
            print("over")
            flag = False
            time.sleep(1) # wait pint() complete
        else:
            time.sleep(0.1)
            print(sched_Timer - now)
                

if __name__ == '__main__':
    sched_Timer = datetime.datetime(2018, 1, 11, 11, 02, 00)
    print("run start time is {0}".format(sched_Timer))
    timerFun(sched_Timer)