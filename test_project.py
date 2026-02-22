import pytest
import pandas as pd
from project import check_valid_date, getpercentage, no_duplicate

def test_check_valid_date():

    assert check_valid_date(2000,12,2) is True
    assert check_valid_date(2000,15,2) is False
    assert check_valid_date(2000,12,200) is False
    assert check_valid_date(0,12,2) is False

def test_getpercentage():
    
    assert getpercentage(50,100) == 50.00
    assert getpercentage(0,100) == 0.00
    assert getpercentage(50,0) == 0.0

def test_no_duplicate():
    
    inputdata = ["Utilities", "Groceries", "Utilities", "Dining Out"]
    outputdata = ["Dining Out", "Groceries", "Utilities"]
    assert no_duplicate(inputdata) == outputdata

def main():
    
    test_check_valid_date()
    test_getpercentage()
    test_no_duplicate()

if __name__ == "__main__":
    main()