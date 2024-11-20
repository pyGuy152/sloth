def comments_correct(comments):
    # I could add the following line of code, but Python handles out of scope error for slicing. On line 7 comments[2:4] might be out of scope but python handles it. :)
    # comments += "//" 
    for i in range(0,len(comments),2):
        if (comments[0:2] == "//"):
            comments = comments[2::]
        elif (comments[:2] == "/*" and comments[2:4] == "*/"):
            comments = comments[4::] + "//"
        else:
            return False
    return True
print(comments_correct("///**/*/*/"))