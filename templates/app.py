from flask import Flask, render_template, request

app = Flask(__name__)

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

        # Renderizando o template resultado.html com o valor do imposto
        return render_template('resultado.html', imposto=imposto)

    return render_template('formulario.html')

if __name__ == '__main__':
    app.run(debug=True)
