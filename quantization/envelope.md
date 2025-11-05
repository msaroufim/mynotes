## Impact of adding 1 more bit to the mantissa or exponent

* Each exponent bit roughly squares your numeric range (max value goes from ~2^(2^k) to ~2^(2^(k+1)))
* Each mantissa bit gives you 0.3 more decimal digits of precision (numbers need to differ by ~1/2^m to be distinguishable)

Exponent bit tends to give you fairly massive range but mantissa bits are more expensive and only give 0.3 decimal digits of precision
