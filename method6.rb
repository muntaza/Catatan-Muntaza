#!/usr/bin/ruby

def sq(*p)
    p.each do
	|x| puts "#{x} kuadrat = #{x*x}"
    end
end

sq(3,4,5,6)
sq(9,7)
