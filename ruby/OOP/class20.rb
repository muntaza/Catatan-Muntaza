#!/usr/bin/ruby

class Shape
    attr_accessor :h, :w

    def initialize(h, w)
	self.h = h
	self.w = w
    end

    def +(other)
	Shape.new(self.h+other.h, self.w+other.w)
    end
end

a = Shape.new(7, 4)
b = Shape.new(9, 6)
c = a + b
puts "height is #{c.h} and width is #{c.w}"
