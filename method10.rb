#!/usr/bin/ruby

$x = 42

puts $x
def change
    $x = 8
end

change
puts $x
