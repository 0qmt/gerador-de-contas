#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Gerador de Contas PSN - VERSÃO CORRIGIDA
Autor: Assistente AI  
Data: 15/10/2025
"""

import os
from datetime import datetime

def gerar_contas_psn():
    """Função principal para gerar contas PSN formatadas"""
    print("=" * 60)
    print("           🎮 GERADOR DE CONTAS PSN 🎮")
    print("=" * 60)
    print()

    try:
        # Obter dados do usuário
        dia = input("📅 Digite o dia (ex: 14): ").strip()
        mes = input("📅 Digite o mês (ex: 10): ").strip()
        numero_inicial = int(input("🔢 Digite o número inicial da conta: "))
        numero_final = int(input("🔢 Digite o número final da conta: "))

        # Validações básicas
        dia_int = int(dia)
        mes_int = int(mes)

        if dia_int < 1 or dia_int > 31 or mes_int < 1 or mes_int > 12:
            print("❌ Erro: Data inválida!")
            return
        if numero_inicial > numero_final:
            print("❌ Erro: Número inicial maior que o final!")
            return

        # Formatar data
        data_formatada = f"{dia.zfill(2)}{mes.zfill(2)}"

        print(f"\n📊 Gerando contas de {numero_inicial} a {numero_final}")
        print("=" * 60)

        # Gerar contas
        contas_geradas = []

        for numero in range(numero_inicial, numero_final + 1):
            conta = f""":PlaystationWhite: Ativação Psn Deluxe

:envelope: E-mail da conta: zyxemstore77+{data_formatada}{numero:02d}@gmail.com
:lock: Senha da conta: Lostggmax2026
:calendar_spiral: Nascimento da conta: 12/03/2000"""

            contas_geradas.append(conta)

        print(f"🎉 {len(contas_geradas)} contas geradas com sucesso!")

        # Salvar arquivo - VERSÃO CORRIGIDA
        salvar = input("\n💾 Salvar em arquivo? (s/n): ").lower().strip()

        if salvar in ['s', 'sim']:
            nome_arquivo = f"contas_psn_{data_formatada}_{numero_inicial}_{numero_final}.txt"

            try:
                with open(nome_arquivo, 'w', encoding='utf-8') as arquivo:
                    arquivo.write("CONTAS PSN GERADAS\n")
                    arquivo.write("=" * 50 + "\n")
                    arquivo.write(f"Data: {dia}/{mes}\n")
                    arquivo.write(f"Range: {numero_inicial} a {numero_final}\n")
                    arquivo.write(f"Total: {len(contas_geradas)} contas\n")
                    arquivo.write("=" * 50 + "\n\n")

                    for i, conta in enumerate(contas_geradas):
                        arquivo.write(f"CONTA #{numero_inicial + i}:\n")
                        arquivo.write(conta)
                        arquivo.write("\n\n" + "-" * 40 + "\n\n")

                print(f"\n✅ Arquivo salvo: {nome_arquivo}")
                print(f"📍 Local: {os.path.abspath(nome_arquivo)}")

            except Exception as e:
                print(f"❌ Erro ao salvar: {e}")

        # Mostrar algumas contas como exemplo
        print("\n📋 EXEMPLOS GERADOS:")
        for i, conta in enumerate(contas_geradas[:2]):
            print(conta)
            print("-" * 40)

    except Exception as e:
        print(f"❌ Erro: {e}")

if __name__ == "__main__":
    gerar_contas_psn()
