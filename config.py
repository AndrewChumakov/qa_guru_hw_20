import os
from dotenv import load_dotenv
from appium.options.android import UiAutomator2Options

from utils.file import abs_path_from_project


def to_driver_options(context):
    options = UiAutomator2Options()

    if context == "local_emulator":
        options.set_capability("remote_url", os.getenv("REMOTE_URL"))
        options.set_capability("deviceName", os.getenv("DEVICE_NAME"))
        options.set_capability("appWaitActivity", os.getenv("APP_WAIT_ACTIVITY"))
        options.set_capability("app", abs_path_from_project(os.getenv("APP")))
        options.set_capability("appActivity", os.getenv("APP_ACTIVITY"))

    if context == "local_real":
        options.set_capability("remote_url", os.getenv("REMOTE_URL"))
        options.set_capability("deviceName", os.getenv("DEVICE_NAME"))
        options.set_capability("appWaitActivity", os.getenv("APP_WAIT_ACTIVITY"))
        options.set_capability("app", abs_path_from_project(os.getenv("APP")))
        options.set_capability("appActivity", os.getenv("APP_ACTIVITY"))
        options.set_capability("language", os.getenv("LANGUAGE"))
        options.set_capability("locale", os.getenv("LOCALE"))

    if context == "bstack":
        options.set_capability("remote_url", os.getenv("REMOTE_URL"))
        options.set_capability("deviceName", os.getenv("DEVICE_NAME"))
        options.set_capability("platformName", os.getenv("PLATFORM_NAME"))
        options.set_capability("platformVersion", os.getenv("PLATFORM_VERSION"))
        options.set_capability("appWaitActivity", os.getenv("APP_WAIT_ACTIVITY"))
        options.set_capability("app", os.getenv("APP"))
        load_dotenv(dotenv_path=abs_path_from_project(".env"))
        options.set_capability(
            "bstack:options", {
                "projectName": "Wikipedia project",
                "buildName": "browserstack-build-1",
                "sessionName": "BStack test",
                "userName": os.getenv("USER"),
                "accessKey": os.getenv("KEY"),
            },
        )

    return options