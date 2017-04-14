#coding=utf-8
import sys

class Solution(object):
	"""docstring for ClassName"""
	def twoSum(self, nums, targets):
		'''
		:type nums: list[int]
		:type target :int
		:rtype List[int]
		'''
		for index in range(0, len(nums)):
			#print "index:{}\tnum{}\t".format(index, nums[index])
			diff_num = targets - nums[index]
			diff_index = self.getIndex(nums, diff_num)

			if (diff_num in nums) and (diff_index != index):
				return [index, diff_index]
			else:
				continue

			return None


	def  getIndex(self, nums, targets):
		for index in range(0, len(nums)):
			if targets == nums[index]:
				return index
			else:
				continue
		return None
