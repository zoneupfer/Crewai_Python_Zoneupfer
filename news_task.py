from crewai import Task
from datetime import date
from textwrap import dedent

class NewsTasks ():
    
    def search_news(self, agent):
        today = date.today()
        return Task(description = "ค้นหาข่าวล่าสุดเกี่ยวกับตลาดคริปโตเคอเรนซี่และสรุปผลลัพธ์",
                    expected_output = dedent(f"""
                                             ค้าหาข่าว ข้อมูลเกี่ยวกับคริปโตในวันที่ {today} หรือประเด็นร้อนแรงที่ทำให้มีผลกระทบต่อราคาคริปโต
                                             จำเป็นต้องค้นหาข่าวที่เป็นข้อมูลที่ถูกต้อง 
                                             และมีความสำคัญจำนวนมากที่สุดพร้อมรายละเอียดที่เป็นประโยชน์
                                             """), agent = agent)
    
    
    def analyze_news(self, agent):
        return Task(description = "วิเคราะห์ข่าวเกี่ยวกับคริปโตที่ได้รับ",
                 expected_output = dedent(f"""
                                          วิเคราะห์ข่าวเกี่ยวกับคริปโตที่ได้รับ 
                                          โดยนำข่าวที่ได้รับมาวิเคราะห์ หาประโยนช์ 
                                          หรือผลกระทบต่อตลาดคริปโต
                                          """), agent = agent)
    
    
    
    def summarize_news(self, agent):
        return Task(description = "สรุปข่าวเกี่ยวกับคริปโตที่ได้รับ โดยนำข่าวที่ได้รับมาสรุปให้สั้นกระชับและเข้าใจง่าย",
                    expected_output = "สรุปข่าวเกี่ยวกับคริปโตที่ได้ทำการวิเคราะห์มาแล้วให้กระชับเข้าใจง่าย",
                    agent = agent)
        
    
    
    def write_news(self, agent):
        return Task(description = "นักเขียนที่ชำนาญในการเขียนข่าวเกี่ยวกับคริปโต มีความสามารถในการเขียนข่าวให้สรุปและเข้าใจง่าย",
                    expected_output = "เขียนข่าวเกี่ยวกับคริปโตตามข้อมูลที่ได้รับมา โดยนำข้อมูลที่ได้รับมา มาเขียนข่าวให้สรุปและเข้าใจง่าย",
                    output_file = 'crypto_news_output.txt',
                    agent = agent)
    
    
    def translate_news(self, agent):
        return Task(description = "แปลข่าวเกี่ยวกับคริปโตที่ได้รับจากภาษาอังกฤษเป็นภาษาเป้าหมาย",
                    expected_output = dedent("""
                                            แปลข่าวเกี่ยวกับคริปโตที่ได้รับจากภาษาอังกฤษเป็นภาษาเป้าหมาย โดยทำให้เนื้อหาสามารถเข้าใจได้ง่าย
                                            และถูกต้องทางภาษา รวมถึงรักษาความหมายเดิมของข่าวโดยไม่บิดเบือน
                                            """),
                    agent = agent)