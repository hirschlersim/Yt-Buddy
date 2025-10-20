from multiprocessing.dummy import Pool as ThreadPool
from functools import partial
from loguru import logger
import numpy as np
import yaml
import sys
import os


def fetch_id(channelName, oldId, channelLink, videoLink):
    url = channelLink + channelName
    newId = os.popen("yt-dlp --q --no-warnings --flat-playlist --print id " + url).read()
    newId = newId.split("\n")
    newId = [x.strip() for x in newId if x.strip()]
    new = set(newId) - set(oldId)

    if 0 < len(new):
        logger.success(f"{channelName}:")
        for i, x in enumerate(new):
            logger.info(f"{i+1}. {videoLink}{x}")
    else:
        logger.trace(f"{channelName}")

    return newId


logger.remove(0)
logger.add(
    sink=sys.stderr,
    format="<green>{time:HH:mm:ss}</green> | <level>{message}</level>",
    enqueue=True,
    level="TRACE",
)

try:
    with open("config.cfg") as f:
        config = yaml.safe_load(f)
except Exception as e:
    logger.error(e)

oldIds = np.genfromtxt(config["data"], dtype=str)

pool = ThreadPool(config["threads"])
newIds = pool.map(partial(fetch_id, 
                       oldId=oldIds, 
                       channelLink=config["channelLink"],
                       videoLink=config["videoLink"]), config["channel"])
pool.close()
pool.join()

newIds = np.concatenate(newIds).ravel()
new = set(newIds) - set(oldIds)
allIds = np.concatenate((oldIds, list(new)))

np.savetxt(config["data"], allIds, fmt="%s")

logger.info("Terminated")