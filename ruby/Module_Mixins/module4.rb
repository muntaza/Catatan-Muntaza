#!/usr/bin/ruby

module Mammal
    class Dog
	def speak
	    puts "Woof!"
	end
    end

    class Cat
	def speak
	    puts "Meow"
	end
    end
end

a = Mammal::Dog.new
b = Mammal::Cat.new

a.speak
b.speak
