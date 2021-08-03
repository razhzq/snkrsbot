

from sneakerfunction import *




sumbit_order_time()



try:
        login()
        early_links()
        print('checkout page success')
        #early_link_success()
        print('zero')
        if early_link_success() == True:
            print('annot')
            try:
              print('one')
              delivery_add()
              payment_card()
              consent_status()
              print('')
            except:
              print('two')
              payment_card() 
              consent_status()
        else: 
            print('three')
            clear_cache()
            login()
            early_links()
            try:
              print('four')
              delivery_add()
              payment_card()
              consent_status()
              print('')
            except:
              print('five')
              payment_card() 
              consent_status()
            
except:
        print('hihu')#if login failed
       

finally:
    print('program finished')






