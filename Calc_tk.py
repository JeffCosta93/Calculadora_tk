import tkinter as tk

class Calculadora(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Calculadora")
        self.geometry("300x400")

        self.resultado_var = tk.StringVar()
        self.resultado_var.set("")


        self.entrada = tk.Entry(self, textvariable=self.resultado_var, font=("Arial", 18), bd=10, insertwidth=4, width=14,
                                justify='right')
        self.entrada.grid(row=0, column=0, columnspan=4)

        # Botões
        botoes = [
            '7', '8', '9', '/',
            '4', '5', '6', '*',
            '1', '2', '3', '-',
            '0', 'C', '=', '+',
        ]

        row_val = 1
        col_val = 0

        for botao in botoes:

            tk.Button(self, text=botao, padx=20, pady=20, font=("Arial", 14), command=lambda b=botao: self.clique_botao(b)).grid(
                row=row_val, column=col_val)
            col_val += 1
            if col_val > 3:
                col_val = 0
                row_val += 1

    def clique_botao(self, valor):
        if valor == '=':
            try:
                resultado = eval(self.entrada.get())
                self.resultado_var.set(resultado)
            except:
                self.resultado_var.set("Erro")
        elif valor == 'C':

            entrada_atual = self.entrada.get()[:-1]
            self.resultado_var.set(entrada_atual)
        else:
            entrada_atual = self.entrada.get()
            entrada_atual += valor
            self.resultado_var.set(entrada_atual)

if __name__ == "__main__":
    app = Calculadora()
    app.mainloop()
