var user = {
    name: "",
    id: "",
    password: ""
};


function checkInput() {
    if(!document.joinIn.name.value) 
    {
        window.alert("이름을 입력해주세요.");
        joinIn.name.focus();
    }
    else if(!document.joinIn.id.value) 
    {
        window.alert("아이디를 입력해주세요.");
        JoinIn.id.focus();
    }
    else if(!document.joinIn.password.value) 
    {
        window.alert("비밀번호를 입력해주세요.");
    }
    else if(document.joinIn.password.value.length < 8 || isNaN(password.value))
    {
        window.alert("비밀번호가 8자 미만입니다.");
    }
    else if(document.joinIn.password.value != document.joinIn.checkpw.value) 
    {
        window.alert("비밀번호를 확인해주세요.");
    }
    else 
    {
        user.name = document.querySelector('#name');
        user.id = document.querySelector('#id');
        user.password = document.querySelector('#password');
        console.log("name =", user.name);
        console.log("id =", user.id);
        console.log("password =", user.password);

        $.ajax({
            url: './msq.php',
            data: {
                userName: user.name,
                userId: user.id,
                userPw: user.password
            },
            type: "POST",
            dataType: "json",
            success: function(data){
                if(data.succ)
                	alert("로그인 성공");
                else
                    alert("로그인 실패");
            }, 
            error: function(err){
				alert(err);
            }
        });

        alert("회원가입이 완료되었습니다.");
    }
};



