#!/usr/bin/ruby

arr = [5, 6, 8, 4]
print "#{arr}\n"

arr << 3
print "#{arr}\n"

arr.reverse!
print "#{arr}\n"

res = arr[2...4]
print "#{res}\n"

puts res[1]
