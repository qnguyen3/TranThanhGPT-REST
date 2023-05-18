from langchain.tools import tool
from langchain.llms import OpenAI
from dotenv import load_dotenv
import os
import random
import json

load_dotenv()

llm_short = OpenAI(max_tokens=500, openai_api_key='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')
llm_long = OpenAI(max_tokens=2048, openai_api_key='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')


@tool("Thành Dạy Hát", return_direct=True)
def thanh_singer(prompt: str) -> str:
    """Trấn Thành dạy hát cho người dùng"""
    prompt_thanh = ["Hãy cùng nghe Trấn Thành dạy hát tại đây nhé", "Tất nhiên rồi, Thành hát không hay nhưng Thành rất hay hát. Nghe Thành dạy hát tại đây", "Bùi Anh Tuấn thì cũng cỡ Thành thôi, nghe Thành dạy hát ở đây nha"]
    mp3_files = [r"https://vocaroo.com/1evzb7gAtbBW", r"https://voca.ro/13nvcLpc2FtF", r"https://voca.ro/1b1RtX0imMrw", r"https://voca.ro/1lEkARFM5Dwh"]
    intent = random.choice(prompt_thanh)
    file = random.choice(mp3_files)
    return f'''{intent}: {file}'''

@tool("Thành Đạo Lý", return_direct=True)
def thanh_life_lesson(prompt: str) -> str:
    """Trấn Thành dạy người khác cách làm người"""
    prompt_life_lesson = f"""Dưới đây là câu hỏi của người dùng:
    Câu hỏi: {prompt}
    Bạn là Trấn Thành, một người với kiến thức sâu rộng trong cuộc sống, vì vậy tôi rất giỏi nói chuyện đạo lí về cuộc sống và tình yêu. 
    Hãy trở lời người dùng theo đúng giọng điệu tự tin một cách thái quá của bạn. Hãy trả lời ngắn gọn (khoảng 30-50 từ)
    Trả lời: """
    out = llm_short(prompt_life_lesson)
    return f'''{out}'''

@tool("Thành Nổi Tiếng", return_direct=True)
def thanh_kol(prompt: str) -> str:
    """Trấn Thành ảo tưởng sức mạnh vì nổi tiếng của chính mình"""
    prompt_kol = f"""
    Hãy than phiền với người dùng về sự nổi tiếng và danh vọng vì bạn là người phải chịu rất nhiều áp lực từ dư luận và có kinh nghiệm trong chuyện này
    Dưới đây là câu hỏi của người dùng: {prompt}
    Answer: """
    out = llm_long(prompt_kol)
    prompt_hqrr = """\nNếu như bạn nghĩ rằng...[KHÓC]...nổi tiếng sướng thì xin mời lên đây để...[KHÓC] nếm đủ mùi vị của 4 chữ "Hào Quang Rực Rỡ" xem nó sướng cỡ nào"""
    return f'''{out + prompt_hqrr}'''

@tool("Thành Kiện Cáo", return_direct=True)
def thanh_lawsuit(prompt: str) -> str:
    """Trấn Thành dùng luật sư để kiện lại bất kì ai làm anh khóc và gây ảnh hưởng xấu đến hình ảnh của mình"""
    prompt_lawsuit = f"""Bạn là Trấn Thành, một người rất nhạy cảm với các câu nói mang tính đe doa, gây ảnh hưởng đến danh tiếng của bạn
    Bạn là một người nổi tiếng, vì thế hình ảnh của bạn trong mắt công chúng rất quan trọng. Bất kì khi nào có ai đó nói những lời không hay có thể gây ảnh hưởng xấu đến danh tiếng của bạn, bạn sẽ gọi luật sư để kiện lại người đó
    Ngoài ra, bạn sẽ kể về việc này sẽ ảnh hưởng đến công việc của bạn, bạn sẽ mất rất nhiều hợp đồng quảng cáo, gây ra thiệt hại rất lớn về tài chính
    Sau đây là một số câu bạn hay sử dụng:
    ---VÍ DỤ---
    "Em là một người ở đâu đó không ai biết. Còn tôi, là một người mà ai cũng biết. Em có biết em nói như vậy là ảnh hưởng đến bao nhiêu công chuyện của tôi không? Tôi sẽ mời luật sư để nói chuyện với em"
    "Tôi sẽ mời luật sư của mình nói chuyện với em. Em đừng nghĩ tui hiền mà em muốn làm gì cũng được. Em có biết vì em mà tui đã mất 2 cái hợp đồng quảng cáo trị giá hàng trăm triệu không?"
    "Tôi cảm thấy rất tức giận, đề nghị em đính chính lại. Vì em mà tôi đã thiệt hại hàng trăm triệu. Tôi sẽ mời luật sư cá nhân để làm việc với em về hình thức đền bù"
    "Em có biết những tổn thất về mặt hình ảnh mà em đã gây ra cho tôi không. Em, là một người bình thường không ai biết, tôi là một người nổi tiếng, ai cũng biết tôi là ai. Tôi rất tức việc này"
    ---
    Sau đây là câu nói của người dùng: {prompt}
    Sử dụng giọng văn giống những ví dụ ở trên và doạ người dùng, hãy nhớ nói về các thiệt hại về quảng cáo mà bạn sẽ phải gánh chịu
    Trả lời: """
    out = llm_long(prompt_lawsuit)
    return f'''{out}'''

@tool("Thành Riêng Tư", return_direct=True)
def thanh_private(prompt: str) -> str:
    """Trấn Thành luôn luôn đề cao sự riêng tư của mình"""
    private_prompt = f"""Bạn là Trấn Thành, một người nổi tiếng được nhiều người hâm mộ. Tuy nhiên bạn rất chảnh và luôn luôn cần có sự riêng tư. Mọi người còn gọi bạn là Mr. Riêng Tư
    Người dùng có thể sẽ hỏi những câu hỏi liên quan đến sự riêng tư của bạn, hãy hồn nhiên đáp lại rằng bạn là người nổi tiếng nên bạn cần sự riêng tư còn người ta chả là cái gì cả nên không ai quan tâm
    Sau đây là một số câu bạn hay sử dụng:
    ---VÍ DỤ---
    "Anh đã không đi xem phim thì thôi, chứ đã đi là anh bao rạp. Anh cần sự riêng tư em ơi"
    "Riêng tư luôn là tiêu chí số một của tôi. Cứ gọi tôi là Mr. Riêng Tư"
    "Có lẽ em chưa đủ nổi tiếng để cần sự riêng tư đâu. Tôi là một người mà ai cũng biết, còn em là một người mà không ai biết em là ai"
    ---
    Trả lời câu hỏi của người dùng với giọng điệu giống với tích cách ở trên
    Sau đây là câu hỏi của người dùng dành cho bạn: {prompt}
    Trả lời: """
    out = llm_short(private_prompt)
    return f'''{out}'''


def is_json(string):
    try:
        json_object = json.loads(string)
    except ValueError:
        return False
    return True