
import time

finished_task = 0


def work_t(task):
    global finished_task

    print('\nWork timer is starting! ')
    t = 1*10  # for actual pomodoro timer change 1*10 to 25*60. 1*10 was only used for quick testing
    while t:
        mins = t // 60
        secs = t % 60
        timer = '{:02d}:{:02d}'.format(mins, secs)
        print(timer, end="\r")
        time.sleep(1)
        t -= 1
    print("\n Break Time! ")
    finished_task += 1
    print("Finished tasks =", finished_task)


def break_t():
    global finished_task

    if finished_task < 4:
        print("\nShort break starting!")
        t2 = 1*5  # for actual pomodoro timer use change 1*5 to 5*60. 1*5 was only used for quick testing
        while t2:
            mins = t2 // 60
            secs = t2 % 60
            timer = '{:02d}:{:02d}'.format(mins, secs)
            print(timer, end="\r")
            time.sleep(1)
            t2 -= 1
        print("\nShort break has ended! ")

    elif finished_task >= 4:
        print("\nLong break starting!")
        t2 = 1*10  # for actual pomodoro timer use change 1*10 to 15*60. 1*10 was only used for quick testing
        while t2:
            mins = t2 // 60
            secs = t2 % 60
            timer = '{:02d}:{:02d}'.format(mins, secs)
            print(timer, end="\r")
            time.sleep(1)
            t2 -= 1
        finished_task = 0
        print("\nLong Break has ended! ")


def main():
    continue_task = 'yes'
    break_start = 'yes'
    task = input('\n Pomodoro Timer! \nPress ENTER to start! ')

    while continue_task == 'yes':
        work_t(task)
        break_start = input("\nPress ENTER to start break  ")
        break_t()
        continue_task = input(
            "\nContinue task? (ENTER) yes or no: ")  # type yes or no
        print("\nTask has ended! \nFinished tasks = ", finished_task)


if __name__ == '__main__':
    main()
