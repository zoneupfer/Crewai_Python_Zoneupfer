from crewai import Agent
from langchain_community.tools import DuckDuckGoSearchRun

search_tool = DuckDuckGoSearchRun()

class NewsAgent():
    
    def searcher(self):
        return Agent(
            role = 'นักค้นหาข้อมูล',
            goal = 'ค้นหาข่าวเกี่ยวกับคริปโตวันนี้ ข่าวล่าสุด หรือข่าวที่มีผลกระทบต่อราคาคริปโต',
            backstory = 'เป็นนักค้นหาข้อมูลที่ชำนาญในการค้นหาข่าวเกี่ยวกับคริปโต',
            tools = [search_tool],
            verbose = True,
            allow_delegation = True)
        
    
    def analyst(self):
        return Agent(
            role = 'นักวิเคราะห์',
            goal = 'วิเคราะห์ข่าวเกี่ยวกับคริปโตที่ได้รับ',
            backstory = 'เป็นนักวิเคราะห์ที่ชำนาญในการวิเคราะห์ข่าวเกี่ยวกับคริปโต มีความสามารถในการวิเคราะห์ข่าวให้เข้าใจง่าย',
            tools = [search_tool],
            verbose = True,
            allow_delegation = True)
    
    
    def summarizer(self):
        return Agent(
            role = 'นักสรุปข่าว',
            goal = 'สรุปข่าวเกี่ยวกับคริปโตที่ได้รับ',
            backstory = 'เป็นนักสรุปข่าวที่ชำนาญในการสรุปข่าวเกี่ยวกับคริปโต มีความสามารถในการสรุปข่าวให้สั้นกระชับและเข้าใจง่าย',
            tools = [search_tool],
            verbose = True,
            allow_delegation = True)
    
    
    def writer(self):
        return Agent(
            role = 'นักเขียน',
            goal = 'เขียนข่าวเกี่ยวกับคริปโตตามข้อมูลที่ได้รับมา',
            backstory = 'เป็นนักเขียนที่ชำนาญในการเขียนข่าวเกี่ยวกับคริปโต มีความสามารถในการเขียนข่าวให้สรุปและเข้าใจง่าย',
            tools = [search_tool],
            allow_delegation = True,
            verbose = True)
    
    
    def translator(self):
        return Agent(
            role = 'นักแปล',
            goal = 'แปลข่าวเกี่ยวกับคริปโตที่ได้รับจากภาษาต้นฉบับเป็นภาษาเป้าหมาย',
            backstory = 'เป็นนักแปลที่ชำนาญในการแปลข่าวเกี่ยวกับคริปโต มีความสามารถในการแปลข่าวให้ถูกต้องและเข้าใจง่าย',
            tools = [search_tool],  # สมมติว่านักแปลอาจใช้เครื่องมือค้นหาเพื่อช่วยในการค้นคว้า
            verbose = True,
            allow_delegation = True)