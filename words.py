# list of words to use
# phase one, using lists
words = """ man boy cow girl apple school hippo couch chair food water fly tail nose knee tooth board tie fish orange banana shoot splash swine juice picture table"""
words = words.split(' ')
hangman = ["""\
============
|          |
|          
|         
|         
|
============""",
"""\
============
|          |
|          0
|         
|         
|
============""",
"""\
============
|          |
|          0
|         /
|         
|
============""",
"""\
============
|          |
|          0
|         /|
|         
|
============""",
"""\
============
|          |
|          0
|         /|\\
|         
|
============""",
"""\
============
|          |
|          0
|         /|\\
|         / 
|
============""",
"""\
============
|          |
|          0
|         /|\\
|         / \\
|
============""" ]

hangman.reverse()

alphabet = 'a b c d e f g h i j k l m n o p q r s t u v w x y z'.split(' ')