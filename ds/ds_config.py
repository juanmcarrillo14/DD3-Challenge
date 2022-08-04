import sqlite3
import pandas as pd
import logging as logger
import sys
import platform

class ddtres_db:
   
    logger.warning("Warning message: Install necessary dependencies - run 'pip install -r requirements.txt' command")
    
    @staticmethod
    def connect(db: str  = 'ddtres_data'):
        """ Generation connection to db

        Considerations
        ---------------------------------------------------------
        When you call this method, this automatically create a connection to default schema

        Returns
        ---------------------------------------------------------

        sqlite3.connect object

        """
        try:
            conn = sqlite3.connect(db) 
            print(f"Connection Established to {db}")
        except:
            logger.error("Connection Error",exc_info=True)

        return conn

    @staticmethod 
    def upload_table(df: str,table: str):
        """ Create Table on ddtres_data.
         
        Parameters
        -----------------------------------------------
         
        df ->  str file name
        table -> str Table name
         
        Returns
        ----------------------------------------------
         
        Confirm Message.
         
        """
        conn = ddtres_db.connect()
        data = pd.read_csv(df + '.csv',index_col=False)
        
        try:
            data.to_sql(name=table, con=conn)
        except:
            pass
        
        logger.info('Table uploaded successfully')
    
    @staticmethod
    def get_query_table(query:str):
        
        """Retrieve table from a specific query
        
        Parameters
        -------------------------------------------------
        
        query -> personalized query (str)
        
        WARNING: Be sure to always specified table schema
        
        Returns
        --------------------------------------------------
        
        pd.DataFrame object
        
        """
        df = pd.read_sql(query,ddtres_db.connect())
                            
        return df
    
    
    @staticmethod
    def show_tables(schema:str = 'ddtres_data') -> list:
        """ Show tables available in specified schema connection
         
        Parameters
        -----------------------------------------------
         
        schema -> name of the database (str) default schema: ddtres_data
         
        Returns
        ----------------------------------------------
         
        pd.DataFrame object
         
        """
        conn = ddtres_db.connect()
        cursor = conn.cursor()
        cursor.execute("SELECT name FROM sqlite_master WHERE type='table'")
                            
        return cursor.fetchall()
     