# LLM Training Visualizer

import matplotlib.pyplot as plt

def parse_data(filename):
    data = {'val': [], 'hella': [], 'train': []}
    
    with open(filename, 'r') as f:
        for line in f:
            step, data_type, value = line.strip().split()
            if data_type in data:
                data[data_type].append((int(step), float(value)))
    
    return data

def plot_data(data):
    plt.figure(figsize=(10, 6))
    
    for data_type, values in data.items():
        if values:
            x, y = zip(*values)
            plt.plot(x, y, label=data_type.capitalize())
    
    plt.xlabel('Step')
    plt.ylabel('Value')
    plt.title('LLM Training Progress')
    plt.legend()
    plt.grid(True)
    
    plt.savefig('llm_training_progress.png')
    plt.show()

if __name__ == '__main__':
    filename = 'training_data.txt'  # Replace with your data file name
    data = parse_data(filename)
    plot_data(data)

# To use this script:
# 1. Save your training data in a text file (e.g., 'training_data.txt')
# 2. Make sure you have matplotlib installed (pip install matplotlib)
# 3. Run this script (python download_script.py)
# 4. The script will generate a plot and save it as 'llm_training_progress.png'
