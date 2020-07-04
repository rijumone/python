import json
import requests
from loguru import logger
from datetime import datetime, timedelta

def main():
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
        'cookie': 'Subdomain=decisiontree.keka.com; ThemeIndex=7; ASP.NET_SessionId=o2ml14pl42pb2rbevjadai15; .AspNet.Cookies=h5rZZ0JJFHmEu3TFo9apXshAat17jrY-r6Legs7vGtPRzLJtw6XT1AnycW4oHlRalckLfG1M2rpExjrOCt99kuipTkc67uD92p-1ug4QR3BM_m6MWZdF6uY5ePeM7SKGczGsP4TAvSHMQ2rk9Nikmox3RFSOw_YLX5t6FHw5xR1e7BbR8lG5FV46yv08IAN_q3ptBOYtkZ9YFzLOkAUnfRLsIOKjm08MpRaq-ztj5JcEARvRmhKrRr9l0hHv2MTpOK2pMpdmD4erHUUwxW_PSUcjwhVLCfZEWX1hJwG0rIk1C58iGz1cnuF9x2k0UuEY3jg_MHpEuLCANAHAt60S46dkGEJ5QzBsasAQ1FcnEGgUFxF37YI--_w8YviQER3Yt-8cB50XIoq92ttZv2jOrr5DENEeqzrBFJp_JjOElc3w_mUrpYYfnlJEjCrcc6kBOStN1sruWN5_ksRDYHnylPKaWFw-GxGRX-xuv_zCRhfxLZUVlzkMMk7Mc8RCagbjpV6X08RnAz6Fp4MgbjFG3XrzQXsbOimBglHw3j9CnAQ98FefBGsVppklNNw7CYd5CGCJ9g3hRlceBqEF0ugah5T3eCUa9zgXQTD9mjsCu9_14Ou1QeVSYaL_wo5USpmVHbU3mNDr0HBnEI1Y8cl6uYuZdsKx_93dJJsOD6R7p8Rg1pJhlknOppwL_EsvxWElJWrsLbyDB5r603l13313U_f_XbW_ouWomdHjcKbm7BN9w4sf_URMBlBd3Br8ArrAyf52f46k4Win7MHSsFNIAwXDUH9CB_FVqvWOvMervOoM62w5r6Dm-8bbYlg3C-IRX6VzCTpuYOske4W9cJnmiHNV1HIKkYhRNnLEja2_7eWcczVkJsiftyBzyGwZDCP08_tUiFYj6aGli-NB-ZI6i30FoCUFHGz9lN9iZzbQ4F2ZySAM5SltP0-SOb6AG0KxCbaWoXmM-SSHD3JyZSAG3TRxjn5tO83lfgdiiGYFpC_FUnfT5u8j56uSI5Pdwy0_ibH8IMZ5CebCo3RiNSfKu8SgPufGzo-LEnsdRxQcVMsF8iMZVZfO2CO5rmFSZVbx4rR7DCtYPlibOthWjAkMygAtB86x9Qu5Gp2nbu0ZehfvpXk0LHIE42jwtT5pkgzcNf2fHrwy6atHMjT0-qGsVfpriuTTHiY1soNAUU_QDUW8yyce1EKwXuYb3Oo456Y5p6V63i5P-mZZnv8PaBtMEOshTjfQuFWAbc0VpwbBky-7V7QQCexArHzU3VyHo3Fx15OrnLgQUGYj4H3KZoojmbrPwGLBY-PPFKK3LnlBKjGmI1Sr70XX4ur5uyTp_fTNfckpt3pmg1UU6z-H2NDARd45yWh75_kl87oBmSrU9l37QDtBAm0zVShRXodYbu5Azmk-25RydRC-ruV3YHj704LQnfDZ8ZgCSNNInNMrYrclBQwjudVdWQGSYJ4gRw8I9OqLvcCFLjKms47zI950zdIzZNlHedw6D7tugIwD7MhhyJCg_Cc_zvdEX52wUtrkij5Tbu1oED37ajMyMYuDo4tX_30e97QqoxmLkmlzWRP8idRP6gr272CZHbH9iIl_O4ZpnvzvAikUx4_Zg3T4kiutfLQZLstNFNsZUFd7RXLhp1S_bQmwyq_EQ22Brpsrl5-KKmZNp9NsFxuDBLnHThsGxG-YpQfnX6ME_LaP0qHvJlsbnBQ3n5hu7wI3iQUCSmHSP6pqyuLNpmrz4H0Bw0BUMD-O8a8x0W5Qlqlx3Hd6P0KgSCkRdc8nUKSLaqobWudj2w3L88FWT0OzqLG92XIuJBbmJ3n-GsD6IPzuCPx2RMhzfHlAr-lVi6exAvd5yeSXzr2e-IWH6UyQa4NM9GfhRomsbFHUn0pBWZ-zjpyV8UBH6GtJmV6fmOaVuWReFtY6Ma7GQ6yF0TbsIg1drmGSGe0rGw7ann9X_wgnjCndWLl_uHpARdeCcGzOyXGMTNMlstXXjJIgQh6jCp4ZTUwl8pC8aKDZ6ju6_LZwqe2eoV09xoJrOPxwg-zZrG690faK6GpMLirMWlDO_CNqI7UuQCkpAjap8nGto3N4brn7a4KzS3H9HBW_1rl_MZw2A0vSnF8Fq2A91-2d6OOaalxMABNDclNoZGwv9MTRkO_JkilHZdwh6GYI8_9j28qb'
    }
    start_date = datetime.strptime('20200622', '%Y%m%d')
    end_date = datetime.strptime('20200624', '%Y%m%d')
    n_dates_diff = (end_date - start_date).days + 1
    current_date = start_date
    for i in range(n_dates_diff):
        
        payload = json.dumps({
            "timeEntries": [],
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