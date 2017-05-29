#!/usr/bin/ruby

module Mampu_berenang
    def berenang
	"Bisa Berenang"
    end
end

module Mampu_berjalan
    def berjalan
	"Bisa Berjalan"
    end
end

class Binatang
    attr_accessor :nama, :warna

    def initialize(nama, warna)
	@nama = nama
	@warna = warna
    end

    def get_info
	puts "#{@nama} berwarna #{@warna}"
    end
end

class Kucing < Binatang
    include Mampu_berjalan

    def suara
	"Meow"
    end
end

k = Kucing.new("Si Uning", "Kuning Putih")
k.get_info
print "#{k.nama} berbunyi #{k.suara}\n"

k.warna = "Cokelat"
k.get_info
print "#{k.nama} #{k.berjalan}\n"

puts "---------------------------"

class Bebek < Binatang
    include Mampu_berjalan
    include Mampu_berenang
end

b = Bebek.new("Si itik", "Abu-abu")
b.get_info
print "#{b.nama} #{b.berjalan} dan #{b.berenang}\n"
