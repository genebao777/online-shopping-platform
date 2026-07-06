<?php
/*
Plugin Name: Cloud Chatbot Embed
Description: 自動在 WordPress 前端載入 AI 客服小幫手
Version: 1.0
*/
add_action('wp_footer', function() {
    ?>
    <script>
        console.log("Cloud Chatbot Loaded.");
    </script>
    <?php
});
