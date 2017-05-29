#!/usr/bin/ruby

cars = {
    bmw:	{year:2006, color:"red"},
    mercedes:	{year:2012, color:"black"},
    porsche:	{year:2014, color:"white"}
}

puts cars[:mercedes][:color]
puts cars.length
