import ugfx
import time

ugfx.init()

ugfx.clear(ugfx.BLACK)

statement = "A human being" 
statement2 = "should be able to"

lines = ["change a diaper,"]
lines.append( "plan an invasion,")
lines.append( "butcher a hog," ) 
lines.append( "conn a ship," )
lines.append( "design a building,") 
lines.append( "write a sonnet,")
lines.append( "balance accounts,")
lines.append( "build a wall,") 
lines.append( "set a bone,")
lines.append( "comfort the dying,")
lines.append( "take orders,")
lines.append( "give orders,")
lines.append( "cooperate,") 
lines.append( "act alone,")
lines.append( "solve equations," ) 
lines.append( "analyze a new problem,")
lines.append( "pitch manure,") 
lines.append( "program a computer,")
lines.append( "cook a tasty meal,")
lines.append( "fight efficiently,")
lines.append( "die gallantly.")

slogan_txt = "Specialization is.."
slogan2_txt = "for insects!"

def heinlein( lines ): 
    for line in lines: 
        ugfx.string(5,5,statement,"Roboto_BlackItalic24",ugfx.WHITE)
        ugfx.string(5,30,statement2,"Roboto_BlackItalic24",ugfx.WHITE)
        ugfx.string(5,55,line,"Roboto_BlackItalic24",ugfx.WHITE)
        time.sleep(0.5)
        ugfx.clear(ugfx.BLACK)

def slogan( slogan_txt ):
    ugfx.clear(ugfx.BLACK)
    ugfx.string(5,30,slogan_txt,"PermanentMarker22",ugfx.WHITE)
    ugfx.string(5,55,slogan2_txt,"PermanentMarker22",ugfx.WHITE)

heinlein( lines );
slogan( slogan_txt );  
