#!/usr/bin/ruby

class Product
    attr_accessor :name, :num

    def initialize(name, num)
	@name = name
	@num = num
    end

    def ==(other)
	self.id == other.id
    end

    protected
    def id
	name.length*num
    end
end

p1 = Product.new("PC", 6)
p2 = Product.new("Laptop", 2)
puts (p1 == p2)
