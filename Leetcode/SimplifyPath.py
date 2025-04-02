class Solution:
    def simplifyPath(self, path: str) -> str:

        if path == "" or path[0] != "/":
            return "Bad Path"
        
        path_steps = path.split("/")
        stack = []
        stack.append("/")
        print(path_steps)
        for directory in path_steps:
            if directory == "":
                continue
            elif directory == "..":
                stack.pop()
            elif directory == ".":
                continue
            else:
                stack.append(directory + "/")
                
        print(stack)

        if len(stack) == 0:
            stack.append("/")

        final_string = "".join(stack)
        if final_string.endswith("/"):
            final_string = final_string[:-1]
        return final_string
             

            


if __name__== "__main__":
    s = Solution()
    path = "/home/user/Documents/../Pictures"
    print(s.simplifyPath(path))