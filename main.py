from dotenv import load_dotenv
from crews.crew_principal import criar_crew


load_dotenv()
tema_debate = "Mudanças climáticas"

crew = criar_crew(tema_debate)

resultado = crew.kickoff()

print("Resultado do debate:")
print(resultado)