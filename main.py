import flet as ft
from app_layout import AppLayout
from flet import (
    AlertDialog,
    AppBar,
    Column,
    Container,
    ElevatedButton,
    Icon,
    Page,
    PopupMenuButton,
    PopupMenuItem,
    TemplateRoute,
    Text,
    TextField,
    UserControl,
    View,
    colors,
    icons,
    margin,
    padding,
    theme,
    IconButton,
)
from user import User
from google_auth import GoogleOAuth
from switch_right_dark import ToggleDarkLight


class CloudflareD1(UserControl):
    def __init__(self, page: Page,):
        super().__init__()
        self.page = page
        page.theme_mode = "light"
        page.bgcolor = ft.colors.TRANSPARENT
        self.page.on_route_change = self.route_change
        self.login_profile_button = PopupMenuItem(
            text="Log in", )
        # on_click=self.login
        menu_button = IconButton(icons.MENU, icon_color=ft.colors.WHITE)
        self.menu_button = menu_button
        self.appbar = AppBar(
            title=Text(f"Seminar App", size=32, color=ft.colors.WHITE),
            leading=menu_button,
            center_title=True,
            leading_width=40,
            toolbar_height=70,
            bgcolor=ft.colors.BLUE_ACCENT_700
        )
        self.page.appbar = self.appbar
        self.page.appbar.actions = []
        # ToggleDarkLight(page, page.appbar.actions)
        GoogleOAuth(page, page.appbar.actions)
        self.page.update()

    def build(self):
        layout = AppLayout(
            self,
            self.page,
            tight=True,
            expand=True,
            vertical_alignment="start",
        )
        self.menu_button.on_click = lambda e: layout.toggle_navigation()
        self.layout = layout
        return self.layout

    def initialize(self):
        self.page.views.clear()
        self.page.views.append(
            View(
                "/",
                [self.appbar, self.layout],
                padding=padding.all(0),
                # bgcolor=colors.BLUE_GREY_200,
            )
        )
        self.page.update()
        self.page.go("/")

    def route_change(self, e):
        troute = TemplateRoute(self.page.route)
        if troute.match("/"):
            self.page.go("/top")
        elif troute.match("/top"):
            self.layout.set_top_view()
        elif troute.match("/seminars"):
            self.layout.set_seminars_view()
        elif troute.match("/add-form"):
            self.layout.set_add_form_view()
        elif troute.match("/setting-account"):
            self.layout.set_setting_view()
        elif troute.match("/temp"):
            self.layout.temp_create_view()
        self.page.update()

def main(page: Page):
    page.title = "Flet Seminar App"
    page.padding = 0
    page.theme = theme.Theme(font_family="Verdana")
    page.theme.page_transitions.windows = "cupertino"
    # page.fonts = {"Pacifico": "Pacifico-Regular.ttf"}
    page.bgcolor = colors.BLUE_GREY_200
    app = CloudflareD1(page)
    page.add(app)
    page.update()
    app.initialize()


# ft.app(target=main, assets_dir="../assets")
ft.app(target=main, port=8550, assets_dir="assets")
