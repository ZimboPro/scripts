nameserver 208.67.222.123
nameserver 208.67.220.123your network to use a specific DNS regardless of network connected.
## How does it work
It watch the `/etc/resolv.conf` file on unix systems. Once a change is detected it will force the DNS
to be set.

## Note
This script was created on Debain so I am not sure if it will work on a BSD or Mac. Windows was not
considered during development.    