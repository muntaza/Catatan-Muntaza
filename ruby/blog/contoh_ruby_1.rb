#!/usr/bin/ruby

def factorial(x)
    (1..x).inject(:*) || 1
end

def sq(*p)
    p.each do
	|x| puts "#{x} kuadrat = #{x*x}"
    end
end

a = 7
puts "factorial dari #{a} adalah #{factorial(a)}"

puts "-----------------"

sq(3,4,5,6)
sq(9,7)
