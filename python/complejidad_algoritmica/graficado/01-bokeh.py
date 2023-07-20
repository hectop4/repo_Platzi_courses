#Bokeh permite construir graficos interactivos de forma simple
#Se puede exportar a html
#Se puede exportar a json
#Se puede exportar a png
#Se puede exportar a svg
#Se puede usar en el servidor de bokeh, flask, django

from bokeh.plotting import figure, output_file, show

if __name__=='__main__':
    output_file('graficado_simple.html')
    fig=figure()
    total_vals=int(input('Cuantos valores quieres graficar?'))
    x_vals=list(range(-total_vals,total_vals+1))
    y_vals=[]
    for x in range(-total_vals,total_vals+1):
        val=int(x**2)
        y_vals.append(val)
    fig.line(x_vals,y_vals,line_width=2)
    show(fig)
    

