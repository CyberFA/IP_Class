
"""
Created on Wed Jul 24 17:21:22 2019

@author: FARZAN AFARANGAN
"""

class IP:
    '''
    Searching for IP Classes and
    Find  Private / Public 
    '''
    def __init__(self,a,b,c,d):
        self.a = a
        self.b = b
        self.c = c
        self.d = d
    def Calc_IP(self):
        if self.a >= 1 and self.a <=126 and self.OCt_C_d() == True: #1-First I Wrote a function for separation of numbers for each Octet
           
                if self.a == 10: #2-If Octet1 is 10 I return private else return public by fomatstring
                    return f"{'Class A  ':^10} / {'Private':^10} | {'Subnet mask':^10}\n{'-'*37}\n    {self.a}.{self.b}.{self.c}.{self.d}{'':^5} | 255.0.0.0 "
                else:
                    return f"{'Class A  ':^10} / {'Public':^10} | {'Subnet mask':^10}\n{'-'*37}\n    {self.a}.{self.b}.{self.c}.{self.d}{'':^7}  |  255.0.0.0 "

        elif self.a >=128 and self.a <=191 and self.OCt_C_d() == True: #3-Searching for Class B 
               
            if self.a == 172 and self.b>=16 and self.b <=31: #4-Is it PRIVATE ?
                return f"{'Class B  ':^10} / {'Private':^10} | {'Subnet mask':^10}\n{'-'*37}\n     {self.a}.{self.b}.{self.c}.{self.d}{'':^5}| 255.240.0.0 "

            else:#5-or Public ??
                return f"{'Class B  ':^10} / {'Public':^10} | {'Subnet mask':^10}\n{'-'*37}\n     {self.a}.{self.b}.{self.c}.{self.d}{'':^5}| 255.255.0.0 "

        elif self.a >=192 and self.a <=223 and  self.OCt_C_d() == True: #6- Searching for Class C
            if self.a ==192 and self.b ==168:#7-Is it Private ??
                return f"{'Class C  ':^10} / {'Private':^10} | {'Subnet mask':^10}\n{'-'*37}\n    {self.a}.{self.b}.{self.c}.{self.d}{'':^5}| 255.255.0.0 "

            else:#8-Or Public ??
                return f"{'Class C  ':^10} / {'Public':^10} | {'Subnet mask':^10}\n{'-'*37}\n    {self.a}.{self.b}.{self.c}.{self.d}{'':^5} | 255.255.255.0 "

            
        elif self.a>=224 and self.a<=239 and self.OCt_C_d() == True:
            return "Class D ------- MULTICAST"
        
        
        elif self.a >=240 and self.a<=254 and self.OCt_C_d() == True:
            return "Class E ------- Experimental"
        
        else:
            return "Wrong number:(\nEach Part must be between -> 0-255"
        
    
                
                             
    def OCt_C_d(self):
        if self.b>=0 and self.b<=255:
            if self.c>=0 and self.c<=255:
                if self.d>=0 and self.d<=255:
                    return True
   
    
ip=IP(10,31,255,255) 
print(ip.Calc_IP())  
    