import sympy as sp
while True:
    try:
        x = sp.symbols('x')
        print("乘用*,除用/,加用+，减用-，幂用**,如x**2表示x的平方,输入括号要是英文括号")
        mode = input("请选择模式（不定积分输入0，定积分输入1）: ")
        if mode not in ['0', '1']:
            raise ValueError("无效的模式选择，请输入0或1.")
        f = eval(input('被积函数f(x) = '))
        if mode == '0':
            F = sp.integrate(f, x)
            print("不定积分F(x) = ", F)
        elif mode == '1':
            F = sp.integrate(f, x)
            print("不定积分F(x) = ", F)
            limits_input = input("请输入定积分的上下限，格式为'a,b' (a和b都是数): ")
            a, b = map(float, limits_input.split(','))
            if len([val for val in [a, b] if isinstance(val, (int, float))]) != 2:
                raise ValueError("定积分的上下限必须是数字.")
            definite_integral = F.subs(x, b) - F.subs(x, a)
            print(f"定积分从{a}到{b}的值 = {definite_integral}")
    except Exception as e:
        print(f"发生错误: {e}, 请重新输入")