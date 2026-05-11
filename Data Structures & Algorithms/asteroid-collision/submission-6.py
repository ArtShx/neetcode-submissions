class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = [asteroids.pop(0), asteroids.pop(0)]
        res = []
        processed = set()

        while 1:
            #print(stack)
            if len(stack) < 2 and asteroids:
                stack.append(asteroids.pop(0))
                continue
            elif len(stack) < 2:
                break
            #print("CKP2", stack)
            seclast = stack[-2]
            last = stack[-1]

            is_same_dir = (last < 0 and seclast < 0) or (last > 0 and seclast > 0)
            #print(is_same_dir)
            if is_same_dir:
                if not asteroids:
                    return stack
                stack.append(asteroids.pop(0))
                continue
            else:
                if seclast > 0:
                    if abs(last) == abs(seclast) and (last < 0 and seclast > 0):
                        stack.pop()
                        stack.pop()
                    elif abs(last) < abs(seclast):
                        stack.pop()
                    else:
                        stack.pop()
                        stack[-1] = last
                else:
                    hashable = (last,seclast)
                    if hashable in processed and not asteroids:
                        return stack
                    if hashable in processed and asteroids:
                        stack.append(asteroids.pop(0))
                    processed.add(hashable)
                        
        return stack

        """
        while asteroids:
            
            ast = asteroids.pop(0)
            if not stack:
                print("empty stack", ast)
                stack.append(ast)
                continue
            last = stack[-1]
            print("<<>>", stack)
            print(last, ast)
            if last < 0:
                stack.append(ast)
            else:
                is_same_dir = (ast < 0 and last < 0) or (ast > 0 and last > 0)
                if is_same_dir:
                    stack.append(ast)
                else:
                    if abs(last) == abs(ast):
                        stack.pop()
                    elif abs(last) < abs(ast):
                        stack[-1] = ast
        return stack



        ## old

        while len(stack) >= 2:
            last = stack[-1]
            seclast = stack[-2]
            #print("<<>>")
            #print(seclast, last)

            is_same_dir = (last > 0 and seclast > 0) or (last < 0 and seclast < 0)
            if is_same_dir and asteroids:
                stack.append(asteroids.pop(0))
                continue
            elif is_same_dir and not asteroids:
                break
            else:
                stack.pop()
                if abs(last) == abs(seclast):
                    stack.pop()
                if abs(last) > abs(seclast):
                    stack.pop()
                    stack.append(last)
                if asteroids:
                    stack.append(asteroids.pop(0))
        
        return stack
        """
            

