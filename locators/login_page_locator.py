from selenium.webdriver.common.by import By


class LoginPageLocator:
    fishman_account_loc = (By.ID, 'com.lchr.diaoyu:id/tv_account_login')
    username_inputbox_loc = (By.ID, 'com.lchr.diaoyu:id/user_id')
    password_inputbox_loc = (By.ID, 'com.lchr.diaoyu:id/passwd_id')
    login_btn_loc = (By.ID, 'com.lchr.diaoyu:id/btn_login')