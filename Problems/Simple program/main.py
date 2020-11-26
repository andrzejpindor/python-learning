import argparse
params = argparse.ArgumentParser()
params.add_argument('--number')
args = params.parse_args()
print(args.number)