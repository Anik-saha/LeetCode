class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        # # Sort and merge with extra memory
        # intervals.sort()
        # merged_interval=[[intervals[0][0],intervals[0][1]]]
        # cnt=0
        # for i in range(1,len(intervals)):
        #     if(merged_interval[cnt][1]>=intervals[i][0] and merged_interval[cnt][0]<=intervals[i][0]):
        #         merged_interval[cnt][1]=max(merged_interval[cnt][1],intervals[i][1])
        #         merged_interval[cnt][0]=min(merged_interval[cnt][0],intervals[i][0])                
        #     else:
        #         merged_interval.append([intervals[i][0],intervals[i][1]])
        #         cnt+=1
        # return merged_interval
        
        # Sort and merge in place
        intervals.sort()
        R = 0
        for i in intervals:
            if i[0] <= intervals[R][1]:
                intervals[R][1] = max(intervals[R][1], i[1])
            else:
                intervals[(R := R + 1)] = i
        return intervals[:R+1]