from crewai import Crew, Process
from agents.coordenador_agent import CoordenadorAgent
from tasks.coordenador_task import CoordenarDebate

def criar_crew(tema_debate):
    coordenador_agent = CoordenadorAgent(tema_debate=tema_debate)

    coordenar_debate_task = CoordenarDebate(agent=coordenador_agent)

    crew = Crew(
        agents=[coordenador_agent],  
        tasks=[coordenar_debate_task],  
        process=Process.sequential  
    )

    return crew  