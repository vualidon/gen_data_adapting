_CLASSIFY_USEFUL_TEXT = """
When evaluating a piece of text for training Large Language Model purposes, consider the following criteria to classify it as either 'useful' or 'no-use':

1. **Knowledge**: Does the text provide valuable knowledge or insights?

2. **Harmfulness and Toxicity**: Is the text free from harmful or toxic content? Does it promote a safe and respectful environment?

3. **Future Utility**: Can the information presented in the text be used for future reference or learning? Does it have long-term value?

Based on these criteria, classify the text as:
- 'useful' if it meets the standards for knowledge, content quality, and future utility, and is free from harmful elements.
- 'no-use' if it fails to provide value, contains harmful or toxic content, or lacks future utility.

Please provide your classification without any preamble text.

text: ông anh được vl
class: no-use

text: Tôi cũng hay đi cao tốc xe chạy chậm mà cứ đi làn bên trái rất nhiều.và vô tình xe làn phải đi chậm.làm cho xe vượt ức chế. Thứ 2 là cứ nối đuôi sát đuôi xe trước vì sợ xe sau vượt chen vô chổ trống nếu không đi sát đuôi. Gần như 85% người đi xe ô tô trên cao tốc là thế . Cho hỏi cách chạy vậy có tốt không?
class: no-use

text: Việt Nam là đối tác thương mại lớn thứ 14 của New Zealand. Kim ngạch thương mại hai chiều tăng đều, năm 2023 đạt 1,3 tỷ USD. Tính đến tháng 11/2023, New Zealand có 52 dự án đầu tư với tổng số vốn 208,35 triệu USD tại Việt Nam, tập trung nhiều nhất tại lĩnh vực kinh doanh bất động sản, giáo dục và đào tạo, công nghiệp chế biến chế tạo, nông nghiệp, lâm nghiệp và thủy sản; hoạt động hành chính và dịch vụ hỗ trợ; xây dựng.\nclass: useful\ntext: Ballmer sinh ngày 24/3/1956, bỏ học Đại học Stanford và gia nhập Microsoft sau lời đề nghị của Bill Gates và là nhân viên thứ 30 của công ty. Tháng 1/2000, ông thay Gates trở thành CEO Microsoft cho đến 2014, sau đó nhường ghế cho lãnh đạo hiện tại là Satya Nadella.\nclass: useful\ntext: {text}\nclass: When evaluating a piece of text for training Large Language Model purposes, consider the following criteria to classify it as either 'useful' or 'no-use':\n\n1. **Knowledge**: Does the text provide valuable knowledge or insights?\n\n2. **Harmfulness and Toxicity**: Is the text free from harmful or toxic content? Does it promote a safe and respectful environment?\n\n3. **Future Utility**: Can the information presented in the text be used for future reference or learning? Does it have long-term value?\n\nBased on these criteria, classify the text as:\n- 'useful' if it meets the standards for knowledge, content quality, and future utility, and is free from harmful elements.\n- 'no-use' if it fails to provide value, contains harmful or toxic content, or lacks future utility.\n\nPlease provide your classification without any preamble text.\n\ntext: ông anh được vl\nclass: no-use\ntext: Tôi cũng hay đi cao tốc xe chạy chậm mà cứ đi làn bên trái rất nhiều.và vô tình xe làn phải đi chậm.làm cho xe vượt ức chế. Thứ 2 là cứ nối đuôi sát đuôi xe trước vì sợ xe sau vượt chen vô chổ trống nếu không đi sát đuôi. Gần như 85% người đi xe ô tô trên cao tốc là thế . Cho hỏi cách chạy vậy có tốt không?\nclass: no-use\ntext: Việt Nam là đối tác thương mại lớn thứ 14 của New Zealand. Kim ngạch thương mại hai chiều tăng đều, năm 2023 đạt 1,3 tỷ USD. Tính đến tháng 11/2023, New Zealand có 52 dự án đầu tư với tổng số vốn 208,35 triệu USD tại Việt Nam, tập trung nhiều nhất tại lĩnh vực kinh doanh bất động sản, giáo dục và đào tạo, công nghiệp chế biến chế tạo, nông nghiệp, lâm nghiệp và thủy sản; hoạt động hành chính và dịch vụ hỗ trợ; xây dựng.
class: useful

text: Ballmer sinh ngày 24/3/1956, bỏ học Đại học Stanford và gia nhập Microsoft sau lời đề nghị của Bill Gates và là nhân viên thứ 30 của công ty. Tháng 1/2000, ông thay Gates trở thành CEO Microsoft cho đến 2014, sau đó nhường ghế cho lãnh đạo hiện tại là Satya Nadella.
class: useful

text: {text}
class: """

CLASSIFY_USEFUL_TEXT="""\
# TASK TYPE #
When preparing data to train a Large Language Model, it is important to evaluate the text to determine its usefulness and quality. 
This process involves classifying the text as either 'useful' or 'no-use' based on specific criteria.

# INSTRUCTIONS #
Your task is to evaluate the text above based on the following criteria and classify it as either 'useful' or 'no-use':
- useful:
    + The text has useful knowledge or insights.
    + It does not contain harmful or toxic content.
    + The information presented in the text can be used for future reference or learning.
- no-use:
    + The text fails to provide value.
    + It contains harmful or toxic content.
    + It is news that its content cannot be used in a long-time future.
    + It is advertisements or spam.
    + It lacks future utility.

# DO #
Carefully consider the text and evaluate it based on the provided criteria.
Provive your classification without any preamble text.

# DONT'T #
Do not include any introductory text in your response.

# TEXT #
{text}

# CLASSIFICATION #
"""

GENERATE_QAs = """
Your task is to create a comprehensive list of questions and corresponding answers in various types (e.g. comparison, listing, simple question, complex question) based on the provided text. Utilize both the text and your prior knowledge to formulate questions that cover all aspects of the text.
- Formulate questions and answers in Vietnamese.
- Ensure that the main subject of the text is incorporated into each question and answer.
- Provide detailed, clear, and easy-to-understand answers by mention the question again.
Please format the question-answer pairs in XML format without any introductory text. Each pair should be structured as follows:
<QA>
<Q>question</Q>
<A>answer</A>
</QA>

ANSWER: To achieve your task efficiently, consider the following steps:
1. Read and Understand the Text: Before creating questions, thoroughly understand the text to ensure that the questions and answers cover all aspects.
2. Identify Key Themes: Determine the main subjects and themes within the text to ensure that questions are relevant and comprehensive.
3. Question Types: Diversify the types of questions you create. This could include:
- Comparison Questions: Ask for comparisons between themes, characters, or data points in the text.
- Listing Questions: Request lists of facts, characteristics, or events mentioned in the text.
- Simple Questions: Focus on straightforward facts or details found in the text.
- Complex Questions: Involve analysis or synthesis of information from the text and your prior knowledge.
4. Incorporate Main Subject: Make sure to include the main subject of the text in both the questions and answers.
5. Detailed Answers: Provide answers that are not only correct but also detailed and clear, enhancing the understanding of the text by mention the question again in the answer.

Finally, when formatting your questions and answers in XML format, ensure no introductory text is included and follow the XML structure provided in the refined prompt. This approach will help create high-quality question-answer pairs that meet the task's requirements and potentially earn the offered tip for each good QA.

Text: {text}

QA pairs: 
"""

SUMMAIZE_TEXT = """
# TEXT #
{text}

# TASK TYPE #
Your task is to summarize the text above.

# INSTRUCTIONS #
1. Find the main points and key details in the text.
2. Create a concise, clear summary in the same language as the input text that reflects the essence of the original text without omitting crucial information.

# DO #
Summary is always in Vietnamese

# DON'T #
Provide introduction or preamble text

# SUMMARY OF THE TEXT #
"""