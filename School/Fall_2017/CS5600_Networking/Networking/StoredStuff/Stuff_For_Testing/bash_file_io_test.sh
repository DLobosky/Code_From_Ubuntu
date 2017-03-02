#VAR1=""
#VAR2=""

#while IFS='' read -r line1 line2 || [ -n "$line" ]; 
#do
#    VAR1=$line1
#    VAR2=$line2
#    echo "$line1 $line2" >> 'output_file.txt'
#done < "test.txt"



#echo VAR1
#echo VAR2 

# { read -r var1 _ && read -r var2 _; } < <(lspci | grep -i 'vga\|graphics\\')

# STARTTIME='date +%-S'
#time1=$((10#$time % 15))

#sleep 2

# ENDTIME='date +%-S'
#time2=$((10#$time % 15))

#RUNTIME=$((ENDTIME-STARTTIME))

#echo RUNTIME

START=$(date +%s.%N)
sleep 3
END=$(date +%s.%N)
DIFF=$(echo "$END - $START" | bc)
echo $DIFF

if [ "$DIFF" -gt 2 ]; then
	echo $DIFF
fi

echo "...done"
