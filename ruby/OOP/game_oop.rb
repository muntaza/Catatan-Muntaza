#!/usr/bin/ruby

class Player
    attr_accessor :name, :health, :power

    def initialize(n, h, pow)
	@name = n
	@health = h
	@power = pow
    end

    def isAlive
	@health > 0
    end

    def hit(opponent)
	opponent.health -= self.power
    end

    def to_s
	"#{name}: Health: #{health} Power: #{power}"
    end
end


class Robot < Player
    def hit(opponent)
	opponent.health -= (self.power * 2)
	self.health += 2
	opponent.power -= 8 if opponent.power > 10
    end
end

def fight(p1, p2)
    while p1.isAlive && p2.isAlive
	p1.hit(p2)
	p2.hit(p1)
	show_info(p1, p2)
    end

    if p1.isAlive
	puts "#{p1.name} WON!"
    elsif p2.isAlive
	puts "#{p2.name} WON!"
    else
	puts "TIE!"
    end
end

def show_info(*p)
    p.each do
	|x| puts x
    end
end


p1 = Robot.new("Merah", 1+rand(100), 1+rand(30))
p2 = Player.new("Biru", 50+rand(100), 20+rand(20))

show_info(p1, p2)
puts "LETS FIGHT!"
fight(p1, p2)
