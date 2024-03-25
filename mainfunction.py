# -*- coding: utf-8 -*-
"""
Created on Sun Sep 17 11:50:39 2023

@author: Admin
"""
import pandas as pd
import yfinance as yf
import reportlab
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle
from reportlab.lib import colors
list_of_stock_tickers = []
start_date = "2010-01-01"
stocks_list = pd.read_excel(r'E:\stock on NSE\MCAP31032023_0.xlsx')
stocks_list_symbol = list(stocks_list['Symbol'])
stk = stocks_list_symbol[10]+".NS"
stk_price_series = yf.download(stk, start=start_date)

stk_price_series.plot(y = 'Close')
pdf = SimpleDocTemplate("dataframe.pdf", pagesize=letter)

table_data = []
for i, row in stk_price_series.iterrows():
    table_data.append(list(row))
    
table = Table(table_data)

table_style = TableStyle([
    ('BACKGROUND', (0, 0), (-1, 0), colors.grey),
    ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
    ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
    ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
    ('FONTSIZE', (0, 0), (-1, 0), 14),
    ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
    ('BACKGROUND', (0, 1), (-1, -1), colors.beige),
    ('TEXTCOLOR', (0, 1), (-1, -1), colors.black),
    ('ALIGN', (0, 1), (-1, -1), 'CENTER'),
    ('FONTNAME', (0, 1), (-1, -1), 'Helvetica'),
    ('FONTSIZE', (0, 1), (-1, -1), 12),
    ('BOTTOMPADDING', (0, 1), (-1, -1), 8),
])

table.setStyle(table_style)

pdf_table = []
pdf_table.append(table)

pdf.build(pdf_table)
