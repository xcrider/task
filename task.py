import requests



api_key = "c895a35c365541c4ac22a61d13bc388d"


def main():
    get_order(customer_order, customer_email)


# def printer(a, b):
#     print(a, b)


def get_order(order, email):
    headers = {"X-API-KEY": api_key}
    responose = requests.get('https://customizations.chatbotize.com/ecommerce/orders', headers=headers)
    responose = responose.json()

    for item in responose['items']:
        if item['orderNumber'] == order:
            if item['email'] == email:       
                if "tracking" in item.keys() and item['status'] != "refunded":               # Hey Maciek, we didn't discuss this scenario behaviour, but I just assumed that if the order is refunded the trackin information are invalid so there is no point in sharing them with the customer
                    print(item['status'], item['tracking']['url'])
                print(item['status'])        
        # print(f"Can't find the order {order} under your {email} account. Please recheck those details in your order confirmation email")                   # Instead it could return some null value to Zowie and this message would be handled there in real world.            


if __name__ == "__main__":
    main()