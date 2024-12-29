from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import requests

driver = webdriver.Chrome()

url = 'https://www.google.com/maps/search/%D8%B4%D8%B1%D9%83%D8%A7%D8%AA+%D8%A7%D9%84%D8%B1%D9%8A%D8%A7%D8%B6%E2%80%AD%E2%80%AD/@24.222142,45.0740834,2771821m/data=!3m2!1e3!4b1?entry=ttu&g_ep=EgoyMDI0MTIxMS4wIKXMDSoASAFQAw%3D%3D'

driver.get(url)

time.sleep(3)

scrollable_div = driver.find_element(By.CSS_SELECTOR, 'div[role="feed"]')
driver.execute_script("""
          var scrollableDiv = arguments[0];
          function scrollWithinElement(scrollableDiv) {
              return new Promise((resolve, reject) => {
                  var totalHeight = 0;
                  var distance = 1000;
                  var scrollDelay = 3000;
                  
                  var timer = setInterval(() => {
                      var scrollHeightBefore = scrollableDiv.scrollHeight;
                      scrollableDiv.scrollBy(0, distance);
                      totalHeight += distance;

                      if (totalHeight >= scrollHeightBefore) {
                          totalHeight = 0;
                          setTimeout(() => {
                              var scrollHeightAfter = scrollableDiv.scrollHeight;
                              if (scrollHeightAfter > scrollHeightBefore) {
                                  return;
                              } else {
                                  clearInterval(timer);
                                  resolve();
                              }
                          }, scrollDelay);
                      }
                  }, 200);
              });
          }
          return scrollWithinElement(scrollableDiv);
  """, scrollable_div)

result_urls = driver.find_elements(By.CSS_SELECTOR, '.hfpxzc')


print(len(result_urls))

driver.quit()