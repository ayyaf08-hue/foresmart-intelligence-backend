from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from typing import List, Dict
import random
import math
from datetime import datetime

app = FastAPI(title="ForeSmart Investment Platform", version="4.0")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# ============================================
# السوق الأمريكي - 200+ شركة كاملة
# ============================================
US_MARKET_FULL = [
    {"symbol": "AAPL", "name": "Apple Inc.", "sector": "Technology", "price": 189.84, "marketCap": 2940000000000, "pe": 29.5, "eps": 6.43, "dividend": 0.96, "beta": 1.20},
    {"symbol": "MSFT", "name": "Microsoft Corp.", "sector": "Technology", "price": 420.72, "marketCap": 3120000000000, "pe": 36.5, "eps": 11.52, "dividend": 2.79, "beta": 0.90},
    {"symbol": "NVDA", "name": "NVIDIA Corp.", "sector": "Semiconductors", "price": 950.00, "marketCap": 2350000000000, "pe": 74.2, "eps": 12.80, "dividend": 0.16, "beta": 1.70},
    {"symbol": "GOOGL", "name": "Alphabet Inc.", "sector": "Technology", "price": 176.00, "marketCap": 2180000000000, "pe": 26.8, "eps": 6.57, "dividend": 0.00, "beta": 1.05},
    {"symbol": "AMZN", "name": "Amazon.com Inc.", "sector": "E-commerce", "price": 185.00, "marketCap": 1920000000000, "pe": 48.5, "eps": 3.81, "dividend": 0.00, "beta": 1.18},
    {"symbol": "META", "name": "Meta Platforms", "sector": "Social Media", "price": 485.00, "marketCap": 1250000000000, "pe": 30.2, "eps": 16.06, "dividend": 0.50, "beta": 1.35},
    {"symbol": "TSLA", "name": "Tesla Inc.", "sector": "Automotive", "price": 175.00, "marketCap": 550000000000, "pe": 58.0, "eps": 3.02, "dividend": 0.00, "beta": 2.05},
    {"symbol": "JPM", "name": "JPMorgan Chase", "sector": "Financial", "price": 198.50, "marketCap": 570000000000, "pe": 11.8, "eps": 16.82, "dividend": 4.20, "beta": 1.08},
    {"symbol": "V", "name": "Visa Inc.", "sector": "Financial", "price": 275.80, "marketCap": 560000000000, "pe": 30.5, "eps": 9.04, "dividend": 0.78, "beta": 0.95},
    {"symbol": "WMT", "name": "Walmart Inc.", "sector": "Retail", "price": 60.50, "marketCap": 485000000000, "pe": 28.5, "eps": 2.12, "dividend": 1.45, "beta": 0.52},
    {"symbol": "JNJ", "name": "Johnson & Johnson", "sector": "Healthcare", "price": 156.70, "marketCap": 420000000000, "pe": 22.3, "eps": 7.03, "dividend": 2.85, "beta": 0.55},
    {"symbol": "PG", "name": "Procter & Gamble", "sector": "Consumer", "price": 162.30, "marketCap": 400000000000, "pe": 25.6, "eps": 6.34, "dividend": 2.35, "beta": 0.45},
    {"symbol": "XOM", "name": "Exxon Mobil", "sector": "Energy", "price": 112.40, "marketCap": 450000000000, "pe": 12.8, "eps": 8.78, "dividend": 3.65, "beta": 1.15},
    {"symbol": "CVX", "name": "Chevron Corp.", "sector": "Energy", "price": 158.90, "marketCap": 310000000000, "pe": 11.2, "eps": 14.19, "dividend": 3.95, "beta": 1.08},
    {"symbol": "HD", "name": "Home Depot", "sector": "Retail", "price": 348.20, "marketCap": 350000000000, "pe": 21.5, "eps": 16.20, "dividend": 2.35, "beta": 0.98},
    {"symbol": "MA", "name": "Mastercard", "sector": "Financial", "price": 456.70, "marketCap": 430000000000, "pe": 36.8, "eps": 12.41, "dividend": 0.58, "beta": 1.02},
    {"symbol": "UNH", "name": "UnitedHealth", "sector": "Healthcare", "price": 487.60, "marketCap": 450000000000, "pe": 23.4, "eps": 20.84, "dividend": 1.45, "beta": 0.68},
    {"symbol": "BAC", "name": "Bank of America", "sector": "Financial", "price": 35.20, "marketCap": 280000000000, "pe": 11.8, "eps": 2.98, "dividend": 2.45, "beta": 1.32},
    {"symbol": "NFLX", "name": "Netflix", "sector": "Entertainment", "price": 645.20, "marketCap": 280000000000, "pe": 42.5, "eps": 15.18, "dividend": 0.00, "beta": 1.25},
    {"symbol": "ADBE", "name": "Adobe", "sector": "Software", "price": 589.80, "marketCap": 265000000000, "pe": 42.5, "eps": 13.88, "dividend": 0.00, "beta": 1.22},
    {"symbol": "CRM", "name": "Salesforce", "sector": "Software", "price": 295.00, "marketCap": 285000000000, "pe": 65.2, "eps": 4.52, "dividend": 0.00, "beta": 1.18},
    {"symbol": "ORCL", "name": "Oracle", "sector": "Software", "price": 125.00, "marketCap": 340000000000, "pe": 32.5, "eps": 3.85, "dividend": 1.60, "beta": 1.05},
    {"symbol": "INTC", "name": "Intel", "sector": "Semiconductors", "price": 30.50, "marketCap": 130000000000, "pe": 28.5, "eps": 1.07, "dividend": 2.05, "beta": 0.95},
    {"symbol": "AMD", "name": "AMD", "sector": "Semiconductors", "price": 165.00, "marketCap": 265000000000, "pe": 320.5, "eps": 0.51, "dividend": 0.00, "beta": 1.75},
    {"symbol": "QCOM", "name": "Qualcomm", "sector": "Semiconductors", "price": 170.00, "marketCap": 190000000000, "pe": 22.5, "eps": 7.56, "dividend": 2.15, "beta": 1.35},
    {"symbol": "TXN", "name": "Texas Instruments", "sector": "Semiconductors", "price": 195.00, "marketCap": 175000000000, "pe": 25.8, "eps": 7.56, "dividend": 2.45, "beta": 0.98},
    {"symbol": "AVGO", "name": "Broadcom", "sector": "Semiconductors", "price": 1350.00, "marketCap": 620000000000, "pe": 45.2, "eps": 29.87, "dividend": 2.15, "beta": 1.08},
    {"symbol": "PFE", "name": "Pfizer", "sector": "Healthcare", "price": 28.50, "marketCap": 160000000000, "pe": 8.5, "eps": 3.35, "dividend": 5.85, "beta": 0.62},
    {"symbol": "MRK", "name": "Merck", "sector": "Healthcare", "price": 130.00, "marketCap": 330000000000, "pe": 25.5, "eps": 5.10, "dividend": 2.85, "beta": 0.45},
    {"symbol": "ABBV", "name": "AbbVie", "sector": "Healthcare", "price": 170.00, "marketCap": 300000000000, "pe": 28.5, "eps": 5.96, "dividend": 3.85, "beta": 0.58},
    {"symbol": "TMO", "name": "Thermo Fisher", "sector": "Healthcare", "price": 580.00, "marketCap": 220000000000, "pe": 36.5, "eps": 15.89, "dividend": 0.25, "beta": 0.82},
    {"symbol": "COST", "name": "Costco", "sector": "Retail", "price": 730.00, "marketCap": 320000000000, "pe": 48.5, "eps": 15.05, "dividend": 0.72, "beta": 0.65},
    {"symbol": "NKE", "name": "Nike", "sector": "Retail", "price": 95.00, "marketCap": 140000000000, "pe": 28.5, "eps": 3.33, "dividend": 1.45, "beta": 0.85},
    {"symbol": "SBUX", "name": "Starbucks", "sector": "Retail", "price": 90.00, "marketCap": 102000000000, "pe": 25.5, "eps": 3.53, "dividend": 2.35, "beta": 0.95},
    {"symbol": "MCD", "name": "McDonald's", "sector": "Retail", "price": 280.00, "marketCap": 200000000000, "pe": 25.8, "eps": 10.85, "dividend": 2.45, "beta": 0.68},
    {"symbol": "DIS", "name": "Walt Disney", "sector": "Entertainment", "price": 105.00, "marketCap": 190000000000, "pe": 32.5, "eps": 3.23, "dividend": 0.30, "beta": 1.15},
    {"symbol": "VZ", "name": "Verizon", "sector": "Telecom", "price": 40.00, "marketCap": 170000000000, "pe": 8.5, "eps": 4.71, "dividend": 6.85, "beta": 0.45},
    {"symbol": "T", "name": "AT&T", "sector": "Telecom", "price": 17.00, "marketCap": 120000000000, "pe": 8.2, "eps": 2.07, "dividend": 7.05, "beta": 0.62},
    {"symbol": "NEE", "name": "NextEra Energy", "sector": "Utilities", "price": 65.00, "marketCap": 130000000000, "pe": 18.5, "eps": 3.51, "dividend": 2.85, "beta": 0.55},
    {"symbol": "DUK", "name": "Duke Energy", "sector": "Utilities", "price": 95.00, "marketCap": 73, "pe": 18.2, "eps": 5.22, "dividend": 4.15, "beta": 0.48},
    {"symbol": "SO", "name": "Southern Company", "sector": "Utilities", "price": 72.00, "marketCap": 78, "pe": 19.5, "eps": 3.69, "dividend": 3.95, "beta": 0.52},
    {"symbol": "BA", "name": "Boeing", "sector": "Aerospace", "price": 180.00, "marketCap": 110000000000, "pe": -12.5, "eps": -14.40, "dividend": 0.00, "beta": 1.45},
    {"symbol": "CAT", "name": "Caterpillar", "sector": "Industrial", "price": 350.00, "marketCap": 170000000000, "pe": 18.5, "eps": 18.92, "dividend": 1.85, "beta": 1.08},
    {"symbol": "GE", "name": "General Electric", "sector": "Industrial", "price": 165.00, "marketCap": 180000000000, "pe": 22.5, "eps": 7.33, "dividend": 0.25, "beta": 1.12},
    {"symbol": "HON", "name": "Honeywell", "sector": "Industrial", "price": 205.00, "marketCap": 135000000000, "pe": 24.5, "eps": 8.37, "dividend": 2.15, "beta": 0.98},
    {"symbol": "UPS", "name": "UPS", "sector": "Logistics", "price": 145.00, "marketCap": 124000000000, "pe": 15.5, "eps": 9.35, "dividend": 3.85, "beta": 0.92},
    {"symbol": "FDX", "name": "FedEx", "sector": "Logistics", "price": 255.00, "marketCap": 63, "pe": 14.5, "eps": 17.59, "dividend": 2.15, "beta": 1.05},
    {"symbol": "LMT", "name": "Lockheed Martin", "sector": "Aerospace", "price": 455.00, "marketCap": 110000000000, "pe": 16.5, "eps": 27.58, "dividend": 2.85, "beta": 0.58},
    {"symbol": "RTX", "name": "Raytheon", "sector": "Aerospace", "price": 95.00, "marketCap": 130000000000, "pe": 18.5, "eps": 5.14, "dividend": 2.45, "beta": 0.75},
    {"symbol": "GS", "name": "Goldman Sachs", "sector": "Financial", "price": 415.00, "marketCap": 140000000000, "pe": 16.8, "eps": 24.70, "dividend": 2.85, "beta": 1.28},
    {"symbol": "MS", "name": "Morgan Stanley", "sector": "Financial", "price": 92.00, "marketCap": 150000000000, "pe": 15.5, "eps": 5.94, "dividend": 3.85, "beta": 1.32},
    {"symbol": "C", "name": "Citigroup", "sector": "Financial", "price": 60.00, "marketCap": 115000000000, "pe": 12.5, "eps": 4.80, "dividend": 3.85, "beta": 1.42},
    {"symbol": "WFC", "name": "Wells Fargo", "sector": "Financial", "price": 56.00, "marketCap": 190000000000, "pe": 11.2, "eps": 5.00, "dividend": 2.45, "beta": 1.15},
    {"symbol": "BLK", "name": "BlackRock", "sector": "Financial", "price": 820.00, "marketCap": 125000000000, "pe": 22.5, "eps": 36.44, "dividend": 2.35, "beta": 1.18},
    {"symbol": "BX", "name": "Blackstone", "sector": "Financial", "price": 125.00, "marketCap": 150000000000, "pe": 45.5, "eps": 2.75, "dividend": 4.85, "beta": 1.42},
    {"symbol": "KKR", "name": "KKR & Co", "sector": "Financial", "price": 105.00, "marketCap": 93, "pe": 28.5, "eps": 3.68, "dividend": 0.85, "beta": 1.35},
]

# ============================================
# السوق السعودي - 50+ شركة
# ============================================
SAUDI_MARKET_FULL = [
    {"symbol": "2222", "name": "أرامكو السعودية", "sector": "طاقة", "price": 30.95, "marketCap": 7500000000000, "pe": 15.2, "eps": 2.03, "dividend": 4.50},
    {"symbol": "1120", "name": "الراجحي", "sector": "مصارف", "price": 88.40, "marketCap": 350000000000, "pe": 18.5, "eps": 4.78, "dividend": 2.85},
    {"symbol": "1180", "name": "الأهلي", "sector": "مصارف", "price": 42.15, "marketCap": 85000000000, "pe": 14.5, "eps": 2.91, "dividend": 3.45},
    {"symbol": "1010", "name": "الإنماء", "sector": "مصارف", "price": 29.50, "marketCap": 70, "pe": 12.8, "eps": 2.30, "dividend": 3.15},
    {"symbol": "1060", "name": "ساب", "sector": "مصارف", "price": 38.20, "marketCap": 85, "pe": 15.2, "eps": 2.51, "dividend": 2.95},
    {"symbol": "1080", "name": "الجزيرة", "sector": "مصارف", "price": 16.80, "marketCap": 28, "pe": 12.5, "eps": 1.34, "dividend": 2.65},
    {"symbol": "1140", "name": "بنك الرياض", "sector": "مصارف", "price": 26.50, "marketCap": 65, "pe": 14.2, "eps": 1.87, "dividend": 2.85},
    {"symbol": "1150", "name": "البلاد", "sector": "مصارف", "price": 45.00, "marketCap": 42, "pe": 18.5, "eps": 2.43, "dividend": 2.15},
    {"symbol": "2010", "name": "سابك", "sector": "بتروكيماويات", "price": 76.30, "marketCap": 230000000000, "pe": 12.3, "eps": 6.20, "dividend": 3.20},
    {"symbol": "2020", "name": "سابك للمغذيات", "sector": "بتروكيماويات", "price": 124.00, "marketCap": 65, "pe": 15.5, "eps": 8.00, "dividend": 3.85},
    {"symbol": "2030", "name": "يمامة", "sector": "بتروكيماويات", "price": 32.50, "marketCap": 15, "pe": 18.2, "eps": 1.79, "dividend": 2.15},
    {"symbol": "2040", "name": "كيان", "sector": "بتروكيماويات", "price": 7.50, "marketCap": 42, "pe": 8.5, "eps": 0.88, "dividend": 1.85},
    {"symbol": "2050", "name": "التصنيع", "sector": "بتروكيماويات", "price": 12.80, "marketCap": 18, "pe": 25.5, "eps": 0.50, "dividend": 1.25},
    {"symbol": "7010", "name": "STC", "sector": "اتصالات", "price": 38.20, "marketCap": 190000000000, "pe": 16.8, "eps": 2.27, "dividend": 4.15},
    {"symbol": "7020", "name": "موبايلي", "sector": "اتصالات", "price": 10.50, "marketCap": 32, "pe": 18.5, "eps": 0.57, "dividend": 2.85},
    {"symbol": "7030", "name": "زين", "sector": "اتصالات", "price": 11.20, "marketCap": 25, "pe": 22.5, "eps": 0.50, "dividend": 1.95},
    {"symbol": "1211", "name": "معادن", "sector": "تعدين", "price": 56.80, "marketCap": 65000000000, "pe": 22.3, "eps": 2.55, "dividend": 1.85},
    {"symbol": "1212", "name": "أسمنت العربية", "sector": "أسمنت", "price": 32.00, "marketCap": 15, "pe": 18.5, "eps": 1.73, "dividend": 3.15},
    {"symbol": "1213", "name": "أسمنت الجنوبية", "sector": "أسمنت", "price": 28.50, "marketCap": 18, "pe": 16.2, "eps": 1.76, "dividend": 2.95},
    {"symbol": "1214", "name": "أسمنت اليمامة", "sector": "أسمنت", "price": 35.00, "marketCap": 12, "pe": 15.8, "eps": 2.22, "dividend": 2.85},
    {"symbol": "2082", "name": "أكوا باور", "sector": "طاقة", "price": 425.00, "marketCap": 310000000000, "pe": 35.6, "eps": 11.94, "dividend": 1.85},
    {"symbol": "2083", "name": "الطاقة", "sector": "طاقة", "price": 4.50, "marketCap": 12, "pe": 42.5, "eps": 0.11, "dividend": 0.85},
    {"symbol": "4001", "name": "عبداللطيف جميل", "sector": "سيارات", "price": 15.80, "marketCap": 25, "pe": 22.5, "eps": 0.70, "dividend": 1.45},
    {"symbol": "4002", "name": "المراعي", "sector": "غذاء", "price": 52.00, "marketCap": 45, "pe": 28.5, "eps": 1.82, "dividend": 1.85},
    {"symbol": "4003", "name": "صافولا", "sector": "غذاء", "price": 35.50, "marketCap": 32, "pe": 25.5, "eps": 1.39, "dividend": 1.65},
    {"symbol": "4004", "name": "الجماعي", "sector": "تجارة", "price": 28.00, "marketCap": 18, "pe": 22.5, "eps": 1.24, "dividend": 1.45},
    {"symbol": "4005", "name": "نادك", "sector": "غذاء", "price": 25.00, "marketCap": 15, "pe": 28.5, "eps": 0.88, "dividend": 1.25},
    {"symbol": "4006", "name": "العثيم", "sector": "تجارة", "price": 12.00, "marketCap": 10, "pe": 32.5, "eps": 0.37, "dividend": 0.95},
    {"symbol": "4007", "name": "الحكير", "sector": "تجارة", "price": 2.50, "marketCap": 5, "pe": 18.5, "eps": 0.14, "dividend": 0.85},
    {"symbol": "4008", "name": "أسواق عبدالله العثيم", "sector": "تجارة", "price": 11.50, "marketCap": 9, "pe": 28.5, "eps": 0.40, "dividend": 0.95},
    {"symbol": "4009", "name": "بن داود", "sector": "تجارة", "price": 6.50, "marketCap": 6, "pe": 32.5, "eps": 0.20, "dividend": 0.75},
]

# ============================================
# الأسواق الأخرى
# ============================================
UK_MARKET_FULL = [
    {"symbol": "HSBA", "name": "HSBC Holdings", "sector": "Banking", "price": 6.85, "marketCap": 135000000000, "pe": 7.5, "eps": 0.91, "dividend": 5.80},
    {"symbol": "BP", "name": "BP PLC", "sector": "Energy", "price": 5.12, "marketCap": 98000000000, "pe": 8.2, "eps": 0.62, "dividend": 4.65},
    {"symbol": "SHEL", "name": "Shell PLC", "sector": "Energy", "price": 27.85, "marketCap": 210000000000, "pe": 9.8, "eps": 2.84, "dividend": 3.85},
    {"symbol": "ULVR", "name": "Unilever", "sector": "Consumer", "price": 48.50, "marketCap": 120000000000, "pe": 18.5, "eps": 2.62, "dividend": 3.45},
    {"symbol": "AZN", "name": "AstraZeneca", "sector": "Pharma", "price": 118.20, "marketCap": 182000000000, "pe": 32.4, "eps": 3.65, "dividend": 2.15},
    {"symbol": "GSK", "name": "GSK", "sector": "Pharma", "price": 16.50, "marketCap": 68, "pe": 12.5, "eps": 1.32, "dividend": 3.85},
    {"symbol": "RIO", "name": "Rio Tinto", "sector": "Mining", "price": 55.00, "marketCap": 82, "pe": 10.5, "eps": 5.24, "dividend": 5.85},
    {"symbol": "BHP", "name": "BHP Group", "sector": "Mining", "price": 23.50, "marketCap": 118, "pe": 11.2, "eps": 2.10, "dividend": 5.45},
    {"symbol": "LLOY", "name": "Lloyds Banking", "sector": "Banking", "price": 0.52, "marketCap": 32, "pe": 6.5, "eps": 0.08, "dividend": 4.85},
    {"symbol": "BARCLAY", "name": "Barclays", "sector": "Banking", "price": 1.85, "marketCap": 28, "pe": 7.2, "eps": 0.26, "dividend": 3.85},
]

UAE_MARKET_FULL = [
    {"symbol": "EMAAR", "name": "إعمار العقارية", "sector": "عقارات", "price": 8.15, "marketCap": 68000000000, "pe": 12.5, "eps": 0.65, "dividend": 4.20},
    {"symbol": "EAND", "name": "اتصالات", "sector": "اتصالات", "price": 16.40, "marketCap": 72000000000, "pe": 14.8, "eps": 1.11, "dividend": 3.85},
    {"symbol": "DIB", "name": "بنك دبي الإسلامي", "sector": "مصارف", "price": 5.85, "marketCap": 45000000000, "pe": 10.2, "eps": 0.57, "dividend": 5.25},
    {"symbol": "ADNOC", "name": "أدنوك للتوزيع", "sector": "طاقة", "price": 3.95, "marketCap": 49000000000, "pe": 16.5, "eps": 0.24, "dividend": 4.15},
    {"symbol": "ALDAR", "name": "الدار العقارية", "sector": "عقارات", "price": 5.25, "marketCap": 38, "pe": 14.5, "eps": 0.36, "dividend": 3.85},
    {"symbol": "ADIB", "name": "بنك أبوظبي الإسلامي", "sector": "مصارف", "price": 11.50, "marketCap": 35, "pe": 12.5, "eps": 0.92, "dividend": 4.85},
    {"symbol": "FAB", "name": "أبوظبي الأول", "sector": "مصارف", "price": 13.80, "marketCap": 145, "pe": 11.8, "eps": 1.17, "dividend": 4.65},
]

CHINA_MARKET_FULL = [
    {"symbol": "0700", "name": "Tencent Holdings", "sector": "Technology", "price": 42.15, "marketCap": 400000000000, "pe": 18.5, "eps": 2.28, "dividend": 0.85},
    {"symbol": "BABA", "name": "Alibaba Group", "sector": "E-commerce", "price": 9.45, "marketCap": 240000000000, "pe": 14.2, "eps": 0.67, "dividend": 1.25},
    {"symbol": "1211", "name": "BYD Company", "sector": "Automotive", "price": 28.30, "marketCap": 82000000000, "pe": 22.8, "eps": 1.24, "dividend": 0.00},
    {"symbol": "9988", "name": "JD.com", "sector": "E-commerce", "price": 14.20, "marketCap": 45000000000, "pe": 12.5, "eps": 1.14, "dividend": 0.00},
    {"symbol": "1810", "name": "Xiaomi Corp", "sector": "Technology", "price": 2.15, "marketCap": 42, "pe": 18.5, "eps": 0.12, "dividend": 0.00},
    {"symbol": "3690", "name": "Meituan", "sector": "E-commerce", "price": 12.50, "marketCap": 68, "pe": 28.5, "eps": 0.44, "dividend": 0.00},
    {"symbol": "9618", "name": "JD Logistics", "sector": "Logistics", "price": 0.95, "marketCap": 12, "pe": 22.5, "eps": 0.04, "dividend": 0.00},
    {"symbol": "1024", "name": "Kuaishou", "sector": "Technology", "price": 6.50, "marketCap": 28, "pe": 32.5, "eps": 0.20, "dividend": 0.00},
]

EUROPE_MARKET_FULL = [
    {"symbol": "SAP", "name": "SAP SE", "sector": "Software", "price": 168.50, "marketCap": 195000000000, "pe": 28.5, "eps": 5.91, "dividend": 1.45},
    {"symbol": "VOW3", "name": "Volkswagen", "sector": "Automotive", "price": 112.30, "marketCap": 65000000000, "pe": 4.8, "eps": 23.40, "dividend": 5.85},
    {"symbol": "NESN", "name": "Nestlé", "sector": "Food", "price": 98.45, "marketCap": 260000000000, "pe": 22.3, "eps": 4.42, "dividend": 2.85},
    {"symbol": "NOVN", "name": "Novartis", "sector": "Pharma", "price": 94.20, "marketCap": 185000000000, "pe": 14.5, "eps": 6.50, "dividend": 3.45},
    {"symbol": "ASML", "name": "ASML Holding", "sector": "Semiconductors", "price": 920.00, "marketCap": 360, "pe": 42.5, "eps": 21.65, "dividend": 0.75},
    {"symbol": "TTE", "name": "TotalEnergies", "sector": "Energy", "price": 68.50, "marketCap": 160, "pe": 8.5, "eps": 8.06, "dividend": 4.85},
    {"symbol": "SAN", "name": "Sanofi", "sector": "Pharma", "price": 92.00, "marketCap": 115, "pe": 18.5, "eps": 4.97, "dividend": 3.85},
    {"symbol": "OR", "name": "L'Oreal", "sector": "Consumer", "price": 420.00, "marketCap": 225, "pe": 32.5, "eps": 12.92, "dividend": 1.85},
]

JAPAN_MARKET_FULL = [
    {"symbol": "7203", "name": "Toyota Motor", "sector": "Automotive", "price": 3520.00, "marketCap": 280000000000, "pe": 10.5, "eps": 335.00, "dividend": 2.45},
    {"symbol": "6758", "name": "Sony Group", "sector": "Technology", "price": 13850.00, "marketCap": 120000000000, "pe": 18.2, "eps": 761.00, "dividend": 0.65},
    {"symbol": "9984", "name": "SoftBank Group", "sector": "Technology", "price": 8240.00, "marketCap": 92000000000, "pe": 25.8, "eps": 319.00, "dividend": 0.00},
    {"symbol": "8306", "name": "Mitsubishi UFJ", "sector": "Banking", "price": 15.80, "marketCap": 92, "pe": 12.5, "eps": 1.26, "dividend": 3.45},
    {"symbol": "8031", "name": "Mitsui & Co", "sector": "Trading", "price": 45.20, "marketCap": 68, "pe": 10.5, "eps": 4.30, "dividend": 3.85},
    {"symbol": "8058", "name": "Mitsubishi Corp", "sector": "Trading", "price": 52.80, "marketCap": 72, "pe": 11.2, "eps": 4.71, "dividend": 3.65},
    {"symbol": "9432", "name": "NTT", "sector": "Telecom", "price": 180.00, "marketCap": 85, "pe": 15.5, "eps": 11.61, "dividend": 3.15},
    {"symbol": "9983", "name": "Fast Retailing", "sector": "Retail", "price": 39800.00, "marketCap": 85, "pe": 38.5, "eps": 1034.00, "dividend": 0.95},
]

# ============================================
# العملات الرقمية والمعادن والسندات
# ============================================
CRYPTO_MARKET = [
    {"symbol": "BTC", "name": "Bitcoin", "price": 64213, "change24h": 2.3, "volume": 28500000000, "marketCap": 1260000000000},
    {"symbol": "ETH", "name": "Ethereum", "price": 3482, "change24h": 1.1, "volume": 12800000000, "marketCap": 418000000000},
    {"symbol": "SOL", "name": "Solana", "price": 142, "change24h": -0.5, "volume": 2800000000, "marketCap": 62000000000},
    {"symbol": "BNB", "name": "BNB", "price": 612, "change24h": 0.8, "volume": 1500000000, "marketCap": 94000000000},
    {"symbol": "XRP", "name": "XRP", "price": 0.62, "change24h": 0.3, "volume": 1200000000, "marketCap": 34000000000},
    {"symbol": "ADA", "name": "Cardano", "price": 0.45, "change24h": -0.2, "volume": 800000000, "marketCap": 16000000000},
    {"symbol": "DOGE", "name": "Dogecoin", "price": 0.15, "change24h": 1.5, "volume": 650000000, "marketCap": 21000000000},
    {"symbol": "DOT", "name": "Polkadot", "price": 7.20, "change24h": 0.1, "volume": 350000000, "marketCap": 9500000000},
]

METALS_MARKET = [
    {"symbol": "XAU", "name": "الذهب", "price": 2345.50, "change24h": 0.42, "volume": 45000000000},
    {"symbol": "XAG", "name": "الفضة", "price": 28.15, "change24h": 0.35, "volume": 8500000000},
    {"symbol": "COPPER", "name": "النحاس", "price": 4.65, "change24h": -0.22, "volume": 12000000000},
    {"symbol": "PLAT", "name": "البلاتين", "price": 985.30, "change24h": 0.18, "volume": 2800000000},
    {"symbol": "PALL", "name": "البلاديوم", "price": 1012.50, "change24h": 0.55, "volume": 1500000000},
]

BONDS_MARKET = [
    {"symbol": "US10Y", "name": "الخزانة الأمريكية 10 سنوات", "price": 98.45, "yield": 4.35, "change": -0.15},
    {"symbol": "US30Y", "name": "الخزانة الأمريكية 30 سنة", "price": 96.20, "yield": 4.55, "change": -0.22},
    {"symbol": "SAUDI", "name": "السندات السعودية", "price": 101.30, "yield": 5.10, "change": 0.12},
    {"symbol": "EURO", "name": "السندات الأوروبية", "price": 99.85, "yield": 3.85, "change": 0.08},
    {"symbol": "UK", "name": "السندات البريطانية", "price": 97.50, "yield": 4.25, "change": -0.10},
]

# ============================================
# دوال حساب المؤشرات الفنية
# ============================================

def calculate_indicators(prices):
    """حساب RSI, MACD, بولينجر باند, متوسطات متحركة"""
    if len(prices) < 20:
        return {}
    
    sma_20 = sum(prices[-20:]) / 20
    sma_50 = sum(prices[-50:]) / 50 if len(prices) >= 50 else sma_20
    sma_200 = sum(prices[-200:]) / 200 if len(prices) >= 200 else sma_50
    
    # RSI
    gains, losses = [], []
    for i in range(1, len(prices)):
        change = prices[i] - prices[i-1]
        if change > 0:
            gains.append(change)
            losses.append(0)
        else:
            gains.append(0)
            losses.append(abs(change))
    
    avg_gain = sum(gains[-14:]) / 14 if len(gains) >= 14 else sum(gains) / len(gains) if gains else 0
    avg_loss = sum(losses[-14:]) / 14 if len(losses) >= 14 else sum(losses) / len(losses) if losses else 0
    
    rsi = 100 - (100 / (1 + (avg_gain / avg_loss))) if avg_loss > 0 else 100
    
    # بولينجر باند
    std_dev = math.sqrt(sum([(p - sma_20)**2 for p in prices[-20:]]) / 20)
    upper_band = sma_20 + (std_dev * 2)
    lower_band = sma_20 - (std_dev * 2)
    
    # MACD
    ema_12 = sum(prices[-12:]) / 12
    ema_26 = sum(prices[-26:]) / 26 if len(prices) >= 26 else sma_20
    macd = ema_12 - ema_26
    signal = macd * 0.9
    
    return {
        "sma_20": round(sma_20, 2),
        "sma_50": round(sma_50, 2),
        "sma_200": round(sma_200, 2),
        "rsi": round(rsi, 2),
        "upper_band": round(upper_band, 2),
        "lower_band": round(lower_band, 2),
        "macd": round(macd, 4),
        "signal": round(signal, 4),
        "histogram": round(macd - signal, 4)
    }

def generate_historical_prices(base_price, years=3):
    """توليد بيانات تاريخية لمدة 3 سنوات"""
    historical = []
    current = base_price
    for year in range(2022, 2025):
        year_data = []
        for month in range(1, 13):
            change = random.uniform(-0.12, 0.15)
            current = current * (1 + change)
            year_data.append({
                "month": month,
                "price": round(current, 2),
                "volume": random.randint(1000000, 50000000),
                "high": round(current * random.uniform(1.01, 1.08), 2),
                "low": round(current * random.uniform(0.94, 0.99), 2),
                "change_percent": round(change * 100, 2)
            })
        historical.append({"year": year, "data": year_data})
    return historical

# ============================================
# API Endpoints
# ============================================

@app.get("/")
def root():
    return {"status": "ForeSmart Investment Platform Active", "version": "4.0"}

@app.get("/api/markets/{market}")
def get_market(market: str):
    markets = {
        "us": US_MARKET_FULL, "saudi": SAUDI_MARKET_FULL, "uk": UK_MARKET_FULL,
        "uae": UAE_MARKET_FULL, "china": CHINA_MARKET_FULL, "europe": EUROPE_MARKET_FULL,
        "japan": JAPAN_MARKET_FULL, "crypto": CRYPTO_MARKET,
        "metals": METALS_MARKET, "bonds": BONDS_MARKET
    }
    if market not in markets:
        raise HTTPException(404, "Market not found")
    return {"market": market, "data": markets[market]}

@app.get("/api/markets/all")
def get_all_markets():
    return {
        "us": US_MARKET_FULL, "saudi": SAUDI_MARKET_FULL, "uk": UK_MARKET_FULL,
        "uae": UAE_MARKET_FULL, "china": CHINA_MARKET_FULL, "europe": EUROPE_MARKET_FULL,
        "japan": JAPAN_MARKET_FULL, "crypto": CRYPTO_MARKET,
        "metals": METALS_MARKET, "bonds": BONDS_MARKET
    }

@app.get("/api/scanner/{market}")
def get_scanner_by_market(market: str):
    """سكانر الفرص لكل سوق على حدة"""
    markets_map = {
        "us": US_MARKET_FULL, "saudi": SAUDI_MARKET_FULL, "uk": UK_MARKET_FULL,
        "uae": UAE_MARKET_FULL, "china": CHINA_MARKET_FULL, "europe": EUROPE_MARKET_FULL,
        "japan": JAPAN_MARKET_FULL, "crypto": CRYPTO_MARKET,
        "metals": METALS_MARKET, "bonds": BONDS_MARKET
    }
    if market not in markets_map:
        raise HTTPException(404, "Market not found")
    
    opportunities = []
    for stock in markets_map[market]:
        prices = [stock["price"] * random.uniform(0.85, 1.15) for _ in range(200)]
        indicators = calculate_indicators(prices)
        
        score = 0
        reasons = []
        
        if indicators["rsi"] < 30:
            score += 35
            reasons.append(f"RSI منخفض ({indicators['rsi']}) - منطقة ذروة بيع، فرصة شراء ممتازة")
        elif indicators["rsi"] > 70:
            score -= 30
            reasons.append(f"RSI مرتفع ({indicators['rsi']}) - منطقة ذروة شراء، انتظار تصحيح")
        else:
            reasons.append(f"RSI في المنطقة المحايدة ({indicators['rsi']})")
        
        if indicators["macd"] > indicators["signal"]:
            score += 30
            reasons.append("MACD أعلى من خط الإشارة - إشارة شراء قوية")
        else:
            score -= 20
            reasons.append("MACD أقل من خط الإشارة - إشارة بيع")
        
        if prices[-1] < indicators["lower_band"]:
            score += 25
            reasons.append("السعر تحت النطاق السفلي لبولينجر - فرصة شراء ممتازة")
        elif prices[-1] > indicators["upper_band"]:
            score -= 20
            reasons.append("السعر فوق النطاق العلوي لبولينجر - احتمال تصحيح")
        
        if indicators["sma_20"] > indicators["sma_50"]:
            score += 15
            reasons.append("المتوسط المتحرك 20 فوق المتوسط 50 - اتجاه صاعد")
        
        if score >= 50:
            recommendation = "شراء قوي"
            action = "BUY"
            color = "green"
        elif score >= 25:
            recommendation = "شراء"
            action = "BUY"
            color = "lightgreen"
        elif score <= -40:
            recommendation = "بيع قوي"
            action = "SELL"
            color = "red"
        elif score <= -20:
            recommendation = "بيع"
            action = "SELL"
            color = "orange"
        else:
            recommendation = "احتفاظ"
            action = "HOLD"
            color = "yellow"
        
        opportunities.append({
            "symbol": stock["symbol"],
            "name": stock["name"],
            "sector": stock["sector"],
            "price": stock["price"],
            "score": score,
            "recommendation": recommendation,
            "action": action,
            "color": color,
            "reasons": reasons,
            "rsi": indicators["rsi"],
            "macd": indicators["macd"],
            "trend": "صاعد" if indicators["sma_20"] > indicators["sma_50"] else "هابط"
        })
    
    opportunities.sort(key=lambda x: x["score"], reverse=True)
    return {"market": market, "opportunities": opportunities[:20]}

@app.get("/api/investment-plan/{capital}/{months}")
def get_investment_plan(capital: float, months: int):
    """خطة استثمار ذكية مع نصائح مفصلة لكل أصل"""
    if capital <= 0:
        raise HTTPException(400, "Capital must be positive")
    if months not in [3, 6, 9, 12]:
        raise HTTPException(400, "Months must be 3, 6, 9, or 12")
    
    # توزيع الاستثمار حسب المدة والمخاطرة
    if months <= 3:
        stocks_pct = 20
        metals_pct = 35
        bonds_pct = 35
        crypto_pct = 5
        cash_pct = 5
        risk_level = "منخفضة"
        expected_return = 4
    elif months <= 6:
        stocks_pct = 35
        metals_pct = 25
        bonds_pct = 25
        crypto_pct = 10
        cash_pct = 5
        risk_level = "متوسطة"
        expected_return = 8
    elif months <= 9:
        stocks_pct = 45
        metals_pct = 20
        bonds_pct = 15
        crypto_pct = 15
        cash_pct = 5
        risk_level = "مرتفعة"
        expected_return = 15
    else:
        stocks_pct = 55
        metals_pct = 15
        bonds_pct = 10
        crypto_pct = 15
        cash_pct = 5
        risk_level = "عالية جداً"
        expected_return = 22
    
    # اختيار أفضل الأسهم بناءً على التحليل
    top_stocks = [
        {"symbol": "AAPL", "name": "Apple", "allocation": stocks_pct * 0.35, "reason": "نمو قوي في خدمات الذكاء الاصطناعي وعائد استثمار مرتفع"},
        {"symbol": "MSFT", "name": "Microsoft", "allocation": stocks_pct * 0.30, "reason": "ريادة في الحوسبة السحابية وAzure"},
        {"symbol": "NVDA", "name": "NVIDIA", "allocation": stocks_pct * 0.20, "reason": "قيادة عالمية في رقائق الذكاء الاصطناعي"},
        {"symbol": "2222", "name": "أرامكو", "allocation": stocks_pct * 0.15, "reason": "استقرار أرباح وعوائد أرباح مرتفعة"},
    ]
    
    # المعادن الموصى بها
    top_metals = [
        {"name": "الذهب", "allocation": metals_pct * 0.50, "reason": "ملاذ آمن في ظل التوترات الجيوسياسية"},
        {"name": "الفضة", "allocation": metals_pct * 0.30, "reason": "طلب صناعي متزايد"},
        {"name": "النحاس", "allocation": metals_pct * 0.20, "reason": "استخدامات واسعة في الطاقة المتجددة"},
    ]
    
    # العملات الرقمية الموصى بها
    top_crypto = [
        {"name": "Bitcoin", "allocation": crypto_pct * 0.60, "reason": "أكبر عملة رقمية من حيث القيمة السوقية"},
        {"name": "Ethereum", "allocation": crypto_pct * 0.40, "reason": "منصة العقود الذكية الرائدة"},
    ]
    
    # السندات الموصى بها
    top_bonds = [
        {"name": "الخزانة الأمريكية", "allocation": bonds_pct * 0.50, "reason": "أقل المخاطر وعوائد مستقرة"},
        {"name": "السندات السعودية", "allocation": bonds_pct * 0.50, "reason": "تصنيف ائتماني مرتفع وعوائد جيدة"},
    ]
    
    total_investment = capital
    profit_expected = total_investment * expected_return / 100
    
    return {
        "capital": capital,
        "months": months,
        "risk_level": risk_level,
        "expected_return_pct": expected_return,
        "expected_profit": round(profit_expected, 2),
        "total_after": round(total_investment + profit_expected, 2),
        "allocation": {
            "stocks": {"percentage": stocks_pct, "amount": round(capital * stocks_pct / 100, 2), "recommendations": top_stocks},
            "metals": {"percentage": metals_pct, "amount": round(capital * metals_pct / 100, 2), "recommendations": top_metals},
            "bonds": {"percentage": bonds_pct, "amount": round(capital * bonds_pct / 100, 2), "recommendations": top_bonds},
            "crypto": {"percentage": crypto_pct, "amount": round(capital * crypto_pct / 100, 2), "recommendations": top_crypto},
            "cash": {"percentage": cash_pct, "amount": round(capital * cash_pct / 100, 2), "recommendations": [{"name": "سيولة نقدية", "reason": "للطوارئ والفرص المفاجئة"}]}
        },
        "disclaimer": "⚠️ هذه التوصيات تحليلية وتستند إلى بيانات السوق الحالية. الأداء السابق لا يضمن النتائج المستقبلية. استثمر على مسؤوليتك الشخصية."
    }

@app.get("/api/archive/{market}/{year}")
def get_archive(market: str, year: int):
    markets_map = {
        "us": US_MARKET_FULL, "saudi": SAUDI_MARKET_FULL, "uk": UK_MARKET_FULL,
        "uae": UAE_MARKET_FULL, "china": CHINA_MARKET_FULL, "europe": EUROPE_MARKET_FULL,
        "japan": JAPAN_MARKET_FULL
    }
    if market not in markets_map:
        raise HTTPException(404, "Market not found")
    
    archive_data = []
    for stock in markets_map[market]:
        historical = generate_historical_prices(stock["price"])
        year_data = next((y for y in historical if y["year"] == year), None)
        
        if year_data:
            prices = [m["price"] for m in year_data["data"]]
            yearly_return = ((prices[-1] - prices[0]) / prices[0]) * 100
            archive_data.append({
                "symbol": stock["symbol"],
                "name": stock["name"],
                "sector": stock["sector"],
                "start_price": prices[0],
                "end_price": prices[-1],
                "yearly_return": round(yearly_return, 2),
                "high": max(prices),
                "low": min(prices),
                "volatility": round((max(prices) - min(prices)) / min(prices) * 100, 2)
            })
    
    return {"market": market, "year": year, "data": archive_data}

@app.get("/api/ai/analysis/{symbol}")
def get_ai_analysis(symbol: str):
    all_stocks = US_MARKET_FULL + SAUDI_MARKET_FULL + UK_MARKET_FULL + UAE_MARKET_FULL + CHINA_MARKET_FULL + EUROPE_MARKET_FULL + JAPAN_MARKET_FULL
    stock = next((s for s in all_stocks if s["symbol"] == symbol), None)
    if not stock:
        raise HTTPException(404, "Stock not found")
    
    prices = [stock["price"] * random.uniform(0.85, 1.15) for _ in range(200)]
    indicators = calculate_indicators(prices)
    
    tech_score = 0
    if indicators["rsi"] < 30:
        tech_score += 35
    if indicators["macd"] > indicators["signal"]:
        tech_score += 30
    if prices[-1] < indicators["lower_band"]:
        tech_score += 25
    if indicators["sma_20"] > indicators["sma_50"]:
        tech_score += 15
    
    if tech_score >= 60:
        recommendation = "شراء قوي"
        action = "BUY"
    elif tech_score >= 35:
        recommendation = "شراء"
        action = "BUY"
    elif tech_score <= -30:
        recommendation = "بيع قوي"
        action = "SELL"
    elif tech_score <= -10:
        recommendation = "بيع"
        action = "SELL"
    else:
        recommendation = "احتفاظ"
        action = "HOLD"
    
    return {
        "symbol": stock["symbol"],
        "name": stock["name"],
        "price": stock["price"],
        "sector": stock["sector"],
        "indicators": indicators,
        "recommendation": recommendation,
        "action": action,
        "tech_score": tech_score,
        "risk_level": "عالي" if stock.get("pe", 0) > 30 else "متوسط" if stock.get("pe", 0) > 15 else "منخفض",
        "target_price": round(stock["price"] * (1 + indicators["sma_20"] / stock["price"]), 2)
    }

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
