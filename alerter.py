import alerter_config
def network_alert_stub(celcius):
    print(f'ALERT: Temperature is {celcius} celcius')
    if(celcius <= alerter_config.alert_threshold):
        return 200
    else:
        return 500
def alert_in_celcius(farenheit):
    celcius = (farenheit - 32) * 5 / 9
    returnCode = network_alert_stub(celcius)
    if returnCode != 200:
        alerter_config.alert_failure_count += 1
