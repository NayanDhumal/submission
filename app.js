document.getElementById('searchButton').addEventListener('click', () => {
    const city = document.getElementById('city').value;
    const apiKey = 'YOUR_API_KEY'; // 
    const url = `https://api.openweathermap.org/data/2.5/weather?q=${city}&appid=${api}&units=metric`;

    fetch(url)
        .then(response => response.json())
        .then(data => {
            
            document.getElementById('cityName').innerText = `Weather in ${data.name}`;
            document.getElementById('description').innerText = data.weather[0].description;
            document.getElementById('temperature').innerText = `Temperature: ${data.main.temp}°C`;
            document.getElementById('humidity').innerText = `Humidity: ${data.main.humidity}%`;
        })
        .catch(error => {
            console.error('Error fetching weather data:', error);
            alert('City not found. Please try again.');
        });
});
