document.getElementById("uploadForm").addEventListener("submit", async function (event){
    event.preventDefault()

    const fileInput = document.getElementById("pdfFiles")
    const files = fileInput.files

    if (files.length > 5) {
        alert("Por favor, selecione no maximo 5 arquivos do tipo PDF!")
        return
    }

    const formData = new FormData()
    for (let i = 0; i < files.length; i++){
        formData.append("pdfFiles", files[i])
    }

    try {
        const response = await fetch("/upload/pdfs", {
            method : "POST",
            body : formData
        })

        const result = await response.json()
        alert(`${result.message}`)
        fileInput.value = ""
    }
    catch (error){
        alert(`${error.message}`)
    }
})