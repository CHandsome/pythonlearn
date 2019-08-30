card_list = []

def show_menu():
    print("*"*50)
    print("欢迎使用名片管理系统")
    print("")
    print("1. 新增名片")
    print("2. 显示全部")
    print("3. 搜索名片")
    print("")
    print("0. 退出系统")
    print("*"*50)

def new_card():
    print("-"*50)
    print("新增名片")

    name = input("请输入姓名：")
    phone = input("请输入电话：")
    qq = input("请输入qq：")
    email = input("请输入邮箱：")

    card_dist = {
        "name":name,
        "phone":phone,
        "qq":qq,
        "email":email
    }

    card_list.append(card_dist)

    print("添加%s成功"%name)

def show_all():
    print("-" * 50)
    print("显示所有名片")

    if len(card_list) == 0:
        print("没有任何的记录，请增加")
        return

    for name in ["姓名","电话","QQ","邮箱"]:
        print(name,end="\t\t")

    print("")

    print("="*50)

    for card_dict in card_list:
        print("%s\t\t%s\t\t%s\t\t%s"%(card_dict["name"],
                                      card_dict["phone"],
                                      card_dict["qq"],
                                      card_dict["email"]))

def serach_card():
    print("-" * 50)
    print("搜索名片")

    find_str = input("请输入要搜索的名字：")

    for card_dict in card_list:
        if card_dict["name"] == find_str:

            print("姓名\t\t电话\t\tqq\t\t邮箱")

            print("")

            for card_dict in card_list:
                print("%s\t\t%s\t\t%s\t\t%s" % (card_dict["name"],
                                                card_dict["phone"],
                                                card_dict["qq"],
                                                card_dict["email"]))
            deal_card(card_dict)
            break
    else:
        print("没有找到%s"%find_str)

def deal_card(find_dict):
    # print(find_dict)
    action_str = input("请选择：1.修改 2.删除 0.返回上级菜单")

    if action_str == "1":
        find_dict['name'] = input_card_info(find_dict['name'],"姓名：")
        find_dict['phone'] = input_card_info( find_dict['phone'],"电话：")
        find_dict['qq'] = input_card_info( find_dict['qq'],"qq：")
        find_dict['email'] = input_card_info(find_dict['email'],"邮箱：")
        print("修改名片成功")
    elif action_str == "2":
        card_list.remove(find_dict)
        print("删除名片")

def input_card_info(dict_value,tip_message):
    result_str = input(tip_message)

    if len(result_str) > 0:
        return result_str
    else:
        return dict_value