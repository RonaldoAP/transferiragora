<?php
// Shortcode para buscar HTML do repositório GitHub
// Uso: [transferir_html arquivo="index"] ou [transferir_html arquivo="dockpay"]

add_shortcode('transferir_html', function ($atts) {
    $atts = shortcode_atts(['arquivo' => 'index'], $atts);
    $arquivo = sanitize_key($atts['arquivo']);
    $cache_key = 'tia_html_' . $arquivo;

    $conteudo = get_transient($cache_key);

    if ($conteudo === false) {
        $branch = 'claude/relaxed-noether-wdt6h1';
        $repo   = 'RonaldoAP/transferiragora';

        if ($arquivo === 'index') {
            $url = "https://raw.githubusercontent.com/{$repo}/{$branch}/pages/index.html";
        } else {
            $url = "https://raw.githubusercontent.com/{$repo}/{$branch}/pages/{$arquivo}/index.html";
        }

        $resposta = wp_remote_get($url, ['timeout' => 10]);

        if (!is_wp_error($resposta) && wp_remote_retrieve_response_code($resposta) === 200) {
            $conteudo = wp_remote_retrieve_body($resposta);
            set_transient($cache_key, $conteudo, HOUR_IN_SECONDS);
        } else {
            $conteudo = '<p style="color:#ff8181;text-align:center">Erro ao carregar conteúdo.</p>';
        }
    }

    return $conteudo;
});

// Limpa cache de todos os arquivos (use em Tools > Code Snippets se precisar forçar atualização)
// Para limpar manualmente, descomente a linha abaixo, salve, depois comente de novo:
// add_action('init', function() { global $wpdb; $wpdb->query("DELETE FROM {$wpdb->options} WHERE option_name LIKE '_transient_tia_html_%'"); });
