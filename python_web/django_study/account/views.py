from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate, login
# 导入LoginForm，刚才编写的form表单，SignUpForm先不管
from .forms import LoginForm, SignUpForm


def user_login(request):
	if request.method == 'GET':
		# 自动生成表单
		login_form = LoginForm()
		context = {}
		# 把表单写入参数并回传给前端模板
		context['form'] = login_form
		return render(request, "account/login.html", context=context)
	if request.method == 'POST':
		# 用POST请求来初始化表单
		login_form = LoginForm(request.POST)
		# 判断用户输入是否合法
		if login_form.is_valid():
			# 用键值对存储了表单中的数据，cleaned_data是一个方法，可以获取键值对
			data = login_form.cleaned_data
			# 直接用authenticate方法验证用户名和密码是否正确
			user = authenticate(username=data['username'], password=data['password'])
			# 如果验证成功
			if user:
				# django自带的登陆函数
				login(request, user)
				# 设置session
				request.session['username'] = data['username']
				# 登录成功后跳转回主页面
				return redirect('/')
			else:
				return HttpResponse('账号或密码错误')
		else:
			return HttpResponse('登录内容有误')