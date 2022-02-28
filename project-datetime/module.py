
import imp

from dateutil import tz
from datetime import datetime, date

local = tz.tzlocal()
utc = tz.UTC

def getDateNow():
    """Tra ve date time"""
    dt = datetime.now(tz=utc)
    return dt 

def demNguocVeTetDuong():
    """Đếm ngược đến tết Dương lịch"""
    today = datetime.now()
    iso_datetime = "2023-01-01"
    tetDuongNamSau = datetime.fromisoformat(iso_datetime)
    day = (tetDuongNamSau - today).days
    return day

# def tinhTuoi():
#     """Viết hàm nhận vào ngày sinh, trả về số tuổi của một người, lưu ý về tháng/ngày sinh"""
#     print("Nhap vao ngay sinh")
#     s = input("> ")
#     dateTimeTuoi = datetime.fromisoformat(s)
#     today = datetime.now()
#     tuoi = (today - dateTimeTuoi)
#     dt = datetime.fromtimestamp(tuoi)
#     return dt.year

def calculate_age(born):
    born = datetime.fromisoformat(born)
    today = date.today()
    return today.year - born.year - ((today.month, today.day) < (born.month, born.day))

def demNgaySinhNhat():
    print("Nhap vao ngay sinh")
    s = input("> ")
    dateTimeTuoi = datetime.fromisoformat(s)
    today = datetime.now()
    tuoi = (today - dateTimeTuoi)
    return tuoi.days
    