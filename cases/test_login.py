from test_data.test_data import success_data
from test_data.test_data import failed_data
from run import logger
import pytest


@pytest.fixture(scope='module')
def prepare_to_login(handler):
    logger.info('开始进入首页')
    handler[1].go_to_login_page()


@pytest.fixture(scope='module')
def agree_the_privacy(handler):
    logger.info('点击同意协议')
    handler[1].agree_privacy()


# @pytest.mark.usefixtures('agree_the_privacy')
@pytest.mark.usefixtures('prepare_to_login')
class TestLogin:
    @pytest.mark.last
    def test_login_success(self, handler):
        handler[1].login(success_data['username'], success_data['password'])
        logger.info("登录完成")
        assert handler[1].is_nickname_exists()
        logger.info('测试通过: ========== pass ==========')

    @pytest.mark.parametrize('data', failed_data)
    def test_login_failed(self, handler, data):
        handler[1].login(data['username'], data['password'])
        logger.info('反向用例，登录失败')
        assert handler[1].is_toast_show(data['error_msg'], 8, 0.2)
        logger.info('测试通过: ========== pass ==========')
