function login(){

    var email = document.getElementById("email").value
    document.getElementById("email").value = ""

    var senha = document.getElementById("senha").value
    document.getElementById("senha").value = ""


    eel.loginIQ(email, senha)(function(conStatus){
        console.log(conStatus)
        console.log(conStatus[1])
        document.getElementById("conectar").disabled = true
        document.getElementById("conectado").innerText = "Conectado"
        document.getElementById("saldo").innerText = "Seu saldo atual é R$ "+conStatus[1]
    })

}

function entraMHI2(){
    eel.mhi2()
}

function atualizaSaldo(){
    console.log("atualiza")
    eel.capturaSaldo()(function(saldoAtual){
        document.getElementById("conectado").innerText = "Seu saldo atual é R$ "+saldoAtual
    })
}