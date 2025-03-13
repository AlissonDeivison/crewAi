from crewai import Task

class CoordenarDebate(Task):
    def __init__(self, agent): 
        super().__init__(
            description="Coordenar um debate televisivo sobre o tema ",
            expected_output="Um relatório detalhado sobre o debate, incluindo os temas discutidos, os participantes envolvidos, as regras estabelecidas, as intervenções realizadas, os conflitos resolvidos, as decisões tomadas e as lições aprendidas.",
            agent=agent, 
        )