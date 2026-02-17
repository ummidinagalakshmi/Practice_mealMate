from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_wordpress_theme_search(setup):
    driver = setup
    wait = WebDriverWait(driver, 30)

    # 1️⃣ Launch URL
    driver.get("https://wordpress.org/")
    assert "WordPress" in driver.title
    print("Title Verified Successfully")

    # 2️⃣ Hover on Extend Menu
    extend_menu = wait.until(EC.presence_of_element_located((By.LINK_TEXT, "Extend")))
    ActionChains(driver).move_to_element(extend_menu).perform()

    # Click Themes
    themes = wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "Themes")))
    themes.click()
    print("Navigated to Themes Page")

    # 3️⃣ Search Theme (input untouched)
    search_box = wait.until(EC.element_to_be_clickable((By.ID, "wp-block-search__input-8")))
    driver.execute_script("arguments[0].scrollIntoView(true);", search_box)
    search_box.clear()
    search_box.send_keys("astra")
    search_box.send_keys(Keys.ENTER)
    print("Searched for Astra theme")
    

    # 4️⃣ Wait until at least one element containing "Astra" appears
    astra_theme = wait.until(
       EC.presence_of_element_located((By.XPATH, "//*[contains(text(), 'Astra')]")))

    # 5️⃣ Collect all theme cards containing "Astra"
    theme_cards = driver.find_elements(
    By.XPATH, "//h2[contains(@class,'wp-block-post-title') and text()='Astra']"
)


    assert len(theme_cards) > 0, "No themes found for 'Astra'"
    print(f"Themes Displayed: {len(theme_cards)}")
    for theme in theme_cards:
        print(theme.text)
