#!/usr/bin/ruby

size = {svga:800, hd:1366, uhd:3840}

size.each do |key,value|
    puts "#{key}\t => \t#{value}"
end
