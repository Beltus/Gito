import gradio as gr

def greet(name):

    if isinstance(name, str):

        return "Hello " + name + "!"
    
    else:
        return "String is expected. Try again"


def isEven(n1, n2):

    s = n1 + n2

    if s%2==0:
        results = 'Sum is Even'

    else:
        results = 'Sum is Odd'

    return results

demo = gr.Interface(fn=isEven, inputs=["number" , "number"], outputs="text")
    
demo.launch()   