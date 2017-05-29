#!/usr/bin/ruby

class Person
    @@count = 0

    def initialize
	@@count += 1
    end

    def self.get_count
	@@count
    end
end

p1 = Person.new
p2 = Person.new

puts Person.get_count
