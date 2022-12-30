import sys,os

#creating a function that would give file name where error is,
# error line number and what error we are getting
def error_message_detail(error, error_detail: sys):

#here we can get the details of the error
    _, _, exc_tb = error_detail.exc_info()

#this gives the file name where error occured
    file_name = exc_tb.tb_frame.f_code.co_filename

#exc_tb.tb_lineno provides the line number of error
    error_message = "Error occurred python script name [{0}] line number [{1}] error message [{2}]".format(
        file_name, exc_tb.tb_lineno, str(error)
    )
    return error_message


#since we are creating customised exception class ,
#  we need to inherit the Exception class

class SensorException(Exception):

    def __init__(self,error_message, error_detail:sys):
        self.error_message = error_message_detail(
            error_message, error_detail=error_detail)

    def __str__(self):
        return self.error_message
