def sum
	s = 0
	(0...1000).each do |i|
		s += i if i%3==0 || i%5==0
	end
	s
end

puts sum
