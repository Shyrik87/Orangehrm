import pytest
from requests import options
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

@pytest.fixture(scope="function", autouse=True)
def driver(request):
	options = Options()
	# options.add_argument("--headless")
	options.add_argument("--no-sandbox")
	options.add_argument("--disable-dev-shm-usege")
	driver = webdriver.Chrome(options=options)
	request.cls.driver = driver
	yield driver
	driver.quit()
# end def