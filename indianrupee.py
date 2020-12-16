from getgauge.python import step, before_scenario, Messages

def dollar_to_rupee(dollar):
    dollar = int(dollar)
    rupee = dollar * 74
    return rupee


# --------------------------
# Gauge step implementations
# 

@step("The conversion of <dollar> dollars to rupee is <rupee>")
def assert_dollar_to_rupee(dollar, rupee):
    actual = dollar_to_rupee(dollar)
    assert str(rupee) == str(actual)
    
    
@step("The dollar symbols should be the same for the <symbol> and the unicode value")
def assert_dollar_symbol(symbol):
    #print(symbol)
    unicode_val = u"\u0024" #dollar.  symbol = u"\u00b0" for degree but gives questionmark in a box
    sentence = ("This is the dollar symbol : " + unicode_val)
    #print(sentence)
    assert sentence == "This is the dollar symbol : " + symbol
    

@step("This tests that the unicode value <val> is passed correctly from gauge to the runner and it prints <symbol>")
def assert_same_symbol(val, symbol):
    print("This is the symbol passed : " + symbol + " and this is the Unicode value passed : " + val)
    assert val == symbol
