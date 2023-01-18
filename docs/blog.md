
<script src="https://cdnjs.cloudflare.com/ajax/libs/showdown/2.1.0/showdown.min.js"></script>
<script>
    jsonPath = '/assets/posts/data.json'
    var blogPath = '/assets/posts'
    fetch(jsonPath)
    .then(response => response.json())
    .then(jsonData => {
        var converter = new showdown.Converter();
        //console.log(jsonData)
        jsonData.forEach(postJson => {
            fetch(`${blogPath}/${postJson.file}`)
            .then(response => {
                console.log("File contents received for file: " + postJson.file);
                return response.text();
            })
            .then(text => {
                var html = converter.makeHtml(text);
                //console.log("HTML generated: " + html);
                var postContainer = document.createElement("div");
                postContainer.setAttribute("class", "blog-class");
                postContainer.innerHTML = html;
                document.getElementById("blog-posts").appendChild(postContainer);
                //console.log("HTML added to the blog-posts container");

                let line = document.createElement("hr");
                postContainer.appendChild(line);

                let dataSpan = document.createElement("span");
                dataSpan.setAttribute("class", "blog-meta-class");
                let metaText = document.createTextNode(postJson.date + ", by " + postJson.author);
                dataSpan.appendChild(metaText);
                postContainer.appendChild(dataSpan);
            });
        });
    })
    .catch(error => {
        console.error('Error:', error);
    });
    
</script>

<div id="blog-posts"></div>
