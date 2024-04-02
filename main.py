from news_task import NewsTasks
from news_agent import NewsAgent
from crewai import Crew
from dotenv import load_dotenv
import warnings
warnings.filterwarnings("ignore")
load_dotenv()

class NewsCrew:

    def run (self):
        agents = NewsAgent()
        tasks = NewsTasks()

        agents_search_news = agents.searcher()
        agents_analyze_news = agents.analyst()
        agents_summarize_news = agents.summarizer()
        agents_write_news = agents.writer()
        agents_translate_news = agents.translator()
        
        
        tasks_search_news = tasks.search_news(agents_search_news)
        tasks_analyze_news = tasks.analyze_news(agents_analyze_news)
        tasks_summarize_news = tasks.summarize_news(agents_summarize_news)
        tasks_write_news = tasks.write_news(agents_write_news)
        tasks_translate_news = tasks.translate_news(agents_translate_news)
        
        
        crew = Crew(
            agents = [agents_search_news, agents_analyze_news, agents_summarize_news, agents_write_news, agents_translate_news],
            tasks = [tasks_search_news, tasks_analyze_news, tasks_summarize_news, tasks_write_news, tasks_translate_news],
            verbose=True)
        
        
        result = crew.kickoff()
        return result


if __name__ == '__main__':
    news_crew = NewsCrew()
    result = news_crew.run()
    
    print("\n\n########################")
    print("##  NEWS CREW RESULT  ##")
    print("########################\n")
    print(result)