class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        merged_interval=[[intervals[0][0],intervals[0][1]]]
        cnt=0
        for i in range(1,len(intervals)):
            # print(intervals[i][0],intervals[i][1])
            if(merged_interval[cnt][1]>=intervals[i][0] and merged_interval[cnt][0]<=intervals[i][0]):
                merged_interval[cnt][1]=max(merged_interval[cnt][1],intervals[i][1])
                merged_interval[cnt][0]=min(merged_interval[cnt][0],intervals[i][0])
                
            else:
                merged_interval.append([intervals[i][0],intervals[i][1]])
                cnt+=1
        return merged_interval
                
        