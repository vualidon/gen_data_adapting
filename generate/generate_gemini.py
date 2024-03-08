import google.generativeai as genai
import random
from time import sleep
def extract_keywords(sentence, key):
    genai.configure(api_key=key)
    model = genai.GenerativeModel('gemini-pro')
    sleep(1.5)
    try:
        prompt = f"""
###INSTRUCTIONS###
Given a sentence, complete the following procedure to produce the requested output:
- Read through the entire sentence carefully to grasp its meaning fully.
- Assign a Primary Category label consisting of one term indicating the dominant subject area (e.g., technology, science, literature, etc.).
- Identify significant words or phrases from the sentence and assign them to the Primary Category.
- Compile a list of Relevant Keywords that correspond to the assigned categories.

###OUTPUT FORMAT###
The answer is always in Vietnamese
The output have to format to below output:
Category: One word describing the overarching theme of the sentence
Keywords: Terms derived directly from the sentence, also include the main object of the sentence connected to the themes described, splited by ";"

###INPUT###
{sentence}
###OUTPUT###
        """
        response = model.generate_content(prompt)
        content = response.candidates[0].content.parts[0].text
        content = content.strip().splitlines()
        category = content[0].split(":")[1].strip()
        keywords = content[1].split(":")[1].strip().split(";")
        return {
            "category": category,
            "keywords": keywords
        }
    except Exception as e:
        print(e)
        return {
            "category": "None",
            "keywords": []
        }


def process_word_to_text(text_item, key="AIzaSyA_eXAP6VQyipGbLLGOYTQsLIhDeZfMj78"):
    # text_item, key = args
    #split by "." or "!" or "?" to get sentences
    sentences = []
    sentence = ""
    paragraph = text_item['text']
    for char in paragraph:
        if char in [".", "!", "?", "\n"]:
            sentences.append(sentence)
            sentence = ""
        else:
            sentence += char
    qas = []
    # print(sentences)
    for sentence in sentences:
        if len(sentence.split()) >= 50:
            response = extract_keywords(sentence, key)
            if response["keywords"]:
                if len(response["keywords"]) >= 3:
                    keywords = [keyword.strip() for keyword in response["keywords"]]
                    q = [f"""Hãy sinh ra một câu với chủ đề {response["category"]} từ các từ khóa sau: {", ".join(keywords)}.\nCâu hoàn chỉnh:\n""",
                    f"""Hãy sinh ra một câu mô tả dài về chủ đề {response["category"]} với các từ khóa sau: {", ".join(keywords)}.\nCâu hoàn chỉnh là:\n""",
                    f"""Hãy sinh ra một câu mô tả dài về chủ đề {response["category"]} từ các từ khóa sau: {", ".join(keywords)}.\nCâu hoàn chỉnh là:\n""",
                    f"""Từ chủ đề {response["category"]} và các từ khóa liên quan: {", ".join(keywords)}, hãy viết một câu có độ dài không dưới 50 từ.\nTrả lời:\n"""]

                    #randomly choose a question in q
                    q = random.choice(q)

                    a = sentence
                    qas.append({
                        "Q": q,
                        "A": a
                    })
    text_item['QAs'] = qas
    return text_item

# def 


# print(extract_keywords("Do đó, điều cần thiết đối với hầu hết các quản trị web là bao gồm một chiến lược tiếp thị với một trang web có thể tiếp cận nhiều người"))
# print(process_word_to_text({"text": "Băng dính : Tham khảo, Liên kết ngoài Wikipedia, bách khoa toàn thư mở » Wikipedia\nWikipedia\nBăng dính\nBăng dính hay băng keo là một loại vật liệu có tính năng kết dính, thường bao gồm keo kết hợp với một vài vật liệu dai, mềm khác như màng nhựa BOPP, PVC, vải, giấy.\nBăng dính sử dụng phần lớn trong nhu cầu đóng gói thành phẩm, bảo vệ sản phẩm. Ngoài ra Băng Dính còn có rất nhiều công dụng trong các ngành như điện tử, công nghiệp,...\nBăng dính được phân loại theo nhiều tiêu chuẩn khác nhau: theo chất keo, theo vật liệu quết keo, theo công dụng và theo kích cỡ, hình dạng. Loại Băng dính thông dụng nhất trên thị trường là băng dính OPP hay còn được gọi là băng dính đóng thùng. Ngoài ra còn có rất nhiều biến thể khác của băng dính như băng keo giấy kraft, băng keo giấy, băng keo vải, băng keo chống thấm,...\nBăng Dính thường được quy đổi theo đơn vị yard (0.91 mét/1 yard) sẽ rất thiệt hại cho khách hàng nếu không hiểu đơn vị này vì phần lớn các đơn vị thương mại thường dùng đơn vị này để gian lận số mét trên cuộn thành phẩm để hạ giá thành.\nBăng dính được phân loại theo nhiều tiêu chuẩn khác nhau: theo chất keo, theo vật liệu quết keo, theo công dụng và theo kích cỡ, hình dạng.\nBăng dính Duct-một loại băng dính dán rất chắc\nDụng cụ cắt băng dính văn phòng\nBăng dính vải\nTham khảo\nBăng keo giấy kraft\nLiên kết ngoài\nPressure Sensitive Tape Council\nThe History of Pressure Sensitive Tape\nCông ty hàng đầu về băng dính tại Việt Nam\nBăng keo Vạn Phát\nBài viết này vẫn còn sơ khai. Bạn có thể giúp Wikipedia mở rộng nội dung để bài được hoàn chỉnh hơn.\nx\nt\ns\nToC\nTham khảo\nLiên kết ngoài\nTrending\nRecent Change\nPowered by xn--videntwiki-96a.vn with NLP\n", "id": "1679296943483.86.parquet/243499"}))