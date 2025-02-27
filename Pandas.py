{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "authorship_tag": "ABX9TyMbV9nZ8ztAnaMVE1t+Oqz5"
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
    },
    "language_info": {
      "name": "python"
    }
  },
  "cells": [
    {
      "cell_type": "markdown",
      "source": [
        "Você é uma pesquisadora que está tentando entender melhor qual o impacto do estilo de vida de uma pessoa na sua qualidade de sono, por isso fez a coleta dos dados de sobre 373 pessoas, onde foram recolhidas 12 características para cada uma delas. Por competência a sua pesquisa foi bem controlada e você não tem dados faltosos na sua base. Chegou o momento de você fazer sua análise e responder algumas perguntas."
      ],
      "metadata": {
        "id": "_OZMtT1-OS8_"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "import pandas as pd\n",
        "\n",
        "df = pd.read_csv('/content/saude_do_sono_estilo_vida.csv')\n",
        "\n",
        "# Verificando se a DataFrame foi realmente importada corretamente\n",
        "print(df.head(10))\n",
        "df.info()"
      ],
      "metadata": {
        "id": "6qE0My0UOXwI"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "markdown",
      "source": [
        "**1. Ao visualizar a base você percebeu que seria melhor alterar o nome de algumas colunas. Mude o ‘ID’ para ‘Identificador’, corrija o nome da coluna que indica a pressão sanguínea, mude a coluna ‘Ocupação’ para ‘Profissão’, a coluna ‘Categoria BMI’ está em parte em inglês, substitua para ‘Categoria IMC’**"
      ],
      "metadata": {
        "id": "TD25AYJFOzSm"
      }
    },
    {
      "cell_type": "markdown",
      "source": [],
      "metadata": {
        "id": "nsTbmLM3OaTC"
      }
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "id": "HCsBmohoLes4"
      },
      "outputs": [],
      "source": [
        "df = df.rename(columns={'ID': 'Identificador'})\n",
        "df = df.rename(columns={'Pressão sanguíneaaaa': 'Pressão sanguínea'})\n",
        "df = df.rename(columns={'Ocupação': 'Profissão'})\n",
        "df = df.rename(columns={'Categoria BMI': 'Categoria IMC'})\n",
        "\n",
        "print(df.head(10))"
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "**Qual é a média, a moda e a mediana de horas de sono para cada uma das profissões? [‘mean’, np.median, pd.Series.mode]**"
      ],
      "metadata": {
        "id": "KmX23pSXTHev"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "profissão_sono = df.groupby('Profissão')['Duração do sono']\n",
        "\n",
        "print('Média: ' + str(profissão_sono.mean()) + '\\n')\n",
        "print('Mediana: ' + str(profissão_sono.median()) + '\\n')\n",
        "print('Moda: Profissão')\n",
        "for profissão, moda in profissão_sono.apply(lambda x: x.mode()).groupby(level=0):\n",
        "    print(f\"{profissão}: {list(moda.values)}\")"
      ],
      "metadata": {
        "id": "Q_qt6jG3THyW"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "markdown",
      "source": [
        "**3. Das pessoas que atuam com engenharia de software qual a porcentagem de obesos?**"
      ],
      "metadata": {
        "id": "w3UOo61UTizX"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "software_obeso = df[(df['Profissão'] == 'Eng. de Software')\n",
        "                    & (df['Categoria IMC'] == 'Obesidade')]\n",
        "\n",
        "total_software = df[df['Profissão'] == 'Eng. de Software']\n",
        "\n",
        "porcentagem_obesos = (len(software_obeso) / len(total_software)) * 100 if len(total_software) > 0 else 0\n",
        "\n",
        "print(f\"Porcentagem de engenheiros de software obesos: {porcentagem_obesos:.2f}%\")"
      ],
      "metadata": {
        "id": "U6vzmTtkTi7r"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "markdown",
      "source": [
        "**4. De acordo com os dados, advogar ou ser representante de vendas faz você dormir menos? (Use o método ‘isin’, considere a média)**"
      ],
      "metadata": {
        "id": "pS0koeLxTqtz"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "profissões_especificas = df[df['Profissão'].isin(\n",
        "    ['Advogado(a)', 'Representante de Vendas'])]\n",
        "\n",
        "verificacao = profissões_especificas['Duração do sono'].mean() < 8\n",
        "\n",
        "if verificacao == True:\n",
        "  print('Sim. De acordo com os dados, advogar ou ser representante de vendas realmente faz você dormir menos.')\n",
        "else:\n",
        "  print('Não. De acordo com os dados, advogar ou ser representante de vendas não faz você dormir menos.')"
      ],
      "metadata": {
        "id": "4KAq06XTTq4O"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "markdown",
      "source": [
        "**5. Entre quem fez enfermagem e quem fez medicina, quem tem menos horas de sono? (Use o método ‘isin’, considere a média)**"
      ],
      "metadata": {
        "id": "Cd3pZYHWUiJ7"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "medico = df[df['Profissão'].isin(['Médico(a)'])]\n",
        "enfermeiro = df[df['Profissão'].isin(['Enfermeiro(a)'])]\n",
        "\n",
        "medico_sono = medico['Duração do sono'].mean()\n",
        "enfermeiro_sono = enfermeiro['Duração do sono'].mean()\n",
        "\n",
        "if medico_sono > enfermeiro_sono:\n",
        "    print('Os(As) Enfermeiros(as) têm menos horas de sono que os(as) médicos(as).')\n",
        "elif medico_sono < enfermeiro_sono:\n",
        "    print('Os(As) Médicos(as) têm menos horas de sono que os(as) enfermeiros(as).')\n",
        "\n",
        "print('------------------------')\n",
        "\n",
        "medias_sono = df[df['Profissão'].isin(['Médico(a)', 'Enfermeiro(a)'])] \\\n",
        "    .groupby('Profissão')['Duração do sono'].mean()\n",
        "\n",
        "if medias_sono['Médico(a)'] < medias_sono['Enfermeiro(a)']:\n",
        "    print('Os(As) Médicos(as) têm menos horas de sono que os(as) enfermeiros(as).')\n",
        "else:\n",
        "    print('Os(As) Enfermeiros(as) têm menos horas de sono que os(as) médicos(as).')"
      ],
      "metadata": {
        "id": "eyW4b0usUiSg"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "markdown",
      "source": [
        "**6. Faça um subconjunto com as colunas Identificador, Gênero, Idade, Pressão sanguínea e Frequência cardíaca.**"
      ],
      "metadata": {
        "id": "h05hQmk0U3Bq"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "subconjunto_colunas = df[['Identificador', 'Gênero', 'Idade', 'Pressão sanguínea', 'Frequência cardíaca']]\n",
        "\n",
        "print(subconjunto_colunas)"
      ],
      "metadata": {
        "id": "6Hg-LLdXU3JM"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "markdown",
      "source": [
        "**7. Descubra qual a profissão menos frequente no conjunto. (Use value_counts)**"
      ],
      "metadata": {
        "id": "jaRbdY3OU91L"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "frequencia = df['Profissão'].value_counts().idxmin()\n",
        "\n",
        "print('A profissão menos frequente no conjunto é o(a) '+ str(frequencia) + '.')"
      ],
      "metadata": {
        "id": "Klo3FeleU-FA"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "markdown",
      "source": [
        "**8. Quem tem maior pressão sanguínea média, homens ou mulheres? (Considere a média)**"
      ],
      "metadata": {
        "id": "yUWkSayIVQer"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "def media_pressao(pressao):\n",
        "    try:\n",
        "        sistolica, diastolica = pressao.split('/')\n",
        "        return (float(sistolica) + float(diastolica)) / 2\n",
        "    except:\n",
        "        return None\n",
        "\n",
        "mulher = df[df['Gênero'].isin(['Mulher'])]\n",
        "homem = df[df['Gênero'].isin(['Homem'])]\n",
        "\n",
        "mulher.loc[:, 'Pressão sanguínea'] = mulher['Pressão sanguínea'].apply(media_pressao)\n",
        "homem.loc[:, 'Pressão sanguínea'] = homem['Pressão sanguínea'].apply(media_pressao)\n",
        "\n",
        "mulher_sangue = mulher['Pressão sanguínea'].mean()\n",
        "print('A pressão sanguínea média das mulheres é: ' + str(mulher_sangue))\n",
        "homem_sangue = homem['Pressão sanguínea'].mean()\n",
        "print('A pressão sanguínea média dos homens é: ' + str(homem_sangue))\n",
        "\n",
        "if mulher_sangue > homem_sangue:\n",
        "    print('\\nAs mulheres têm maior pressão sanguínea que os homens.')\n",
        "elif mulher_sangue < homem_sangue:\n",
        "    print('\\nOs homens têm maior pressão sanguínea que as mulheres.')"
      ],
      "metadata": {
        "id": "mjGGD9iVVQmu"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "markdown",
      "source": [
        "**9. É predominante entre os participantes dormir 8 horas por dia (considere usar Moda como medida)?**"
      ],
      "metadata": {
        "id": "uL6k1RtVVkO5"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "sono_geral = df['Duração do sono']\n",
        "\n",
        "moda_geral = sono_geral.mode()\n",
        "\n",
        "if moda_geral.iloc[0] < 8:\n",
        "    print(f'Moda geral: {moda_geral.iloc[0]}. Logo, os participantes, predominantemente, dormem menos de 8 horas por dia.\\n')\n",
        "else:\n",
        "    print(f'Moda geral: {moda_geral.iloc[0]}. Logo, os participantes, predominantemente, dormem 8 horas por dia (ou mais!).\\n')"
      ],
      "metadata": {
        "id": "EqDXcn9WVkYO"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "markdown",
      "source": [
        "**10. Pessoas com frequências cardíacas acima de 70 dão mais passos que pessoas com frequência cardíaca menor ou igual a 70? (Use a média)**"
      ],
      "metadata": {
        "id": "fY2C4rQwVvqW"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "freq_mais70 = df['Frequência cardíaca'] >= 70\n",
        "freq_menos70 = df['Frequência cardíaca'] <= 70\n",
        "\n",
        "freq_mais70_passo = df[freq_mais70]['Passos diários'].mean()\n",
        "print(freq_mais70_passo)\n",
        "freq_menos70_passo = df[freq_menos70]['Passos diários'].mean()\n",
        "print(freq_menos70_passo)\n",
        "\n",
        "if freq_mais70_passo > freq_menos70_passo:\n",
        "    print('\\nSim! Pessoas com frequências cardíacas acima de 70 dão mais passos que pessoas com frequência cardíaca menor ou igual a 70.')\n",
        "elif freq_mais70_passo < freq_menos70_passo:\n",
        "    print('\\nNão. Pessoas com frequências cardíacas acima de 70 não dão mais passos que pessoas com frequência cardíaca menor ou igual a 70.')\n",
        "else:\n",
        "    print('\\nPessoas com frequências cardíacas acima de 70 dão os mesmos passos que pessoas com frequência cardíaca menor ou igual a 70.')"
      ],
      "metadata": {
        "id": "BpfiNVEpVvzN"
      },
      "execution_count": null,
      "outputs": []
    }
  ]
}