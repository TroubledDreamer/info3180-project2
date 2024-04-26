<script setup>
import { ref , onMounted } from 'vue';
let csrf_token = ref("");
let fetchResponse = ref("");
let fetchResponseType = ref("");

    



function getCsrfToken() {

    fetch("/api/v1/csrf-token")
    .then((response) => response.json())
    .then((data) => {
        console.log(data);
        csrf_token.value = data.csrf_token;
    })

}


onMounted(() => {
    getCsrfToken();
})


function Post() {
    let movieForm = document.getElementById('Post');
    let form_data = new FormData(PostForm);
    


    fetch("/api/v1/register", {
        method: "POST",
        body: form_data,
        headers: {
        'X-CSRFToken': csrf_token.value
        } 
    })

    .then(function(response) {
        return response.json();
    })

    .then(function(data) {
        console.log(data);
        fetchResponse.value = data
                    
        if(data.hasOwnProperty('errors')) {
                fetchResponseType.value = "danger"
            } else {
                fetchResponseType.value = "success"
            }

    })
    .catch(function(error) {
        console.log(error);
    });
}








</script>
