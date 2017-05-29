#!/usr/bin/ruby

class Animal
    def initialize(name, color)
	@name = name
	@color = color
    end

    def speak
	puts "Hi"
    end

    def get_info
	puts "#{@name} berwarna #{@color}"
    end
end

class Cat < Animal
end

d = Cat.new("Teteh", "White")
d.speak
d.get_info
