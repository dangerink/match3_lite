
from erlport import Port
from match3.application import Match3Protocol


proto = Match3Protocol()
proto.run(Port(packet=4, use_stdio=True, compressed=True))



