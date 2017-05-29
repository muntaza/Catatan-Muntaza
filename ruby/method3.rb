#!/usr/bin/ruby

def sum(a, b)
    print "#{a} + #{b} = #{a+b}\n"
end

sum(4, 5)
sum(37, 11)

def sum_f(a, b=8)
    print "#{a} + #{b} = #{a+b}\n"
end

sum_f(4)
sum_f(4, 5)
