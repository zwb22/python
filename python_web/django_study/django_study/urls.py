"""django_study URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.shortcuts import render
from django.shortcuts import HttpResponse
import pymysql


# 登录页面
def login(request):
    # 指定要访问的页面，render的功能：将请求的页面结果提交给客户端
    return render(request, 'login.html')


# 注册页面
def register(request):
    return render(request, 'register.html')


# 连接到mysql数据库
def __connect_to_mysql():
    p_mysql_obj = pymysql.connect(
        host='127.0.0.1',
        user='python_web@ZhengWeibin',
        password='aa956956',
        database='python_web'
    )
    # 使用cursor()方法创建一个游标对象
    p_db_cursor = p_mysql_obj.cursor()
    return p_mysql_obj, p_db_cursor


# 保存注册的数据
def save(request):
    # 判断当前用户是否已经注册过
    b_has_register = False
    p_get_request = request.GET
    s_user_name = p_get_request.get('username')
    s_password = p_get_request.get('password')
    print(f's_user_name {s_user_name}')
    print(f's_password {s_password}')

    # 连接到mysql数据库
    p_mysql_obj, p_db_cursor = __connect_to_mysql()

    s_sql_sentence = 'SELECT * FROM users_info'
    # 执行sql语句
    p_db_cursor.execute(s_sql_sentence)
    # 获取全部数据库
    l_all_users_info = p_db_cursor.fetchall()
    print(f'save:l_all_users_info {l_all_users_info}')
    for t_user_info in l_all_users_info:
        if s_user_name not in t_user_info:
            continue
        b_has_register = True
    # 当前用户已经注册过了
    if b_has_register:
        s_tips_info = '该用户已存在'
    else:
        s_insert_sql = 'INSERT INTO users_info(user_name,user_password) VALUES(%s,%s)'
        p_db_cursor.execute(s_insert_sql, (s_user_name, s_password))
        # 必须进行提交
        p_mysql_obj.commit()
        s_tips_info = '注册成功'
    # 关闭游标和数据库的连接
    p_db_cursor.close()
    p_mysql_obj.close()
    return HttpResponse(s_tips_info)


def query(request):
    p_get_request = request.GET
    s_user_name = p_get_request.get('username')
    s_password = p_get_request.get('password')
    # 连接到mysql数据库
    p_mysql_obj, p_db_cursor = __connect_to_mysql()
    s_sql_sentence = 'SELECT * FROM users_info'
    # 执行sql语句
    p_db_cursor.execute(s_sql_sentence)
    # 获取全部数据库
    l_all_users_info = p_db_cursor.fetchall()
    print(f'save:l_all_users_info {l_all_users_info}')
    # 数据库里是否有该用户
    b_has_user = False
    # 输入密码是否正确
    b_is_pwd_correct = False
    for t_user_info in l_all_users_info:
        if s_user_name not in t_user_info:
            continue
        b_has_user = True
        if s_password in t_user_info:
            b_is_pwd_correct = True
    if b_has_user:
        if b_is_pwd_correct:
            s_tip_info = '登录成功'
        else:
            s_tip_info = '密码错误'
    else:
        s_tip_info = f'用户({s_user_name})不存在'
    # 关闭游标和数据库的连接
    p_db_cursor.close()
    p_mysql_obj.close()
    return HttpResponse(s_tip_info)


urlpatterns = [
    # 系统默认创建的
    path('admin/', admin.site.urls),
    # 用于打开登录页面
    path('login/', login),
    # 用于打开注册页面
    path('register/', register),
    # 输入用户名密码后提交给后台save函数处理
    path('register/save', save),
    # 输入用户名密码后提交给后台query函数处理
    path('login/query', query),
]