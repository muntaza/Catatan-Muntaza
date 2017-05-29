#!/usr/bin/ruby

class Person
    def initialize(name)
	@name = name
    end
    def get_name
	@name
    end
end

p = Person.new("Ahmad")
puts p.get_name
