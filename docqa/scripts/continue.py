import argparse

from docqa.trainer import resume_training
from docqa.model_dir import ModelDir


def main():
    parser = argparse.ArgumentParser(description='')
    parser.add_argument('name', help='name of output to exmaine')
    parser.add_argument('--filename')
    parser.add_argument('--eval', "-e", action="store_true")
    parser.add_argument('--dryrun', "-d", action="store_true", help="dry run")
    args = parser.parse_args()

    resume_training(ModelDir(args.name), start_eval=args.eval, filename=args.filename, dry_run=args.dryrun)


if __name__ == "__main__":
    main()
