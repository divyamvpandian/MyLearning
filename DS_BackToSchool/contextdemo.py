
class LoggingContextManager:
    def __enter__(self):
        return "You are with blc"

    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_type is None:
            print('LoggingContextManager.__exit__Normal Exit')
        else:
            print('LoggingContextManager.__exit__({} {} {})'.format(exc_type,exc_val,exc_tb))
        # return True


def main():
    try:
        with LoggingContextManager() as x:
            raise ValueError("Core Melts")
            print(x)
    except ValueError:
        print("dfwfwef")
        raise
if __name__ == '__main__':
    main()