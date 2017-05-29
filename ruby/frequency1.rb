#!/usr/bin/ruby

text = "I am learning Ruby and it is fun!"
puts text
text.downcase!
freqs = {}
freqs.default = 0

text.each_char {
    |char| freqs[char] += 1
}

("a".."z").each {
    |x| puts "#{x}: #{freqs[x]}"
}

puts freqs
