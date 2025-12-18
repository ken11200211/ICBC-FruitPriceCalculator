class FruitSale:
    def __init__(self):
        self.base_prices={'apple':8,'strawberry':13,'mango':20}
    
    def calculate_price_a(self,apple_weight,strawberry_weight):
        """
        只購買蘋果和草莓，無促銷
        水果斤數為大於等於0的整數
        """
        total=(apple_weight*self.base_prices['apple']+strawberry_weight*self.base_prices['strawberry'])
        return total
    
    def calculate_price_b(self,apple_weight,strawberry_weight,mango_weight):
        """
        購買三種水果，無促銷
        水果斤數為大於等於0的整數
        """
        total=(apple_weight*self.base_prices['apple']+strawberry_weight*self.base_prices['strawberry']+mango_weight*self.base_prices['mango'])
        return total
    
    def calculate_price_c(self,apple_weight,strawberry_weight,mango_weight):
        """
        草莓打8折
        水果斤數為大於等於0的整數
        """
        strawberry_price=self.base_prices['strawberry']*0.8#草莓8折
        total=(apple_weight*self.base_prices['apple']+strawberry_weight*strawberry_price+mango_weight*self.base_prices['mango'])
        return total
    
    def calculate_price_d(self,apple_weight,strawberry_weight,mango_weight):
        """
        草莓打8折，且滿100減10
        水果斤數為大於等於0的整數
        """
        #計算基礎價格
        strawberry_price=self.base_prices['strawberry']*0.8#草莓8折
        total=(apple_weight*self.base_prices['apple']+strawberry_weight*strawberry_price+mango_weight*self.base_prices['mango'])
        
        #滿100減10
        if total>=100:
           total-=10
            
        return total