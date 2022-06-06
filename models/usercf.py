"""
Steps:
---
1. read_data
2. User_Item_Matrix  --> Customer_Order_times
3. Compute The Similarity Matrix(Users)
4. Judge the Specific Customer like the Product or not (get score), and decide the Recommendation

"""

import pandas as pd 
import numpy as np 

class UserCF:
    def __init__(self) -> None:
        super().__init__()
        
    def preprocess(self, customer, date, order, product):
        """
        target:
        ---
            dict customer_product_times
        steps:
        ---
            1. compute len(customer)
            2. compute len(product)
            3. count times according to order
        """
        score_matrix = np.zeros((len(customer), len(product)))
        for i in range(len(order)):
            pass
        
        
        
        
    def fit(self, train_data):
        """
        Args:
            train_data: 训练数据
        """
        self.train_data = train_data
        