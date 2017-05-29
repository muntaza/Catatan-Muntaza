#!/usr/bin/ruby

module MyMath
    PI = 3.14

    def self.square(x)
	x*x
    end

    def self.negate(x)
	-x
    end

    def self.factorial(x)
	(1..x).inject(:*) || 1
    end
end

puts MyMath.factorial(4)
puts MyMath::square(4)
puts MyMath.negate(4)
