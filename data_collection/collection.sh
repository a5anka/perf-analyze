#!/bin/sh

# Print help message
# Executable name should be given as the argument
function print_help {
    echo "usage: $1 [<options>] [<command>]"
    echo -e "\noptions:"
    echo -e "\t -e event1,event2,..."
    echo -e "\t -o output file name"
    echo -e "\t -p perf binary location"
    echo
}

# default event list
event_list="r00c0,r0149,r0151,r02a2,r0126,r0227,r0224,r08a2,r01b0,r20f0,r02f1,r01f2,r01b8,r02b8,r04b8,r40cb"
perf_location=/usr/sbin/perf
output_file="data.out"
perf_input=perf.data

program_name=$0

while getopts "e:op:" opt; do
    case "$opt" in
    e)  event_list=$OPTARG
        ;;
    o)  output_file=$OPTARG
        ;;
    p)  perf_location=$OPTARG
        ;;
    esac
done

shift $((OPTIND-1))

[ "$1" = "--" ] && shift

if [[ -z "$@" ]] ; then
    print_help $program_name
    exit
fi

# Record performance data in to a file
$perf_location record -e "$event_list" $@ 2> /dev/null

# Write processed data to the output file
$perf_location report > $output_file

rm $perf_input

# END OF FILE
