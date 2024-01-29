import pytest
import requests
import json


@pytest.mark.parametrize("cellphone", ["09333974776"])
def test_login_mobile_with_no_password(cellphone):
    url = "https://snappfood.ir/mobile/v2/user/loginMobileWithNoPass"
    headers = {
        'Content-Type': 'application/x-www-form-urlencoded',
    }
    data = {
        'deviceType': 'WEBSITE',
        'appVersion': '8.1.1',
        'cellphone': cellphone
    }

    response = requests.post(url, headers=headers, data=data)

    assert response.status_code == 200
    # Add more assertions to validate the response as needed

    assert 'access_token' in response.json()
    assert response.json()['status'] == 'success'


@pytest.mark.parametrize("cellphone, code", [("09333974776", "50689")])
def test_login_mobile_with_token(cellphone, code):
    url = "https://snappfood.ir/mobile/v2/user/loginMobileWithToken"
    headers = {
        'Content-Type': 'application/x-www-form-urlencoded',
        'Cookie': 'PHPSESSID=d9d154db04846d992911515e03c63d59'
    }
    data = {
        'optionalClient': 'WEBSITE',
        'client': 'WEBSITE',
        'deviceType': 'WEBSITE',
        'appVersion': '8.1.1',
        'cellphone': cellphone,
        'code': code
    }

    response = requests.post(url, headers=headers, data=data)

    assert response.status_code == 200
    # Add more assertions to validate the response as needed

    # Example assertion: Check if the response contains a specific key in the JSON data
    assert 'access_token' in response.json()

    # Example assertion: Check if the response data matches an expected value
    assert response.json()['status'] == 'success'
    response_data = response.text
    with open("response2.json", "w") as file:
        json.dump(response_data, file)
    res = response.json()
    access_token = res.get('nested_jwt')


@pytest.mark.parametrize("vendor_code, page", [("0qqwd9", 1)])
def test_vendor_comment(vendor_code, page):
    url = 'https://snappfood.ir/mobile/v1/restaurant/vendor-comment'
    cookies = {

        'jwt-token_type': 'Bearer',
        'jwt-expires_in': '2678400',
        'jwt-access_token': 'eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiIsImp0aSI6ImZkODFlMjA2NGRmOTE2ZDZlMTdhNjEyNzNlZTgxMmE2OWMyZWY2N2NlMDkzM2FlNDM5M2E5YWM5ZjQyZTQxNDJjYzdmMGEwMTAzZmM1ZmFjIn0.eyJhdWQiOiJzbmFwcGZvb2RfcHdhIiwianRpIjoiZmQ4MWUyMDY0ZGY5MTZkNmUxN2E2MTI3M2VlODEyYTY5YzJlZjY3Y2UwOTMzYWU0MzkzYTlhYzlmNDJlNDE0MmNjN2YwYTAxMDNmYzVmYWMiLCJpYXQiOjE3MDY0NDQ4ODYsIm5iZiI6MTcwNjQ0NDg4NiwiZXhwIjoxNzA5MTIzNDA2LCJzdWIiOiIiLCJzY29wZXMiOlsibW9iaWxlX3YyIiwibW9iaWxlX3YxIiwid2VidmlldyJdfQ.Kh9vFXKar00EaeKjyP2t2WdYm8VDaOlc_Y5JOIG9BzRMelf2X0-yiToVkNN6yATQf3nisPXXQXgrrtuNwSjI71Ee5_SVLD6VH7cKpfU44oKE8GjhO2rOj1IWjqjg-EaA4Z-lpYPFBH-ohpwIjeiaaLeaX9L7Qr-IeBedYe2lgVs-16AeX0aUsfy0XbV1GkJdYgB3gfzIjgiCufMXAlAdT5RYiUc-p3AwWnzNdEEz1HZBeXLPDq4t3UkQp-TDb22u9M6jqclGgnagT0iiquCLxGukU1ZHOxT0GLS2m4W2MxFZJ18uyy0VztzErUOVrvYr_SzZQKG87k-icuTY1-vQFPwIp0JH4lOJEej0H-9gAggFmQ0n-GNGcywbfCfbFpm-egJ0zniKNG9jTHEqy7mbnZZPY4gD-UHtePffkxls3_YewfA4RSEQklgyc45u3dcrrXgj1TL47SPt0dPr4Vm3MJF0Tjufl5rpfDCfCt7v470IYH6kQrAdrnr8MtjZ0NiGpdTzPM6j3bf4ajIHe4TFvcS1wSQZ-u1MGYgnv69XfJBxOrIDcQUo_LDxEolqNjpTcNu7JpZ2OBJI9HSDqtdNlOVtKnAagGpwDJ0VksdbRWmzxwp1xQg0B26WD-J84LrupIy4k9m8DpMHSrZBNrE7qXyljyJUzmVgyOO7Ey2YhPSFdYLbZP150awTCHKm1n1SZBaX6jbVNixino9K25iTvNx7me6rr_FtsnaXKSr6eq5SpDiPnKuKgY8WrDFghbLrGNUGYYH4lad0qjKXRCFC51rJJ_OeUdPbmWq6dTmTcl5cM7PatwDiuXjIJP9FZ3vPaMo_fj6oVvUKG8AYOYSkfwv561fRdxi__A0WzZYQ0Q_cGFl_LpHiE040B1wRrXwTajM-Bb9LxgqOQLFtuqzm9o93lu53_vwiwMK_GdLJyywFSGA-ezXqFlV1yi1gqdmjvh7OOFB-IAXCPkgvmoUw3Jkl7rl4jX6HkEqtmobZMNtfA0Ky5FWInxdmTIXDnFiKoWT0MPV20_aD0Sgewa8kc6CkvyHm5FmmDBAlF3v44Tx5CQSDYN9gUgLfDuS-ne4JDGyeTAr0NjxhYOPwxfhtQxLhnHBcrds5a0RVPm-6RSkiAVBlH0Q9f6IOLCuW4nzCI__aQ1rJ8DkzxCF917CalrephticDniXFomUSFohQAZ5eq7Mma_yP9D9rPnkax9QGl23fc_L-mRALlpG2ktUdY3Z_iuJns3cr1uyX69Wbhu4GcbWBTewzvjXORz3xX8Lin5_--fLww-MPjJ_BiQ-SyPuKAgfjMNwic2sqaDRR7ja9MT7-Z_BcY0j4G4MkCCXBf92Pe9cn6hbde5T0gIp7F03YcIVO7hYbTvsofZXehv6MADyr9jQpjnIBx_ohA2Zd2Rbng9fTR0-cdnxed9yI3RrZYWdGMs9qVmde6jDcgGzVk_6QgCciqYuQuHPWW1TNd6GXo0hSej7HdlYnWoU1sVwcE2yHYCNDK_5l8LVriX6C8wyVRnjGR0hilqJHe1WkAmTecdb-GuA4MYb6DCD1b2OpIf7P3-OH3oHmaMFRn5Nl1hNSGPxyFJXDa6l0Xs82STcyYBESqQ9fpnK_7lrVJafnp1qUHeZt5oJoXgUh-3DUlLlnnYrM8Tbpeix0LMUoevwdBEx22rs9n6mPxi6MhOqVahAaIGUFSANE_aXfcmUW2oWXkTWhuXVqMDtODzEhA0jHte0t7h0JSFnCXM1QW8NrmDNwiSx_1gIunaW0T5UXp0zx0HGZkLJmrYuOAVlNuMRD33OUh-A497AnFr9oriocx-nOyxs0GHf7o-aduh12Tw0jqnv1KJ050zqfWFM973WQr_ZIYSq9tYs9P4aCEccEOAPAvqU-y_1AxBNyrUx0RppFt7vAdISBZ42YHTUVYLraDGszzBGni3x0MHWMoChYmCdtd-z8s1Ey2HFwFM5H42qVx4H82Mi_uAd0ILEVPl9pvqm16jpC56BhIZjwgn-UGKNkh365oFieuBKm2RBiE7aGGThnWFLb79eGH9Z99rmDoUc4P5wX69T-Oy6MbBLp-BaRYbJteJvHsJ8ucf0lYe4JtytonIoHYxAjDY7vtE-ZAcMjf9x1f-zH8lTnSXLa25xOMldQCGetO0VRO2Lkzg8yyZqqe8aU-CWPw99-pATW0miXekLuYRaAXxc8UHYLGTWGZ9DFxPRIERJS5vn04Cn1SqLOFt5SM1u6CQRGQtcH8VWTDb1IZ6u1PE4jDcffrIGZKF0RobH3me46MJEIt90TLKG4Vvci1tUFUqQ_uYXoSVziN0q71sU6GH3kz6OxfqiQjgr3zL9VnodeRhIGNx9R6_e2WToBzNiPnmBu4o0EljfYk-RrID5cPqh4usQGalq-oSSAjZnqNqhCM5g969HjUc2GJthmaVNP3PdYRA_G41i3W7d1OHPjWhN8diDhUQN-7QK-PHpEQHyWmyhvgTWbxfhkNv2LRKmv2sBUaRgMOdcMxBLElK7UOjVOMaC1IlLCA6AUuQZOLHC2hCKTSiweS2B54QnE3qh7X1uEa4xER4Y9nfoZol9w5R8lp_flb8piq6liMnXOVkcZvhcXl1Zlkfj90VhvefrYuH-u_Y5LwjduvFCQ4pzDEP2YNgp4SvG-JSLWF8mo_6KCzc3InUErtQtYBG9XCbCMoDITs-7ZbAHdzhAMvb34bOKR_Uwz5_bIfqYZHh4u6p4MRc',
        'rl_session': 'RudderEncrypt%3AU2FsdGVkX187Im1WOJG5fmKrAAC5JORrA2fx7%2FtzHPLtn4J3d5%2BDyGYlSwkUHWW2RjgXvGjm1fzXg4jFK%2FB7RVwoztMwyBOQhSnwGdbjt9mFXLglCb9LwgztuzAfCOXrs7WbjvKMHYEU6fKSS%2BmYgg%3D%3D',
        '_hjSessionUser_3300609': 'eyJpZCI6IjE4NmU4ZWQ3LWYyZGUtNTExZi05ZjU0LTVkMmNiZWM0NTZkYiIsImNyZWF0ZWQiOjE3MDY0NDY0ODI4MTgsImV4aXN0aW5nIjpmYWxzZX0=',
        '_ga_DLKJDL41ZH': 'GS1.1.1706446470.1.1.1706446560.60.0.0',
        '_ga_S8BD3BVGB1': 'GS1.2.1706446527.1.0.1706446560.27.0.0',
        '_ga_G5J9VQQMGL': 'GS1.1.1706446470.1.1.1706446560.60.0.0',
        'rl_user_id': 'RudderEncrypt%3AU2FsdGVkX1%2BqS8qCr2FSCBLEt79gdljqH8VxnjWFiLg%3D',
        'rl_anonymous_id': 'RudderEncrypt%3AU2FsdGVkX1%2B9ir4uywXWr%2BTDihwP8%2F8gkN7m618Qzkvoqwim1hRHGfGzBvXW6tkhmZM%2FeIogr%2FLpZvsevOzLWg%3D%3D',
        'PHPSESSID': '36372986506f4b5d9bfee70c5cab36a1',
    }

    headers = {
        'authority': 'snappfood.ir',
        'accept': 'application/json, text/plain, */*',
        'accept-language': 'fa,en-US;q=0.9,en;q=0.8',
        'authorization': 'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiIsImp0aSI6ImZkODFlMjA2NGRmOTE2ZDZlMTdhNjEyNzNlZTgxMmE2OWMyZWY2N2NlMDkzM2FlNDM5M2E5YWM5ZjQyZTQxNDJjYzdmMGEwMTAzZmM1ZmFjIn0.eyJhdWQiOiJzbmFwcGZvb2RfcHdhIiwianRpIjoiZmQ4MWUyMDY0ZGY5MTZkNmUxN2E2MTI3M2VlODEyYTY5YzJlZjY3Y2UwOTMzYWU0MzkzYTlhYzlmNDJlNDE0MmNjN2YwYTAxMDNmYzVmYWMiLCJpYXQiOjE3MDY0NDQ4ODYsIm5iZiI6MTcwNjQ0NDg4NiwiZXhwIjoxNzA5MTIzNDA2LCJzdWIiOiIiLCJzY29wZXMiOlsibW9iaWxlX3YyIiwibW9iaWxlX3YxIiwid2VidmlldyJdfQ.Kh9vFXKar00EaeKjyP2t2WdYm8VDaOlc_Y5JOIG9BzRMelf2X0-yiToVkNN6yATQf3nisPXXQXgrrtuNwSjI71Ee5_SVLD6VH7cKpfU44oKE8GjhO2rOj1IWjqjg-EaA4Z-lpYPFBH-ohpwIjeiaaLeaX9L7Qr-IeBedYe2lgVs-16AeX0aUsfy0XbV1GkJdYgB3gfzIjgiCufMXAlAdT5RYiUc-p3AwWnzNdEEz1HZBeXLPDq4t3UkQp-TDb22u9M6jqclGgnagT0iiquCLxGukU1ZHOxT0GLS2m4W2MxFZJ18uyy0VztzErUOVrvYr_SzZQKG87k-icuTY1-vQFPwIp0JH4lOJEej0H-9gAggFmQ0n-GNGcywbfCfbFpm-egJ0zniKNG9jTHEqy7mbnZZPY4gD-UHtePffkxls3_YewfA4RSEQklgyc45u3dcrrXgj1TL47SPt0dPr4Vm3MJF0Tjufl5rpfDCfCt7v470IYH6kQrAdrnr8MtjZ0NiGpdTzPM6j3bf4ajIHe4TFvcS1wSQZ-u1MGYgnv69XfJBxOrIDcQUo_LDxEolqNjpTcNu7JpZ2OBJI9HSDqtdNlOVtKnAagGpwDJ0VksdbRWmzxwp1xQg0B26WD-J84LrupIy4k9m8DpMHSrZBNrE7qXyljyJUzmVgyOO7Ey2YhPSFdYLbZP150awTCHKm1n1SZBaX6jbVNixino9K25iTvNx7me6rr_FtsnaXKSr6eq5SpDiPnKuKgY8WrDFghbLrGNUGYYH4lad0qjKXRCFC51rJJ_OeUdPbmWq6dTmTcl5cM7PatwDiuXjIJP9FZ3vPaMo_fj6oVvUKG8AYOYSkfwv561fRdxi__A0WzZYQ0Q_cGFl_LpHiE040B1wRrXwTajM-Bb9LxgqOQLFtuqzm9o93lu53_vwiwMK_GdLJyywFSGA-ezXqFlV1yi1gqdmjvh7OOFB-IAXCPkgvmoUw3Jkl7rl4jX6HkEqtmobZMNtfA0Ky5FWInxdmTIXDnFiKoWT0MPV20_aD0Sgewa8kc6CkvyHm5FmmDBAlF3v44Tx5CQSDYN9gUgLfDuS-ne4JDGyeTAr0NjxhYOPwxfhtQxLhnHBcrds5a0RVPm-6RSkiAVBlH0Q9f6IOLCuW4nzCI__aQ1rJ8DkzxCF917CalrephticDniXFomUSFohQAZ5eq7Mma_yP9D9rPnkax9QGl23fc_L-mRALlpG2ktUdY3Z_iuJns3cr1uyX69Wbhu4GcbWBTewzvjXORz3xX8Lin5_--fLww-MPjJ_BiQ-SyPuKAgfjMNwic2sqaDRR7ja9MT7-Z_BcY0j4G4MkCCXBf92Pe9cn6hbde5T0gIp7F03YcIVO7hYbTvsofZXehv6MADyr9jQpjnIBx_ohA2Zd2Rbng9fTR0-cdnxed9yI3RrZYWdGMs9qVmde6jDcgGzVk_6QgCciqYuQuHPWW1TNd6GXo0hSej7HdlYnWoU1sVwcE2yHYCNDK_5l8LVriX6C8wyVRnjGR0hilqJHe1WkAmTecdb-GuA4MYb6DCD1b2OpIf7P3-OH3oHmaMFRn5Nl1hNSGPxyFJXDa6l0Xs82STcyYBESqQ9fpnK_7lrVJafnp1qUHeZt5oJoXgUh-3DUlLlnnYrM8Tbpeix0LMUoevwdBEx22rs9n6mPxi6MhOqVahAaIGUFSANE_aXfcmUW2oWXkTWhuXVqMDtODzEhA0jHte0t7h0JSFnCXM1QW8NrmDNwiSx_1gIunaW0T5UXp0zx0HGZkLJmrYuOAVlNuMRD33OUh-A497AnFr9oriocx-nOyxs0GHf7o-aduh12Tw0jqnv1KJ050zqfWFM973WQr_ZIYSq9tYs9P4aCEccEOAPAvqU-y_1AxBNyrUx0RppFt7vAdISBZ42YHTUVYLraDGszzBGni3x0MHWMoChYmCdtd-z8s1Ey2HFwFM5H42qVx4H82Mi_uAd0ILEVPl9pvqm16jpC56BhIZjwgn-UGKNkh365oFieuBKm2RBiE7aGGThnWFLb79eGH9Z99rmDoUc4P5wX69T-Oy6MbBLp-BaRYbJteJvHsJ8ucf0lYe4JtytonIoHYxAjDY7vtE-ZAcMjf9x1f-zH8lTnSXLa25xOMldQCGetO0VRO2Lkzg8yyZqqe8aU-CWPw99-pATW0miXekLuYRaAXxc8UHYLGTWGZ9DFxPRIERJS5vn04Cn1SqLOFt5SM1u6CQRGQtcH8VWTDb1IZ6u1PE4jDcffrIGZKF0RobH3me46MJEIt90TLKG4Vvci1tUFUqQ_uYXoSVziN0q71sU6GH3kz6OxfqiQjgr3zL9VnodeRhIGNx9R6_e2WToBzNiPnmBu4o0EljfYk-RrID5cPqh4usQGalq-oSSAjZnqNqhCM5g969HjUc2GJthmaVNP3PdYRA_G41i3W7d1OHPjWhN8diDhUQN-7QK-PHpEQHyWmyhvgTWbxfhkNv2LRKmv2sBUaRgMOdcMxBLElK7UOjVOMaC1IlLCA6AUuQZOLHC2hCKTSiweS2B54QnE3qh7X1uEa4xER4Y9nfoZol9w5R8lp_flb8piq6liMnXOVkcZvhcXl1Zlkfj90VhvefrYuH-u_Y5LwjduvFCQ4pzDEP2YNgp4SvG-JSLWF8mo_6KCzc3InUErtQtYBG9XCbCMoDITs-7ZbAHdzhAMvb34bOKR_Uwz5_bIfqYZHh4u6p4MRc',
        'content-type': 'application/x-www-form-urlencoded',
    }

    params = {

        'optionalClient': 'WEBSITE',
        'client': 'WEBSITE',
        'deviceType': 'WEBSITE',
        'appVersion': '8.1.1',
        'vendorCode': vendor_code,
        'page': page,

    }

    response = requests.get(
        url,
        params=params,
        headers=headers,
        cookies=cookies

    )
    assert response.status_code == 200
    response_data = response.text
    with open("response.json", "w") as file:
        json.dump(response_data, file)
