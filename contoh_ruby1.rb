#!/usr/bin/ruby

def sq(*p)
    p.each do
	|x| puts "#{x} kuadrat = #{x*x}"
    end
end

sq(9,7)
