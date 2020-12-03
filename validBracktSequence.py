def validBracketSequence(sequence):
    # create a stack & traverse our sequence, pushing in all opening values
    
    stack = []
    
    for char in sequence:
        if char in ['(', '{', '[']:
            stack.append(char)
            
        else:
            # if it's not an opening bracket, then it's closing. And if that's the case, our stack has to already have something in it
            if not stack:
                return False
            
            # need to grab the nextchar off the stack & compare it to the next char in the sequence
            # if they are a pair (opening & closing chars) return true
            # if they're not, then the sequence is false  
            current = stack.pop()
            
            if current == '(':
                if char != ')':
                    return False  
            elif current == '{':
                if char != '}':
                    return False      
            elif current == '[':
                if char != ']':
                    return False
                    
    if stack:
        return False
    else:
        return True