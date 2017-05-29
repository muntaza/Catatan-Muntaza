#!/usr/bin/ruby

class Animal
    @age = 0
    def initialize(name, age)
	@name = name
	@age = age
    end
end

ob = Animal.new("Jacky", 3)
