#!/usr/bin/ruby

greet = Proc.new do
    |x|
    puts "Welcome #{x}"
end

googbye = Proc.new do
    |x|
    puts "Goodbye #{x}"
end

def say(arr, proc)
    arr.each do
	|x|
	proc.call x
    end
end

people = ["Ahmad", "Fauzan", "Adzima"]

say(people, greet)
say(people, googbye)
