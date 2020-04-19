import sys
from .classmodule import example_class
from .funcmodule import example_function

def main():
    print('Entering main function')
    args = sys.argv[1:]
    print('Counting no of args :: {}'.format(len(args)))
    for arg in args:
        print('Passed argument :: {}'.format(arg))
    
    example_function('Hello World')
    example_object = example_class('aj-0x616a')
    example_object.say_name()

if __name__ == '__main__':
    main()
