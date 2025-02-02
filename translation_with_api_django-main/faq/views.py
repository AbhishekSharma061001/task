from django.shortcuts import render
from django.http import JsonResponse
from deep_translator import GoogleTranslator
from bs4 import BeautifulSoup
from django.core.cache import cache
from faq.models import FAQ


def translate_text(text, lang="en", is_rich_text=False):
    translator = GoogleTranslator(source='auto', target=lang)

    if not is_rich_text:
        return translator.translate(text)

    soup = BeautifulSoup(text, "html.parser")
    return str(soup)

def getFaqs(request):
    lang = request.GET.get("lang", "en")
    cache_key = f"faqs_{lang}"

    # Check cache
    data = cache.get(cache_key)
    if not data:
        faqs = FAQ.objects.all()
        data = []

        for faq in faqs:
            translated_question = translate_text(faq.question, lang)
            translated_answer = translate_text(faq.answer, lang, is_rich_text=True)
            data.append({"question": translated_question, "answer": translated_answer})

        cache.set(cache_key, data, timeout=3600)

    return JsonResponse(data, safe=False)

#Test dev server -{manifest 1 endpoint/Debarghya}
def home(request):
    return JsonResponse({"message": "Welcome to the FAQ API"})

def translate_view(request):
    text = request.GET.get('text', '')
    lang = request.GET.get('lang', 'en')
    translated_text = translate_text(text, lang)
    return JsonResponse({
        'original_text': text,
        'translated_text': translated_text
    })
