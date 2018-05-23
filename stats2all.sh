#! /bin/bash

if [ -f "log.txt" ]; then
rm "log.txt"
fi

c1=0
f1=0
c2=0
f2=0
c3=0
f3=0


printf "RAM\tURAM\tSWAP\tUSWAP\tDISK\tUDISK\tCPU\t\n" >>log.txt
end=$((SECONDS+36000))

while [ $SECONDS -lt $end ]; do
RAM=$(free  | awk 'NR==2{printf "%.2f\t", $2/(1000*1000) }')
URAM=$(free  | awk 'NR==2{printf "%.2f\t", $3/(1000*1000) }')
SWAP=$(free  | awk 'NR==3{printf "%.2f\t", $2/(1000*1000)}')
USWAP=$(free  | awk 'NR==3{printf "%.2f\t", $3/(1000*1000) }')


DISK=$(df  | awk '$NF=="/"{printf "%.2f\t", $2/(1000*1000) }')
UDISK=$(df  | awk '$NF=="/"{printf "%.2f\t", $3/(1000*1000) }')


CPU=$(top -bn1 | grep load | awk '{printf "%.2f\t\n", $(NF-2)}')
echo "$RAM$URAM$SWAP$USWAP$DISK$UDISK$CPU" >> log.txt

./cpu.py
./disk.py
./ram.py

if (( $(expr $f1 \> 0 ) )); then
c1=$(expr $c1 + 1)
fi
if (( $(expr $c1 \> 30 ) )); then
f1=0
c1=0
fi
if (( $(expr $CPU \> 4 ) )); then
if (( $(expr $f1 \< 1 ) )); then
f1=1

./mail.py

fi
fi



if (( $(expr $f2 \> 0 ) )); then
c2=$(expr $c2 + 1)
fi
if (( $(expr $c2 \> 30 ) )); then
f2=0
c2=0
fi
if (( $(expr $UDISK \> 1 ) )); then
if (( $(expr $f2 \< 1 ) )); then
f2=1

./maild.py
fi
fi





if (( $(expr $f3 \> 0 ) )); then
c3=$(expr $c3 + 1)
fi
if (( $(expr $c3 \> 30 ) )); then
f3=0
c3=0
fi
if (( $(expr $URAM \> 1 ) )); then
if (( $(expr $f3 \< 1 ) )); then
f3=1
./mailr.py
fi
fi



done
