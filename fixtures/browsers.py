import os
import re
import allure
import pytest
from _pytest.fixtures import SubRequest
from playwright.sync_api import Playwright, Page
from config import settings
def sanitize_filename(name: str) -> str:
    return re.sub(r'[<>:"/\\|?*\n\r\t]', '_', name)

@pytest.fixture
def chromium_page(request: SubRequest, playwright: Playwright) -> Page:
    browser = playwright.chromium.launch(headless=settings.headless)
    context = browser.new_context(record_video_dir=settings.videos_dir)
    context.tracing.start(screenshots=True, snapshots=True, sources=True)
    page = context.new_page()
    yield page

    sanitized_name = sanitize_filename(request.node.name)
    trace_path = os.path.join('tracing', f'{sanitized_name}.zip')

    context.tracing.stop(path=trace_path)
    browser.close()
    allure.attach.file(trace_path, name='trace', extension='zip')
    allure.attach.file(page.video.path(), name='video', attachment_type=allure.attachment_type.WEBM)