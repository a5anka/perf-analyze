#!/bin/sh

# Print help message
# Executable name should be given as the argument
function print_help {
    echo "usage: $1 [<options>] <command>"
    echo -e "\noptions:"
    echo -e "\t -e event1,event2,..."
    echo -e "\t -o output file name"
    echo -e "\t -p perf binary location"
    echo
}

# default event list
perf_location=/usr/sbin/perf
output_file="data.out"
perf_input=perf.data
event_config_file=./events.cfg
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

if [[ -z $event_list ]] ; then
    cpu_model=$(cat /proc/cpuinfo | grep "model name" | sed 's/model name[[\t ]]*: //g' | sed 's/ [ ]\+/ /g' | uniq)

    # Read default event  lists from config file
    source $event_config_file
    if [[ ${default_events[$cpu_model]} ]] ; then
	event_list=${default_events["$cpu_model"]}
    else
	event_list="instructions,cache-references,cache-misses,L1-dcache-loads,L1-dcache-load-misses,\
L1-dcache-stores,L1-dcache-store-misses,dTLB-load-misses,dTLB-store-misses"
    fi
fi

# Record performance data in to a file
$perf_location record -e "$event_list" $@ 2> /dev/null

# Write processed data to the output file
$perf_location report > $output_file

rm $perf_input

# END OF FILE
