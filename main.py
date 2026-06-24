
import flet as ft

icons_path = ["./icon_svg/google-plus-g.svg",
              "./icon_svg/facebook-f.svg",
              "./icon_svg/github.svg",
              "./icon_svg/linkedin-in.svg"]

def social_icons():
    return ft.Row(
        spacing=20,
        controls=[
            ft.Container(
                width=40,
                height=40,
                border=ft.Border.all(1, ft.Colors.GREY),
                border_radius=10,
                padding=ft.Padding.all(10),
                content=ft.Image(src=path),
            )
            for path in icons_path
        ],
        alignment=ft.MainAxisAlignment.CENTER
    )


def toggle_view(page: ft.Page, container: ft.Container, target_view: str):
    """切换视图 - 实现滑动动画 """
    stack = container.content
    if not isinstance(stack, ft.Stack):
        return

    # 获取四个面板
    sign_in_form = stack.controls[0]
    sign_up_form = stack.controls[1]
    sign_up_panel = stack.controls[2]
    sign_in_panel = stack.controls[3]

    if target_view == "sign_in":
        # 切换到登录：整体向左滑动
        sign_in_form.offset = ft.Offset(0, 0)    # 登录表单在左
        sign_up_form.offset = ft.Offset(1, 0)    # 注册表单在右（隐藏）
        sign_up_panel.offset = ft.Offset(0, 0)   # 紫色面板在右
        sign_in_panel.offset = ft.Offset(-1, 0)  # 紫色面板在左（隐藏）
    else:
        # 切换到注册：整体向右滑动
        sign_in_form.offset = ft.Offset(-1, 0)   # 登录表单在左（隐藏）
        sign_up_form.offset = ft.Offset(0, 0)    # 注册表单在左
        sign_up_panel.offset = ft.Offset(1, 0)   # 紫色面板在右（隐藏）
        sign_in_panel.offset = ft.Offset(0, 0)   # 紫色面板在左

    page.update()


def login_and_register(page: ft.Page, main_container: ft.Container):
    """ 创建登录注册页面 """

    # 登录表单
    sign_in_form = ft.Container(
        width=400,
        height=460,
        bgcolor=ft.Colors.WHITE,
        padding=ft.Padding(40, 20, 40, 20),
        content=ft.Column(
            spacing=20,
            controls=[
                ft.Text("登 录", size=40, weight=ft.FontWeight.BOLD),
                social_icons(),
                ft.Text("或者使用你的邮箱登录", size=15),
                ft.TextField(label="Email", width=250, height=36),
                ft.TextField(label="Password", password=True, can_reveal_password=True, width=250, height=36),
                ft.Text("忘记你的密码？", size=15),
                ft.Button(
                    content=ft.Text("登" + " " * 8 + "录", size=20, weight=ft.FontWeight.BOLD),
                    bgcolor="#5137aa",
                    color="#ffffff",
                    style=ft.ButtonStyle(
                        shape=ft.RoundedRectangleBorder(radius=10),
                        padding=ft.Padding(20, 15, 20, 15),
                        side=ft.BorderSide(width=0),
                        elevation=5,
                    ),
                    width=200,
                    height=50,
                    on_click=lambda e: print("Signing up----------------------"),
                )
            ],
            alignment=ft.MainAxisAlignment.CENTER,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        )
    )

    # 注册表单
    sign_up_form = ft.Container(
        width=400,
        height=460,
        bgcolor=ft.Colors.WHITE,
        padding=ft.Padding(40, 20, 40, 20),
        content=ft.Column(
            spacing=20,
            controls=[
                ft.Text("创 建 账 号", size=36, weight=ft.FontWeight.BOLD),
                social_icons(),
                ft.Text("或者使用你的邮箱注册", size=15),
                ft.TextField(label="Name", width=250, height=36),
                ft.TextField(label="Email", width=250, height=36),
                ft.TextField(label="Password", password=True, can_reveal_password=True, width=250, height=36),
                ft.Button(
                    content=ft.Text("注" + " " * 8 + "册", size=20, weight=ft.FontWeight.BOLD),
                    bgcolor="#5137aa",
                    color="#ffffff",
                    style=ft.ButtonStyle(
                        shape=ft.RoundedRectangleBorder(radius=10),
                        padding=ft.Padding(20, 15, 20, 15),
                        side=ft.BorderSide(width=0),
                        elevation=5,
                    ),
                    width=200,
                    height=50,
                    on_click=lambda e: print("Registering-------------------------"),
                )
            ],
            alignment=ft.MainAxisAlignment.CENTER,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        )
    )

    # 切换为注册页面  (右侧)
    sign_up_panel = ft.Container(
        width=400,
        height=460,
        bgcolor="#5445b1",
        border_radius=ft.BorderRadius(
            top_left=100,
            top_right=20,
            bottom_left=100,
            bottom_right=20,
        ),
        padding=20,
        content=ft.Column(
            spacing=40,
            controls=[
                ft.Text("Hello, Friend !", size=36, weight=ft.FontWeight.BOLD, color="#ffffff"),
                ft.Text("注册您的个人资料，即可进入网站", size=15, color="#ffffff"),
                ft.Button(
                    content=ft.Text("注" + " " * 8 + "册", size=20, weight=ft.FontWeight.BOLD),
                    bgcolor="#5137aa",
                    color="#ffffff",
                    style=ft.ButtonStyle(
                        shape=ft.RoundedRectangleBorder(radius=10),
                        padding=ft.Padding(20, 15, 20, 15),
                        side=ft.BorderSide(width=1, color=ft.Colors.WHITE),
                        elevation=8,
                    ),
                    width=200,
                    height=50,
                    on_click=lambda e: toggle_view(page, main_container, "sign_up"),
                )
            ],
            alignment=ft.MainAxisAlignment.CENTER,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        )
    )

    # 切换为登录页面 (左侧)
    sign_in_panel = ft.Container(
        width=400,
        height=460,
        bgcolor="#5445b1",
        border_radius=ft.BorderRadius(
            top_left=20,
            top_right=100,
            bottom_left=20,
            bottom_right=100,
        ),
        padding=20,
        content=ft.Column(
            spacing=40,
            controls=[
                ft.Text("Welcome Back !", size=36, weight=ft.FontWeight.BOLD, color="#ffffff"),
                ft.Text("请输入您的个人信息,以使用网站的全部功能", size=15, color="#ffffff"),
                ft.Button(
                    content=ft.Text("登" + " " * 8 + "录", size=20, weight=ft.FontWeight.BOLD),
                    bgcolor="#5137aa",
                    color="#ffffff",
                    style=ft.ButtonStyle(
                        shape=ft.RoundedRectangleBorder(radius=10),
                        padding=ft.Padding(20, 15, 20, 15),
                        side=ft.BorderSide(width=1, color=ft.Colors.WHITE),
                        elevation=8,
                    ),
                    width=200,
                    height=50,
                    on_click=lambda e: toggle_view(page, main_container, "sign_in"),
                )
            ],
            alignment=ft.MainAxisAlignment.CENTER,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        )
    )

    # Stack 叠加所有面板
    return ft.Stack(
        width=800,
        height=460,
        controls=[
            ft.Container(
                content=sign_in_form,
                width=400,
                height=460,
                left=0,
                top=0,
                animate_offset=ft.Animation(600, ft.AnimationCurve.EASE_IN_OUT),
                offset=ft.Offset(0, 0),
            ),
            ft.Container(
                content=sign_up_form,
                width=400,
                height=460,
                left=400,
                top=0,
                animate_offset=ft.Animation(600, ft.AnimationCurve.EASE_IN_OUT),
                offset=ft.Offset(1, 0),
            ),
            ft.Container(
                content=sign_up_panel,
                width=400,
                height=460,
                left=400,
                top=0,
                animate_offset=ft.Animation(600, ft.AnimationCurve.EASE_IN_OUT),
                offset=ft.Offset(0, 0),
            ),
            ft.Container(
                content=sign_in_panel,
                width=400,
                height=460,
                left=0,
                top=0,
                animate_offset=ft.Animation(600, ft.AnimationCurve.EASE_IN_OUT),
                offset=ft.Offset(-1, 0),
            ),
        ]
    )


def main(page: ft.Page):
    page.title = "登录 注册"
    page.padding = 0
    page.theme_mode = ft.ThemeMode.LIGHT
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER

    # 创建主容器
    main_container = ft.Container(
        width=800,
        height=460,
        bgcolor="#ffffff",
        border_radius=ft.BorderRadius.all(20),
        shadow=ft.BoxShadow(
            blur_radius=20,
            spread_radius=2,
            color=ft.Colors.with_opacity(0.3, ft.Colors.BLACK),
            offset=ft.Offset(0, 4),
        ),
        clip_behavior=ft.ClipBehavior.HARD_EDGE,
    )

    # 设置页面内容
    main_container.content = login_and_register(page, main_container)

    page.add(main_container)


if __name__ == "__main__":
    ft.run(main)