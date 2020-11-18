import time
import click
import subprocess
from loguru import logger


class AstroCapture:
    def __init__(self,):
        pass

    def capture(self):
        cmd = [
            'adb',
            'shell',
            'input',
            'tap',
            '543',
            '1832',
        ]
        logger.info(' '.join(cmd))
        subprocess.call(cmd)


class AstroCaptureOneplus5T(AstroCapture):
    def wait_for_exposure(self, exposure_seconds):
        time.sleep(exposure_seconds + 1)


@click.command()
@click.option('--seconds_till_ready', type=int, default=10, help='Wait for n seconds before starting the capture loop')
@click.option('--exposure_seconds', type=int, default=10, help='Exposure time in seconds')
def main(seconds_till_ready, exposure_seconds):
    logger.add('astro.log')

    logger.info('Starting to capture in {} second{}'.format(
        seconds_till_ready,
        's' if seconds_till_ready > 1 else ''
    ))
    time.sleep(seconds_till_ready)
    ctr = 0
    logger.info('instantiating AstroCapture object')
    ac_obj = AstroCaptureOneplus5T()
    while True:
        ctr += 1
        logger.info('Capturing {}...'.format(ctr))

        ac_obj.capture()

        ac_obj.wait_for_exposure(exposure_seconds)

        cmd = [
            'adb',
            'shell',
            'input',
            'tap',
            '957',
            '1861',
        ]
        logger.info(' '.join(cmd))
        subprocess.call(cmd)

        logger.info('Sleeping for 0.75 seconds...')
        time.sleep(0.75)

        cmd = [
            'adb',
            'shell',
            'input',
            'keyevent',
            'KEYCODE_BACK',
        ]
        logger.info(' '.join(cmd))
        subprocess.call(cmd)

        logger.info('Sleeping for 0.75 seconds...')
        time.sleep(0.75)


if __name__ == '__main__':
    main()
