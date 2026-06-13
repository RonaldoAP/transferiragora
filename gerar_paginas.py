#!/usr/bin/env python3
"""Gera páginas de venda para cada domínio a partir de um template."""

import os

ACCESS_KEY = "0458cda2-114f-4697-b79b-c2f0008b52f1"

DOMINIOS = [
    {
        "slug": "acompanharvoo",
        "dominio": "acompanharvoo",
        "tld": ".com.br",
        "tagline": "O endereço ideal para serviços de rastreamento e acompanhamento de voos no Brasil. Memorável, direto e sem concorrência.",
        "valor": "R$ 3.500",
        "cards": [
            ("01", "Turismo digital em alta", "O setor aéreo brasileiro movimenta bilhões. Quem domina o nome domina a busca — e o cliente que está pesquisando voo agora."),
            ("02", "Nome descritivo = tráfego grátis", "Usuários digitam exatamente o que precisam. 'Acompanhar voo' é uma das buscas mais frequentes no Google Brasil."),
            ("03", "Zero concorrência no .com.br", "Este domínio existe uma única vez no Brasil. Sem alternativas idênticas para o seu concorrente registrar."),
            ("04", "Valorização garantida", "Domínios do setor de viagens sempre se valorizam. O que custa hoje será mais caro amanhã — se ainda estiver disponível."),
        ],
    },
    {
        "slug": "atacadoshopping",
        "dominio": "atacadoshopping",
        "tld": ".com.br",
        "tagline": "Perfeito para marketplaces, atacadistas e plataformas de compra em grande volume. Um nome que explica e vende por si só.",
        "valor": "R$ 5.500",
        "cards": [
            ("01", "E-commerce no atacado explode", "O atacado online cresce mais rápido que o varejo. Quem chegar com o nome certo na cabeça do comprador ganha o mercado."),
            ("02", "Duas palavras de alto impacto", "Atacado + Shopping: dupla poderosa que comunica volume, variedade e economia. O nome já é a proposta de valor."),
            ("03", "Tráfego orgânico imediato", "Pessoas que buscam por 'atacado' e 'shopping' já são compradores em potencial. O domínio capta esse tráfego naturalmente."),
            ("04", "Preço sobe com o setor", "O mercado de atacado digital só cresce. Cada mês que passa, domínios assim ficam mais disputados e mais caros."),
        ],
    },
    {
        "slug": "brasilpromocoes",
        "dominio": "brasilpromocoes",
        "tld": ".com.br",
        "tagline": "Um dos termos mais buscados no e-commerce brasileiro. Domínio de alto potencial de tráfego orgânico e reconhecimento imediato.",
        "valor": "R$ 6.500",
        "cards": [
            ("01", "Promoção é o gatilho #1 no Brasil", "'Promoção' está entre as palavras mais buscadas em compras online. Este domínio é um ímã de tráfego gratuito."),
            ("02", "Escala nacional desde o primeiro dia", "Com 'Brasil' no nome, a marca nasce nacional. Credibilidade e alcance sem precisar investir em branding extra."),
            ("03", "Versátil para qualquer nicho", "Cupons, cashback, afiliados, marketplace — qualquer modelo de negócio de ofertas se encaixa neste endereço."),
            ("04", "Janela de oportunidade", "Domínios com termos genéricos e de alta busca raramente ficam disponíveis por muito tempo. Este é um deles."),
        ],
    },
    {
        "slug": "buscapay",
        "dominio": "buscapay",
        "tld": ".com.br",
        "tagline": "Nome curto, memorável e perfeito para fintechs, meios de pagamento e soluções financeiras digitais. Combina busca + pagamento.",
        "valor": "R$ 8.500",
        "cards": [
            ("01", "Fintech é o setor que mais cresce", "O Brasil é o maior mercado fintech da América Latina. Entrar com o nome certo agora vale muito mais do que entrar tarde."),
            ("02", "Curto, sonoro e internacional", "Apenas 8 letras. Fácil de falar, de ouvir e de lembrar — em português e em inglês. Ideal para escalar além das fronteiras."),
            ("03", "Pay: palavra de credibilidade", "Sufixo 'pay' associa a marca a pagamentos digitais globais como PicPay, MercadoPay, ApplePay. Entra nessa categoria pelo nome."),
            ("04", "Raridade no mercado", "Domínios curtos e semânticos no setor financeiro valem 5 a 10x mais do que domínios genéricos. Este é um ativo real."),
        ],
    },
    {
        "slug": "casadaraposa",
        "dominio": "casadaraposa",
        "tld": ".com.br",
        "tagline": "Nome criativo e memorável, ideal para restaurantes, bares, moda boutique ou marcas com personalidade forte e conceito único.",
        "valor": "R$ 2.800",
        "cards": [
            ("01", "Nomes criativos geram viralidade", "Marcas com nomes inusitados são compartilhadas naturalmente. 'Casa da Raposa' já desperta curiosidade antes do primeiro contato."),
            ("02", "Identidade visual pronta na cabeça", "A raposa é símbolo de astúcia e elegância. O branding se escreve sozinho — e fica na memória do cliente."),
            ("03", "Versátil entre nichos premium", "Gastronomia, moda, decoração, pet — qualquer mercado que valorize conceito e estilo pode usar este nome com autoridade."),
            ("04", "Ativo de marca duradouro", "Domínios com identidade forte se valorizam com o tempo. Uma marca construída aqui pode valer muito mais que o endereço."),
        ],
    },
    {
        "slug": "casadoaviao",
        "dominio": "casadoaviao",
        "tld": ".com.br",
        "tagline": "Domínio temático com forte apelo para o setor aéreo, lojas de aeromodelismo, turismo ou qualquer marca ligada à aviação.",
        "valor": "R$ 3.800",
        "cards": [
            ("01", "Aviação é paixão e negócio", "Do aeromodelismo ao turismo aéreo, o setor tem um público fiel e crescente. Um nome temático atrai esse público direto ao site."),
            ("02", "Referência imediata no setor", "Quem procura por aviação e encontra 'Casa do Avião' já sabe com quem está falando. O nome entrega confiança antes do conteúdo."),
            ("03", "Mercado em expansão", "O setor aéreo brasileiro retomou crescimento acelerado. Entrar agora, com o nome certo, é posicionar a marca antes da concorrência."),
            ("04", "Único no .com.br", "Não existe outro. Quem registrar este domínio fecha a porta para qualquer concorrente que queira o mesmo endereço."),
        ],
    },
    {
        "slug": "construtorasantaefigenia",
        "dominio": "construtorasantaefigenia",
        "tld": ".com.br",
        "tagline": "Domínio institucional registrado para construtora com nome consolidado. Ideal para empresa do setor imobiliário da região.",
        "valor": "R$ 1.800",
        "cards": [
            ("01", "Nome já existe no mercado", "Construtoras com este nome já operam no Brasil. Quem adquirir o domínio ganha autoridade digital imediata no segmento."),
            ("02", "Setor imobiliário aquecido", "Construção civil e imóveis seguem em alta. Um domínio profissional é o primeiro passo para captar clientes no digital."),
            ("03", "Credibilidade local e regional", "Nomes com bairro ou santo padroeiro transmitem enraizamento e confiança — ativos valiosos para construtoras regionais."),
            ("04", "Oportunidade pontual", "Domínios de empresas estabelecidas raramente ficam livres. Esta janela pode fechar a qualquer momento."),
        ],
    },
    {
        "slug": "dockpay",
        "dominio": "dockpay",
        "tld": ".com.br",
        "tagline": "Nome curto, moderno e internacionalizável para soluções de pagamento digital, open finance ou plataformas de gestão financeira.",
        "valor": "R$ 9.500",
        "cards": [
            ("01", "Fintech de alto crescimento", "O Brasil lidera fintechs na América Latina. Startups de pagamento captam investimentos bilionários — e precisam de nomes que escalam."),
            ("02", "Dock: referência em infraestrutura", "Dock é uma palavra forte no universo de APIs e banking-as-a-service. O nome já posiciona a marca nessa categoria premium."),
            ("03", "Sete letras, impacto global", "Curto o suficiente para qualquer tela, forte o suficiente para qualquer pitch de investidor. Raro no mercado .com.br."),
            ("04", "Ativo financeiro real", "Domínios fintech curtos são negociados no mercado secundário por valores muito acima do registro. Este é um investimento."),
        ],
    },
    {
        "slug": "energiaprime",
        "dominio": "energiaprime",
        "tld": ".com.br",
        "tagline": "Domínio premium para o setor de energia limpa, distribuidoras, energia solar, ou marcas de suplementação e performance.",
        "valor": "R$ 6.800",
        "cards": [
            ("01", "Energia solar em boom no Brasil", "O Brasil é um dos maiores mercados de energia solar do mundo. Um nome premium nesse setor tem valor crescente e comprador certo."),
            ("02", "Prime = posicionamento diferenciado", "O sufixo 'Prime' eleva qualquer marca ao nível premium imediatamente. Energia + Prime cria uma combinação poderosa e aspiracional."),
            ("03", "Dupla aplicação de nicho", "Funciona igualmente bem para empresas de energia elétrica e para marcas de suplementos/performance. Dois mercados, uma oportunidade."),
            ("04", "Valorização contínua", "Com a transição energética global acelerando, domínios do setor de energia limpa só tendem a se valorizar nos próximos anos."),
        ],
    },
    {
        "slug": "fbitricolor",
        "dominio": "fbitricolor",
        "tld": ".com.br",
        "tagline": "Domínio temático com apelo direto às comunidades tricolores do futebol brasileiro. Base de fãs apaixonada e engajada.",
        "valor": "R$ 3.200",
        "cards": [
            ("01", "Futebol é o maior mercado de fãs", "O Brasil tem mais de 100 milhões de torcedores apaixonados. Conteúdo e produtos para esse público têm demanda garantida."),
            ("02", "Comunidade tricolor unida", "Tricolor é identidade — e identidade gera engajamento. Um hub para essa comunidade tem audiência antes mesmo do lançamento."),
            ("03", "Múltiplas aplicações", "Blog, loja de produtos oficiais, plataforma de apostas temática, podcast esportivo — o nome funciona para todos esses formatos."),
            ("04", "Escassez real", "Domínios temáticos esportivos específicos não ficam disponíveis duas vezes. Quem registrou, registrou."),
        ],
    },
    {
        "slug": "flash360",
        "dominio": "flash360",
        "tld": ".com.br",
        "tagline": "Nome versátil e moderno para agências digitais, plataformas de conteúdo, apps de tecnologia ou qualquer marca que queira transmitir velocidade e completude.",
        "valor": "R$ 7.200",
        "cards": [
            ("01", "Flash = velocidade e impacto", "Em um mercado que valoriza agilidade, um nome que comunica 'rápido' e 'completo' já está na frente antes mesmo do primeiro produto."),
            ("02", "360: visão total e diferenciada", "O sufixo 360 posiciona a marca como solução completa. Muito usado em agências, consultorias e plataformas de gestão."),
            ("03", "Funciona em qualquer setor", "Tech, marketing, logística, financeiro — Flash360 se adapta a qualquer segmento sem perder identidade ou impacto."),
            ("04", "Domínio de agência com valor de mercado", "Agências e startups pagam prêmio por nomes que comunicam serviço sem precisar explicar. Este é um deles."),
        ],
    },
    {
        "slug": "fnabrasil",
        "dominio": "fnabrasil",
        "tld": ".com.br",
        "tagline": "Domínio institucional ideal para federações, associações nacionais, franquias ou qualquer organização de abrangência nacional com sigla FNA.",
        "valor": "R$ 3.500",
        "cards": [
            ("01", "Siglas institucionais têm valor", "Federações, associações e redes franqueadas buscam domínios com sua sigla. Quem tiver o .com.br da sigla FNA controla a presença digital."),
            ("02", "Brasil no nome = alcance nacional", "A combinação sigla + Brasil comunica abrangência e legitimidade desde o primeiro acesso. Ideal para organizações de grande porte."),
            ("03", "Credibilidade sem esforço", "Um domínio institucional com sigla transmite seriedade e organização — atributos que custam muito para construir e nada para ter com o endereço certo."),
            ("04", "Comprador certo existe", "Qualquer organização, associação ou rede com a sigla FNA precisa deste domínio para proteger sua marca. O comprador já existe — só falta o contato."),
        ],
    },
]


TEMPLATE = '''<!-- Domínio: {dominio_full} | Gerado automaticamente -->
<style>
  .dv-scope {{
    --bg: #15171a;
    --ink: #eef1f3;
    --ink-dim: #9aa1a8;
    --green: #20B038;
    --green-light: #60D66A;
    --grad: linear-gradient(135deg, #20B038 0%, #60D66A 100%);
    --line: rgba(238, 241, 243, .09);
    --card: rgba(238, 241, 243, .025);
    --radius: 18px;
    background: var(--bg);
    color: var(--ink);
    font-family: 'Inter', system-ui, sans-serif;
    font-weight: 400;
    line-height: 1.55;
    overflow: hidden;
    position: relative;
    max-width: 100%;
  }}
  .dv-scope * {{ margin: 0; padding: 0; box-sizing: border-box; }}
  .dv-scope::before {{
    content: "";
    position: absolute;
    inset: 0;
    z-index: 0;
    pointer-events: none;
    background: radial-gradient(700px 420px at 78% -8%, rgba(32, 176, 56, .18), transparent 60%),
                radial-gradient(600px 500px at 8% 110%, rgba(96, 214, 106, .08), transparent 55%);
  }}
  .dv-wrap {{ position: relative; z-index: 1; max-width: 1000px; margin: 0 auto; padding: 0 28px; }}
  .dv-status {{ font-size: .72rem; font-weight: 500; letter-spacing: .06em; color: var(--ink-dim); display: flex; align-items: center; gap: 8px; }}
  .dv-dot {{ width: 7px; height: 7px; border-radius: 50%; background: var(--green-light); animation: dvpulse 2.4s infinite; }}
  @keyframes dvpulse {{
    0%   {{ box-shadow: 0 0 0 0 rgba(96, 214, 106, .5); }}
    70%  {{ box-shadow: 0 0 0 9px rgba(96, 214, 106, 0); }}
    100% {{ box-shadow: 0 0 0 0 rgba(96, 214, 106, 0); }}
  }}
  .dv-scope header {{ padding: 64px 0 60px; text-align: center; }}
  .dv-badge {{ display: inline-flex; align-items: center; gap: 9px; font-size: .7rem; font-weight: 600; letter-spacing: .14em; text-transform: uppercase; color: var(--green-light); background: rgba(32, 176, 56, .10); border: 1px solid rgba(96, 214, 106, .30); padding: 9px 18px; border-radius: 100px; margin-bottom: 30px; }}
  .dv-badge .dv-dot {{ width: 6px; height: 6px; }}
  .dv-domain {{ font-size: 64px; font-weight: 700; line-height: 1.04; letter-spacing: -.03em; white-space: nowrap; max-width: 100%; }}
  .dv-domain .dv-tld {{ background: var(--grad); -webkit-background-clip: text; background-clip: text; -webkit-text-fill-color: transparent; }}
  .dv-tagline {{ font-size: clamp(1.05rem, 2.5vw, 1.35rem); color: var(--ink-dim); max-width: 560px; margin: 24px auto 0; font-weight: 400; }}
  .dv-cta {{ display: flex; gap: 14px; justify-content: center; flex-wrap: wrap; margin-top: 42px; }}
  .dv-btn {{ font-size: .9rem; font-weight: 600; padding: 16px 32px; border-radius: 100px; text-decoration: none; border: 1px solid transparent; transition: transform .25s, filter .25s; cursor: pointer; font-family: inherit; }}
  .dv-btn-primary {{ background: var(--grad); color: #08130b; }}
  .dv-btn-primary:hover {{ transform: translateY(-2px); filter: brightness(1.08); }}
  .dv-btn-ghost {{ border-color: var(--line); color: var(--ink); }}
  .dv-btn-ghost:hover {{ border-color: var(--green-light); color: var(--green-light); transform: translateY(-2px); }}
  .dv-trust {{ display: flex; justify-content: center; gap: 34px; flex-wrap: wrap; margin-top: 64px; padding: 28px 0; border-top: 1px solid var(--line); border-bottom: 1px solid var(--line); }}
  .dv-trust > div {{ display: flex; flex-direction: column; align-items: center; gap: 6px; }}
  .dv-trust .dv-ic {{ font-size: 1.1rem; color: var(--green-light); }}
  .dv-trust .dv-lbl {{ font-size: .68rem; font-weight: 500; letter-spacing: .08em; text-transform: uppercase; color: var(--ink-dim); text-align: center; }}
  .dv-scope section {{ padding: 64px 0; }}
  .dv-sec-title {{ font-size: clamp(1.6rem, 4vw, 2.3rem); font-weight: 700; text-align: center; margin-bottom: 14px; letter-spacing: -.02em; }}
  .dv-sec-sub {{ text-align: center; color: var(--ink-dim); max-width: 520px; margin: 0 auto 48px; font-size: 1rem; font-weight: 400; }}
  .dv-grid {{ display: grid; grid-template-columns: repeat(auto-fit, minmax(220px, 1fr)); gap: 16px; }}
  .dv-card {{ background: var(--card); border: 1px solid var(--line); border-radius: var(--radius); padding: 30px 26px; transition: transform .3s, border-color .3s, background .3s; }}
  .dv-card:hover {{ transform: translateY(-4px); border-color: rgba(96, 214, 106, .35); background: rgba(32, 176, 56, .05); }}
  .dv-num {{ font-size: .78rem; font-weight: 700; background: var(--grad); -webkit-background-clip: text; background-clip: text; -webkit-text-fill-color: transparent; }}
  .dv-card h3 {{ font-size: 1.2rem; font-weight: 600; margin: 12px 0 9px; }}
  .dv-card p {{ color: var(--ink-dim); font-size: .93rem; font-weight: 400; }}
  .dv-offer {{ background: linear-gradient(160deg, rgba(32, 176, 56, .08), rgba(238, 241, 243, .02)); border: 1px solid var(--line); border-radius: 26px; padding: clamp(30px, 5vw, 52px); max-width: 620px; margin: 0 auto; }}
  .dv-offer h2 {{ font-size: clamp(1.5rem, 4vw, 2rem); font-weight: 700; margin-bottom: 10px; text-align: center; letter-spacing: -.02em; }}
  .dv-offer .dv-sec-sub {{ margin-bottom: 28px; }}
  .dv-value {{ background: rgba(32, 176, 56, .06); border: 1px solid rgba(96, 214, 106, .22); border-radius: 14px; padding: 18px 20px; margin-bottom: 26px; text-align: center; }}
  .dv-value-lbl {{ font-size: .66rem; font-weight: 600; letter-spacing: .14em; text-transform: uppercase; color: var(--ink-dim); margin-bottom: 6px; }}
  .dv-value-num {{ font-size: 1.7rem; font-weight: 700; background: var(--grad); -webkit-background-clip: text; background-clip: text; -webkit-text-fill-color: transparent; line-height: 1.1; }}
  .dv-scarcity {{ display: inline-flex; align-items: center; gap: 7px; margin-top: 12px; font-size: .74rem; font-weight: 500; color: var(--green-light); }}
  .dv-scarcity .dv-dot {{ width: 6px; height: 6px; }}
  .dv-field {{ margin-bottom: 18px; }}
  .dv-field label {{ display: block; font-size: .72rem; font-weight: 500; letter-spacing: .1em; text-transform: uppercase; color: var(--ink-dim); margin-bottom: 8px; }}
  .dv-field input, .dv-field textarea {{ width: 100%; background: rgba(21, 23, 26, .7); border: 1px solid var(--line); border-radius: 12px; padding: 14px 16px; color: var(--ink); font-family: inherit; font-size: .95rem; font-weight: 400; transition: border-color .25s; }}
  .dv-field input:focus, .dv-field textarea:focus {{ outline: none; border-color: var(--green); }}
  .dv-field textarea {{ resize: vertical; min-height: 90px; }}
  .dv-two {{ display: grid; grid-template-columns: 1fr 1fr; gap: 14px; }}
  .dv-submit {{ width: 100%; margin-top: 8px; border: none; font-size: .95rem; }}
  .dv-submit:disabled {{ opacity: .6; cursor: wait; }}
  .dv-note {{ text-align: center; font-size: .74rem; font-weight: 400; color: var(--ink-dim); margin-top: 18px; }}
  .dv-result {{ display: none; text-align: center; padding: 28px; font-size: 1.02rem; font-weight: 500; }}
  .dv-result.ok {{ color: var(--green-light); }}
  .dv-result.err {{ color: #ff8181; }}
  @media (max-width: 768px) {{
    .dv-domain {{ font-size: 22px; }}
    .dv-cta {{ flex-direction: column; }}
    .dv-btn {{ width: 100%; text-align: center; }}
    .dv-trust {{ gap: 20px 28px; }}
    .dv-two {{ grid-template-columns: 1fr; }}
    .dv-tagline {{ font-size: 16px !important; }}
  }}
  .dv-footer {{ padding: 46px 0 56px; text-align: center; border-top: 1px solid var(--line); margin-top: 36px; }}
  .dv-footer p {{ font-size: .74rem; font-weight: 400; color: var(--ink-dim); line-height: 1.9; }}
  .dv-footer a {{ color: var(--green-light); text-decoration: none; }}
  @media (hover: none) {{
    .dv-card:hover {{ transform: none; }}
    .dv-btn-primary:active {{ transform: scale(.98); }}
  }}
</style>

<div class="dv-scope">
  <div class="dv-wrap">
    <header>
      <div class="dv-badge">
        <span class="dv-dot"></span> Disponível para aquisição
      </div>
      <h1 class="dv-domain">{dominio}<span class="dv-tld">{tld}</span></h1>
      <p class="dv-tagline">{tagline}</p>
      <div class="dv-cta">
        <a href="#dv-oferta" class="dv-btn dv-btn-primary">Fazer uma oferta</a>
        <a href="#dv-porque" class="dv-btn dv-btn-ghost">Por que este domínio?</a>
      </div>
      <div class="dv-trust">
        <div>
          <span class="dv-ic">⚡</span>
          <span class="dv-lbl">Transferência<br>em até 48h</span>
        </div>
        <div>
          <span class="dv-ic">🔒</span>
          <span class="dv-lbl">Pagamento<br>protegido</span>
        </div>
        <div>
          <span class="dv-ic">✓</span>
          <span class="dv-lbl">Registro.br<br>verificado</span>
        </div>
        <div>
          <span class="dv-ic">↺</span>
          <span class="dv-lbl">Suporte na<br>transferência</span>
        </div>
      </div>
    </header>

    <section id="dv-porque">
      <h2 class="dv-sec-title">Por que você deve ter esse domínio?</h2>
      <p class="dv-sec-sub">
        Um domínio só pertence a uma marca. Enquanto você decide, ele continua
        disponível para&nbsp;qualquer um.
      </p>
      <div class="dv-grid">
        {cards}
      </div>
    </section>

    <section id="dv-oferta">
      <div class="dv-offer">
        <h2>Faça uma oferta</h2>
        <p class="dv-sec-sub">
          Envie sua proposta para este domínio. Respondo em até 24 horas&nbsp;úteis.
        </p>
        <div class="dv-value">
          <div class="dv-value-lbl">Valor de mercado estimado</div>
          <div class="dv-value-num">{valor}</div>
          <div class="dv-scarcity">
            <span class="dv-dot"></span> Domínio único
          </div>
        </div>
        <form id="dvForm">
          <input type="hidden" name="access_key" value="{access_key}">
          <input type="hidden" name="subject" value="Nova oferta — {dominio_full}">
          <input type="hidden" name="from_name" value="Pagina de Venda de Dominio">
          <input type="checkbox" name="botcheck" style="display:none">
          <div class="dv-two">
            <div class="dv-field">
              <label>Nome</label>
              <input type="text" name="nome" required placeholder="Seu nome">
            </div>
            <div class="dv-field">
              <label>E-mail</label>
              <input type="email" name="email" required placeholder="voce@email.com">
            </div>
          </div>
          <div class="dv-field">
            <label>Sua oferta (R$)</label>
            <input type="text" name="oferta" placeholder="Ex.: {valor} ou faço proposta">
          </div>
          <div class="dv-field">
            <label>Mensagem (opcional)</label>
            <textarea name="msg" placeholder="Conte rapidamente sobre o seu projeto..."></textarea>
          </div>
          <button type="submit" class="dv-btn dv-btn-primary dv-submit" id="dvBtn">Enviar proposta</button>
          <p class="dv-note">Sem compromisso · seus dados não são&nbsp;compartilhados</p>
        </form>
        <div class="dv-result ok" id="dvOk">✓ Proposta enviada! Entrarei em contato em&nbsp;breve.</div>
        <div class="dv-result err" id="dvErr">Algo deu errado. Tente novamente ou escreva para&nbsp;contato@transferiragora.com.br</div>
      </div>
    </section>

    <footer class="dv-footer">
      <p>
        Negociação intermediada com segurança · Transferência via&nbsp;Registro.br<br>
        Contato: <a href="mailto:contato@transferiragora.com.br">contato@transferiragora.com.br</a> · WhatsApp disponível mediante&nbsp;contato
      </p>
    </footer>
  </div>
</div>

<script>
  (function () {{
    var form = document.getElementById('dvForm'),
        btn  = document.getElementById('dvBtn'),
        ok   = document.getElementById('dvOk'),
        err  = document.getElementById('dvErr');
    if (!form) return;
    form.addEventListener('submit', function (e) {{
      e.preventDefault();
      ok.style.display = 'none';
      err.style.display = 'none';
      btn.disabled = true;
      btn.textContent = 'Enviando...';
      fetch('https://api.web3forms.com/submit', {{
        method: 'POST',
        body: new FormData(form)
      }})
        .then(function (r) {{ return r.json(); }})
        .then(function (j) {{
          if (j.success) {{
            form.style.display = 'none';
            ok.style.display = 'block';
          }} else {{
            throw new Error(j.message || 'Falha');
          }}
        }})
        .catch(function () {{
          err.style.display = 'block';
          btn.disabled = false;
          btn.textContent = 'Enviar proposta';
        }});
    }});
  }})();
</script>
'''

CARD_TEMPLATE = '''        <div class="dv-card">
          <span class="dv-num">{num}</span>
          <h3>{titulo}</h3>
          <p>{texto}</p>
        </div>'''


def gerar_cards(cards):
    return "\n".join(CARD_TEMPLATE.format(num=n, titulo=t, texto=p) for n, t, p in cards)


def gerar_html(d):
    dominio_full = d["dominio"] + d["tld"]
    return TEMPLATE.format(
        dominio=d["dominio"],
        tld=d["tld"],
        dominio_full=dominio_full,
        tagline=d["tagline"],
        valor=d["valor"],
        cards=gerar_cards(d["cards"]),
        access_key=ACCESS_KEY,
    )


def main():
    base = os.path.join(os.path.dirname(__file__), "pages")
    os.makedirs(base, exist_ok=True)

    for d in DOMINIOS:
        pasta = os.path.join(base, d["slug"])
        os.makedirs(pasta, exist_ok=True)
        caminho = os.path.join(pasta, "index.html")
        with open(caminho, "w", encoding="utf-8") as f:
            f.write(gerar_html(d))
        print(f"✓ {d['dominio']}{d['tld']}  →  pages/{d['slug']}/index.html  ({d['valor']})")

    print(f"\n{len(DOMINIOS)} páginas geradas em ./pages/")


if __name__ == "__main__":
    main()
