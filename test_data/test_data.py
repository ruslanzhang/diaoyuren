success_data = {'name': '登录功能-正常登录', 'username': '15510817996', 'password': '123456Ok'}
failed_data = [
    {'name': '登录功能-异常登录-用户名为空', 'username': '', 'password': '654321', 'error_msg': '用户名不能为空'},
    {'name': '登录功能-异常登录-用户名错误', 'username': 'abc', 'password': '654321Ok', 'error_msg': '账号或密码错误'},
    {'name': '登录功能-异常登录-用户名错误', 'username': '15566669999', 'password': '654321Ok', 'error_msg': '用户不存在'},
    {'name': '登录功能-异常登录-密码为空', 'username': '15510817996', 'password': '', 'error_msg': '密码不能为空'},
    {'name': '登录功能-异常登录-密码错误', 'username': '15510817996', 'password': '654321', 'error_msg': '账号或密码错误'}
]
