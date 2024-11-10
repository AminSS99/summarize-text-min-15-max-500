from transformers import pipeline

# Initialize the summarization pipeline
summarizer = pipeline("summarization")

def summarize_text(text):
    # Summarize the text
    summary = summarizer(text , max_length=500 ,min_length=15, do_sample=False)
    return summary[0]['summary_text']

#example usage
if __name__== "__main__":
    text = """
    write your text here , which is need to be summarized
    """
    summary = summarize_text(text)
    print("Original Text:\n", text)
    print("\nSummary:\n", summary)