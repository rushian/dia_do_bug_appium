# This sample code uses the Appium python client v2
# pip install Appium-Python-Client
# Then you can paste this into a file and simply run with Python

from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy

# For W3C actions
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.actions import interaction
from selenium.webdriver.common.actions.action_builder import ActionBuilder
from selenium.webdriver.common.actions.pointer_input import PointerInput
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

caps = {}
caps["platformName"] = "Android"
caps["appium:automationName"] = "uiautomator2"
caps["appium:deviceName"] = "emulator-5554"
caps["appium:appPackage"] = "com.gta.demoapp"
caps["appium:appActivity"] = "com.gta.demoapp.view.MainActivity"
caps["appium:avd"] = "Pixel2"
caps["appium:deviceOrientation"] = "portrait"
caps["appium:ensureWebviewsHavePages"] = True
caps["appium:nativeWebScreenshot"] = True
caps["appium:newCommandTimeout"] = 3600
caps["appium:connectHardwareKeyboard"] = True

driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", caps)


tempo = 3
resultado_esperado = 'Thank you for your purchase!'
# deslizar até a blusa presa
actions = ActionChains(driver)
actions.w3c_actions = ActionBuilder(driver, mouse=PointerInput(interaction.POINTER_TOUCH, "touch"))
actions.w3c_actions.pointer_action.move_to_location(900,600)
actions.w3c_actions.pointer_action.pointer_down()
actions.w3c_actions.pointer_action.move_to_location(200,600)
actions.w3c_actions.pointer_action.release()
actions.w3c_actions.pointer_action.pause(2)
actions.perform()

actions = ActionChains(driver)
actions.w3c_actions = ActionBuilder(driver, mouse=PointerInput(interaction.POINTER_TOUCH, "touch"))
actions.w3c_actions.pointer_action.move_to_location(900,600)
actions.w3c_actions.pointer_action.pointer_down()
actions.w3c_actions.pointer_action.move_to_location(200,600)
actions.w3c_actions.pointer_action.release()
actions.w3c_actions.pointer_action.pause(2)
actions.perform()

WebDriverWait(driver, tempo).until(lambda driver:  driver.find_element(by=AppiumBy.XPATH,
                                                                       value="(//android.widget.ImageView[@content-desc=\"img\"])[3]"))
# clicar na blusa presa
el1 = driver.find_element(by=AppiumBy.XPATH, value="(//android.widget.ImageView[@content-desc=\"img\"])[3]")
el1.click()

WebDriverWait(driver, tempo).until(lambda driver:  driver.find_element(by=AppiumBy.ID, value="com.gta.demoapp:id/quantity_selector"))
# abrir quantidade de blusas
el2 = driver.find_element(by=AppiumBy.ID, value="com.gta.demoapp:id/quantity_selector")
el2.click()

WebDriverWait(driver, tempo).until(lambda driver:  driver.find_element(by=AppiumBy.XPATH,
                          value="/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.ListView/android.widget.CheckedTextView[2]"))
# escolher quantidade 2
el3 = driver.find_element(by=AppiumBy.XPATH,
                          value="/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.ListView/android.widget.CheckedTextView[2]")
el3.click()

WebDriverWait(driver, tempo).until(lambda driver:  driver.find_element(by=AppiumBy.ID, value="com.gta.demoapp:id/button"))
# clicar em adicionar ao carrinho
el4 = driver.find_element(by=AppiumBy.ID, value="com.gta.demoapp:id/button")
el4.click()

WebDriverWait(driver, tempo).until(lambda driver:  driver.find_element(by=AppiumBy.ID, value="android:id/button2"))
# clicar em continuar comprando
el5 = driver.find_element(by=AppiumBy.ID, value="android:id/button2")
el5.click()

#WebDriverWait(driver, tempo).until(lambda driver:  driver.find_element(by=AppiumBy.XPATH,
#                          value="/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout[1]/android.view.ViewGroup/android.widget.TextView"))

#el6 = driver.find_element(by=AppiumBy.XPATH,
#                         value="/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout[1]/android.view.ViewGroup/android.widget.TextView")
#el6.click()

WebDriverWait(driver, tempo).until(lambda driver:  driver.find_element(by=AppiumBy.XPATH, value="(//android.widget.ImageView[@content-desc=\"img\"])[4]"))
# clicar na agenda azul

el7 = driver.find_element(by=AppiumBy.XPATH, value="(//android.widget.ImageView[@content-desc=\"img\"])[4]")
el7.click()

WebDriverWait(driver, tempo).until(lambda driver:  driver.find_element(by=AppiumBy.ID, value="com.gta.demoapp:id/button"))
# clicar em adicionar ao carrinho
el8 = driver.find_element(by=AppiumBy.ID, value="com.gta.demoapp:id/button")
el8.click()

WebDriverWait(driver, tempo).until(lambda driver:  driver.find_element(by=AppiumBy.ID, value="android:id/button1"))
# clicar em ir ao carrinho
el9 = driver.find_element(by=AppiumBy.ID, value="android:id/button1")
el9.click()

WebDriverWait(driver, tempo).until(lambda driver:  driver.find_element(by=AppiumBy.ID, value="com.gta.demoapp:id/emptycart"))

el11 = driver.find_element(by=AppiumBy.XPATH,
                           value="/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout[2]/android.widget.ScrollView/android.view.ViewGroup/android.support.v7.widget.RecyclerView/android.view.ViewGroup[2]/android.widget.TextView[2]")

assert '$12.99' == el11.text
print('Valor da agenda ', repr(el11.text))
WebDriverWait(driver, tempo).until(lambda driver:  driver.find_element(by=AppiumBy.ID, value="com.gta.demoapp:id/checkout_btn"))
# clicar em prosseguir pra checkout
el12 = driver.find_element(by=AppiumBy.ID, value="com.gta.demoapp:id/checkout_btn")
el12.click()

# Verificar se mensagem de agradecimento foi exibida
WebDriverWait(driver, tempo).until(lambda driver:  driver.find_element(by=AppiumBy.ID, value="com.gta.demoapp:id/textView2"))
el13 = driver.find_element(by=AppiumBy.ID, value="com.gta.demoapp:id/textView2")
assert resultado_esperado == el13.text
print('\nTexto exibido ', repr(el13.text))
#WebDriverWait(driver, tempo)
#el14 = driver.find_element(by=AppiumBy.ID, value="com.gta.demoapp:id/BACK")
#el14.click()

#driver.quit()