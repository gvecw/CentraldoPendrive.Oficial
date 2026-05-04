with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Imagem customizada
html = html.replace(
    'src="https://i.imgur.com/CaESU8Al.jpg"',
    'src="Gemini_Generated_Image_zhxjxxzhxjxxzhxj.png"'
)

# Urgency bar
html = html.replace(
    '⏳ O PREÇO VAI SUBIR EM BREVE! OFERTA VÁLIDA PARA',
    '🔥 CORRA! ESSA PROMOÇÃO ESTÁ ACABANDO! VÁLIDA SOMENTE ATÉ'
)

# Hero badge
html = html.replace(
    '🎵 ACESSO IMEDIATO VITALÍCIO',
    '🎵 ACESSO INSTANTÂNEO + PARA SEMPRE'
)

# Hero H1
html = html.replace(
    '+5 MIL MÚSICAS</span> DOS ANOS 70, 80 E 90',
    '+5.000 CLÁSSICOS</span> DAS DÉCADAS DE 70, 80 E 90'
)
html = html.replace(
    '— SÓ OS MAIORES SUCESSOS DO —',
    '— A COLEÇÃO DEFINITIVA DO MELHOR —'
)

# Hero paragraph
html = html.replace(
    'Reviva a magia dos anos 70, 80 e 90 com áudio em alta definição (320kbps). Sem anúncios, sem chiados, apenas os maiores sucessos da história na sua tela ou no seu rádio.',
    'Mergulhe na era de ouro da música com som nítido em 320kbps. Sem propagandas, sem interrupções — só os hits inesquecíveis que marcaram gerações, tocando quando e onde você quiser.'
)

# Hero CTA button
html = html.replace(
    '>BAIXAR AGORA - APENAS R$ 10,00<',
    '>GARANTIR MINHA COLEÇÃO - SÓ R$ 10,00<'
)

# Social proof
html = html.replace(
    '⭐ Seleção Recomendada por +15.200 Clientes | Satisfação 100%',
    '⭐ Aprovado por +15.200 Compradores Satisfeitos | Garantia Total'
)

# Nostalgia section title
html = html.replace(
    'UMA VIAGEM <span class="highlight-cyan">NOSTÁLGICA</span> COMPLETA',
    'O PASSADO QUE VOCÊ <span class="highlight-cyan">NUNCA ESQUECE</span>'
)
html = html.replace(
    'Nossa biblioteca é organizada meticulosamente para que você encontre o clima perfeito em segundos.',
    'Todo o conteúdo separado por época, para você escolher o estilo certo na hora que bater saudade.'
)

# Bonus section
html = html.replace(
    'PRESENTE EXCLUSIVO',
    'BÔNUS SURPRESA'
)
html = html.replace(
    '+100 VIDEOCLIPES',
    '+100 CLIPES ORIGINAIS'
)
html = html.replace(
    'Compre hoje e leve também uma coletânea épica de clipes originais para passar na sua TV ou projetor e transformar sua sala numa verdadeira discoteca!',
    'Adquira agora e ganhe de bônus uma seleção incrível de videoclipes icônicos para assistir na TV, notebook ou projetor e transformar qualquer ambiente numa viagem no tempo!'
)
html = html.replace(
    '🎬 Vídeos em alta qualidade (MP4)',
    '🎬 Clipes originais em formato MP4 de alta qualidade'
)
html = html.replace(
    '🌍 Principais artistas internacionais e nacionais',
    '🌍 Artistas nacionais e internacionais que fizeram história'
)
html = html.replace(
    '⚡ Download imediato junto com suas músicas',
    '⚡ Receba junto com toda a sua coleção de músicas'
)
html = html.replace(
    'Valor normal: <s>R$ 47,00</s> | Hoje: <strong>INCLUSO DE GRAÇA</strong>',
    'Preço avulso: <s>R$ 47,00</s> | Na oferta de hoje: <strong>TOTALMENTE GRÁTIS</strong>'
)

# Testimonials header
html = html.replace(
    'FEEDBACK DOS <span class="highlight">COMPRADORES</span>',
    'O QUE DIZEM OS <span class="highlight">NOSSOS CLIENTES</span>'
)
html = html.replace(
    '12 Comentários',
    '15 Comentários'
)

# Comments
html = html.replace(
    'Cara, que coleção incrível! Tá tocando aqui na festa e o pessoal tá amando. Melhor investimento que fiz 👏👏',
    'Gente, que achado! Coloquei pra tocar no churrasquinho e todo mundo pediu o link. Vale cada centavo! 👏👏'
)
html = html.replace(
    'Já recebi o meu e gostei, muito bom 🤩 as músicas são todas de qualidade real, sem chiado! Amei as românticas.',
    'Recebi na hora e fiquei impressionada! 🤩 Qualidade de estúdio mesmo, zero ruído. As músicas românticas são demais!'
)
html = html.replace(
    'DJ aqui, uso profissionalmente. Qualidade 320kbps real, organização perfeita por decade. Aprovado! 🎧',
    'Sou DJ e tô usando nas minhas apresentações. O áudio é impecável, 320kbps de verdade, tudo bem organizado por época. Recomendo! 🎧'
)
html = html.replace(
    'Pensei que fosse golpe por ser tão barato mas chegou tudo certinho kkk sensacional demais 🎶 O bônus dos clipes é top!',
    'Fiquei desconfiado com o preço tão acessível, mas chegou tudinho na hora kkk Absurdamente bom 🎶 Os videoclipes de bônus são incríveis!'
)

# Offer section
html = html.replace(
    'APROVEITE NOSSA <span class="highlight">OFERTA ESPECIAL</span>',
    'NÃO PERCA ESSA <span class="highlight">OPORTUNIDADE ÚNICA</span>'
)
html = html.replace(
    '>PENDRIVE VIRTUAL + BÔNUS<',
    '>BIBLIOTECA DIGITAL + BÔNUS GRÁTIS<'
)
html = html.replace(
    'De R$ 47,00 por apenas',
    'Era R$ 47,00, hoje somente'
)
html = html.replace(
    'PAGAMENTO ÚNICO - ACESSO IMEDIATO',
    'UMA SÓ VEZ - ACESSO ETERNO'
)
html = html.replace(
    'Acesso vitalício a +5000 músicas selecionadas',
    'Biblioteca completa com +5.000 músicas selecionadas a dedo'
)
html = html.replace(
    'Qualidade máxima de estúdio (320kbps MP3)',
    'Áudio profissional de estúdio em 320kbps MP3'
)
html = html.replace(
    'Bônus: +100 Videoclipes FLASHBACK (MP4)',
    'Bônus exclusivo: +100 Videoclipes icônicos (MP4)'
)
html = html.replace(
    'Livre de anúncios e vinhetas irritantes',
    'Zero propagandas e zero vinhetas no meio das músicas'
)
html = html.replace(
    'Pode baixar e ouvir offline onde quiser',
    'Baixe uma vez e ouça em qualquer lugar, sem internet'
)
html = html.replace(
    '>QUERO BAIXAR AGORA!<',
    '>QUERO GARANTIR MEU ACESSO AGORA!<'
)

# Guarantee section
html = html.replace(
    'RISCO ZERO: <br><span>7 DIAS DE GARANTIA</span>',
    'COMPRA SEGURA: <br><span>GARANTIA DE 7 DIAS</span>'
)
html = html.replace(
    'Você tem <strong>7 dias inteiros</strong> para acessar a plataforma, baixar as músicas, os clipes e testar tudo no seu carro, TV ou celular.',
    'Você tem <strong>7 dias completos</strong> para explorar todo o conteúdo, ouvir as músicas, assistir os clipes e testar em qualquer aparelho.'
)
html = html.replace(
    'Se você não ficar impressionado com a qualidade ou achar que não era o que esperava, basta mandar um único e-mail e <strong>devolveremos 100% do seu dinheiro</strong> na mesma hora. Sem perguntas e sem burocracia. O risco é todo nosso!',
    'Se por qualquer motivo você não ficar satisfeito, basta enviar uma mensagem e <strong>devolvemos 100% do valor</strong> sem complicação. Nenhuma pergunta feita, nenhuma burocracia. O risco é completamente nosso!'
)

# FAQ
html = html.replace(
    'DÚVIDAS <span class="highlight">FREQUENTES</span>',
    'PERGUNTAS <span class="highlight">MAIS COMUNS</span>'
)
html = html.replace(
    'O que é o Pendrive Virtual?',
    'O que eu vou receber exatamente?'
)
html = html.replace(
    'É uma biblioteca digital completa! Você recebe um link exclusivo de acesso imediato por e-mail para baixar todas as músicas. Assim, você não paga frete e tem o conteúdo na hora, podendo transferir para o seu pendrive físico depois!',
    'Você recebe uma biblioteca digital completa! Logo após a compra, chegará no seu e-mail um link exclusivo para baixar tudo. Não tem frete, não tem espera — é digital e na hora, podendo salvar no pendrive físico depois.'
)
html = html.replace(
    'Como recebo o acesso?',
    'Quanto tempo leva para receber?'
)
html = html.replace(
    'O envio é automático! Assim que o pagamento for aprovado (Pix e Cartão aprovam na hora), você receberá em seu e-mail os dados para acessar e baixar todo o material.',
    'É imediato! Assim que o pagamento confirmar (Pix e Cartão são aprovados na hora), o link de acesso chega automaticamente no seu e-mail. Em minutos você já pode baixar tudo.'
)
html = html.replace(
    'Posso ouvir no carro ou TV?',
    'Funciona no rádio do carro e na TV?'
)
html = html.replace(
    'Sim! As músicas estão em formato MP3 de alta qualidade. Basta passar os arquivos para qualquer pendrive e espetar no rádio do carro, TV, caixa de som ou computador.',
    'Sim, perfeitamente! As músicas são em MP3 de alta qualidade. É só copiar para qualquer pendrive e conectar no rádio do carro, TV, caixa de som ou computador. Funciona em tudo!'
)
html = html.replace(
    'Consigo ouvir as músicas sem internet (offline)?',
    'Preciso de internet para ouvir depois de baixar?'
)
html = html.replace(
    'Com certeza! Você só precisa de internet para baixar os arquivos na primeira vez. Depois que salvar no seu celular, computador ou transferir para o pendrive, poderá ouvir todas as músicas e assistir aos clipes 100% offline, em qualquer lugar, sem gastar seus dados!',
    'Não! Basta internet apenas no momento do download. Depois de salvar no celular, computador ou pendrive, você ouve as músicas e assiste os clipes 100% offline, sem consumir nenhum dado do seu plano.'
)
html = html.replace(
    'As músicas têm vinheta chata?',
    'Tem propaganda ou vinheta no meio das músicas?'
)
html = html.replace(
    'Não! Esqueça as propagandas e vinhetas no meio do som. Com nossa coleção você tem uma experiência auditiva limpa, do início ao fim da música.',
    'Absolutamente não! As músicas são limpas do começo ao fim. Nada de propaganda, nada de vinheta no meio. Uma experiência de audição pura e sem interrupções.'
)
html = html.replace(
    'E se eu tiver dúvidas após a compra?',
    'Tem suporte caso eu precise de ajuda?'
)
html = html.replace(
    'Nós temos uma equipe de suporte dedicada! Dentro da plataforma de entrega do conteúdo, você terá um e-mail direto para falar com nosso time caso precise de ajuda para baixar ou organizar os arquivos.',
    'Sim! Temos uma equipe pronta para te atender. Na plataforma de entrega você encontra um e-mail direto para tirar qualquer dúvida sobre o download ou organização dos arquivos.'
)

# Final CTA FAQ
html = html.replace(
    '>SIM, QUERO GARANTIR MEU ACESSO!<',
    '>SIM, QUERO MINHA COLEÇÃO AGORA!<'
)

# Footer
html = html.replace(
    'PENDRIVE VIRTUAL FLASHBACK © 2026',
    'COLEÇÃO DIGITAL FLASHBACK © 2026'
)
html = html.replace(
    'As músicas e imagens são para fins de entretenimento e nostalgia. Ao adquirir você concorda com nossos termos.',
    'Todo o conteúdo é disponibilizado para fins de entretenimento e nostalgia pessoal. Ao realizar a compra, você declara concordar com nossos termos de uso.'
)

# Popup
html = html.replace(
    'Acabou de comprar a coleção! 🚀',
    'Acabou de garantir o acesso! 🎶'
)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)

print("Textos atualizados com sucesso!")
