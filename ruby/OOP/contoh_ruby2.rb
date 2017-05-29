#!/usr/bin/ruby

class Person

    attr_accessor :name

    def initialize(name)
	@name = name
    end
end

p = Person.new("Ahmad")
puts p.name

p.name = "Hasan"
puts p.name
