<?php
// 1. Expõe _elementor_data e _elementor_edit_mode para a REST API
add_action('rest_api_init', function () {
    foreach (['_elementor_data', '_elementor_edit_mode'] as $key) {
        register_post_meta('page', $key, [
            'show_in_rest'  => true,
            'single'        => true,
            'type'          => 'string',
            'auth_callback' => '__return_true',
        ]);
    }
});

// 2. Shortcode que busca HTML do GitHub com cache de 1 hora
add_shortcode('transferir_html', function ($atts) {
    $atts    = shortcode_atts(['arquivo' => 'index'], $atts);
    $arquivo = sanitize_key($atts['arquivo']);
    $cache   = get_transient('tia_' . $arquivo);
    if ($cache === false) {
        $repo  = 'RonaldoAP/transferiragora';
        $branch = 'claude/relaxed-noether-wdt6h1';
        $url   = $arquivo === 'index'
            ? "https://raw.githubusercontent.com/{$repo}/{$branch}/pages/index.html"
            : "https://raw.githubusercontent.com/{$repo}/{$branch}/pages/{$arquivo}/index.html";
        $r     = wp_remote_get($url, ['timeout' => 10]);
        $cache = (!is_wp_error($r) && wp_remote_retrieve_response_code($r) === 200)
            ? wp_remote_retrieve_body($r)
            : '<p style="color:#f00">Erro ao carregar conteúdo.</p>';
        set_transient('tia_' . $arquivo, $cache, HOUR_IN_SECONDS);
    }
    return $cache;
});
