#!/usr/bin/ruby

car = {brand:"BMW", year:2016, color:"red", length:205}
puts car.values
print "---------------------\n"

puts car

car.delete(:length)
puts car.values
puts car.keys
