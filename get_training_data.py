import re
import sys
sys.stdout.reconfigure(encoding='utf-8')



def extract_conversations(file_path, your_name = "Parth"):
    """Method to extract the question answer pairs from the chats.txt file. 
    It also preserves the multiple responses by seperate messages """
    with open (file_path, "r", encoding="utf-8") as file:
        lines = file.readlines()
    
    conversations = []
    prev_mssg = None
    prev_sender = None
    response_buffer = []  # To store the multiple responses before adding it as the question answer pair

    # pattern for regex matching 
    pattern = r"\[\d{2}/\d{2}/\d{2}, \d{1,2}:\d{2}:\d{2}\s?[APM]*\] (.*?): (.*)"

    for line in lines:
        match = re.match(pattern, line)
        if match:
            sender, mssg = match.groups()
            mssg = clean_text(mssg)

            if sender == your_name and prev_sender == your_name:
                response_buffer.append(mssg)
            elif sender == your_name:
                response_buffer = [mssg]
            else:
                if prev_sender == your_name and response_buffer:
                    conversations.append((prev_mssg, response_buffer.copy()))

                    prev_mssg = mssg
                    response_buffer =[]
                
            prev_sender = sender


    return conversations

def clean_text(text):
    "Cleans the text by removing the unrequired spaces and also the links"
    text = text.strip()
    return text

if __name__ == "__main__":
    chat_file = "_chat.txt"
    qa_pairs = extract_conversations(chat_file, your_name="Parth")


    print(f"Total Q&A pairs: {len(qa_pairs)}")
    print("Sample Pairs:", qa_pairs[:5])  # Print first 5 Q&A pairs