#coleta


CONFIG_NEGOCIO = {

    "materiais": {

        "Plástico": {
            "densidade": 0.90
        },

        "Vidro": {
            "densidade": 2.50
        },

        "Metal": {
            "densidade": 7.80
        }
    },

    "frota": {

        # caminhão
        "capacidade_volume_litros": 10000,

        # alerta
        "limite_compliance_percentual": 90,

        # ociosidade
        "carga_minima_percentual": 30
    },

    "rota": {

        # Custo o por quilômetro
        "custo_km": 20.50
    }
}


#CALCULAR VOLUME


def calcular_volume(material, peso):

    # Verifica se o material existe
    if material not in CONFIG_NEGOCIO["materiais"]:
        raise ValueError(
            "Material inválido."
        )

    # Verifica se o peso é válido
    if peso < 0:
        raise ValueError(
            "O peso não pode ser negativo."
        )

    # Obtém a densidade do material
    densidade = CONFIG_NEGOCIO[
        "materiais"
    ][material]["densidade"]

    # Fórmula:
    # Volume = Peso / Densidade
    volume = peso / densidade

    return volume



# PERCENTUAL DA CARGA


def calcular_percentual_carga(volume):

    capacidade = CONFIG_NEGOCIO[
        "frota"
    ]["capacidade_volume_litros"]

    percentual = (
        volume / capacidade
    ) * 100

    return percentual



#CALCULAR CUSTO DA ROTA


def calcular_custo_rota(distancia):

    custo_km = CONFIG_NEGOCIO[
        "rota"
    ]["custo_km"]

    custo = distancia * custo_km

    return custo



# DADOS DA COLETA


def cadastrar_coletas():

    coletas = []

    
    print("       CADASTRO DOS PONTOS")
   

    while True:

        
        print("NOVO PONTO DE COLETA")
     

        bairro = input(
            "Informe o bairro: "
        ).strip()

        if bairro == "":
            print("O bairro não pode ficar vazio.")
            continue

       
        # MATERIAL
       

        print("\nMateriais disponíveis:")

        print("1 - Plástico")
        print("2 - Vidro")
        print("3 - Metal")

        opcao = input(
            "Escolha o material: "
        ).strip()

        if opcao == "1":
            material = "Plástico"

        elif opcao == "2":
            material = "Vidro"

        elif opcao == "3":
            material = "Metal"

        else:
            print("Material inválido.")
            continue

      
        # PESO
     

        while True:

            try:

                peso = float(
                    input(
                        "Informe a carga em kg: "
                    ).replace(",", ".")
                )

                if peso < 0:
                    print(
                        "O peso não pode ser negativo."
                    )
                    continue

                break

            except ValueError:

                print(
                    "Digite um valor numérico válido."
                )

       
        # DISTÂNCIA
       

        while True:

            try:

                distancia = float(
                    input(
                        "Informe a distância até o bairro (km): "
                    ).replace(",", ".")
                )

                if distancia < 0:
                    print(
                        "A distância não pode ser negativa."
                    )
                    continue

                break

            except ValueError:

                print(
                    "Digite uma distância válida."
                )

      
        # CALCULA VOLUME
     

        volume = calcular_volume(
            material,
            peso
        )

        
        # ADICIONA A COLETA
       

        coletas.append({

            "bairro": bairro,

            "material": material,

            "peso": peso,

            "volume": volume,

            "distancia_km": distancia
        })

        print("\nPonto cadastrado com sucesso!")

        print(
            f"Volume calculado: "
            f"{volume:.2f} L"
        )

      
        # CONTINUAR?
      

        continuar = input(
            "\nDeseja cadastrar outro ponto? (S/N): "
        ).strip().upper()

        if continuar != "S":
            break

    return coletas



#ROTA AUTOMATICAMENTE


def montar_rota(coletas):

    capacidade = CONFIG_NEGOCIO[
        "frota"
    ]["capacidade_volume_litros"]

    volume_total = 0

    distancia_total = 0

    rota = []

    nao_coletados = []

  
    # ORGANIZA PELA MAIOR CARGA
    
    coletas_ordenadas = sorted(
        coletas,
        key=lambda coleta: coleta["volume"],
        reverse=True
    )

    
    print("       ANÁLISE DOS PONTOS")
    

    for coleta in coletas_ordenadas:

        bairro = coleta["bairro"]

        volume = coleta["volume"]

        
        # VERIFICA SE ESTÁ VAZIO
     

        if volume <= 0:

            nao_coletados.append(coleta)

            print(
                f"\n{bairro}: NÃO COLETAR"
            )

            print(
                "Motivo: ponto sem carga."
            )

            continue

       
        # VERIFICA CAPACIDADE
       

        if volume_total + volume <= capacidade:

            rota.append(coleta)

            volume_total += volume

            distancia_total += (
                coleta["distancia_km"]
            )

            print(
                f"\n{bairro}: COLETAR"
            )

            print(
                f"Carga: "
                f"{coleta['peso']:.2f} kg"
            )

            print(
                f"Volume: "
                f"{volume:.2f} L"
            )

        else:

            nao_coletados.append(coleta)

            print(
                f"\n{bairro}: NÃO COLETAR"
            )

            print(
                "Motivo: capacidade do caminhão "
                "insuficiente."
            )

    return (
        rota,
        nao_coletados,
        volume_total,
        distancia_total
    )



#  MOSTRAR RESULTADO


def mostrar_resultado(
    rota,
    nao_coletados,
    volume_total,
    distancia_total
):

    capacidade = CONFIG_NEGOCIO[
        "frota"
    ]["capacidade_volume_litros"]

    limite_compliance = CONFIG_NEGOCIO[
        "frota"
    ]["limite_compliance_percentual"]

    carga_minima = CONFIG_NEGOCIO[
        "frota"
    ]["carga_minima_percentual"]

   
    # PERCENTUAL DA CAPACIDADE
   

    percentual = (
        volume_total / capacidade
    ) * 100

   
    # CUSTO DA ROTA
   

    custo = calcular_custo_rota(
        distancia_total
    )

    
    print("          ROTA DEFINIDA")
    
    if len(rota) == 0:

        print(
            "\nNenhum ponto foi selecionado."
        )

    else:

        for numero, coleta in enumerate(
            rota,
            start=1
        ):

            print(
                f"\n{numero}. "
                f"{coleta['bairro']}"
            )

            print(
                f"   Material: "
                f"{coleta['material']}"
            )

            print(
                f"   Peso: "
                f"{coleta['peso']:.2f} kg"
            )

            print(
                f"   Volume: "
                f"{coleta['volume']:.2f} L"
            )

            print(
                f"   Distância: "
                f"{coleta['distancia_km']:.2f} km"
            )

   
    # RESUMO
  

    print("\n--------------------------------------")

    print(
        f"Volume total: "
        f"{volume_total:.2f} L"
    )

    print(
        f"Capacidade do caminhão: "
        f"{capacidade:.2f} L"
    )

    print(
        f"Capacidade utilizada: "
        f"{percentual:.2f}%"
    )

    print(
        f"Distância total: "
        f"{distancia_total:.2f} km"
    )

    print(
        f"Custo estimado: "
        f"R$ {custo:.2f}"
    )

    
    # OCIOSIDADE
    

    if percentual < carga_minima:

        print(
            "\nALERTA DE OCIOSIDADE!"
        )

        print(
            "A carga está abaixo de "
            f"{carga_minima}% da capacidade."
        )

    else:

        print(
            "\nCarga adequada para a rota."
        )

   
    # COMPLIANCE, limite
    

    if percentual >= limite_compliance:

        print(
            "\nALERTA DE COMPLIANCE!"
        )

        print(
            "A carga atingiu "
            f"{limite_compliance}% da capacidade."
        )

    
    # PONTOS NÃO ATENDIDOS
   

    if len(nao_coletados) > 0:

        print(
            "\n--------------------------------------"
        )

        print(
            "PONTOS NÃO INCLUÍDOS NA ROTA"
        )

        for coleta in nao_coletados:

            print(
                f"- {coleta['bairro']}"
            )

    print("\n======================================")



#  PROGRAMA PRINCIPAL


def main():

   
    print("        COLETA SELETIVA")
   

    print(
        "\nO sistema receberá os dados "
        "dos pontos de coleta."
    )

    print(
        "A rota será definida "
        "automaticamente."
    )


    # CADASTRA OS PONTOS
   

    coletas = cadastrar_coletas()


    # VERIFICA SE EXISTEM COLETAS
   

    if len(coletas) == 0:

        print(
            "\nNenhum ponto de coleta "
            "foi cadastrado."
        )

        return

   
    # MONTA A ROTA
    
    (
        rota,
        nao_coletados,
        volume_total,
        distancia_total
    ) = montar_rota(coletas)

    
    # MOSTRA RESULTADO
   

    mostrar_resultado(
        rota,
        nao_coletados,
        volume_total,
        distancia_total
    )



#  EXECUÇÃO

if __name__ == "__main__":
    main()