import json
V="2026-10-16"
A="A1-C2"
# id,name,url,levels(lo,hi),skills,audience,tier,start,note,pricing_source,verified
rows=[
("diffit","Diffit","https://web.diffit.me",("A1","C1"),"reading,vocabulary","teacher","Freemium","Free Basic; paid teacher/school licenses","Rewrites any article or topic into leveled readings with vocab and questions.","https://web.diffit.me/pricing",1),
("eduaide","Eduaide.ai","https://www.eduaide.ai",("A1","C2"),"reading,writing,vocabulary,grammar","teacher","Freemium","Free tier; Pro unverified","Generates lesson resources, activities and feedback from a topic.","https://www.eduaide.ai/pricing",0),
("gemini","Google Gemini","https://gemini.google.com",("A2","C2"),"speaking,writing,grammar,vocabulary,reading","both","Freemium","Free","General assistant; learners can practice conversation, teachers draft materials.","https://gemini.google.com",0),
("readingcoach","Microsoft Reading Coach","https://coach.microsoft.com",("A1","B1"),"reading,pronunciation","learner","Free","Free","Reading-aloud practice with feedback on tricky words.","https://coach.microsoft.com",1),
("chatgpt","ChatGPT","https://chatgpt.com",("A2","C2"),"speaking,listening,writing,grammar,vocabulary,reading","both","Freemium","Free plan; Go/Plus/Pro paid","Voice mode for conversation practice; teachers build worksheets and role-plays.","https://chatgpt.com/pricing",1),
("kahoot","Kahoot!","https://kahoot.com",("A1","C1"),"vocabulary,grammar","teacher","Freemium","Free account; paid education plans","AI-assisted quiz builder for vocabulary and grammar review games.","https://kahoot.com/pricing",1),
("heygen","HeyGen","https://www.heygen.com",("A2","C1"),"listening","teacher","Freemium","Free 3 videos/mo; Creator $29/mo","Make short AI-presenter listening clips and dialogues.","https://www.heygen.com/pricing",1),
("elsa","ELSA Speak","https://elsaspeak.com",("A2","C1"),"pronunciation,speaking","learner","Freemium","Free limited; Pro unverified","AI pronunciation coach scoring individual sounds and stress.","https://elsaspeak.com",0),
("promova","Promova","https://promova.com",("A1","B2"),"vocabulary,speaking,grammar","learner","Freemium","Free limited; Premium unverified","Bite-size English lessons with AI conversation practice.","https://promova.com",0),
("speak","Speak","https://www.speak.com",("A1","B2"),"speaking,listening","learner","Paid","Free trial; subscription unverified","Speaking-first app with an AI tutor for spoken drills.","https://www.speak.com",0),
("eslvideo","ESLvideo / Neo English","https://eslvideo.com",("A1","B2"),"listening,vocabulary","both","Freemium","Unverified","Video-based listening quizzes; teachers can build their own.","https://eslvideo.com",0),
("gliglish","Gliglish","https://gliglish.com",("A2","C1"),"speaking,listening","learner","Freemium","Free daily minutes; paid unverified","Voice chat with an AI teacher in role-play scenarios.","https://gliglish.com",0),
("lessonmate","Lesson Mate AI","https://www.lessonmate.ai",("A1","C1"),"reading,writing,grammar,vocabulary","teacher","Freemium","Unverified","AI lesson-plan generator aimed at language teachers.","https://www.lessonmate.ai",0),
("magicschool","MagicSchool","https://www.magicschool.ai",("A1","C1"),"reading,writing,vocabulary","teacher","Freemium","Free; Plus $12.99/mo ($8.33 billed annually)","80+ teacher tools incl. text leveler and vocab lists; built for K-12 but useful for adults.","https://www.magicschool.ai/pricing",1),
("brisk","Brisk Teaching","https://www.briskteaching.com",("A1","C2"),"reading,writing","teacher","Freemium","Unverified","Chrome extension to re-level texts and give writing feedback in Google Docs.","https://www.briskteaching.com",0),
("notebooklm","NotebookLM","https://notebooklm.google.com",("B1","C2"),"listening,reading","both","Free","Free (paid tiers via Google One unverified)","Turns readings into audio overviews for listening practice.","https://notebooklm.google.com",0),
("copilot","Microsoft Copilot","https://copilot.microsoft.com",("A2","C2"),"speaking,writing,grammar,vocabulary","both","Freemium","Free","General assistant with voice; handy for drafting and explaining grammar.","https://copilot.microsoft.com",0),
("claude","Claude","https://claude.ai",("B1","C2"),"writing,grammar,reading","both","Freemium","Free; Pro unverified","Strong at explaining grammar and giving gentle writing feedback.","https://claude.ai",0),
("twee","Twee","https://twee.com",("A1","C2"),"reading,listening,vocabulary,grammar,writing","teacher","Freemium","Free plan; paid unverified","Built for English teachers: questions from YouTube videos, texts, dialogues, vocab tasks.","https://twee.com",0),
("writeimprove","Write & Improve (Cambridge)","https://writeandimprove.com",("A1","C2"),"writing,grammar","learner","Free","Free","Cambridge's writing checker gives a CEFR-aligned level and feedback.","https://writeandimprove.com",0),
("grammarly","Grammarly","https://www.grammarly.com",("B1","C2"),"writing,grammar","learner","Freemium","Free; Pro from $12/mo billed annually","Grammar and clarity suggestions for emails and essays.","https://www.grammarly.com/plans",1),
("languagetool","LanguageTool","https://languagetool.org",("B1","C2"),"writing,grammar","learner","Freemium","Free; Premium unverified","Multilingual grammar checker; can explain errors in the learner's first language context.","https://languagetool.org/premium",0),
("quillbot","QuillBot","https://quillbot.com",("B1","C2"),"writing,grammar,vocabulary","learner","Freemium","Free; Premium unverified","Paraphraser and grammar checker for upper-level writing practice.","https://quillbot.com/premium",0),
("praktika","Praktika","https://www.praktika.ai",("A1","C1"),"speaking,listening","learner","Freemium","Unverified","AI avatar tutors for spoken English conversation.","https://www.praktika.ai",0),
("talkpal","Talkpal","https://talkpal.ai",("A1","C1"),"speaking,listening,grammar","learner","Freemium","Unverified","GPT-powered conversation partner with role-plays and debates.","https://talkpal.ai",0),
("langua","Langua","https://languatalk.com",("A1","C2"),"speaking,listening,vocabulary","learner","Paid","Unverified","AI conversation partner with corrections and saved vocab.","https://languatalk.com",0),
("boldvoice","BoldVoice","https://www.boldvoice.com",("B1","C2"),"pronunciation,speaking","learner","Paid","Unverified (free trial)","Accent and pronunciation training from coach videos plus AI feedback.","https://www.boldvoice.com",0),
("cathoven","Cathoven","https://cathoven.com",("A1","C2"),"reading,writing,vocabulary","teacher","Freemium","Unverified","CEFR text analyzer and adapter; checks reading level of any passage.","https://cathoven.com",0),
("eslbrains","ESL Brains","https://www.eslbrains.com",("A2","C1"),"speaking,reading,vocabulary,listening","teacher","Freemium","Some free lessons; premium unverified","Ready-made adult ESL lessons plus AI-assisted lesson tools.","https://www.eslbrains.com",0),
("youglish","YouGlish","https://youglish.com",("A2","C2"),"pronunciation,listening","both","Free","Free","Hear any word or phrase in real YouTube speech (not generative AI, but a great companion).","https://youglish.com",0),
("duolingomax","Duolingo Max","https://www.duolingo.com/max",("A1","B2"),"speaking,listening,vocabulary,grammar","learner","Paid","Unverified","Duolingo's AI tier with Video Call and Explain My Answer.","https://www.duolingo.com/max",0),
]
L=["A1","A2","B1","B2","C1","C2"]
out=[dict(id=r[0],name=r[1],url=r[2],levels=L[L.index(r[3][0]):L.index(r[3][1])+1],skills=r[4].split(","),audience=r[5],price_tier=r[6],starting_price=r[7],note=r[8],pricing_source=r[9],pricing_verified=bool(r[10]),last_checked=V) for r in rows]
json.dump(out,open("data/tools.json","w"),indent=1)
open("data/tools.js","w").write("window.TOOLS="+json.dumps(out)+";")
print(len(out),sum(o["pricing_verified"] for o in out))
