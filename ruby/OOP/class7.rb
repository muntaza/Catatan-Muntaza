#!/usr/bin/ruby

class Person
    def initialize(name)
	@name = name
    end
    def name
	@name
    end
    def name=(name)
	@name = name
    end
end

p = Person.new("Ahmad")
puts p.name

p.name = "Hasan"
puts p.name
