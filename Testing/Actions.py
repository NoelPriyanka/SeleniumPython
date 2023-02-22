from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.support.color import Color
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select
import time

#serv_obj = Service("/usr/local/bin/chromedriver.exec")
#driver = webdriver.Chrome(service=Service('/usr/local/bin/chromedriver.exec'))
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.implicitly_wait(10)
mywait=WebDriverWait(driver,10)
driver.get("https://example.cypress.io/commands/actions")
driver.maximize_window()
print("Maximised the window")

#To type the email Address
eid=driver.find_element(By.ID,"email1")
eid.send_keys("fake@email.com")
print("Type the email Address")

#To Type special character sequences
act=ActionChains(driver)
act.key_down(Keys.COMMAND).send_keys("a").key_up(Keys.COMMAND).perform()
act.key_down(Keys.DELETE).key_up(Keys.DELETE).perform()
act.key_down(Keys.ARROW_LEFT).key_down(Keys.ARROW_LEFT).perform()
act.key_down(Keys.ARROW_RIGHT).key_down(Keys.ARROW_RIGHT).perform()
act.key_down(Keys.ARROW_UP).key_down(Keys.ARROW_UP).perform()
act.key_down(Keys.ARROW_DOWN).key_down(Keys.ARROW_DOWN).perform()
print("Typed special character sequences")

#To Type with key modifiers
act.key_down(Keys.ALT).key_down(Keys.ALT).perform()
act.key_down(Keys.CONTROL).key_down(Keys.CONTROL).perform()
act.key_down(Keys.COMMAND).key_down(Keys.COMMAND).perform()
act.key_down(Keys.SHIFT).key_down(Keys.SHIFT).perform()
print("Typed with key modifiers")




#Delay each keypress by 0.1 sec
text = " slow.typing@email.com"
for character in text:
    eid.send_keys(character)
    time.sleep(0.1)
print("Delayed each keypress by 0.1 sec")

#To focus on a element
password=driver.find_element(By.ID,"password1")
password.send_keys(" ")
print("Focused on the element")


#Not Coded yet
#String visibilityAfter =driver.findElement(By.ID, "password").getCssValue("color: orange");
#print(visibilityAfter)

#rgb = password.value_of_css_property('color: orange;')
#hex = Color.from_string(rgb).hex
#print("Colour:", hex)
#Not Code


#Blur

#JavascriptExecutor js = (JavascriptExecutor) driver
 #       StringBuilder stringBuilder = new StringBuilder()
  #      stringBuilder.append("var x = driver.find_element(By.CSS_SELECTOR,".action-blur")")
 #       stringBuilder.append("x.blur();")
   #     js.executeScript(stringBuilder.toString());


#To Clear
toclear=driver.find_element(By.CSS_SELECTOR,".action-clear")
toclear.send_keys("To Clear")
print("To Clear")
toclear.clear()
print("Cleared")


#Submit
btnsubmit=driver.find_element(By.CSS_SELECTOR,".action-form")
btnsubmit.submit()
#assert btnsubmit.text == "Your form has been submitted!"


#To click
btn=mywait.until(EC.presence_of_element_located((By.CLASS_NAME,"action-btn")))
btn.click()
btn1=mywait.until(EC.presence_of_element_located((By.ID,"action-canvas")))
btn1.click()
#btn2=mywait.until(EC.presence_of_element_located((By.ID,"action-labels")))
act.move_to_element_with_offset(btn1, 80, 75).click().perform()
act.move_to_element_with_offset(btn1, 170, 75).click().perform()
print("clicked")
act.move_to_element_with_offset(btn1, 55, 55).click().perform()
act.move_to_element_with_offset(btn1, 100, 75).click().perform()
act.move_to_element_with_offset(btn1, 125, 75).click().perform()
act.move_to_element_with_offset(btn1, 150, 75).click().perform()
act.move_to_element_with_offset(btn1, 170, 75).click().perform()
print("Clicked on the button")


#To double Click
#tbox=driver.find_element(By.CLASS_NAME,"action-div")
#tbox=mywait.until(EC.presence_of_element_located((By.XPATH,"//input[@value='Double click to edit']")))
#act.double_click(tbox).perform()
#print("Double Clicked on the box")



#To RightClick
#box=WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//input[@value='Right click to edit']")))

box=driver.find_element(By.CSS_SELECTOR,".action-div")
#driver.execute_script("window.scrollBy(0,500)","")
#driver.execute_script("arguments[0].scrollIntoView()", box)
act.context_click(box).perform()
box.click()
print("Right Clicked on the box")



#Checkbox
#def scroll_shim(passed_in_driver, object):
 #   x = object.location['x']
 #   y = object.location['y']
 #   scroll_by_coord = 'window.scrollTo(%s,%s);' % (
 #       x,
 #       y
 #   )
  #  scroll_nav_out_of_way = 'window.scrollBy(0, -120);'
  #  passed_in_driver.execute_script(scroll_by_coord)
  #  passed_in_driver.execute_script(scroll_nav_out_of_way)


chk=driver.find_element(By.XPATH,"//div[@class='action-checkboxes']//div[1]//label[1]//input[1]")
#chk=mywait.until(EC.presence_of_element_located((By.CSS_SELECTOR,".action-checkboxes[type='checkbox']")))
chk.click()
print("Checked the checkbox")

#Check multiple checkboxes
checkboxes=driver.find_elements(By.CSS_SELECTOR,".action-multiple-checkboxes [type='checkbox']")
print(len(checkboxes))
for i in range(len(checkboxes)):
    checkboxes[i].click()
print("Checked multiple checkboxes")

#uncheck checkboxes
checkboxes=driver.find_elements(By.CSS_SELECTOR,".action-check [type='checkbox']")
print(len(checkboxes))
for i in range(len(checkboxes)):
    checkboxes[i].click()
print("Checked multiple checkboxes")

for checkbox in checkboxes:
    if checkbox.is_selected():
        checkbox.click()
print("Unchecked all checkboxes")

#Radio Button
chk1=driver.find_element(By.ID,"optionsRadios1")
#chk=mywait.until(EC.presence_of_element_located((By.CSS_SELECTOR,".action-checkboxes[type='checkbox']")))
chk1.click()
print("Clicked on radio button")

#Select from dropdown
#drp=driver.find_element(By.CSS_SELECTOR, ".action-select")
drp=Select(driver.find_element(By.CSS_SELECTOR, ".action-select"))
drp.select_by_visible_text("apples")
print("Selected Apples from the dropdown")




#ScrollIntoView

scrllh=driver.find_element(By.CSS_SELECTOR, '#scroll-horizontal button')
driver.execute_script("arguments[0].scrollIntoView();",scrllh)
#value=driver.execute_script("Return window.pageXOffset;")
#print("Number of pixels moved:", value)
print("Scrolled Horrizontally")

scrllv=driver.find_element(By.CSS_SELECTOR, '#scroll-vertical button')
driver.execute_script("arguments[0].scrollIntoView();",scrllv)
print("Scrolled Vertically")

scrllboth=driver.find_element(By.CSS_SELECTOR, '#scroll-both button')
driver.execute_script("arguments[0].scrollIntoView();",scrllboth)
print("Scrolled both ways")

#Trigger

slider=driver.find_element(By.CSS_SELECTOR, ".trigger-input-range")
print("Location of sliders before moving")
print(slider.location)
#act.drag_and_drop_by_offset(slider,900,0).perform()
#print("Location of sliders after moving")
#print(slider.location)