import account
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import threading
import logging


class BoughtPs5:
    PS5_bought = False


class CheckOutBot_Walmart:
    def __init__(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://www.walmart.com")
        # self.accept_cookies()

    def accept_cookies(self):
        button = self.driver.find_element_by_id("privacy-layer-accept-all-button")
        button.click()

    def login(self, email, password):

        self.driver.get(
            "https://www.walmart.com/account/login?tid=0&returnUrl=%2F%3F%26adid%3D22222222220220085369%26wmlspartner%3Dwmtlabs%26wl0%3De%26wl1%3Dg%26wl2%3Dc%26wl3%3D178555472384%26wl4%3Dkwd-27665750%26wl5%3D9018505%26wl6%3D%26wl7%3D%26wl8%3D%26veh%3Dsem%26gclid%3DEAIaIQobChMI8YThyZjW7QIVDr7ACh2kygpVEAAYASAAEgI6hvD_BwE")
        # time.sleep(5)
        email_input = self.driver.find_element_by_id("email")
        email_input.clear()
        email_input.send_keys(email)
        pass_input = self.driver.find_element_by_id("password")
        pass_input.clear()
        pass_input.send_keys(password)
        pass_input.send_keys(Keys.RETURN)
        time.sleep(5)

    def check_in_stock(self):
        self.driver.get("https://www.walmart.com/ip/PlayStation-5-Console/363472942")
        try:
            stock_availability = self.driver.find_element_by_class_name("prod-blitz-copy-message")
        except:
            print("PS5 not in stock at Walmart")
        # print(stock_availability.text)

    def add_product_to_chart(self, link):
        self.driver.get(link)
        try:
            WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(
                (By.XPATH, '//span[text()="Add to cart"]'))).click()
        except:
            print("Error with adding stuff to cart")
        # click_button = add_to_cart_button.find_elements_by_class_name('btn btn-primary btn-lg btn-block btn-leading-ficon add-to-cart-button')
        # add_to_cart_button.click()
        time.sleep(2)

    def checkout(self):
        time.sleep(5)
        not_done = True
        number_of_attempts = 0
        cart_clicked = False
        continue_1_clicked = False
        continue_2_clicked = False
        cvv_entered = False
        review_order_clicked = False
        while not_done:
            try:
                # Goes to cart to checkout and clicks the checkout button with only one item in the cart
                if not cart_clicked:
                    try:
                        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(
                            (By.XPATH, '//span[text()="Check out"]'))).click()
                        cart_clicked = True
                        time.sleep(2)
                    except:
                        try:
                            WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(
                                (By.XPATH, '//span[text()="Check out (1)"]'))).click()
                            cart_clicked = True
                            time.sleep(2)
                        except:
                            print("Stuff ain't working right")
                # Presses the continue option in the check out
                if not continue_1_clicked:
                    try:
                        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(
                            (By.XPATH, '//span[text()="Continue"]'))).click()
                        continue_1_clicked = True
                        time.sleep(2)
                    except:
                        pass
                # Presses the continue option in the check out again
                if not continue_2_clicked:
                    try:
                        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(
                            (By.XPATH, '//span[text()="Continue"]'))).click()
                        continue_2_clicked = True
                        time.sleep(2)
                    except:
                        pass
                # inputs the CVV
                if not cvv_entered:
                    try:
                        cvv_input = self.driver.find_element_by_id("cvv-confirm")
                        cvv_input.clear()
                        cvv_input.send_keys(account.CVV)
                        cvv_entered = True
                        time.sleep(2)
                    except:
                        pass
                # Click the review your order button
                if not review_order_clicked:
                    try:
                        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(
                            (By.XPATH, '//span[text()="Review your order"]'))).click()
                        review_order_clicked = True
                    except:
                        pass
                if cart_clicked and continue_2_clicked and continue_1_clicked and cvv_entered and review_order_clicked:
                    not_done = False
                    BoughtPs5.PS5_bought = True
                # Clicks the Place order Button
                print("Stop here")
            except:
                print("Error, trying again for attempt number: {}".format(number_of_attempts))
                number_of_attempts += 1
            '''
            # DO NOT Uncomment !!!!!
            WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(
                (By.XPATH, '//span[text()="Place order"]'))).click()
            '''
            # this is how you click the final checkout button
            # self.driver.find_elements_by_class_name(
            #     "ContinueButton__StyledContinue-fh9abp-0"
            # )[2].click()

    def __del__(self):
        self.driver.close()


class CheckOutBot_BestBuy:
    def __init__(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://www.bestbuy.com")
        # self.accept_cookies()
        time.sleep(2)

    def accept_cookies(self):
        button = self.driver.find_element_by_id("privacy-layer-accept-all-button")
        button.click()

    def login(self, email, password):
        self.driver.get("https://www.bestbuy.com/identity/signin?token=tid%3A235c31be-4402-11eb-a761-0a9b66fd4de5")
        time.sleep(2)
        logged_in = False
        email_done = False
        password_done = False
        while not logged_in:
            if not email_done:
                try:
                    email_input = self.driver.find_element_by_id("fld-e")
                    email_input.clear()
                    email_input.send_keys(email)
                    email_done = True
                except:
                    pass
            if not password_done:
                try:
                    pass_input = self.driver.find_element_by_id("fld-p1")
                    pass_input.clear()
                    pass_input.send_keys(password)
                    pass_input.send_keys(Keys.RETURN)
                    password_done = True
                except:
                    pass
            if email_done and password_done:
                logged_in = True
                time.sleep(2)
            else:
                time.sleep(2)

    def add_product_to_chart(self):
        time.sleep(2)
        product_added_to_cart = False
        while not product_added_to_cart:
            try:
                WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(
                    (By.XPATH, '//button[text()="Add to Cart"]'))).click()
                product_added_to_cart = True
            except:
                print("Error with adding stuff to cart")
            time.sleep(2)

    def checkout(self):
        self.driver.get("https://www.bestbuy.com/cart")
        time.sleep(3)
        not_done = True
        number_of_attempts = 0
        cart_clicked = False
        cvv_entered = False
        review_order_clicked = False
        while not_done:
            try:
                # Goes to cart to checkout and clicks the checkout button with only one item in the cart
                if not cart_clicked:
                    try:
                        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(
                            (By.XPATH, '//button[text()="Checkout"]'))).click()
                        cart_clicked = True
                        time.sleep(2)
                    except:
                        try:
                            WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(
                                (By.XPATH, '//span[text()="Check out (1)"]'))).click()
                            cart_clicked = True
                            time.sleep(2)
                        except:
                            print("Stuff ain't working right")
                # inputs the CVV
                if not cvv_entered:
                    try:
                        cvv_input = self.driver.find_element_by_id("credit-card-cvv")
                        cvv_input.clear()
                        cvv_input.send_keys(account.CVV)
                        cvv_entered = True
                        time.sleep(2)
                    except:
                        pass
                # Click the review your order button
                if not review_order_clicked:
                    try:
                        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(
                            (By.XPATH, '//span[text()="Review your order"]'))).click()
                        review_order_clicked = True
                    except:
                        pass
                if cart_clicked and cvv_entered and review_order_clicked:
                    not_done = False
                    bought = False
                    while not bought:
                        # DO NOT Uncomment !!!!!
                        try:
                            if BoughtPs5.PS5_bought:
                                bought = True
                            else:
                                WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(
                                    (By.XPATH, '//span[text()="Place Your Order"]'))).click()
                                bought = True
                                BoughtPs5.PS5_bought = True
                                time.sleep(10)
                        except:
                            pass
                    break
                # Clicks the Place order Button
                print("Stop here")
            except:
                print("Error, trying again for attempt number: {}".format(number_of_attempts))
                number_of_attempts += 1

    def __del__(self):
        self.driver.close()

    def check_in_stock(self):
        # TODO - change to False later
        in_stock1 = False
        self.driver.get("https://www.bestbuy.com/site/sony-playstation-5-console/6426149.p?skuId=6426149")
        while not in_stock1:
            try:
                stock_availability = self.driver.find_element_by_xpath(
                    '//button[text()="Sold Out"]')
                print(stock_availability.text)
                self.driver.refresh()
            except:
                print("PS5 is in stock at Best Buy")
                in_stock1 = True
            if in_stock1:
                return True
        print("Here")


def buyingPs5Thread():
    checkout_bot_BB = CheckOutBot_BestBuy()
    checkout_bot_BB.login(account.email, account.password)
    in_stock = checkout_bot_BB.check_in_stock()
    if in_stock:
        checkout_bot_BB.add_product_to_chart()
        checkout_bot_BB.checkout()


if __name__ == "__main__":

    threads = list()
    for index in range(3):
        logging.info("Main    : create and start thread %d.", index)
        x = threading.Thread(target=buyingPs5Thread)
        threads.append(x)
        x.start()

    for index, thread in enumerate(threads):
        logging.info("Main    : before joining thread %d.", index)
        thread.join()
        logging.info("Main    : thread %d done", index)
