import os 
from database.db_operations import save_user_token, get_user_token, update_user_token


class TokenManager(): 
    """
    Class that manages and handles tokens, interacting with Oath system. 
    """
    
    def __init__(self, db_connection):
        self.db_connection = db_connection
        
        
    def save_new_token(self, user_id, token): 
        """
        Save's user_id's new token in self.db_connection
        
        Args: 
            user_id (string): string representation of user_id
            token (): new token 
        """
        save_user_token(user_id, token)
        
        
    def refresh_token(self, user_id): 
        """
        Refreshes user with id [user_id]'s tokens 
        
        Args: 
            user_id (): id of selected user given self.db_connection
        """
        user_token = get_user_token(user_id)
        new_token = self.new_token(user_id)
        save_user_token(user_id, new_token)
    
    
    def new_token(self, user_id): 
        """
        Obtains new token of user with id [user_id]
        
        Args: 
            user_id (): user_id 
        """
        pass
        
        
