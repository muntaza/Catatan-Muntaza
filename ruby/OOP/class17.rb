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

class Mouse < Animal
end

class Cat < Animal
    attr_accessor :age

    def speak
	puts "Meow"
    end
end

d = Cat.new("Teteh", "White")
d.speak
d.age = 2
d.get_info

