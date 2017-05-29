#!/usr/bin/ruby

print "How old are you? "

age = gets.to_i
puts age

print "Hi, "

case age
    when 0..3
	puts "Little baby"
    when 4..14
	puts "Child"
    when 15..24
	puts "Youth"
    when 25..60
	puts "Adult"
    else
	puts "Senior"
end
