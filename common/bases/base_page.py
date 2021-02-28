from run import img_dir
import time
from run import logger
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from datetime import datetime
from selenium.webdriver.common.by import By
import time
from run import logger

class BasePage:
    def __init__(self, driver):
        self.driver = driver

    # 等待时间秒
    def sleep(self, s):
        time.sleep(s)

    # 查找页面元素
    def search_element(self, locator):
        logger.info('开始寻找页面元素： {}'.format(locator))
        return self.driver.find_element(*locator)

    # 点击页面元素
    def click_element(self, locator):
        element = self.search_element(locator)
        logger.info('已找到页面元素： {}'.format(element))
        element.click()
        logger.info('页面元素： {} 已点击'.format(element))

    # 向编辑输入框传数据
    def send_data(self, locator, data):
        # self.clear_text(locator)
        element = self.search_element(locator)
        logger.info('已找到页面元素： {}'.format(element))
        element.send_keys(data)
        logger.info('已向页面元素: {} 传送数据'.format(element))

    # 截图
    def save_picture(self, msg=''):
        img_path = img_dir + '{0}-{1}.png'.format(msg, time.strftime('%Y-%m-%d_%H_%M_%S', time.localtime()))
        try:
            self.driver.save_screenshot(img_path)
            logger.info('截图成功，图片保存路径为：{}'.format(img_path))
        except Exception as e:
            logger.info('截图失败，{}'.format(msg))
            logger.info(e)

    # 清除输入框内容
    def clear_text(self, locator):
        self.search_element(locator).clear()

    # 等待页面元素可见
    def wait_element_visible(self, locator, msg=''):
        try:
            now = datetime.now()
            WebDriverWait(self.driver, 20). \
                until(EC.visibility_of_element_located(locator))
            end = datetime.now()
            total_time = (end - now).total_seconds()
            logger.info('the total time of waiting for {0} visible is {1}'.format(locator, total_time))
        except Exception as e:
            logger.info(e)
            self.driver.save_picture(msg)

    # 获取页面元素的文本
    def get_element_text(self, locator, msg=''):
        self.wait_element_visible(locator, msg)
        return self.search_element(locator).text

    # 判断toast是否出现
    def is_toast_show(self, msg, timeout=20, poll_frequency=0.5):
        """

        :param msg: toast 中显示的文本中包含的内容
        :param timeout:
        :param poll_frequency:
        :return:
        """
        logger.info('waiting for toast element to show')
        locator = (By.XPATH, "//*[contains(@text, '%s')]" % msg)
        try:
            WebDriverWait(self.driver, timeout, poll_frequency).until(EC.presence_of_element_located(locator))
            return True
        except Exception as e:
            logger.warning('toast not found.')
            logger(e)
            return False






