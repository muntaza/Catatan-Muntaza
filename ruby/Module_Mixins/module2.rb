#!/usr/bin/ruby

module Flyable
    def fly
	puts "I'm flying!"
    end
end

class Vehicle
end

class Car < Vehicle
end

class Jet < Vehicle
    include Flyable
end

class Plane < Vehicle
    include Flyable
end

ob = Jet.new
ob.fly
