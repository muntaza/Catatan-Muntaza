#!/usr/bin/ruby

greet = Proc.new do
    |x|
    puts "Welcome #{x}"
end

greet.call "Ahmad"
greet.call "Hasan"
greet.call "Fauzan"
greet.call "Adzima"
