//bluecube.innerText = 'olololo';
//bluecube.onmousemove = function (event) {
//    this.style.background = 'red'
//};
//bluecube.onmouseleave = function (event) {
//    this.style.background = 'green'
//};
//http://127.0.0.1:8000/api/v1/teachers/


// -------------------------------- read -------------------------------------
let show_teachers = document.getElementById('show_teachers_button');
show_teachers.onclick = async function (event) {
    let response = await fetch('http://127.0.0.1:8000/api/v1/teachers/');
    response = await response.json();
    let teacherList = document.getElementById('teacher-list');
    teacherList.innerHTML = '';
    for(let i=0; i<response.length; i++) {
        let li = document.createElement('li');
        li.innerText = response[i].id + ' '
        + response[i].username + ' '
        + response[i].first_name + ' '
        + response[i].last_name + ' '
        + response[i].age;
        teacherList.appendChild(li);
    }
};
// -------------------------------- write -------------------------------------
document.getElementById('create_teacher_button').onclick = async function (event) {
    let newTeacher = {
        username: document.getElementById('new_teacher_username').value,
        first_name: document.getElementById('new_teacher_first_name').value,
        last_name: document.getElementById('new_teacher_last_name').value,
        email: document.getElementById('new_teacher_email').value,
        age: document.getElementById('new_teacher_age').value
    };
    let response = await fetch('http://127.0.0.1:8000/api/v1/teachers/', {
        method: 'POST',
        body: JSON.stringify(newTeacher),
        headers: {
            'Content-Type': 'application/json'
        }
    });
}
// -------------------------------- update -------------------------------------
document.getElementById('update_teachers_button').onclick = async function (event) {
    let teacher_id = document.getElementById('update_teacher_id').value;
    let teacher_url = 'http://127.0.0.1:8000/api/v1/teachers/' + teacher_id + "/";
    let updatedTeacher = {
        username: document.getElementById('update_teacher_username').value,
        first_name: document.getElementById('update_teacher_first_name').value,
        last_name: document.getElementById('update_teacher_last_name').value,
        email: document.getElementById('update_teacher_email').value,
        age: document.getElementById('update_teacher_age').value
    };
    let response = await fetch(teacher_url, {
        method: 'PUT',
        body: JSON.stringify(updatedTeacher),
        headers: {
            'Content-Type': 'application/json'
        }
    });
}
// -------------------------------- delete -------------------------------------
document.getElementById('delete_teachers_button').onclick = async function (event) {
    let teacher_id = document.getElementById('delete_teacher_id').value;
    let teacher_url = 'http://127.0.0.1:8000/api/v1/teachers/' + teacher_id + "/";
    let response = await fetch(teacher_url, {
        method: 'DELETE',
        body: JSON.stringify(teacher_id),
        headers: {
          'Content-Type': 'application/json'
        }
    });
};
