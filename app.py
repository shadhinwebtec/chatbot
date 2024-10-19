from g4f.client import Client
import gradio as gr 


client = Client()

def chatbot_response(user_input):
    
    response = client.chat.completions.create(
      model="gpt-3.5-turbo",
      messages=[{"role": "user", "content": user_input}]
    
    # Add any other necessary parameters
    )
    return (response.choices[0].message.content)

#Gradio interface
interface=gr.Interface(fn=chatbot_response,
                       inputs=gr.Textbox(lines=2,placeholder="Write your question here..."),
                       outputs="text",
                       title="AI assistant chatbot",
                       description=" Ask any question and AI assistant will response")

#launch the interface
if __name__=="__main__":
    interface.launch(share=True)
    
    



