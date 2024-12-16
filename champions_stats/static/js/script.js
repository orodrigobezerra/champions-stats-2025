// champions_stats/static/champions_stats/js/script.js

window.onload = function() {
  var ctx = document.getElementById('goalsChart').getContext('2d');

  var goalsChart = new Chart(ctx, {
      type: 'bar',
      data: {
          labels: ['Jogador 1', 'Jogador 2', 'Jogador 3'], // Nome dos jogadores
          datasets: [{
              label: 'Gols',
              data: [10, 5, 7], // Gols de cada jogador
              backgroundColor: 'rgba(0, 123, 255, 0.6)',
              borderColor: 'rgba(0, 123, 255, 1)',
              borderWidth: 1
          }]
      },
      options: {
          responsive: true,
          scales: {
              y: {
                  beginAtZero: true
              }
          }
      },
  });
}
