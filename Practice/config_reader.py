def configRead():
    try:
        with open('config.txt', 'r+') as config:
            content = config.readlines()
            recognition = content[1]
            starting = content[4]
            multitasking = content[7]
            late_game = content[10]
            settings = content[13]
            r_words = recognition.split(', ')
            intermediate = r_words[-1].split('\n')
            r_words.pop(-1)
            r_words.append(intermediate[0])
            r_num = len(r_words)
            for i in range(6 - len(r_words)):
                r_words.append('')
            s_words = starting.split(', ')
            intermediate = s_words[-1].split('\n')
            s_words.pop(-1)
            s_words.append(intermediate[0])
            s_num = len(s_words)
            for i in range(6 - len(s_words)):
                s_words.append('')
            m_words = multitasking.split(', ')
            intermediate = m_words[-1].split('\n')
            m_words.pop(-1)
            m_words.append(intermediate[0])
            for i in range(6 - len(m_words)):
                m_words.append('')
            l_words = late_game.split(', ')
            intermediate = l_words[-1].split('\n')
            l_words.pop(-1)
            l_words.append(intermediate[0])
            l_num = len(l_words)
            for i in range(6 - len(l_words)):
                l_words.append('')
            settings = settings.split(', ')
            return r_words, r_num, s_words, s_num, m_words, l_words, l_num, settings
    except IndexError:
        return [[']', 0]]
