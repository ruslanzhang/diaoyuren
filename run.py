import pytest
import os, sys
from common.bases.get_config import read_config
from common.bases.get_log import Log


BASE_DIR = os.path.dirname(__file__)
if sys.platform == "win32":
    conf_dir = os.path.join(BASE_DIR, 'common/config/config.ini').replace('/', '\\')
else:
    conf_dir = os.path.join(BASE_DIR, 'common/config/config.ini')
log_dir = read_config(conf_dir, "log", "log_path")
img_dir = read_config(conf_dir, 'img', 'img_path')
json_report_path = read_config(conf_dir, 'report', 'json_report_path')
html_report_path = read_config(conf_dir, 'report', 'html_report_path')
logger = Log(log_dir)

if __name__ == '__main__':
    # 生成测试结果文件保存在json_report_path路径下
    args = ['-s', '-q', '--alluredir', json_report_path]
    self_args = sys.argv[1:]
    # print('args + self_args: ', args + self_args)
    pytest.main(args + self_args)
    cmd = 'allure generate %s -o %s -c' % (json_report_path, html_report_path)
    os.system(cmd)
