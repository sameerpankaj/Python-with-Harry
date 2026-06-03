#finally always runs

def main():
    try:
        a = int(input('Hey, Enter a number:'))
        print(a)

    except Exception as e: #except is same as catch in c or c++ or java
        print(e)

    finally:
        print('I am inside finally')

main()