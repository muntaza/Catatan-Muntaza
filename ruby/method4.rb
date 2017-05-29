#!/usr/bin/ruby

def greet(name="")
    if name==""
	puts "Greetings!"
    else
	puts "Welcome, #{name}"
    end
end

print "Input your name: "
greet(gets.chomp)
