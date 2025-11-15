import arrow

brewing_time = arrow.utcnow()
brewing_time.to("Europe/london")

from collections import namedtuple
chaiProfile = namedtuple('chaiProfile',['name','spiciness','sweetness','milkiness'])