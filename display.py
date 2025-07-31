letter = ''' Dear <|Name|>,
          You are selected! 
          <|Date|>'''

print(letter.replace("<|Name|>", "Khushi").replace("<|Date|>", "27 October 2006"))
