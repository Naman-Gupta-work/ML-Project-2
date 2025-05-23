import sys
import logging
from networksecurity.logging import logger



def error_message_detail(error,error_detail:sys):
    _,_,exc_tb= error_detail.exc_info()
    file_name=exc_tb.tb_frame.f_code.co_filename
    error_message=" Error occured at python script [{0}] at line [{1}] error message[{2}]".format(
        file_name,exc_tb.tb_lineno,str(error)
    )
    return error_message


class NetworkSecurityException(Exception):
    def __init__(self,error_message,error_detail:sys):
        super().__init__(error_message)
        self.error_message=error_message_detail(error_message,error_detail=error_detail)

    def __str__(self):
        return self.error_message
    

# if __name__=='__main__':
#     try:
#         logger.logging.info("Enter the try block")
#         a=1/0
#     except Exception as e:
#         raise NetworkSecurityException(e,sys)                            WORKING FINE 