""" Copy template and create input file for a new day """

import logging
import logging.config

logging.config.fileConfig("logging.conf", disable_existing_loggers=False)
log = logging.getLogger("new-day")

import os
import datetime
import subprocess

import load_input

def get_day():
    """ Get todays day-number """
    return datetime.datetime.today().day

def get_template():
    """ Read template from file """
    with open("./template.py", "r") as f:
        log.debug("Reading ./template.py")
        return f.read()

def copy_template(day):
    """ Replace placeholders in template and write it to file """
    template = get_template()
    template = template.replace("XXX", str(day))
    log.debug(f"Replaced `XXX` with {day} in template")
    
    with open(f"./day-{day}.py", "w") as f:
        log.debug(f"Writing template to ./day-{day}.py")
        f.write(template)

def create_input_file(day):
    """ Create input files for real and sample input """
    with open(f"./inputs/day-{day}.txt", "w") as f:
        log.debug(f"Creating input-file to ./inputs/day-{day}.txt")
        f.write(load_input.load_input(day))

    with open(f"./inputs/day-{day}-sample.txt", "w") as f:
        log.debug(f"Creating input-file to ./inputs/day-{day}-sample.txt")
        f.write("<<Insert input here>>")

def main():
    day = get_day()

    if os.path.isfile(f"day-{day}.py"):
        log.critical("new_day.py has already been ran today!")
        return 0

    copy_template(day)
    create_input_file(day)

    log.info(f"Created script and input files for day {day} succesfully")

    subprocess.run(["./edit.sh", f"{day}"])

main()
