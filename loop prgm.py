password=2387
n=3
w=int(input())
for i in range(3):
    if(w==password):
         print("successfully logged in")
    else:
        if n==1:
            print("Your account is blocked, try after 24 hours")
        else:
            print("incorrect password, you are left with",n-1,"attempts")

