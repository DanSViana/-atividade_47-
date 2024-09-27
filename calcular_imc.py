
'''
Crie um programa que calcule o IMC do usuário, em Flet. Ao terminar, envie o link do repositório.
'''

import flet as ft

def main(page: ft.Page):
    page.title = "Calculadora de IMC"
    page.scroll = "adaptive"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER

    # Campos de entrada
    altura = ft.TextField(label="Altura (m)", width=200)
    peso = ft.TextField(label="Peso (kg)", width=200)
    resultado_text = ft.Text()

    def calcular_imc(e):
        
            altura = float(altura.value.replace(',','.'))
            peso = float(peso.value.replace(',','.'))
            imc = peso / (altura ** 2)
            resultado_text.value = f"Seu IMC é: {imc:.2f}"
        
            resultado_text.value = "Por favor, insira valores válidos."

            resultado_text.update()

    calcular_button = ft.ElevatedButton("Calcular IMC", on_click=calcular_imc)

    # Adiciona os componentes à página
    page.add(
        ft.Row(
            [ft.Text("IMC", size=40, weight="bold")],
            alignment=ft.MainAxisAlignment.CENTER
        ),
        ft.Row(
            [altura],
            alignment=ft.MainAxisAlignment.CENTER
        ),
        ft.Row(
            [peso],
            alignment=ft.MainAxisAlignment.CENTER
        ),
        ft.Row(
            [ft.ElevatedButton("Calcular IMC", on_click=calcular_imc)],
            alignment=ft.MainAxisAlignment.CENTER
        ),
        ft.Row(
            [resultado_text],
            alignment=ft.MainAxisAlignment.CENTER
        ))
    

# Executa o aplicativo
ft.app(main)
