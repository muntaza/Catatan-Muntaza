#!/usr/bin/ruby

size = {svga:800, hd:1366, uhd:3840}

size.each { |key,value|
    puts "#{key}\t => \t#{value}"
}
