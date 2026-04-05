def create_profile(name):
    email = name.lower().replace(" ","")+"@company.com"
    return email

def discount_cal (price,dis_per):
    dis_amt = price * (dis_per/100)
    return(price-dis_amt)


def welcome(name):
    return f"Welcome to ABC Company {name}"