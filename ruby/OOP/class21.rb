#!/usr/bin/ruby

class Person
    def initialize(age)
	@age = age
    end

    def show
	puts "#{@age} year = #{days_lived} days"
    end

    private
    def days_lived
	@age * 365
    end
end

p = Person.new(42)
p.show
