class Instaprofile :
    def __init__(self , followers , following , username , bio):
        self._followers = followers
        self._following = following
        self._username = username
        self._bio = bio
        #making of getter 
    @property
    def followers(self):
        return self._followers
    @property
    def following(self):
        return self._following
    @property
    def username(self):
        return self._username
    @property
    def bio(self):
        return self._bio
        
user = Instaprofile(190,71,"krish lakhotia","hi i am a codder")
print(f"followers:{user.followers}\n")  
print(f"following:{user.following}\n")  
print(f"username:{user.username}\n")  
print(f"bio:{user.bio}\n")        

            

       