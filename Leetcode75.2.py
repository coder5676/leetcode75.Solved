def gcdOfStrings( str1: str, str2: str) -> str:
        def isdivisible(l):
            if(len(str1)%l or len(str2)%l):
                return False
           
            x=len(str1)//l
            y=len(str2)//l
            return str1[:l]*x==str1 and str1[:l]*y==str2
        for i in range(min(len(str1),len(str2)),0,-1):
            if(isdivisible(i)):
                return str1[:i]
           
        return"" 



            
        

        
        
        




        
