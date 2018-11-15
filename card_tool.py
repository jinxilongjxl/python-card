list = []
def show_menu():
    '''
    显示菜单
    '''
    print("*" * 50)
    print("欢迎使用【菜单管理系统】V1.0")
    print("")
    print("1.新建名片")
    print("2.显示全部")
    print("3.查询名片")
    print("")
    print("0.退出系统")
    print("*" * 50)


def create_card():
    dict = {
        "name":input("请输入姓名"),
        "phone":input("请输入电话"),
        "qq":input("请输入QQ"),
        "email":input("请输入email"),
    }
    list.append(dict)
    print("添加成功")
    print(dict)
    print("成功添加%s的名片" % dict["name"])


def show_all():

    print("-" * 50)
    print("功能：显示全部")

    # 打印表头
    for name in ["姓名", "电话", "QQ", "邮箱"]:
        print(name,end="\t\t")

    print("")
    # 打印分隔线
    print("=" * 50)
    for val in list:
        print("%s\t\t%s\t\t%s\t\t%s" % (
            val["name"],
            val["phone"],
            val["qq"],
            val["email"]
        ))