import unittest
import statistics
import math


class EmailAlert:
    emailSent = 0
    
class LEDAlert:    
    ledGlows = 0
    
class StatsAlerter:
    def __init__(self, maxThreshold, alert):
        self.maxThreshold = maxThreshold
        self.emailAlert = alert[0]
        self.ledAlert = alert[1]
    
    def checkAndAlert(self, values):
        self.values = values
        for i in values:
            if i > self.maxThreshold:
                self.emailAlert.emailSent = 1
                self.ledAlert.ledGlows = 1
        
    

class StatsTest(unittest.TestCase):
    def test_report_min_max_avg(self):
        computedStats = {}
        computedStats['avg'] = statistics.mean([1.5, 8.9, 3.2, 4.5])
        computedStats['max'] = max([1.5, 8.9, 3.2, 4.5])
        computedStats['min'] = min([1.5, 8.9, 3.2, 4.5])
        epsilon = 0.001
        self.assertAlmostEqual(computedStats["avg"], 4.525, delta=epsilon)
        self.assertAlmostEqual(computedStats["max"], 8.9, delta=epsilon)
        self.assertAlmostEqual(computedStats["min"], 1.5, delta=epsilon)


    def test_avg_is_nan_for_empty_input(self):
        computedStats = {}
        computedStats['avg'] = math.nan
        computedStats['max'] = math.nan
        computedStats['min'] = math.nan
    
        #Assertion
        self.assertTrue(math.isnan(computedStats['avg']))
        self.assertTrue(math.isnan(computedStats['max']))
        self.assertTrue(math.isnan(computedStats['min']))
        
    def test_raise_alerts_when_max_above_threshold(self):
        emailAlert = EmailAlert()
        ledAlert = LEDAlert()
        maxThreshold = 10.5
        statsAlerter = StatsAlerter(maxThreshold, [emailAlert, ledAlert])
        statsAlerter.checkAndAlert([22.6, 12.5, 3.7])
        self.assertTrue(emailAlert.emailSent)
        self.assertTrue(ledAlert.ledGlows)        

if __name__ == "__main__":
    unittest.main()  
