// champions_stats/static/champions_stats/js/script.js

document.addEventListener('DOMContentLoaded', function() {
    const audio = document.getElementById('background-music');
    const playButton = document.getElementById('play-button');

    // Verifica se a música já foi tocada anteriormente
    if (sessionStorage.getItem('audioPlayed')) {
        audio.currentTime = sessionStorage.getItem('audioCurrentTime') || 0;
        if (sessionStorage.getItem('audioPlaying') === 'true') {
            audio.play();  // Continua tocando automaticamente ao mudar de página
            playButton.textContent = 'Mute';
        } else {
            playButton.textContent = 'UEFA Champions League Theme';
        }
    }

    // Controle de play/pause
    playButton.addEventListener('click', function() {
        if (audio.paused) {
            audio.play().catch((error) => {
                console.error("Falha ao tocar a música:", error);
            });
            playButton.textContent = 'Mute';
            sessionStorage.setItem('audioPlaying', 'true'); // Marca que a música está tocando
        } else {
            audio.pause();
            playButton.textContent = 'UEFA Champions League Theme';
            sessionStorage.setItem('audioPlaying', 'false'); // Marca que a música foi pausada
        }
    });

    // Atualiza o tempo da música ao longo da reprodução
    audio.ontimeupdate = function() {
        sessionStorage.setItem('audioCurrentTime', audio.currentTime);
    };

    // Marca que a música foi tocada quando o usuário clicar para iniciar
    audio.onplay = function() {
        sessionStorage.setItem('audioPlayed', 'true');
    };
});
