# Ping-Sweep-Host-Discovery
For when nmap fails.

In the organization that I work for, we have a tool that regularly claims it detects a new subnet on the network.  I'll load up NMap and run through a scan and receive hits claiming there are host devices hanging off of this new subnet.  When I talk with the IT department, no one knows about the subnet and when we review the logs, it doesn't exist and isn't seen.

So, I'm writing my own scanner that just runs through a ping sweep to prove someone wrong at a basic level.