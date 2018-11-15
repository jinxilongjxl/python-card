import card_tool

while True:
    card_tool.show_menu()
    action = input("请选择操作功能")

    if action in ["1", "2", "3"]:
        # 新增名片
        if action == "1":
            card_tool.create_card()

        # 显示全部
        if action == "2":
            card_tool.show_all()
    elif action == "0":
        print("欢迎再次使用")
        break
    else:
        print("输入错误，请重新输入")