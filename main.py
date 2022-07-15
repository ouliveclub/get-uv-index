import requests
import tkinter as tk


# Vị trí
lat = '10.769444'    # Vĩ độ
lon = '106.681944'   # Kinh độ
city = 'Thành phố Hồ Chí Minh'

# Cấu hình API
api_url = 'https://api.openuv.io/api/v1/uv?lat=10.82&lng=106.69'
access_token = '7b38de561ff1059867763dae7fd80ef1'

def get_uv_data():
    r = None
    try:
        r = requests.get(api_url, headers={'x-access-token': access_token})
    except Exception as e:
        print(e)

    if r != None and r.status_code == 200:
        return r.json()

    return r

data = get_uv_data()

if data != None:
    data = data['result']
    uv_index = data['uv']
    uv_description = ''
    uv_color = ''

    if uv_index >= 0 and uv_index <= 2.9:
        uv_description = 'Nguy cơ gây hại rất thấp 😊'
        uv_color = '#388e3c'
    elif uv_index >= 3 and uv_index <= 5.9:
        uv_description = 'Nguy cơ gây hại trung bình 😐'
        uv_color = '#fbc02d'
    elif uv_index >= 6 and uv_index <= 7.9:
        uv_description = 'Nguy cơ gây hại cao 😣'
        uv_color = '#fb8c00'
    elif uv_index >= 8 and uv_index <= 10.9:
        uv_description = 'Nguy cơ gây hại cực cao 😫'
        uv_color = '#b91400'
    elif uv_index >= 11:
        uv_description = 'Ra đường chết ráng chịu 😵‍💫'
        uv_color = '#7b1fa2'


    # Giao diện
    window = tk.Tk()
    window.title('Chương trình lấy chỉ số UV - Live Club')
    window.geometry('500x500')
    window.config(padx=10, pady=100)

    title_label = tk.Label(
        text='Chỉ số tia UV'
    )
    title_label.config(font=('Arial', 13))
    title_label.config(fg='#444444')
    title_label.pack()

    city_label = tk.Label(
        text=f'Tại {city}'
    )
    city_label.config(font=('Arial', 15))
    city_label.config(fg='#333333')
    city_label.pack()

    uv_index_label = tk.Label(
        text=f'{uv_index}'
    )

    uv_index_label.config(font=('Arial', 40))
    uv_index_label.config(fg=uv_color)
    uv_index_label.pack()

    uv_description_label = tk.Label(
        text=uv_description
    )
    uv_description_label.config(fg='#666666')
    uv_description_label.config(font=('Arial', 12))
    uv_description_label.pack()


    window.mainloop()