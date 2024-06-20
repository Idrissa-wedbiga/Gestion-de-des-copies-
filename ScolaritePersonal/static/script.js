document.addEventListener('DOMContentLoaded', function() {
    var matriculeField = document.getElementById('id_enseignant_matricule');
    var nomField = document.getElementById('id_enseignant_nom');
    var prenomField = document.getElementById('id_enseignant_prenom');

    matriculeField.addEventListener('blur', function() {
        var matricule = matriculeField.value;
        if (matricule) {
            fetch(`/get_enseignant_details/?matricule=${matricule}`)
                .then(response => response.json())
                .then(data => {
                    console.log(data);
                    if (data.error) {
                        alert(data.error);
                        nomField.value = '';
                        prenomField.value = '';
                    } else {
                        nomField.value = data.username;
                        prenomField.value = data.prenom;
                    }
                });
        } else {
            nomField.value = '';
            prenomField.value = '';
        }
    });
});
