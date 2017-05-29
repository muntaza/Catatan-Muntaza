#!/usr/bin/ruby

age = 42

case age
    when 0..3
	puts "Little baby"
    when 4..14
	puts "Child"
    when 15..24
	puts "Youth"
    when 25..60
	puts "Adult"
    when age > 60
	puts "Senior"
    else
	puts "Wrong age"
end
