from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import unittest


class NewVisitorTest(unittest.TestCase):

    def setUp(self):
        """初始化浏览器实例"""
        self.browser = webdriver.Firefox()
        self.browser.implicitly_wait(3)

    def tearDown(self):
        """退出浏览器"""
        self.browser.quit()

    def test_can_start_a_list_and_retrieve_it_later(self):
        # 伊迪斯听说有一个很酷的在线待办项应用
        # 她去首页看了这个应用的首页
        self.browser.get('http://localhost:8000/home_page/')

        # 她注意到网页的标题和头部都包含 “To-Do” 这个词
        self.assertIn('To-Do', self.browser.title)
        header_text = self.browser.find_element(By.TAG_NAME, 'h1').text
        self.assertIn('To-Do', header_text)

        # 应用邀请她输入一个代表事项
        input_box = self.browser.find_element(By.ID, 'id_new_item')
        self.assertEqual(
            input_box.get_attribute('placeholder'),
            'Enter a to-do item'
        )

        # 她在一个文本框中输入了 "Buy peacock feathers"
        # 伊迪斯的爱好是使用假蝇饵作为饵钓鱼
        input_box.send_keys('Buy peacock feathers')

        # 她按回车键后，页面更新了
        # 代表事项表格中显示了"1: Buy peacock feathers"
        input_box.send_keys(Keys.ENTER)
        table = self.browser.find_element(By.ID, 'id_list_table')
        rows = table.find_element(By.TAG_NAME, 'tr')
        self.assertTrue(
            any(row.text == '1: Buy peacock feathers' for row in rows)
        )

        self.fail("Finish the test!")
        # 页面中又显示了一个文本框，可以输入其他的代表事项
        # 她输入了 “Use peacock feathers to make a fly”
        # 伊迪斯做事很有条理

        # 页面再次更新，她的清单中显示了这两个待办事项

        # 伊迪斯想知道这个网站是否会记住她的清单

        # 她看到网站为她生成了一个唯一的 URL

        # 而且也没中有一些文字解说这个功能

        # 她访问那个 URL ，发现他的代办事项列表还在

        # 她很满意，去睡觉了


if __name__ == "__main__":
    unittest.main()
