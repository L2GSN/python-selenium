def alert_assert (case_order,alert_text):
    if wd.switch_to.alert.text == alert_text:
        wd.switch_to.alert.accept()
        print(case_order + ': PASS')

    else:
        print(wd.switch_to.alert.text)
