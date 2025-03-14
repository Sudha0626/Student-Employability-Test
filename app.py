import gradio as gr

# Function to check employability
def check_employability(name, communication, leadership, time_management, presentation, teamwork):
    score = (communication + leadership + time_management + presentation + teamwork) / 5

    if score >= 7:
        message = f"🚀 {name}, you are highly employable! Keep it up! 🚀"
    elif score >= 5:
        message = f"✨ {name}, you have potential! Keep improving! ✨"
    else:
        message = f"😟 {name}, work on your skills! Keep learning! 📚"

    return message

# Gradio UI - Minimal Layout
with gr.Blocks(theme=gr.themes.Soft()) as app:
    gr.Markdown("<h4 style='text-align: center; color: #4CAF50;'>🌟 Employability Check 🌟</h4>")
    
    with gr.Column():  # Column layout for a compact UI
        name = gr.Textbox(label="Your Name", placeholder="Enter your name", interactive=True)
        
        gr.Markdown("#### 🎯 Rate Your Skills (1-10)")
        
        communication = gr.Slider(1, 10, label="🗣 Communication", value=5, interactive=True)
        leadership = gr.Slider(1, 10, label="🔄 Leadership", value=5, interactive=True)
        time_management = gr.Slider(1, 10, label="⏳ Time Management", value=5, interactive=True)
        presentation = gr.Slider(1, 10, label="🎤 Presentation", value=5, interactive=True)
        teamwork = gr.Slider(1, 10, label="🤝 Teamwork", value=5, interactive=True)
        
        button = gr.Button("🚀 Check Employability 🚀", size="sm")  # Smaller button
        result = gr.Textbox(label="Employability Status", interactive=False)
        
        button.click(check_employability, inputs=[name, communication, leadership, time_management, presentation, teamwork], outputs=result)

# Start the app
if __name__ == "__main__":
    app.launch()
