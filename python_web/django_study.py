"""
Created on 2021.08.08
@author:zhengweibin
@functions: django学习

"""
import django
import traceback


class DjangoObject:
    def __init__(self):
        pass

    def django_main(self):
        print('郑伟斌----')


if __name__ == '__main__':
    try:
        # 调用主函数
        DjangoObject().django_main()
    except Exception as p_web_error:
        print(f'error:运行出错，错误信息为：{p_web_error}-{traceback.format_exc()}')