from common.bases.base_page import BasePage
from locators.login_page_locator import LoginPageLocator
from locators.me_page_locator import MePageLocator
from locators.setting_page_locator import SettingPageLocator
from locators.main_page_locator import MainPageLocator
from run import logger
from selenium.common.exceptions import NoSuchElementException


class PagesAction(BasePage):
    def login(self, username, password):
        self.send_data(LoginPageLocator.username_inputbox_loc, username)
        self.send_data(LoginPageLocator.password_inputbox_loc, password)
        self.click_element(LoginPageLocator.login_btn_loc)
        self.sleep(3)

    # 判断用户是否登录
    def is_user_login(self):
        try:
            logger.info('is search for element {}'.format(MePageLocator.click_to_login_loc))
            if self.search_element(MePageLocator.click_to_login_loc):
                logger.info('found the element {}'.format(MePageLocator.click_to_login_loc))
                return False
        except Exception as e:
            logger.info('the element {} not found.'.format(MePageLocator.click_to_login_loc))
            logger.info(e)
            return True

    # 退出登录
    def logout(self):
        logger.info('begin to perform logout operation')
        try:
            self.click_element(MePageLocator.setting_btn_loc)
            self.sleep(2)
            self.click_element(SettingPageLocator.logout_btn_loc)
            self.sleep(1)
            self.click_element(SettingPageLocator.confirm_btn_loc)
        except Exception as e:
            logger.info('logout failed!')
            logger(e)

    # 到钓鱼人账号登录页
    def go_to_login_page(self):
        self.go_to_me_page()
        if self.is_user_login():
            self.logout()
        self.click_element(MePageLocator.click_to_login_loc)
        self.sleep(2)
        self.click_element(LoginPageLocator.fishman_account_loc)
        self.sleep(2)

    def go_to_me_page(self):
        self.sleep(2)
        self.cancel_edition_upgrade()
        logger.info('开始准备进入我的页面')
        self.click_element(MainPageLocator.me_icon_loc)
        logger.info('已经进入我的页面')
        self.sleep(2)

    # 登录后判断登录是否成功
    def is_nickname_exists(self):
        if self.search_element(MePageLocator.nickname_loc):
            logger.info('已找到页面元素： {}'.format(MePageLocator.nickname_loc))
            return True
        else:
            return False

    # 点击版本更新弹窗中的取消版本更新
    def cancel_edition_upgrade(self):
        try:
            self.sleep(3)
            logger.info('开始查找版本更新窗口中的版本更新页面元素')
            if self.search_element(MainPageLocator.edition_upgrade_loc):
                logger.info('找到版本更新页面元素')
                logger.info('开始点击取消版本更新按钮')
                self.click_element(MainPageLocator.upgrade_btn_cancel_loc)
                logger.info('完成点击取消版本更新按钮')
        except NoSuchElementException:
            logger.info('the element: {} not found.'.format(MainPageLocator.edition_upgrade_loc))
        except Exception as e:
            logger.info(e)
