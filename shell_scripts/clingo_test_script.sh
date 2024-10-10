#!/bin/bash

# Path to the input file containing instances
input_file="clingo_instances"

# Path to the output log file
output_log="clingo_execution_times.log"

# Path to the temporary file where each instance will be stored
temp_instance="instance.lp"

# Path to the main Clingo script that will be executed on each instance
clingo_script="ex_exam.pl"

# Time limit for Clingo in seconds (5 minutes = 300 seconds)
time_limit=300

# Clear the log file if it already exists
> "$output_log"

# Initialize the instance counter
instance_counter=1

# Clear the temporary instance file
> "$temp_instance"

# Read the input file line by line
while IFS= read -r line || [[ -n "$line" ]]; do

    if [[ "$line" == "----------" ]]; then
        echo "Solving instance $instance_counter with Clingo script..."
        echo "Instance $instance_counter" >> "$output_log"
        echo "% Instance $instance_counter" >> "$temp_instance"

        clingo --quiet=2 --time-limit=300000 "$clingo_script" "$temp_instance" >> "$output_log" 2>&1

        ((instance_counter++))

        > "$temp_instance"
    else
        echo "$line" >> "$temp_instance"
    fi

done < "$input_file"

echo "All instances processed for Clingo. Check $output_log for execution times."