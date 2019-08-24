#!/usr/bin/env python
# -*- coding=utf-8 -*-

from selenium import webdriver

import time

from threading import Thread

class HongZha(object):

    def __init__(self):

        self.phone = '18028068523'

        self.num = 0

        self.opt = webdriver.ChromeOptions()

        self.opt.add_argument('headless')

    def send_yzm(self,button,name):

        button.click()

        self.num+=1

        print("{}  第{}次  发送成功  {}".format(self.phone,self.num,name))

        time.sleep(65) #两次发送的间隔必须在60秒以上。所以这边定义的是65秒

    def guazi(self, name):
        while True:
            browser = webdriver.Chrome(chrome_options=self.opt)
            browser.implicitly_wait(10)
            browser.get("https://www.guazi.com/www/bj/buy")
            a_btn = browser.find_element_by_xpath("//a[@class='uc-my']")
            a_btn.click()
            tel = browser.find_element_by_xpath("//input[@placeholder='请输入您的手机号码']")
            tel.send_keys(self.phone)
            button = browser.find_element_by_xpath("//button[@class='get-code']")
            self.send_yzm(button, name)
            browser.quit()
    def wphui(self,name):
        while True:
            driver = webdriver.Chrome(chrome_options=self.opt)
            # driver = webdriver.Chrome()
            driver.implicitly_wait(10)
            driver.get ( "https://passport.vip.com/register?src=https%3A%2F%2Fwww.vip.com%2F" )
            tel = driver.find_element_by_xpath ( "//input[@placeholder='请输入手机号码']" )
            tel.send_keys ( self.phone )
            driver.find_element_by_xpath('//*[@id="J_mobile_reg_button"]').click()
            driver.find_element_by_xpath ( '//*[@id="J_mobile_verifycode_btn"]').click()
            button = driver.find_element_by_xpath ("//a[@class='ui-btn-medium btn-verify-code ui-btn-secondary']" )
            self.send_yzm ( button, name)
            driver.quit ()

    def suning(self, name):
        while True:
            # driver = webdriver.Chrome(executable_path="C:/Users/Administrator/AppData/Local/Programs/Python/Python36/chromedriver.exe")
            # driver = webdriver.Chrome(chrome_options=self.opt)
            driver = webdriver.Chrome(chrome_options=self.opt)
            driver.implicitly_wait(10)
            driver.get("https://reg.suning.com/person.do")
            driver.find_element_by_xpath('/html/body/div[5]/div[2]/div[2]/a').click()
            tel = driver.find_element_by_xpath("//input[@id='mobileAlias']")
            tel.send_keys(self.phone)
            button = driver.find_element_by_xpath(
                "//a[@id='sendSmsCode']")
            self.send_yzm(button, name)
            driver.quit()

    def func0(self, name):
        while True:
            # browser = webdriver.Chrome()
            browser = webdriver.Chrome(chrome_options=self.opt)
            # browser = webdriver.Chrome(options=self.options)
            browser.implicitly_wait(8)
            browser.get('https://www.baidu.com/')
            browser.find_element_by_xpath('//*[@id="u1"]/a[7]').click()
            browser.find_element_by_xpath('//*[@id="TANGRAM__PSP_10__footerULoginBtn"]').click()
            browser.find_element_by_xpath('//*[@id="TANGRAM__PSP_10__smsSwitchWrapper"]').click()
            browser.find_element_by_xpath('//*[@id="TANGRAM__PSP_10__smsPhone"]').send_keys(self.phone)
            button = browser.find_element_by_xpath('//*[@id="TANGRAM__PSP_10__smsTimer"]')
            self.send_yzm(button, name)
            browser.quit()
    def func2(self, name):
        while True:
            browser = webdriver.Chrome(chrome_options=self.opt)
            browser.implicitly_wait(8)
            browser.get('https://login.10086.cn/login.html')
            browser.find_element_by_xpath('//*[@id="sms_login_1"]').click()
            browser.find_element_by_xpath('//*[@id="sms_name"]').send_keys(self.phone)
            button = browser.find_element_by_xpath('//*[@id="getSMSPwd1"]')
            self.send_yzm(button, name)
            browser.quit()
    def func3(self, name):
        while True:
            browser = webdriver.Chrome(chrome_options=self.opt)
            browser.implicitly_wait(8)
            browser.get('http://caigou.51book.com/caigou/manage/designatedRegistryNewSignon.in')
            browser.find_element_by_xpath('//*[@id="cg_06"]').send_keys(self.phone)
            button = browser.find_element_by_xpath('//*[@id="sendMSgBtu"]')
            self.send_yzm(button, name)
            browser.quit()
    def func4(self, name):
        while True:
            browser = webdriver.Chrome(chrome_options=self.opt)
            browser.implicitly_wait(8)
            browser.get('http://www.shijiebang.com/reg/')
            browser.find_element_by_xpath('/html/body/div[1]/div/div[3]/div/ul[1]/li[1]/a').click()
            browser.find_element_by_xpath('/html/body/div[8]/div[2]/div/div[2]/div/label[2]/input').click()
            browser.find_element_by_xpath(
                '/html/body/div[8]/div[2]/div/div[2]/table[2]/tbody/tr[1]/td/div/input').send_keys(self.phone)
            button = browser.find_element_by_xpath(
                '/html/body/div[8]/div[2]/div/div[2]/table[2]/tbody/tr[2]/td/div/button')
            self.send_yzm(button, name)
            browser.quit()
    def func5(self, name):
        while True:
            browser = webdriver.Chrome(chrome_options=self.opt)
            browser.implicitly_wait(8)
            browser.get('https://account.youku.com/register.htm')
            browser.find_element_by_xpath('//*[@id="passport"]').send_keys(self.phone)
            browser.find_element_by_xpath('//*[@id="password"]').send_keys('helloworld998')
            browser.find_element_by_xpath('//*[@id="repeatPsd"]').send_keys('helloworld998')
            button = browser.find_element_by_xpath('//*[@id="getMobileCode"]')
            self.send_yzm(button, name)
            browser.quit()

    def func6(self, name):
        while True:
            browser = webdriver.Chrome(chrome_options=self.opt)
            browser.implicitly_wait(8)
            browser.get(
                'https://www.amazon.cn/ap/register?_encoding=UTF8&openid.assoc_handle=cnflex&openid.claimed_id=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.identity=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.mode=checkid_setup&openid.ns=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0&openid.ns.pape=http%3A%2F%2Fspecs.openid.net%2Fextensions%2Fpape%2F1.0&openid.pape.max_auth_age=0&openid.return_to=https%3A%2F%2Fwww.amazon.cn%2Fgp%2Fyourstore%2Fhome%3Fie%3DUTF8%26ref_%3Dnav_custrec_newcust')
            # browser.find_element_by_xpath('//*[@id="nav-flyout-ya-newCust"]/a').click()
            browser.find_element_by_xpath('//*[@id="ap_customer_name"]').send_keys('Mike998')
            browser.find_element_by_xpath('//*[@id="ap_phone_number"]').send_keys(self.phone)
            browser.find_element_by_xpath('//*[@id="ap_password"]').send_keys('pwd123456')
            browser.find_element_by_xpath('//*[@id="ap_register_form"]/div/div/div[5]/div/label/input').click()
            button = browser.find_element_by_xpath('//*[@id="continue"]')
            self.send_yzm(button, name)
            browser.quit()
    # 私否
    def func7(self, name):
        browser = webdriver.Chrome(chrome_options=self.opt)
        browser.implicitly_wait(8)
        browser.get('https://segmentfault.com/')
        browser.maximize_window()
        browser.find_element_by_xpath('//*[@id="loginBanner"]/div/div/div[2]/form/a[2]').click()
        browser.find_element_by_xpath('/html/body/div[7]/div/div/div[2]/div/div/div/form/div[4]/a').click()
        browser.find_element_by_xpath('/html/body/div[7]/div/div/div[2]/div/div/div/form/div[1]/input').send_keys(self.phone)
        button = browser.find_element_by_xpath('/html/body/div[7]/div/div/div[2]/div/div/div/form/div[2]/div[1]/span/button')
        self.send_yzm(button, name)
        browser.quit()

        # 97格格
        # 唯品会


    def func13(self, name):
        while True:
            browser = webdriver.Chrome(chrome_options=self.opt)
            browser.implicitly_wait(8)
            browser.get('http://www.jaja123.com/web/register')
            browser.find_element_by_xpath('/html/body/div/div[4]/form/div/div[1]/div[2]/div[1]/input').send_keys(u'张飞')
            browser.find_element_by_xpath('/html/body/div/div[4]/form/div/div[1]/div[3]/div[1]/input').send_keys(
                self.phone)
            browser.find_element_by_xpath('/html/body/div/div[4]/form/div/div[1]/div[4]/div[1]/input').send_keys(
                'pwd123456')
            browser.find_element_by_xpath('/html/body/div/div[4]/form/div/div[1]/div[5]/div[1]/input').send_keys(
                'pwd123456')
            button = browser.find_element_by_xpath(
                '/html/body/div/div[4]/form/div/div[1]/div[6]/div[1]/div/span/button')
            button.click()
            self.send_yzm(button, name)
            browser.quit()

        # 小米

    def func14(self, name):
        while True:
            browser = webdriver.Chrome(chrome_options=self.opt)
            browser.implicitly_wait(8)
            browser.get('https://cn.account.xiaomi.com/pass/register?_locale=zh_CN')
            browser.find_element_by_xpath(
                '//*[@id="main_container"]/div[3]/div[1]/div/div[3]/div[2]/label/input').send_keys(self.phone)
            button = browser.find_element_by_xpath('//*[@id="main_container"]/div[3]/div[1]/div/div[6]/input')
            button.click()
            self.send_yzm(button, name)
            browser.quit()

        # 巨人网络

    def func15(self, name):
        while True:
            browser = webdriver.Chrome(chrome_options=self.opt)
            browser.implicitly_wait(8)
            browser.get('http://reg.ztgame.com/')
            browser.find_element_by_xpath('//*[@id="reg_form"]/div[1]/input').send_keys(self.phone)
            button = browser.find_element_by_xpath('//*[@id="reg_form"]/div[2]/input[2]')
            button.click()
            self.send_yzm(button, name)
            browser.quit()

        # 微盟

    def func16(self, name):
        while True:
            browser = webdriver.Chrome(chrome_options=self.opt)
            browser.implicitly_wait(8)
            browser.get('https://account.weimob.com/register')
            browser.find_element_by_xpath('//*[@id="phone"]').send_keys(self.phone)
            button = browser.find_element_by_xpath('//*[@id="signUpForm"]/div[3]/a')
            button.click()
            self.send_yzm(button, name)
            browser.quit()

    # 商品宅配
    # def func17(self):
    #     browser = webdriver.Chrome()
    #     browser.implicitly_wait(8)
    #     browser.get('http://www.homekoo.com/zhixiao/cuxiao/index.php')
    #     browser.find_element_by_xpath('//*[@id="username5"]').send_keys(u'张飞')
    #     browser.find_element_by_xpath('//*[@id="tel5"]').send_keys(self.phone)
    #     browser.find_element_by_xpath('//*[@id="submit_img5"]').click()
    #     browser.quit()

    # 快乐购
    def func18(self,name):
        while True:
            browser = webdriver.Chrome(chrome_options=self.opt)
            browser.implicitly_wait(8)
            browser.get('http://www.happigo.com/register/')
            browser.find_element_by_xpath('//*[@id="mobile"]').send_keys(self.phone)
            button = browser.find_element_by_xpath('//*[@id="send_auth_code"]')
            button.click()
            self.send_yzm(button, name)
            browser.quit()

    # 手机中国
    def func19(self,name):
        while True:
            browser = webdriver.Chrome(chrome_options=self.opt)
            browser.implicitly_wait(8)
            browser.get('http://passport.cnmo.com/register/')
            browser.find_element_by_xpath('//*[@id="m_mobile"]').send_keys(self.phone)
            browser.find_element_by_xpath('//*[@id="m_uname"]').send_keys('helloworld998')
            browser.find_element_by_xpath('//*[@id="m_password"]').send_keys('pwd123456')
            browser.find_element_by_xpath('//*[@id="m_confirm"]').send_keys('pwd123456')
            button = browser.find_element_by_xpath('//*[@id="m_getcode"]')
            button.click()
            self.send_yzm(button, name)
            browser.quit()

    # 苏宁
    # def func20(self):
    #     browser = webdriver.Chrome()
    #     browser.implicitly_wait(8)
    #     browser.get('https://reg.suning.com/person.do')
    #     browser.find_element_by_xpath('//*[@id="mobileAlias"]').send_keys(self.phone)
    #     browser.find_element_by_xpath('//*[@id="sendSmsCode"]').click()
    #     browser.quit()

    # 爱奇艺
    # def func21(self):
    #     browser = webdriver.Chrome()
    #     browser.implicitly_wait(8)
    #     browser.get('http://www.iqiyi.com/iframe/loginreg?is_reg=1&')
    #     browser.find_element_by_xpath('/html/body/div[2]/div[2]/div[1]/div[1]/div[1]/div/div[2]/i').click()
    #     browser.find_element_by_xpath('/html/body/div[2]/div[2]/div[1]/div[1]/div[1]/div/div[1]/div[2]/input').send_keys(self.phone)
    #     browser.find_element_by_xpath('/html/body/div[2]/div[2]/div[1]/div[1]/div[1]/div/a[2]').click()
    #     browser.quit()

    def func22(self,name):
        while True:
            browser = webdriver.Chrome(chrome_options=self.opt)
            browser.implicitly_wait(8)
            browser.get('https://www.facebank.cn/user.html')
            # browser.switch_to.alert()
            browser.find_element_by_xpath('//*[@id="mobile"]').send_keys(self.phone)
            time.sleep(1)
            button = browser.find_element_by_xpath('//*[@id="getSmsCode"]')
            button.click()
            self.send_yzm(button, name)
            time.sleep(1)
            browser.quit()


    def func25(self,name):
        while True:
            browser = webdriver.Chrome(chrome_options=self.opt)
            browser.implicitly_wait(8)
            browser.get('http://jrh.financeun.com/Login/jrwLogin?web=jrw')
            browser.find_element_by_xpath('//*[@id="login-segment-phoneLogin"]').click()
            browser.find_element_by_xpath('//*[@id="quickMobile"]').send_keys(self.phone)
            time.sleep(1)
            button = browser.find_element_by_xpath('//*[@id="quickSendMsgCode"]')
            button.click()
            self.send_yzm(button, name)
            browser.quit()

    def func26(self,name):
        while True:
            browser = webdriver.Chrome(chrome_options=self.opt)
            browser.implicitly_wait(8)
            browser.get('https://www.maifupay.com/register')
            browser.find_element_by_xpath('/html/body/div[2]/div/div[1]/form/div[1]/input').send_keys(self.phone)
            browser.find_element_by_xpath('//*[@id="sendVerifySmsButton"]').click()
            browser.quit()

    def func27(self):
        browser = webdriver.Chrome()
        browser.implicitly_wait(8)
        browser.get('https://passport.ingping.com/reg/index?retUrl=https%3A%2F%2Fwww.ingping.com&fxPid=')
        browser.find_element_by_xpath('//*[@id="phoneNum"]').send_keys(self.phone)
        browser.find_element_by_xpath('//*[@id="sendRegMsgA"]').click()
        browser.quit()

    def func28(self,name):
        while True:
            browser = webdriver.Chrome(chrome_options=self.opt)
            browser.implicitly_wait(8)
            browser.get('https://www.decathlon.com.cn/zh/create')
            browser.find_element_by_xpath('//*[@id="mobile"]').send_keys(self.phone)
            time.sleep(1)
            browser.find_element_by_xpath('//*[@id="login-button"]').click()
            time.sleep(1)
            browser.quit()


    def func30(self,name):
        while True:
            browser = webdriver.Chrome(chrome_options=self.opt)
            browser.implicitly_wait(8)
            browser.get('https://my.ruanmei.com/?page=register')
            browser.find_element_by_xpath('//*[@id="phone"]').send_keys(self.phone)
            time.sleep(1)
            button = browser.find_element_by_xpath('//*[@id="sendsms"]')
            button.click()
            self.send_yzm(button, name)
            browser.quit()

    def func31(self,name):
        while True:
            browser = webdriver.Chrome(chrome_options=self.opt)
            browser.implicitly_wait(8)
            browser.get('https://www.juhe.cn/register')
            browser.find_element_by_xpath('//*[@id="username"]').send_keys('helloworld998')
            browser.find_element_by_xpath('//*[@id="password"]').send_keys('pwd123456')
            browser.find_element_by_xpath('//*[@id="mobilephone"]').send_keys(self.phone)
            button = browser.find_element_by_xpath('//*[@id="reg_smsbtn"]')

            button.click()
            self.send_yzm(button, name)
            time.sleep(1)
            browser.quit()

    def func32(self,name):
        while True:
            browser = webdriver.Chrome(chrome_options=self.opt)
            browser.implicitly_wait(8)
            browser.get('http://passport.zongheng.com/webreg?location=http%3A%2F%2Fwww.zongheng.com%2F')
            browser.find_element_by_xpath('//*[@id="regphone"]').send_keys(self.phone)
            time.sleep(1)
            button = browser.find_element_by_xpath('/html/body/div[3]/div[2]/p[3]/span')
            button.click()
            self.send_yzm(button, name)
            browser.quit()

if __name__ == '__main__':

    hongzha = HongZha()
    guazi = Thread ( target=hongzha.guazi,args=("瓜子",) )
    wphui = Thread(target=hongzha.wphui,args=("唯品会",))
    suning = Thread(target=hongzha.suning,args=("苏宁",))
    baidu = Thread(target=hongzha.func0, args=("baidu",))
    baidu2 = Thread(target=hongzha.func2, args=("baidu2",))
    baidu3 = Thread(target=hongzha.func3, args=("baidu3",))
    baidu4 = Thread(target=hongzha.func4, args=("baidu4",))
    baidu5 = Thread(target=hongzha.func5, args=("baidu5",))
    baidu6 = Thread(target=hongzha.func6, args=("baidu6",))
    baidu12 = Thread(target=hongzha.func13, args=("baidu10",))
    baidu14= Thread(target=hongzha.func14, args=("baidu11",))
    baidu15 = Thread(target=hongzha.func15, args=("baidu12",))
    baidu13 = Thread(target=hongzha.func16, args=("baidu13",))
    baidu18 = Thread(target=hongzha.func18, args=("baidu14",))
    baidu19 = Thread(target=hongzha.func19, args=("baidu15",))
    baidu22 = Thread(target=hongzha.func22, args=("baidu17",))
    baidu25= Thread(target=hongzha.func25, args=("baidu18",))
    baidu26 = Thread(target=hongzha.func26, args=("baidu19",))
    baidu27 = Thread(target=hongzha.func27, args=("baidu20",))
    baidu28 = Thread(target=hongzha.func28, args=("baidu21",))
    baidu30 = Thread(target=hongzha.func30, args=("baidu23",))
    baidu31 = Thread(target=hongzha.func31, args=("baidu24",))
    baidu32 = Thread(target=hongzha.func32, args=("baidu25",))
    guazi.start()
    wphui.start()
    suning.start()
    baidu.start()
    baidu2.start()
    baidu3.start()
    baidu4.start()
    baidu5.start()
    baidu6 .start()
    baidu12.start()
    baidu14.start()
    baidu15.start()
    baidu13.start()
    baidu18.start()
    baidu19.start()
    baidu22.start()
    baidu25.start()
    baidu28.start()
    baidu30.start()
    baidu31.start()
    baidu32.start()





