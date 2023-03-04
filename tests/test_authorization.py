class TestAuthorization:

    def test_login_correct(self, open_login_page):
        open_login_page.fill_authorization_form()
        open_login_page.submit_authorization()
        assert open_login_page.get_current_url() in ['http://localhost/dashboard', 'http://localhost:80/dashboard']
        assert open_login_page.get_alert().text == f'Successful authorization. Greets you, {open_login_page.login}.'

    def test_login_incorrect(self, open_login_page):
        open_login_page.fill_authorization_form_incorrect()
        open_login_page.submit_authorization()
        assert open_login_page.get_current_url() in ['http://localhost/sign-in', 'http://localhost:80/sign-in']
        assert open_login_page.get_alert().text == 'Invalid credentials, try again please'

    def test_logout(self, authorization):
        authorization.logout()
        assert authorization.get_current_url() in ['http://localhost/sign-in', 'http://localhost:80/sign-in']
        assert authorization.get_alert().text == "Logged Out"






