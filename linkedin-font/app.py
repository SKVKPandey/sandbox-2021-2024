from flask import Flask, render_template, request, jsonify
from bs4 import BeautifulSoup
import google.generativeai as genai
import PIL.Image
from docx import Document
import pandas as pd

app = Flask(__name__)
genai.configure(api_key="REDACTED")

ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}

def convert_to_bold_unicode(text):
    result = ""
    for char in text:
        if char.isupper():
            result += chr(ord('𝗔') + (ord(char) - ord('A')))
        elif char.islower():
            result += chr(ord('𝗮') + (ord(char) - ord('a')))
        elif char.isdigit():
            result += chr(ord('𝟬') + (ord(char) - ord('0')))
        else:
            result += char
    return result

def convert_to_italic_unicode(text):
    result = ""
    for char in text:
        if char.isupper():
            result += chr(ord('𝐴') + (ord(char) - ord('A')))  # Use 𝐴 for italic uppercase
        elif char.islower():
            result += chr(ord('𝑎') + (ord(char) - ord('a')))  # Use 𝑎 for italic lowercase
        elif char.isdigit():
            result += chr(ord('𝟬') + (ord(char) - ord('0')))  # Use 𝟬 for italic digits
        else:
            result += char
    return result

def convert_to_bold_italic_unicode(text):
    result = ""
    for char in text:
        if char.isupper():
            result += chr(ord('𝗔') + (ord(char) - ord('A')))  # Bold uppercase
        elif char.islower():
            result += chr(ord('𝗮') + (ord(char) - ord('a')))  # Bold lowercase
        elif char.isdigit():
            result += chr(ord('𝟬') + (ord(char) - ord('0')))  # Bold digits
        else:
            result += char
    return result

def convert_to_invert_unicode(text):
    result = ""
    for char in text:
        if char.isupper():
            result += chr(ord('Ⓐ') + (ord(char) - ord('A')))  # Bold uppercase
        elif char.islower():
            result += chr(ord('ⓐ') + (ord(char) - ord('a')))  # Bold lowercase
        elif char.isdigit():
            result += chr(ord('⓪') + (ord(char) - ord('0')))  # Bold digits
        else:
            result += char
    return result

def convert_to_heading_unicode(text, use_styled_heading):
    result = ""
    for char in text:
        if char.isupper():
            result += chr(ord('𝕬') + (ord(char) - ord('A'))) if use_styled_heading else chr(ord('𝗔') + (ord(char) - ord('A')))
        elif char.islower():
            result += chr(ord('𝖆') + (ord(char) - ord('a'))) if use_styled_heading else chr(ord('𝗮') + (ord(char) - ord('a')))
        elif char.isdigit():
            result += chr(ord('0') + (ord(char) - ord('0'))) if use_styled_heading else chr(ord('𝟬') + (ord(char) - ord('0')))
        else:
            result += char
    return result

def convert_to_format_unicode(text):
    result = ""
    for char in text:
        if char.isupper():
            result += chr(ord('𝓐') + (ord(char) - ord('A')))  # Bold uppercase
        elif char.islower():
            result += chr(ord('𝓪') + (ord(char) - ord('a')))  # Bold lowercase
        elif char.isdigit():
            result += chr(ord('0') + (ord(char) - ord('0')))  # Bold digits
        else:
            result += char
    return result

def read_docx(file):
    doc = Document(file)
    text = ''
    for para in doc.paragraphs:
        text += para.text + '\n'
    return text

def read_csv(file):
    df = pd.read_csv(file)
    return df.to_csv(index=False)

def read_xlsx(file):
    df = pd.read_excel(file)
    return df.to_csv(index=False)

@app.route('/fileHandle', methods=['POST'])
def file_handle():
    try:
        uploaded_file = request.files['docfile']
        file_extension = uploaded_file.filename.split('.')[-1].lower()

        if file_extension == 'docx':
            data = read_docx(uploaded_file)
        elif file_extension == 'csv':
            data = read_csv(uploaded_file)
        elif file_extension == 'xlsx':
            data = read_xlsx(uploaded_file)
        else:
            return jsonify({'error': 'Unsupported file type'}), 400

        return jsonify({'data': data}), 200

    except Exception as e:
        return jsonify({'error': str(e)}), 500

def convert_source_code(text, use_styled_heading):
    soup = BeautifulSoup(text, 'html.parser')
    tag_list = soup.find_all(['strong', 'em', 's', 'h1', 'h2', 'h3', 'pre'])

    for tag in tag_list:
        if 'strong' in tag.name and ('em', 's', 'h1', 'h2', 'h3', 'pre') not in tag_list:
            content = convert_to_bold_unicode(tag.get_text())
            tag.string.replace_with(content)
        elif 'em' in tag.name and ('strong', 's', 'h1', 'h2', 'h3', 'pre') not in tag_list:
            content = convert_to_italic_unicode(tag.get_text())
            tag.string.replace_with(content)
        elif 'h1' in tag.name and ('strong', 's', 'em', 'h2', 'h3', 'pre') not in tag_list:
            content = convert_to_heading_unicode(tag.get_text(), use_styled_heading)
            tag.string.replace_with(content)
        elif 'h2' in tag.name and ('strong', 's', 'h1', 'em', 'h3', 'pre') not in tag_list:
            content = convert_to_heading_unicode(tag.get_text(), use_styled_heading)
            tag.string.replace_with(content)
        elif 'h3' in tag.name and ('strong', 's', 'h1', 'h2', 'em', 'pre') not in tag_list:
            content = convert_to_bold_unicode(tag.get_text())
            tag.string.replace_with(content)
        elif 's' in tag.name and ('strong', 'em', 'h1', 'h2', 'h3', 'pre') not in tag_list:
            content = convert_to_invert_unicode(tag.get_text())
            tag.string.replace_with(content)
        elif 'pre' in tag.name and ('strong', 'em', 'h1', 'h2', 'h3', 's') not in tag_list:
            content = convert_to_format_unicode(tag.get_text())
            tag.string.replace_with(content)
        elif 'em' in tag.name and 'strong' in tag.name and ('s', 'h1', 'h2', 'h3', 'pre') not in tag_list:
            content = convert_to_bold_italic_unicode(tag.get_text())
            tag.string.replace_with(content)

    return str(soup)

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS



@app.route('/search', methods=['POST'])
def search():
    search_content = request.form.get('search_content')
    socialMediaSelect = request.form.get('socialMediaSelect', 'LinkedIn')
    contentTypeSelect = request.form.get('contentTypeSelect', 'Post')
    otherSocialMedia = request.form.get('otherSocialMedia')
    otherContentType = request.form.get('otherContentType')
    heading = str()
    keywords = str()
    num_emojis = int(request.form.get('numEmojis', 0))  # Default to 0 if missing
    formality_percent = int(request.form.get('formalityPercent', 0))
    selected_Language = request.form.get('selectedLanguage', 'English')

    if len(request.form.get('heading')) > 0:
        heading = f" The heading should be like {request.form.get('heading')}."
    if len(request.form.get('keywords')) > 0:
        keywords = f" The keywords to be included in the body content are {request.form.get('keywords')}."

    if len(otherSocialMedia) > 0:
        socialMediaSelect = otherSocialMedia;
    if len(otherContentType) > 0:
        contentTypeSelect = otherContentType;

    # Prompt for generating a promotional text
    prompt = f"Compose a well-crafted {socialMediaSelect} {contentTypeSelect} based on the given image in HTML Format for the given prompt: '{search_content}'. Ensure proper structuring and spacing within the content. Number of emojis that should be used should be {num_emojis}. The content should be {formality_percent}% formal.{heading}{keywords} Use appropriate and heigh reach hastags in the end. Generate the content in {selected_Language} Language."

    file = request.files.get('file')

    if file:

        if file and allowed_file(file.filename):

            img = PIL.Image.open(file)

        model = genai.GenerativeModel(model_name="gemini-pro-vision")
        prompt = f"{prompt}. Use image for the mentioned stuff."
        link_content = model.generate_content([f"{prompt}", img])
        # link_content = link_content.text.replace("```html", "")
        # link_content = link_content.replace("```", "")

        # Process the search_content and generate the result as HTML content
        result_html = f'{link_content.strip()}'

        return jsonify({
            'search_result_html': result_html
        })

    
    else:
        prompt = f"Compose a well-crafted {socialMediaSelect} {contentTypeSelect} in HTML Format for the given prompt: '{search_content}'. Ensure proper structuring and spacing within the content. Number of emojis that should be used should be {num_emojis}. The content should be {formality_percent}% formal.{heading}{keywords} Use appropriate and heigh reach hastags in the end. Generate the content in {selected_Language} Language."

        # Generate text response using Gemini Pro
        model = genai.GenerativeModel('gemini-pro')
        link_content = model.generate_content(prompt)
        link_content = link_content.text.replace("```html","")
        link_content = link_content.replace("```", "")
        
        # Process the search_content and generate the result as HTML content
        result_html = f'{link_content.strip()}'

        return jsonify({
            'search_result_html': result_html
        })

@app.route('/research', methods=['POST'])
def research():
    search_content = request.form.get('search_content')
    socialMediaSelect = request.form.get('socialMediaSelect', 'LinkedIn')
    contentTypeSelect = request.form.get('contentTypeSelect', 'Post')
    otherSocialMedia = request.form.get('otherSocialMedia')
    otherContentType = request.form.get('otherContentType')
    heading = str()
    keywords = str()
    num_emojis = int(request.form.get('numEmojis', 0))  # Default to 0 if missing
    formality_percent = int(request.form.get('formalityPercent', 0))
    selected_Language = request.form.get('selectedLanguage', 'English')
    editorData = request.form.get('editorData')

    if len(request.form.get('heading')) > 0:
        heading = f" The heading should be like {request.form.get('heading')}."
    if len(request.form.get('keywords')) > 0:
        keywords = f" The keywords to be included in the body content are {request.form.get('keywords')}."

    if len(otherSocialMedia) > 0:
        socialMediaSelect = otherSocialMedia;
    if len(otherContentType) > 0:
        contentTypeSelect = otherContentType;

    # Prompt for generating a promotional text
    prompt = f"Rephrase and make changes in the content '{editorData}' considering the prompt: '{search_content}'. The output should be a {socialMediaSelect} {contentTypeSelect} based on the given image in HTML Format. Ensure proper structuring and spacing within the content. Number of emojis that should be used is {num_emojis}. The content should be {formality_percent}% formal.{heading}{keywords} Use appropriate and heigh reach hastags in the end. Generate the content in {selected_Language} Language."

    file = request.files.get('file')
    print(file)
    if file:

        if file and allowed_file(file.filename):

            img = PIL.Image.open(file)

        model = genai.GenerativeModel(model_name="gemini-pro-vision")
        prompt = f"{prompt}. Use image for the mentioned stuff."
        link_content = model.generate_content([f"{prompt}", img])
        # link_content = link_content.text.replace("```html", "")
        # link_content = link_content.replace("```", "")

        # Process the search_content and generate the result as HTML content
        result_html = f'{link_content.parts}'

        return jsonify({
            'research_result_html': result_html
        })

    
    else:
        prompt = f"Rephrase and make changes in the content '{editorData}' considering the prompt: '{search_content}'. The output should be a {socialMediaSelect} {contentTypeSelect} in HTML Format. Ensure proper structuring and spacing within the content. Number of emojis that should be used is {num_emojis}. The content should be {formality_percent}% formal.{heading}{keywords} Use appropriate and heigh reach hastags in the end. Generate the content in {selected_Language} Language."

        # Generate text response using Gemini Pro
        model = genai.GenerativeModel('gemini-pro')
        link_content = model.generate_content(prompt)
        # link_content = link_content.text.replace("```html", "")
        # link_content = link_content.replace("```", "")

        # Process the search_content and generate the result as HTML content
        result_html = f'{link_content.parts}'

        return jsonify({
            'research_result_html': result_html
        })

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/convert', methods=['POST'])
def convert():
    input_html = request.form['editor_content']
    use_styled_heading = request.form.get('styledHeading') == 'true'  # Check if the checkbox is checked
    output_html = convert_source_code(input_html, use_styled_heading)
    return {'input_html': input_html, 'output_html': output_html}

if __name__ == '__main__':
    app.run(debug=True)
