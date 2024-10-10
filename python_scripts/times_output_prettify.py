# Let's read both the Clingo and MiniZinc log files and extract execution times into the required format

clingo_log_path = "../results/clingo_execution_times.log"
minizinc_log_path = "../results/minizinc_execution_times.log"


def parse_log_minizinc(file_path):
    times = {
        "reachability_GeCode": [],
        "reachability_HiGHS": [],
        "steiner_GeCode": [],
        "steiner_HiGHS": [],
        "weighted_ST_GeCode": [],
        "weighted_ST_HiGHS": []
    }

    with open(file_path, 'r') as file:
        current_problem = None
        current_solver = None
        for line in file:
            line = line.strip()
            if "Instance" in line:
                if "reachability" in line:
                    current_problem = "reachability"
                elif "steiner" in line:
                    current_problem = "steiner"
                elif "weighted_ST" in line:
                    current_problem = "weighted_ST"
            if "GeCode" in line:
                current_solver = "GeCode"
            elif "HiGHS" in line:
                current_solver = "HiGHS"
            elif "% time elapsed:" in line:
                try:
                    time_value = float(line.split(":")[1].strip().replace('s', '')) * 1000
                    if current_solver and current_problem:
                        times[f"{current_problem}_{current_solver}"].insert(0, time_value)
                except ValueError:
                    print(f"Warning: Could not parse time value from line: {line}")
    return times


def parse_log_clingo(file_path, identifier_prefix):
    times = {
        "reachability": [],
    }

    with open(file_path, 'r') as file:
        current_problem = "reachability"
        for line in file:
            line = line.strip()
            if "CPU Time" in line:
                time_value = float(line.split(":")[1].strip().split()[0].replace('s', '')) * 1000
                times[current_problem].insert(0, time_value)
    return {
        f"{problem}_{identifier_prefix}": times[problem] for problem in times
    }


# Parse both the Clingo and MiniZinc log files
def create_data():
    data = {}
    data.update(parse_log_clingo(clingo_log_path, "Clingo"))
    data.update(parse_log_minizinc(minizinc_log_path))
    print("data = ", data)
    return data


# Parse both the Clingo and MiniZinc log files
data = {}
data.update(parse_log_clingo(clingo_log_path, "Clingo"))  # Prolog-based results from Clingo
data.update(parse_log_minizinc(minizinc_log_path))  # GeCode-based results from MiniZinc

# Input sizes based on your original data
input_sizes = [8, 9, 10, 11, 12, 13, 14, 15, 16, 17]

print("input_sizes =", input_sizes)
print("data = ", data)
