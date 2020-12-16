from getgauge.python import step, before_scenario, Messages

def add_nums(a,b):
    sum = int(a) + int(b)
    return (sum)

# --------------------------
# Gauge step implementations
# --------------------------

@step("The sum of <a> and <b> is <c>.")
def assert_sum(a,b,c):
    sum1 = add_nums(a,b)
    assert str(c) == str(sum1)
    
    
    
        
    

    
    
