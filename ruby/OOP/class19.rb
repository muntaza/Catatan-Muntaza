#!/usr/bin/ruby

class Animal
    def initialize(name)
	@name = name
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
    def initialize(name, age)
	super(name)
	@age = age
    end

    def to_s
	"#{@name} berumur #{@age} tahun"
    end

    def speak
	puts "Meow"
    end
end

d = Cat.new("Teteh", 1)
puts d
