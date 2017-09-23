import sys

def main():

    errorFlag=True
    while errorFlag ==True: #loops while a error occurs

        firstNumber=input('enter a number ')
        secondNumber=input('enter a number ')


        try:

            finalTotal=str(float(firstNumber)/float(secondNumber))
            print('The ans is :'+finalTotal)
            errorFlag=False

        except ZeroDivisionError:
              print('The answer is infinite')
              sys.exit() # exit program when this error occurs
        except ValueError:
              print('Division is only done using numeric values, please enterr a numeric value')
              errorFlag=True #using boolean as a pointer

        except:
            error=sys.exc_info()[0]
            print('Error occured!!!')
            print(error)
        finally: # finally will always run (in any situation)   
            print('I will always run')

        if not errorFlag:
            print ('This message will be displayed only if no error occured')
    return
main()