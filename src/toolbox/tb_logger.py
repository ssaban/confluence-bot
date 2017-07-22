# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.

__author__ = "sarel"
__date__ = "$Mar 14, 2015 11:39:57 AM$"

if __name__ == "__main__":
    print "running from %s"%__name__
    
    
import logging

class tb_logger:
    '''logger class is primal ancestor any class with logging attribute, 
    its based on logging package
    
    debugLevel accept default levels:
    logging.CRITICAL
    logging.ERROR
    logging.WARNING
    logging.INFO
    logging.DEBUG
    
    To write a log message in one of these five levels, use the following functions:

    self.logger.critical('Critical msg.')
    self.logger.error('Error msg')
    self.logger.warning('Warning msg')
    self.logger.info('Info msg')
    self.logger.debug('Debug msg')

    '''
    
    def __init__(self,debugLevel = logging.WARNING):
            
        #define name of logger (child of root logger)
        self.name = self.__class__.__name__
        
        #file logger 
        #file handler to use to output logger data (in addition to STDOUT
        # by default no file is used hence set handler to 0
        # note: currently each logger can have one file...
        self.loggerFileName = 0

        #activate the name logger, and set the debug level
        self.logger = logging.getLogger(self.name)
        self.logger.setLevel(debugLevel)

        #create console handler and set level to debug
        self.ch = logging.StreamHandler()
        self.ch.setLevel(debugLevel)

        #create formatter
        #formatter = logging.Formatter("[%(asctime)s] - [%(name)s] - [%(levelname)s] : %(message)s")
        self.formatter = logging.Formatter("[%(name)s] - [%(levelname)s] : %(message)s")
        
        #add formatter to consoul handler
        self.ch.setFormatter(self.formatter)
        #add consoul handler to logger for this class
        self.logger.addHandler(self.ch)
    
    
    def updateLoggerLevel(self,debugLevel):
        #self.name = self.__class__.__name__
        #self.logger = logging.getLogger(self.name)
        self.logger.setLevel(debugLevel)

        #create console handler and set level to debug
        #self.ch = logging.StreamHandler()
        self.ch.setLevel(debugLevel)
        
        
        
    def addFileLogger(self, logFileName):
        
        if self.loggerFileName:
            print "ERROR ------ logger file name already exist - METHOD DO NOTHING"
        else:
            self.loggerFileName = logFileName
            looger_fh = logging.FileHandler(logFileName, "a+")
            self.logger.addHandler(looger_fh)
            
        
    def getLoggerFileName(self):
        return self.loggerFileName
    
            
            
        
        #self.logger.addHandler.setFormatter(self.formatter)
            
            

