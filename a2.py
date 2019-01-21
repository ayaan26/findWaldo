
#template tiny waldo
#search image
#1
def compareOne(template,search,x,y):
   x1=0
   y1=0
   total=0
  
   #range within x that the function goes up until
   for i in range(x,x+getWidth(template)): 
     if x>getWidth(search): #if x exceeds the width of the search image
       break #stop running 
    
      #range within y that the function goes up until
     for j in range(y,y+getHeight(template)): 
       if y>getHeight(search): #if y exceeds height of search image
         break 
       sPx = getPixel(search,i,j)
       tempPx =getPixel(template,x1,y1) 
       slum=getRed(sPx)  #assume grayscale, get any color pixel in search image
       templum=getRed(tempPx) #assume grayscale,get any color pixel in template image 
       total+=abs(templum-slum) #subtract luminance value of template from luminance of search image  
       y1+=1 #increment y by 1
     y1=0 #set y to 0 to not exceed range
     x1+=1 #increment x by 1 
   return total

#2 for loops go through x and y values 
def compareAll(template,search):
  W=getWidth(search)
  H=getHeight(search)
  W1=getWidth(template)
  H1=getHeight(template)
  BIG=1000000
  #setting matrix to include the total differnces of luminance 
  matrix=[[BIG for i in range(W)] for j in range (H)]    
  #defining ranges
  for i in range(0,W-W1):
    for j in range(0,H-H1): 
      #letting matrix to access luminance values of compareOne function
      matrix[i][j]=compareOne(template,search,i,j)
  return matrix
  
#3
def find2Dmin(matrix):

  col=0
  row=0
  for i in range(0,len(matrix)): # defining range of x
    for j in range(0,len(matrix[i])): #defining range of y
      if matrix[i][j]<matrix[row][col]:
        row=i #i refers to row variable 
        col=j #j refers to col variable
  
  return(row,col)
  
#4
def displayMatch(search,x1,y1,w1,h1,color):
  width=3 #3 pixel width
  for i in range(0,3): #range
    addRect(search,x1,y1,w1,h1,color)
    y1+=1 #incrementation
    x1+=1
    w1+=-2
    h1+=-2
#5
 
def grayscale(picture):
  for px in getPixels(picture):
    r=getRed(px)
    g=getGreen(px)
    b=getBlue(px)
    lum=(r+g+b)/3
    color=makeColor(lum,lum,lum)
    setColor(px,color)
  

#6

# grayscale(target)
#  grayscale(search)
def findWaldo(template,search):
  grayscale(search)
  grayscale(template) #images grayscaled so any color pixel can be used for luminance
  compareAll(template,search)
  matrix=compareAll(template,search)
  v=find2Dmin(matrix) #defining v to set row and col in next function
  displayMatch(search,v[0],v[1],getWidth(template),getHeight(template),red)#setting target rectangle 
  show(search)
  writePictureTo(search,"foundwaldo.jpg")
  

template=makePicture("tinywaldo.jpg")
search=makePicture("tinyscene.jpg")
findWaldo(template,search)
