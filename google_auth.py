import flet as ft
from flet import (
    Container,
    ElevatedButton,
    Page,
)
from flet.auth.providers import GoogleOAuthProvider
import os
from dotenv import load_dotenv
load_dotenv()

ClientID = os.getenv('ClientID')
ClientSecret = os.getenv('ClientSecret')
RedirectUrl= os.getenv('RedirectUrl')

class GoogleOAuth():
    def __init__(
        self,
        page: Page,
        contents: list,
        * args,
        **kwargs,
    ):
        super().__init__(*args, **kwargs)

        self.page = page

        # GoogleOAuthのProvider定義
        provider = GoogleOAuthProvider(
            client_id=ClientID,
            client_secret=ClientSecret,
            redirect_url=RedirectUrl
        )

        # ログイン処理
        def login_google(e):
            self.page.login(provider)
            # page.session.set("auth", True)

        # ログアウト処理
        def logout_google(e):
            self.page.logout()

        # ログインボタン
        login_button = Container(
            content=ElevatedButton(
                "Sign in Google", bgcolor=ft.colors.LIGHT_BLUE_500, color=ft.colors.WHITE, on_click=login_google,
            ),
            margin=ft.margin.only(right=10)
        )

        # ログアウトボタン
        logout_button = Container(
            content=ElevatedButton(
                "Sign out Google", bgcolor=ft.colors.RED_300, color=ft.colors.WHITE, on_click=logout_google),
            margin=ft.margin.only(right=10)
        )

        def on_login(e):
            # print(page.auth.user['name'], page.auth.user['email'])
            contents.pop()
            # 画面に表示するボタンを「ログアウト」ボタンに
            log_inout_button = logout_button
            contents.append(log_inout_button)
            page.update()
            page.go('/')

        def on_logout(e):
            contents.pop()
            log_inout_button = login_button
            contents.append(log_inout_button)
            page.update()
            page.go('/logout')

        page.on_login = on_login
        page.on_logout = on_logout
        # 画面に表示するボタンを「ログイン」ボタンに
        log_inout_button = login_button
        contents.append(log_inout_button)

# reference
# https://www.youtube.com/watch?v=t9ca2jC4YTo
