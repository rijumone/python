import time
import click
import subprocess
from loguru import logger


class AstroCapture:
    def capture(self, ):
        cmd = [
            'adb',
            'shell',
            'input',
            'tap',
            self.capture_x,
            self.capture_y,
        ]
        logger.info(' '.join(cmd))
        subprocess.call(cmd)

    def wait_for_exposure(self, exposure_seconds):
        time.sleep(exposure_seconds + 1)

    def additional_activities(self, ):
        pass


class AstroCaptureOneplus5T(AstroCapture):
    capture_x = '543'
    capture_y = '1832'

    def additional_activities(self, ):
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


class AstroCaptureSamsungGalaxyNote10Plus(AstroCapture):
    capture_x = '570'
    capture_y = '1960'


PHONE_MAKE_MODEL_MAP = {
    'oneplus5t': AstroCaptureOneplus5T,
    'samsunggalaxynote10plus': AstroCaptureSamsungGalaxyNote10Plus
}


@click.command()
@click.option('--phone_make_model', type=str, default='samsunggalaxynote10plus', help='Phone\'s make and model. One of {}. Defaults to samsunggalaxynote10plus'.format(', '.join(PHONE_MAKE_MODEL_MAP.keys())))
@click.option('--seconds_till_ready', type=int, default=10, help='Wait for n seconds before starting the capture loop. Defaults to 10.')
@click.option('--exposure_seconds', type=int, default=10, help='Exposure time in seconds. Defaults to 10.')
def main(phone_make_model, seconds_till_ready, exposure_seconds):
    logger.add('astro.log')

    logger.info('Starting to capture in {} second{}'.format(
        seconds_till_ready,
        's' if seconds_till_ready > 1 else ''
    ))
    time.sleep(seconds_till_ready)
    ctr = 0
    logger.info('instantiating AstroCapture object')
    ac_obj = PHONE_MAKE_MODEL_MAP[phone_make_model]()
    while True:
        ctr += 1
        logger.info('Capturing {}...'.format(ctr))

        ac_obj.capture()

        ac_obj.wait_for_exposure(exposure_seconds)

        ac_obj.additional_activities()

        logger.info('Sleeping for 0.75 seconds...')
        time.sleep(0.75)


if __name__ == '__main__':
    main()
