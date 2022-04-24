const searchField = document.querySelector("#searchField");
const emailResult = document.querySelector(".email_ajax_result");
const listAjax = document.querySelector(".list_ajax");
emailResult.style.display = "none";

const listDisplay = document.querySelector(".list_div");
const result = document.querySelector(".result");


searchField.addEventListener('keyup', function (e) {

    const searchValue = e.target.value;
    if (searchValue.trim().length > 0) {
        console.log('searchValue', searchValue);
        listAjax.innerHTML = " "
        fetch("/emails/search-email/", {
            body: JSON.stringify({searchText: searchValue}),
            method: "POST",
        })
            .then((res) => res.json())
            .then((data) => {
                console.log("data", data);

                listDisplay.style.display = "none";
                emailResult.style.display = "block";

                if (data.length === 0) {
                    emailResult.innerHTML = "No result!";
                } else {
                    emailResult.innerHTML = " "
                    data.forEach((item) => {
                        emailResult.style.display = "none"
                        listAjax.innerHTML +=

                            `<li>
                                        <a href="/emails/detail/" onclick="location.href=this.href+${item.email_id};return false;">
                                          from  ${item.user_id} : ${item.id} - ${item.created_date}
                                        </a>
                            </li>`

                    })
                }

            });

    } else {
        listAjax.innerHTML = " "
        emailResult.style.display = "none";
        listDisplay.style.display = "block";
    }

})