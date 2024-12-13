import sympy as sp

def main():
    x = sp.symbols('x')
    print("""
    欢迎使用积分计算器！
    乘用*, 除用/, 加用+, 减用-, 幂用**, 如x**2表示x的平方, 输入括号要是英文括号。
    支持的函数：
    - 三角函数：sin, cos, tan
    - 指数函数：exp
    - 对数函数：ln (自然对数), log(x) (默认以e为底), log(x, b) (以b为底的对数)
    - 平方根：sqrt
    - 自然常数：可以用 e 或 E 表示
    例如: sin(x), cos(2*x), exp(-x), ln(x), log(x), log(x, 2), sqrt(x), e**x
    """)
    
    while True:
        try:
            mode = input("请选择模式（不定积分输入0，定积分输入1，退出输入q）: ").strip().lower()
            if mode == 'q':
                print("感谢使用积分计算器，再见！")
                break
            if mode not in ['0', '1']:
                raise ValueError("无效的模式选择，请输入0或1.")
            f_input = input('被积函数f(x) = ')
            f = sp.sympify(f_input, locals={'e': sp.E, 'E': sp.E, 'ln': sp.log})
            if mode == '0':
                F = sp.integrate(f, x)
                print("不定积分F(x) = ", F)
            elif mode == '1':
                limits_input = input("请输入定积分的上下限，格式为'a,b' (a和b都是数): ")
                a, b = map(float, limits_input.split(','))
                definite_integral = sp.integrate(f, (x, a, b))
                print(f"定积分从{a}到{b}的值 = {definite_integral}")
        except Exception as e:
            print(f"发生错误: {e}, 请检查您的输入并重试")
if __name__ == "__main__":
    main()