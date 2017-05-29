#!/usr/bin/ruby

a = [6, 3, 8, 7, 9]
b = [100, 110, 7, 6]

print "a = #{a}\n"
print "b = #{b}\n"
nums = a + b
print "a + b = #{nums}\n"
nums = a - b
print "a - b = #{nums}\n"

nums = a * 2
print "a * 2 = #{nums}\n"
nums = a & b
print "a \& 2 = #{nums}\n"
nums = a | b
print "a \| 2 = #{nums}\n"

print "sort = #{nums.sort}\n"
print "reverse = #{nums.reverse}\n"

print "#{nums}\n"
