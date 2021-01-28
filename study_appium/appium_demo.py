#导入包
from appium import webdriver

#设置desired capabilities
from selenium.webdriver.common.by import By

desired_caps={}
desired_caps['platformName']='Android'
desired_caps['deviceName']='127.0.0.1:7555'
desired_caps['appPackage']='com.xueqiu.android'
desired_caps['appActivity']='.view.WelcomeActivityAlias'
desired_caps['noReset']=True
desired_caps['dontStopAppOnReset']=True  #首次启动的时候，不停止APP，方便进行调试
desired_caps['skipDeviceInitialization']=True   #跳过安装，权限设置等操作
#print(desired_caps)

#创建driver对象
driver=webdriver.Remote('http://127.0.0.1:4723/wd/hub',desired_caps)
driver.implicitly_wait(60)


# el6 = driver.find_element_by_id("com.xueqiu.android:id/home_search")
# el6.click()
# el7 = driver.find_element_by_id("com.xueqiu.android:id/search_input_text")
# el7.send_keys("123")
# el8 = driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.RelativeLayout/android.widget.FrameLayout/android.widget.LinearLayout/androidx.recyclerview.widget.RecyclerView/android.widget.RelativeLayout[1]/android.widget.LinearLayout/android.widget.TextView[1]")
# el8.click()
#
# driver.back()
try:
    el=driver.find_elements(By.XPATH,'//*[@text="行情"]')
except Exception as e:
    print("未找到")
#driver.quit()