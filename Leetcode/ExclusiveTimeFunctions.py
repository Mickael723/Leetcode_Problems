class Solution:
    def exclusiveTime(self, n: int, logs: list) -> list:

        call_stack = []
        func_times = [0] * n
        prev_time = 0

        for log in logs:

            split_log = log.split(":")
            id = int(split_log[0])
            op = split_log[1]
            time = int(split_log[2])

            if not call_stack:
                call_stack.append((id, op, time))
                prev_time = time
                continue

            if op == "start":
                time_dif = abs(time - prev_time)
                prev_id = call_stack[-1][0]
                func_times[prev_id] += time_dif
                call_stack.append((id, op, time))
                prev_time = time
            else:
                time_dif = abs((time + 1) - prev_time)
                prev_id = call_stack[-1][0]
                func_times[prev_id] += time_dif
                call_stack.pop()
                prev_time = time + 1
            
        
        return func_times


if __name__=="__main__":
    s = Solution()
    print(s.exclusiveTime(2, ["0:start:0","1:start:2","1:end:5","0:end:6"]))
    print(s.exclusiveTime(1, ["0:start:0","0:start:2","0:end:5","0:start:6","0:end:6","0:end:7"]))
    print(s.exclusiveTime(2, ["0:start:0","0:start:2","0:end:5","1:start:6","1:end:6","0:end:7"]))