const getNews = (word) => {
  try {
    fetch(
      `http://127.0.0.1:5000/news/${word}`
    )
      .then((res) => res.json())
      .then((response) => {
        let value = "";
        if (response.totalResults !== 0) {
          response.articles.forEach((data) => {
            console.log(data.emotions);
            value =
              value +
              `<a href="${data.url}"><div id="news">
                <p id="title">${data.title}</p>
                <p id="desc">${data.description}</p>
                <img id="img"
                    src="${data.urlToImage}"
                    alt="news image" >
            </div></a>`;
          });
        } else {
          alert("Data Not Found");
        }
        document.getElementById("news-container").innerHTML = value;
      });
  } catch (error) {
    var desc = document.getElementById("error");
    console.log(error);
    desc.innerHTML = "Something went wrong!";
    desc.style.color = "red";
  }
};
const search = () => {
  document.querySelector(".search").addEventListener("blur", (event) => {
    getNews(event.target.value);
  });
};
