import time
from ..Tests.conftest import Test_BasicTest
from ..Config.config import TestData


class TestMain(Test_BasicTest):
    def test_login(self):
        "Login Page is displayed"
        # self.login_page.register(TestData.USER_NAME, TestData.PASSWORD)
        self.login_page.login(TestData.USER_NAME, TestData.PASSWORD)
        time.sleep(10)
    # #
    def test_dashboard(self):
        "It redirects to Dashboard and fetch all the data and validate the account balance."
        self.dashboard_page.get_all_data()
        self.dashboard_page.account_bal()
        self.dashboard_page.val_account_bal()
        time.sleep(10)

    def test_templates(self):
        "It will select the template."
        self.template_page.templates()
        time.sleep(10)

    def test_recording(self):
        "It will upload the recordings of Greet and Default feedback."
        self.recording_page.recordings()
        time.sleep(10)
    # #
    def test_audience(self):
        "It will create a new record of an audience."
        self.audience_page.create_audience()
        time.sleep(10)

    def test_campaign(self):
        "It will create a new campaign and run the camapign."
        self.campaign_page.create_campaign()
        self.campaign_page.trigger_call()
    #
