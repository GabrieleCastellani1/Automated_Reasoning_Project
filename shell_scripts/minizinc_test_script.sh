#!/bin/bash

cd ..

# Path to the input file
input_file="data/minizinc_instances"

# Path to the output log file
output_log="minizinc_execution_times.log"

# Path to the temporary file where each instance will be stored
temp_instance="instance.mzn"

# List of MiniZinc script files
minizinc_scripts=("Exam_reachability_predicate_version.mzn" "Exam_steiner_predicate.mzn" "Exam_weighted_ST_predicate.mzn")

# Clear the log file if it already exists
> "$output_log"

# Iterate through each MiniZinc script
for script in "${minizinc_scripts[@]}"; do
    echo "Processing with $script..." >> "$output_log"

    instance_counter=1

    > "$temp_instance"

    # Read the input file line by line
    while IFS= read -r line || [[ -n "$line" ]]; do

        if [[ "$line" == *"----------"* ]]; then
            echo "Solving instance $instance_counter with script $script using GeCode..." >> "$output_log"
            echo "Instance $instance_counter using $script with GeCode" >> "$output_log"

            temp_output=$(minizinc --time-limit 300000 --solver gecode --output-time "$script" "$temp_instance" 2>&1)

            processed_output=$(echo "$temp_output" | grep -m 1 '% time elapsed:')

            echo "$processed_output" >> "$output_log"
            echo "Solving instance $instance_counter with script $script using HiGHS..." >> "$output_log"
            echo "Instance $instance_counter using $script with HiGHS" >> "$output_log"

            temp_output=$(minizinc --time-limit 300000 --solver highs --output-time "$script" "$temp_instance" 2>&1)

            processed_output=$(echo "$temp_output" | grep -m 1 '% time elapsed:')

            echo "$processed_output" >> "$output_log"

            ((instance_counter++))

            > "$temp_instance"
        else
            echo "$line" >> "$temp_instance"
        fi

    done < "$input_file"

    echo "Finished processing with $script." >> "$output_log"
done

echo "All instances processed for all scripts. Check $output_log for execution times."
