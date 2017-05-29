#!/usr/bin/ruby

class Person
    attr_accessor :name, :age

    def initialize(name, age)
	@name = name
	@age = age
    end

    def change(n, a)
	self.name = n
	self.age = a
    end

    def show_info
	puts "#{self.name} is #{self.age}"
    end
end

p = Person.new("Ahmad", 8)
print p.show_info

p.change("Hasan", 12)
print p.show_info
