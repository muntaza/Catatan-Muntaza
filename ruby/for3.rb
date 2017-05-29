#!/usr/bin/ruby

for i in (0..10)
    next if i % 2 == 0
    puts "i = #{i}"
end
