#!/usr/bin/ruby

require "ostruct"

person = OpenStruct.new
person.name = "Jhon"
person.age = 42
person.salary = 250

puts person.name
