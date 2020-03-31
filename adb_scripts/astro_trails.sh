# astro_trails.sh

echo 'Starting to capture in 20 seconds'
sleep 20

while :
do
	input tap 543 1832
	echo 'Sleeping for 31 seconds...'
	sleep 31

	input tap 957 1861
	echo 'Sleeping for 31 seconds...'
	sleep 31

	input keyevent KEYCODE_BACK
	echo 'Sleeping for 0.5 seconds...'
	sleep 0.5
done
