n = 600851475143
i = 3

while n > 1
	if n%i == 0
		n/=i.to_i
	else
		i+=2
	end
end

puts i
