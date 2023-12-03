""" Copy template and create input file for a new day """

import logging
import logging.config

logging.config.fileConfig("logging.conf", disable_existing_loggers=False)
log = logging.getLogger("new-day")

import datetime

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
    log.debug("Replaced `XXX` with {day} in template")
    
    with open(f"./day-{day}.py", "w") as f:
        log.debug("Writing template to ./day-{day}.py")
        f.write(template)

def create_input_file(day):
    """ Create input files for real and sample input """
    with open(f"./inputs/day-{day}.txt", "w") as f:
        log.debug("Creating input-file to ./inputs/day-{day}.txt")
        f.write("")

    with open(f"./inputs/day-{day}-sample.txt", "w") as f:
        log.debug("Creating input-file to ./inputs/day-{day}-sample.txt")
        f.write("")

def main():
    day = get_day()
    copy_template(day)
    create_input_file(day)

    log.info("Created script and input files for day {day} succesfully")

main()
