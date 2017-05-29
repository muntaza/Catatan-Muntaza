#!/usr/bin/ruby

Point = Struct.new(:x, :y)

origin = Point.new(0, 0)
dest = Point.new(15, 42)

puts dest.y
