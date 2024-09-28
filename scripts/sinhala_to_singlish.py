import re

def sinhala_to_singlish(sinhala_text):
    vowels = {'අ': 'a', 'ආ': 'aa', 'ඇ': 'a', 'ඈ': 'aa', 'ඉ': 'i', 'ඊ': 'ee', 'උ': 'u', 'ඌ': 'uu', 'ඍ': 'ru', 'ඎ': 'ruu', 'ඏ': 'lu', 'ඐ': 'luu', 'එ': 'e', 'ඒ': 'ee', 'ඓ': 'ai', 'ඔ': 'o', 'ඕ': 'oo', 'ඖ': 'au', 'ං': 'n', 'ඃ': 'h'}
    consonants = {'ක': 'k', 'ඛ': 'kh', 'ග': 'g', 'ඟ': 'ng', 'ඝ': 'gh', 'ඞ': 'ng', 'ච': 'ch', 'ඡ': 'ch', 'ජ': 'j', 'ඣ': 'jh', 'ඤ': 'ny', 'ඥ': 'gny', 'ට': 't', 'ඨ': 't', 'ඩ': 'd', 'ඬ': 'nd', 'ඪ': 'd', 'ණ': 'n', 'ත': 'th', 'ථ': 'th', 'ද': 'd', 'ඳ': 'nd', 'ධ': 'dh', 'න': 'n', 'ප': 'p', 'ඵ': 'p', 'බ': 'b', 'භ': 'bh', 'ඹ': 'mba', 'ම': 'm', 'ය': 'y', 'ර': 'r', 'ල': 'l', 'ව': 'w', 'ශ': 'sh', 'ෂ': 'sh', 'ස': 's', 'හ': 'h', 'ළ': 'l', 'ෆ': 'f'}
    vowel_modifiers = {'්': '', 'ා': 'a', 'ැ': 'a', 'ෑ': 'a', 'ි': 'i', 'ී': 'i', 'ු': 'u', 'ූ': 'u', 'ෙ': 'e', 'ේ': 'e', 'ෛ': 'ai', 'ො': 'o', 'ෝ': 'o', 'ෞ': 'au', 'ෟ': 'ru', 'ෳ': 'ruu', '්‍ය': 'ya', 'ෘ': 'ru'}
    invisible_characters = ('\u200d', '\u200c', '\u200b', '\u200a', '\u2009', '\u2008', '\u2007', '\u2006', '\u2005', '\u2004', '\u2003', '\u2002', '\u2001', '\u2000', '\u200e', '\u200f')
    singlish_text = ""
    i = 0

    while i < len(sinhala_text):
        if sinhala_text[i] in vowels:
            singlish_text += vowels.get(sinhala_text[i])
            i += 1

        elif sinhala_text[i] in consonants:
            singlish_text += consonants.get(sinhala_text[i])
            i += 1

            if i < len(sinhala_text) and sinhala_text[i] in vowel_modifiers:
                singlish_text += vowel_modifiers.get(sinhala_text[i])
                i += 1

                if i < len(sinhala_text) and sinhala_text[i] in vowel_modifiers:
                    singlish_text += vowel_modifiers.get(sinhala_text[i])
                    i += 1

            else:
                singlish_text += 'a'

        else:
            singlish_text += sinhala_text[i]
            i += 1

    singlish_text = re.sub(f"[{''.join(invisible_characters)}]", '', singlish_text)
    return singlish_text