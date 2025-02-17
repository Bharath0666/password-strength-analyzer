def password_analyser(password):
    length=len(password)>=8
    score=0
    has_upper=any(c.isupper() for c in password )
    has_lower=any(c.islower() for c in password)
    has_number=any(c.isdigit() for c in password)
    has_specialChar=any(not c.isalnum() for c in password)
    weak_passwords = ["password", "123456", "qwerty", "abc123","admin", "letmein","123456780","123456789","12345678"]
    
    if password.lower() in weak_passwords:
       return "Your password is very weak. Avoid common passwords!"
    
    if has_upper:
        score+=1
    if has_lower:
        score+=1
    if has_number:
        score+=1
    if has_specialChar:
        score+=1
    if length:
        score+=1
        
    if score>=5:
        return "Your password is very strong"
        
    elif score==4:
        return "Your password is strong"
        
    elif score==3:
        return "Your password is Good"
        
    else:
        return "Your password is weak.Try using Upperacase, Numbers or Special characters."
        
password=input("Enter the password:")
strength=password_analyser(password)
print(f"{strength}")