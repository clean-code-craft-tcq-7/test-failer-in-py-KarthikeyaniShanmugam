from alerter import *
import alerter_config

class Alerter:
    def __init__(self, strategy_env=None):
        self.strategy_env = strategy_env
    def set_environment(self):
        if self.strategy_env:
            print(self.strategy_env())

def testing():
    alert_in_celcius(303.6)  # Celcius threshold : 392   < threshold :  alert False
    alert_in_celcius(392)    # Celcius threshold : 392   = threshold :  alert False 
    alert_in_celcius(400.5)  # Celcius threshold : 392   > threshold : alert True
    print(f'{alerter_config.alert_failure_count} alert greater that threshold.')
    assert(alerter_config.alert_failure_count==1)
    return "Done testing!"

def production():
    return "Production environment is ready!"
     
if __name__ == "__main__":
    # alerter = Alerter(strategy_env=production)
    alerter = Alerter(strategy_env=testing)
    alerter.set_environment()

