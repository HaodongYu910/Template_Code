
echo ""
echo " ==================================================================== "
echo "              welcome to use dds transfer speed calculator            "
echo "                                            @copyright by HaodongYU   "
echo " ==================================================================== "
echo ""

echo " ----------------- please enter the number of Theread --------------------- "
read -p "Theread number: " Theread_num
if [ -z "$Theread_num" ]; then
    echo "Theread_num cannot be empty..."
    exit 1;
fi
t_num=$(($Theread_num+0))

cat syncpacs.log | grep -o "elapsed_time_per_instance:\d*.* " | cut -d : -f 2 -> 111.log

# calculate the number of record
a=0
all=0
while read line
do
    echo $line
    a=$(($a+1)) 
    echo "we come to line $a"
done < 111.log

sum=$(cat 111.log | awk -FS '{sum+=$1} END {print sum}')
a_t=$(echo "scale=2;$a*$t_num" | bc)
avg=$(echo "scale=2;$a_t/$sum" | bc)
echo "finally $avg"