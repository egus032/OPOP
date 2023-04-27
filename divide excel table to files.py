from pathlib import Path
import xlwings as xw  # pip install xlwings


EXCEL_FILE = r'C:\Users\User\Desktop\Рабочая папка\от Геращенковой\2023\февраль 2023\Тесты по компетенциям.xlsx'
OUTPUT_DIR = Path(__file__).parent / 'Output'

# Create Output directory
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

with xw.App(visible=False) as app:
    wb = app.books.open(EXCEL_FILE)
    for sheet in wb.sheets:
        wb_new = app.books.add()
        sheet.copy(after=wb_new.sheets[0])
        wb_new.sheets[0].delete()
        wb_new.save(OUTPUT_DIR / f'{sheet.name}.xlsx')
        wb_new.close()