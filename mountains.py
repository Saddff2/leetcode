class Solution:
    def findPeaks(mountain = []):
        l = mountain
        peaks = []
        for i in range(1, len(l) - 1):
            if l[i] > l[i+1]:
                peaks.append(i)
        return peaks
    
Solution.findPeaks(mountain = [1,4,3,8,5])