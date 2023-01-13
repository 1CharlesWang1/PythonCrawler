from bs4 import BeautifulSoup
html='''<div class="bj">
    <form action="http://localhost:8080/RGZJ_war/message.html" method="post" id="regform">
        <div class="bgDiv">
            <div class="login">
                <img class="logoImg" src="./css/hh.png"/>
                <p2>登录页面</p2>

                <div class="user">
                    用户
                    <select name="users" >
                        <option value="student">学生</option>
                        <option value="teacher" selected>教师</option>
                        <option value="gly">管理员</option>
                    </select>
                </div>

                <div class="username">
                    <p id="er1" class="check_user" >用户名为空</p>
                    <img class="userImg" src="./css/yh.png"/>
                    <input class="userInp" id="user_name" name="username" type="text"  placeholder="请输入用户名"/>
                </div>
                <div class="pwd">
                    <p id="er2" class="check_password" >密码为空</p>
                    <img class="pwdImg" src="./css/ma.png"/>
                    <input class="pwdInp" type="password" id="password" name="password"  placeholder="请输入密码"/>
                </div>
                <div class="rem">记住密码<input id="remember" name="remember" value="1" type="checkbox"></div>
                <div class="check_num">
                    <p id="er3" class="check_user" >验证码错误</p>
                    <img class="checkImg" src="./css/yzm.png"/>
                    <input class="userInp" id="check_num" name="check_num" type="text"  placeholder="请输入验证码"/>
                </div>
                <input type="submit" value="登录" id="regform1">
                <div class="reset">
                    <input type="reset">
                </div>
            </div>
            <a href="register.html">注册</a>
            <a href="register.html">登录</a>
        
        </div>
    </form>
</div>
'''
#创建BeautifulSoup对象
soup=BeautifulSoup(html,'lxml')

#查找div标签
# title=soup.find('div')
# print(title)

#查找a标签
a=soup.find('a')
print(a)

a_all=soup.find_all('a')
print(a_all)

#根据属性，id查找
a=soup.find(id='er1')
print(a)

a=soup.find(attrs={'id':'er1'})
print(a)

text=soup.find(text='注册')
print(text)

#Tag对象
print(type(a))
print('标签名',a.name)
print('属性',a.attrs)
print('标签文本内容',a.text)