import pandas as pd

df = pd.read_csv('/content/saude_do_sono_estilo_vida.csv')

# Verificando se a DataFrame foi realmente importada corretamente
print(df.head(10))
df.info()

# Alteração dos nomes das colunas conforme solicitado
df = df.rename(columns={'ID': 'Identificador'})
df = df.rename(columns={'Pressão sanguíneaaaa': 'Pressão sanguínea'})
df = df.rename(columns={'Ocupação': 'Profissão'})
df = df.rename(columns={'Categoria BMI': 'Categoria IMC'})

print(df.head(10))

# Cálculo da média, moda e mediana de horas de sono por profissão
profissao_sono = df.groupby('Profissão')['Duração do sono']

print('Média: ' + str(profissao_sono.mean()) + '\n')
print('Mediana: ' + str(profissao_sono.median()) + '\n')
print('Moda: Profissão')
for profissao, moda in profissao_sono.apply(lambda x: x.mode()).groupby(level=0):
    print(f"{profissao}: {list(moda.values)}")

# Cálculo da porcentagem de engenheiros de software obesos
software_obeso = df[(df['Profissão'] == 'Eng. de Software') & (df['Categoria IMC'] == 'Obesidade')]
total_software = df[df['Profissão'] == 'Eng. de Software']

porcentagem_obesos = (len(software_obeso) / len(total_software)) * 100 if len(total_software) > 0 else 0
print(f"Porcentagem de engenheiros de software obesos: {porcentagem_obesos:.2f}%")

# Verificação se advogados ou representantes de vendas dormem menos
profissoes_especificas = df[df['Profissão'].isin(['Advogado(a)', 'Representante de Vendas'])]

verificacao = profissões_especificas['Duração do sono'].mean() < 8

if verificacao:
    print('Sim. De acordo com os dados, advogar ou ser representante de vendas realmente faz você dormir menos.')
else:
    print('Não. De acordo com os dados, advogar ou ser representante de vendas não faz você dormir menos.')

# Comparação entre médicos e enfermeiros sobre quem dorme menos
medico = df[df['Profissão'] == 'Médico(a)']
enfermeiro = df[df['Profissão'] == 'Enfermeiro(a)']

medico_sono = medico['Duração do sono'].mean()
enfermeiro_sono = enfermeiro['Duração do sono'].mean()

if medico_sono > enfermeiro_sono:
    print('Os(As) Enfermeiros(as) têm menos horas de sono que os(as) médicos(as).')
elif medico_sono < enfermeiro_sono:
    print('Os(As) Médicos(as) têm menos horas de sono que os(as) enfermeiros(as).')

# Criação de subconjunto com colunas específicas
subconjunto_colunas = df[['Identificador', 'Gênero', 'Idade', 'Pressão sanguínea', 'Frequência cardíaca']]
print(subconjunto_colunas)

# Identificação da profissão menos frequente
frequencia = df['Profissão'].value_counts().idxmin()
print('A profissão menos frequente no conjunto é o(a) ' + str(frequencia) + '.')

# Comparação da pressão sanguínea média entre homens e mulheres
def media_pressao(pressao):
    try:
        sistolica, diastolica = pressao.split('/')
        return (float(sistolica) + float(diastolica)) / 2
    except:
        return None

mulher = df[df['Gênero'] == 'Mulher']
homem = df[df['Gênero'] == 'Homem']

mulher['Pressão sanguínea'] = mulher['Pressão sanguínea'].apply(media_pressao)
homem['Pressão sanguínea'] = homem['Pressão sanguínea'].apply(media_pressao)

mulher_sangue = mulher['Pressão sanguínea'].mean()
homem_sangue = homem['Pressão sanguínea'].mean()

print(f'A pressão sanguínea média das mulheres é: {mulher_sangue}')
print(f'A pressão sanguínea média dos homens é: {homem_sangue}')

if mulher_sangue > homem_sangue:
    print('As mulheres têm maior pressão sanguínea que os homens.')
elif mulher_sangue < homem_sangue:
    print('Os homens têm maior pressão sanguínea que as mulheres.')

# Verificação da predominância de dormir 8 horas por dia
sono_geral = df['Duração do sono']
moda_geral = sono_geral.mode()

if moda_geral.iloc[0] < 8:
    print(f'Moda geral: {moda_geral.iloc[0]}. Logo, os participantes predominantemente dormem menos de 8 horas por dia.')
else:
    print(f'Moda geral: {moda_geral.iloc[0]}. Logo, os participantes predominantemente dormem 8 horas ou mais por dia.')
