from selenium.webdriver.common.by import By


class MainPageLocator:
    me_icon_loc = (By.ID, 'com.lchr.diaoyu:id/btn_tab_mine')
    edition_upgrade_loc = (By.ID, 'com.lchr.diaoyu:id/dialog_title')
    upgrade_btn_cancel_loc = (By.ID, 'com.lchr.diaoyu:id/btn_cancel')