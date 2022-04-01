import time
import typing

from dataclasses import dataclass

from .webdriver import IWebDriver


YOUTUBE_URL = "https://studio.youtube.com"

VIDEO_PATH_SELECTOR = '[name="Filedata"]'
VIDEO_THUMBNAIL_SELECTOR = "#still-picker #file-loader"
VIDEO_TITLE_SELECTOR = "#title-textarea #textbox"
VIDEO_DESCRIPTION_SELECTOR = "#description-container #textbox"
VIDEO_TAGS_SELECTOR = "#chip-bar #text-input"
VIDEO_PUBLIC_BUTTON_SELECTOR = '[name="PUBLIC"] #offRadio'
NOT_FOR_KIDS_SELECTOR = '[name="VIDEO_MADE_FOR_KIDS_NOT_MFK"] #offRadio'
MORE_BUTTON_SELECTOR = "#toggle-button"
NEXT_BUTTON_SELECTOR = "#next-button"
DONE_BUTTON_SELECTOR = "#done-button"
CREATE_VIDEO_BUTTON_SELECTOR = "#create-icon"
UPLOAD_VIDEO_BUTTON_SELECTOR = "#creation-menu #text-item-0"

VIDEO_TAGS_SEPARATOR = ","


@dataclass
class Video:
    path: str
    thumbnail: str

    title: str
    category: str
    description: str
    tags: typing.List[str]

    channel: str | None = None


@dataclass
class YouTubeUploader:
    webdriver: IWebDriver

    def login(self):
        self.webdriver.open_page(YOUTUBE_URL)
        input("Have you logged in successfully?")

    def upload(self, video: Video) -> None:
        if video.channel:
            self.webdriver.open_page(video.channel)
        else:
            self.webdriver.open_page(YOUTUBE_URL)

        time.sleep(5)

        self.webdriver.wait_for_element(CREATE_VIDEO_BUTTON_SELECTOR)
        self.webdriver.click(CREATE_VIDEO_BUTTON_SELECTOR)

        self.webdriver.wait_for_element(UPLOAD_VIDEO_BUTTON_SELECTOR)
        self.webdriver.click(UPLOAD_VIDEO_BUTTON_SELECTOR)

        self.webdriver.set_input_value(VIDEO_PATH_SELECTOR, video.path)
        self.webdriver.wait_for_element(VIDEO_THUMBNAIL_SELECTOR)

        self.webdriver.set_input_value(VIDEO_THUMBNAIL_SELECTOR, video.thumbnail)
        self.webdriver.set_input_value(VIDEO_TITLE_SELECTOR, video.title)
        self.webdriver.set_input_value(VIDEO_DESCRIPTION_SELECTOR, video.description)
        self.webdriver.click(NOT_FOR_KIDS_SELECTOR)
        self.webdriver.click(MORE_BUTTON_SELECTOR)

        for tag in video.tags:
            self.webdriver.set_input_value(VIDEO_TAGS_SELECTOR, tag, False)
            self.webdriver.set_input_value(VIDEO_TAGS_SELECTOR, VIDEO_TAGS_SEPARATOR, False)

        for _ in range(3):
            time.sleep(5)
            self.webdriver.click(NEXT_BUTTON_SELECTOR)

        self.webdriver.click(VIDEO_PUBLIC_BUTTON_SELECTOR)
        time.sleep(5)
        self.webdriver.click(DONE_BUTTON_SELECTOR)
        time.sleep(10)
