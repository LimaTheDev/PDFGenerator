from fpdf import FPDF

projeto = input('Digite a descrição do projeto: ')
horas_previstas = int(input('Digite a quantidade de horas previstas: '))
valor_hora = int(input('Digite o valor da hora trabalhada: '))
prazo = input('Digite o prazo: ')

valor_orçamento = horas_previstas * valor_hora

print(valor_orçamento)

pdf = FPDF()

pdf.add_page
pdf.set_font("Arial")

pdf.text(115, 145, projeto)
pdf.text(115, 160, horas_previstas)
pdf.text(115, 175, valor_hora)
pdf.text(115, 190, prazo)
pdf.text(115, 205, str(valor_orçamento))


pdf.output("Orçamento.pdf")