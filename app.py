# Importando as bibliotecas necessárias
from flask import Flask, render_template, request
from reportlab.pdfgen import canvas

app = Flask(__name__)

# Rota para a página inicial
@app.route('/', methods=['GET', 'POST'])
def calcular_irpf():
    if request.method == 'POST':
        # Recebendo os dados do formulário
        ganho_liquido = float(request.form['ganho_liquido'])
        custos_operacionais = float(request.form['custos_operacionais'])

        # Calculando a base de cálculo do IRPF
        base_calculo = ganho_liquido - custos_operacionais

        # Determinando a alíquota do IRPF
        if base_calculo <= 35000:
            aliquota = 0.15
        else:
            aliquota = 0.20

        # Calculando o valor do imposto
        imposto = base_calculo * aliquota

        # Gerando o DARF (PDF)
        pdf_filename = 'darf.pdf'
        gerar_darf(pdf_filename, imposto)

        # Renderizando o template resultado.html com o valor do imposto e link para download do DARF
        return render_template('resultado.html', imposto=imposto, pdf_filename=pdf_filename)

    return render_template('formulario.html')

def gerar_darf(filename, imposto):
    # Criação do PDF do DARF
    c = canvas.Canvas(filename)
    c.drawString(100, 700, 'DARF - Imposto de Renda')
    c.drawString(100, 680, f'Valor do imposto: R$ {imposto:.2f}')
    # Adicione mais informações relevantes ao DARF, como data de vencimento, código de receita, etc.
    c.save()

if __name__ == '__main__':
    app.run(debug=True)
