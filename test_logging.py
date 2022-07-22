#!/usr/bin/python3
import logging


def toLog(log_name, message):
  logging.basicConfig(
    filename = log_name,
    format='%(asctime)s,%(levelname)s - %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S', level=logging.INFO
  )
  return logging.info(message)


toLog('imager_download.log', 'test log')
