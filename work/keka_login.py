import json
import click
import requests
from loguru import logger
from datetime import datetime, timedelta


@click.command()
@click.option('--cookie', required=True, help='login cookie value is required for authentication')
@click.option('--start_date', required=True, help='date starting which attendance needs to be marked')
@click.option('--end_date', required=True, help='date till which attendance needs to be marked')
def main(cookie, start_date, end_date):
    url = "https://decisiontree.keka.com/api/mytime/attendance/saveattendanceadjustment"

    headers = {
        'authority': 'decisiontree.keka.com',
        'accept': 'application/json, text/plain, */*',
        'dnt': '1',
        'x-requested-with': 'XMLHttpRequest',
        'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36',
        'content-type': 'application/json; charset=UTF-8',
        'origin': 'https://decisiontree.keka.com',
        'sec-fetch-site': 'same-origin',
        'sec-fetch-mode': 'cors',
        'sec-fetch-dest': 'empty',
        'referer': 'https://decisiontree.keka.com/ui/',
        'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8',
        'cookie': cookie
    }
    start_date = datetime.strptime(start_date, '%Y-%m-%d')
    end_date = datetime.strptime(end_date, '%Y-%m-%d')
    n_dates_diff = (end_date - start_date).days + 1
    current_date = start_date
    for _ in range(n_dates_diff):
        if (current_date.isoweekday() in (6, 7)):
            logger.warning(
                'Skipping due to weekend on {}'.format(current_date))
            current_date += timedelta(days=1)
            continue
        payload = json.dumps({
            "timeEntries": [
                {
                    "actualTimestamp": "{}T10:00:00.000Z".format(
                        datetime.strftime(current_date, '%Y-%m-%d')
                    ),
                    "adjustedTimestamp": "{}T10:00:00.000Z".format(
                        datetime.strftime(current_date, '%Y-%m-%d')
                    ),
                    "timestamp": "{}T10:00:00.000Z".format(
                        datetime.strftime(current_date, '%Y-%m-%d')
                    ),
                    "originalPunchStatus": 0,
                    "modifiedPunchStatus": 0,
                    "punchStatus": 0,
                    "attendanceLogSource": 1,
                    "premiseName": "Attendance Adjustment",
                    "manualClockinType": 2,
                    "isAdjusted": True,
                    "isEditable": True,
                    "isManuallyAdded": True
                },
                {
                    "actualTimestamp": "{}T18:00:00.000Z".format(
                        datetime.strftime(current_date, '%Y-%m-%d')
                    ),
                    "adjustedTimestamp": "{}T18:00:00.000Z".format(
                        datetime.strftime(current_date, '%Y-%m-%d')
                    ),
                    "timestamp": "{}T18:00:00.000Z".format(
                        datetime.strftime(current_date, '%Y-%m-%d')
                    ),
                    "originalPunchStatus": 1,
                    "modifiedPunchStatus": 1,
                    "punchStatus": 1,
                    "attendanceLogSource": 1,
                    "premiseName": "Attendance Adjustment",
                    "manualClockinType": 2,
                    "isAdjusted": True,
                    "isEditable": True,
                    "isManuallyAdded": True
                }
            ],
            "note": ".",
            "employeeId": 33992,
            "requestDate": datetime.strftime(current_date, '%Y-%-m-%-d'),
            "requestType": 7
        })
        current_date += timedelta(days=1)

        logger.info('requesting for {}'.format(payload))

        response = requests.request("POST", url, headers=headers, data=payload)

        logger.success(response.text)


if __name__ == '__main__':
    main()


'''
Usage:
python keka_login.py --cookie='Subdomain=decisiontree.keka.com; ThemeIndex=7; ASP.NET_SessionId=mwz4gvjphgh2cnly54torhvm; .AspNet.Cookies=leHYw9xzyygkARY-tCnSPsIIJjDZxc-Tidq1MW_WCMgWAvlTmUJbTOtJnvVR7Zo7vzpLrdYM9Yrq_KwRQGL5PmUqBeNZq3q_pym9hvWpohKsrVTfjjwSRfpNHq9feFXZfOqrBg29hfTtEAoZ2q5443c5C315motIruHboKOqNNt53d8G9cyg89jRXgESo0liRYE7CWhlHPYXhw8hcO-3OTAjAYXsG6ZTRsnBvyPto_CfpXSGR9HyLWZM8iAI6cQThE4R9rgwEdMT-Oz9u1S74xbVdlMGfP_5qUkj6ZJfSMdjIu3MLuLhCctVY24kdRi7xbbcpfqayq6oiTQeLcFWxf_2K72bQSytzBhi18Gl5D0w7fsgfPukE0KylZTRczEuZ8Eegsx1RgKiYgbZNMaCGwBi8hoa5CBk5uYIfQ0morUOapnNbO0Zz2umC5M9e0zE7gFQZLfvDPxMLAosCGMyVEQHVgVK15ctU4j8XHVgqbZY_uFddIqNYfDY2klxz5Uu7MNEXOux9iLCKNoSIQkMV3qbDWHv6NQEM4PW1S44FSm6S0H8vtOoD7VCD9WRx_SXcDKSGDaTFQilmof9PO0jJgjYXv7_-8ZykTZphSiT8lwZ2P49F5BzRrHstvLYuXlvXRcDaSfRxBtk_HsBifGr8ePw4UHhA37VJY4JlnIt5P3-QGG6-F06Tx7rLH3xsJeHx6Ly4G20UCzeRjlduMsoAuVi-a3i6Lp1Rotv2g3nzq1w4OoshEW0fXdMXvprx3LPA-L-tFxyiTEmRx5Td3oQfOZxraYEW4HdypstYjpPH8s8guByulHqKzNmXUo5Ykr_-eA-hZmkJJuNE3k4JSC3mzcQJtylv5U7udwp-n0_ESvlWhLwXLK7HTXLbvROgaCpyjVMAeLxzIbya3q0sbxoavGuyQYOoWeMQvVYUmOwMHQnwnitz5Lf60MYZkaIDCEysVGSmkyJ4UfqB1eAbt3sN1qBR9opU0SMrRBgN9moObQ4YVpjq9ijTLxuUIwd8bXfm2rp992IWM00FS_awQjla8NkIv-pdjTsdY_ODyCOlVYahCRSiGictLznguS3npeSxtljDKZsbk93A6l_a7_VIVCjgdp5KYaXPOofJsWJ3RaQvjFYPL87wjTmPgG2TrycI0x2Q_zbkZF30ipw2ONj14IzjkaUK0IMPqS9tsY0danzh_lsn23OUB3YHLEVrhJWlzXbIg5yGT8Je3Vcu7vU6seRbKuGHOUJOYzH-tTiBgjw-tZD5PEU77qfkyGmT8pWcgQceDf9RyY3OwHVWUTqdfF0V1PGuZcIYSS0oAzw7T3pCsgGcMMgaj6QS1cIbHE6Pe8buWR-36Qrqe30Uev7F3Y3qP5imJXba2tkkOnVGsFHoaxhcOBMnqLQPGSX1vVS2dZCoX7H6642pMG0z-I-1AyZrYVx6eVwjoSPIqO4VxyE24Gb5DsC_aitbPtIUHKY2tybkbH7yR8JkTj6yUO7OaC90oPkcvfOKmnEliwOkWBHHhlGtVn_q0MTEfEne-XyCj5StpPw6rTJ83z8uOA12W9qclQN_8JZzteq67ZjuiCgRDnObR5jiA1gM37cQZZ8ZfI2BdeaDXENGGQALbjclVlecQIHyFLaNlmhIy-fJorsmDWWsjjq8hv6fxR-yFCGycRGxfPTYFTez14o_smutYbVbteKVtzE7HbJrKgxd4PgNtPJdJL8IVWCSiT5IBI56LoPevkCHo7lwFv65ZpY07Zecnw9Z4LhuVrPXl9OpLmtqos_htCKZI_NkZW2NDRFrQ9_xR-UyAvyizwUD80sqDPT6Pwq_n3HJckGXZrafIKajvFmQ03O3Nq7Q6tcx1CKd9onFwBJDu96g1vpEq528SIPGfhhsYPM91St3AYEbt0wRiJ25d73G_m5uuI3nmgX2zwRCRAYGeAM0uQpRyITHKDViGkig5-xB0_hTI_C32b7zpmrAQRtq-0HBf0R-RzmDYEZ7JK0TSqdl0ybr8gtqGUppdUdMykefSUpYnphZCiajOM79kfhv1_Ko74yZwGYM2F0SrSuKewJ1gSOw7uEVXXU-1a27OQkRmNVuJeHezXsKBiGCXxCm6jnrgfNyUYaCGlPpgRvdY2RbjBZZN-BwCUJfMqrr34IhI_T7NY8Fmw' --start_date=2020-08-24 --end_date=2020-08-31
'''
