class HomePageLocator:
    SEARCH_BAR = '/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input'
    BUTTON_SUBMIT = '/html/body/div[1]/div[3]/form/div[1]/div[1]/div[3]/center/input[1]'


class CalcPageLocator:
    MEMORY_FIELD = '//*[@id="rso"]/div[1]/div/div/div[1]/div/div/div[1]/div[2]/div[1]/div/span'
    RESULT_FIELD = '//*[@id="cwos"]'
    BUTTON_NUM = '//*[@id="rso"]/div[1]/div/div/div[1]/div/div/div[3]/div/table[2]/tbody/tr[4]/td[{}]/div/div'
    # {} here for formatting
    BUTTON_OPER = '//*[@id="rso"]/div[1]/div/div/div[1]/div/div/div[3]/div/table[2]/tbody/tr[{}]/td[4]/div/div'
    # {} here for formatting
    BUTTON_EQUAL = '//*[@id="rso"]/div[1]/div/div/div[1]/div/div/div[3]/div/table[2]/tbody/tr[5]/td[3]/div/div'
