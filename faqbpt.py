from chatterbot.trainers import ListTrainer
from chatterbot import chatterbot

df = ["O que é o PPGEL? Qual é o seu objetivo?","O Programa de Pós-Graduação em Estudos de Linguagens da UTFPR, câmpus Curitiba, tem o objetivo de formar profissionais capazes de compreender como diferentes linguagens se articulam com a tecnologia. Espera-se que o egresso consiga analisar os diferentes modos de produção de sentido nas mais variadas esferas de interação humana, como a Língua, a Literatura e a Comunicação, podendo atuar nas áreas de pesquisa, ensino e em comunicação social. Nesse sentido, o egresso terá como diferencial a experiência em disciplinas e grupos de pesquisa que entendem a linguagem como ponto central nos processos interacionais, propiciando aos discentes uma visão crítica e reflexiva sobre a interface entre tecnologia e linguagens. Conheça a área de concentração e as linhas de pesquisa AQUI.",
"O Curso é gratuito?",
"Sim, PPGEL é inteiramente gratuito, ofertado para todos aqueles que já têm uma graduação concluída.",
"O PPGEL oferece bolsas?",

"O PPGEL conta com um número limitado de bolsas (duas), de modo que a maioria dos alunos precisará cursar o programa sem ajudas de custos. A seleção dos bolsistas segue os critérios estabelecidos no Regulamento e na Comissão de Seleção e Bolsas do Programa.",

 

"Quero ser aluno do PPGEL. Por onde começo?",

"Em primeiro lugar, prepare-se para o processo seletivo, seguindo as especificações para isso, conforme indicação de editais e exemplos de provas anteriores. Depois, veja o que os DOCENTES estão pesquisando; verifique em quais linha e projeto sua proposta de pesquisa se encaixa, a fim de que seu projeto tenha coerência com as linhas de pesquisa do Programa.",

 

"Como funciona o processo seletivo?",

"O processo seletivo ocorre geralmente em meados de setembro, anualmente. É realizada uma prova escrita, com questões discursivas, fundamentadas na bibliografia recomendada para a prova. É indispensável que o candidato leia tais obras, além de outras da área, para estabelecer reflexões pertinentes com o que se espera de um aluno de pós-graduação. Além da prova escrita, há uma defesa do projeto de pesquisa e uma análise do Currículum Vitae do candidato. O PPGEL disponibiliza as provas anteriores e a expectativa da banca de correção AQUI.",

 

"Quantas horas semanais são dedicadas às aulas presenciais?",

"No primeiro ano de ingresso, o aluno precisa dispensar pelo menos três tardes inteiras da semana para as DISCIPLINAS, ministradas preferencialmente à tarde. No segundo ano, há uma maior flexibilidade, a fim de que o aluno intensifique a escrita da dissertação. É desejável que o aluno participe de atividades de pesquisa e eventos dentro e fora do PPGEL durante todo o período do curso.",

 

"Posso me candidatar a aluno especial (externo), ou seja, cursar uma disciplina isolada no PPGEL?",

"A figura do aluno especial, aqui denominado de aluno externo, segue critérios do regulamento do Programa, tendo uma chamada específica, logo após o período de matrículas. Em geral, as matrículas para o primeiro semestre ocorrem entre fevereiro e março, e as do segundo semestre entre julho e agosto. Os interessados devem ficar atentos na Página Inicial ou acessar a Área Discente.",

 

"Posso participar de eventos no PPGEL?",

"Os eventos abertos à comunidade são divulgados AQUI.",

 

"Eu tenho acesso a Biblioteca ou outros meios de buscas?",

"Todos os alunos da Pós-Graduação possuem acesso a Biblioteca da UTFPR, que utiliza o sistema Pergamum, pelo qual os alunos podem fazer consulta ao acervo, reserva de obras, entre outros serviços. Nas dependências da Universidade o aluno também pode acessar o portal de períodico da CAPES, uma biblioteca virtual que disponibiliza o melhor da produção científica nacional e internacional.",


"Sou aluno do PPGEL. Como faço para obter auxílio financeiro para participar de eventos?",

"""O mestrando deve entregar, na secretaria do Programa (ou do Dalic), com pelo menos 10 dias de antecedência, os seguintes itens:

    Folder do evento
    Nome completo
    CPF
    Dados bancários (PAGAMENTO SOMENTE NA CONTA DO FAVORECIDO): banco, agência e número da conta (indicar se é corrente ou poupança).

Depois de realizado o evento, para prestação de contas, o beneficiado deve:

    Entregar certificado ou declaração de participação no evento.

Obs.: Evento já realizado não caracteriza auxílio financeiro à estudante, e despesas com alimentação, hospedagem e passagem não podem ser pagas com restituição, ou seja, SEMPRE a requisição de auxílio deve ser feita antes da data do evento e não pode ser substituída por restituição.""",

 
"Sou aluno do PPGEL e estou prestes a defender minha dissertação. O que devo fazer?",
"Na seção Secretaria/Procedimentos, você encontra um checklist para a finalização do seu trabalho. Em caso de dúvidas, procure seu orientador e a coordenação do Programa."]

bot = ChatBot("faqbot")

bot.set_