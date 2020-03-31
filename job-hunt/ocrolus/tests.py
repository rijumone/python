from phonebook import main

import unittest 

  
class Test(unittest.TestCase): 
  
    def test(self):         
        self.assertEqual(
        	main(), ("Matches for Smith","Result 1: Smith, John, New York, (917) 958-1191","Matches for Doe","Result 1: Doe, John, New York, (917) 958-1191","Result 2: Doe, John, California, (212) 234-1191","Result 3: Doe, John, Florida, (919) 234-1192","Matches for Tyson","No results found",) ) 
  
if __name__ == '__main__': 
    unittest.main() 