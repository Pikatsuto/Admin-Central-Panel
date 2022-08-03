function updatemenu() {
    if (document.getElementById('responsive-menu').checked == true) {
        document.getElementById('menu').style.borderBottomRightRadius = '0';
        document.getElementById('menu').style.borderBottomLeftRadius = '0';
    }else{
        document.getElementById('menu').style.borderRadius = '10px';
    }
}

var showTogg = 0
var execTogg = []
var execTogg2 = []
var numTogg = 0

function onOffTogg(showBoxId, showBoxId1, maskBoxId, maskBoxId1, buttun) {
    if (showTogg === 0) {
        multiTogg(maskBoxId, maskBoxId1, false);
        showTogg ++
        document.getElementById(buttun).classList.add("is-show");
    }
    else if (showTogg === 1){
        multiTogg(maskBoxId, maskBoxId1, false);
        multiTogg(showBoxId, showBoxId1, false);
        showTogg ++
    }
    else if (showTogg >= 2){
        multiTogg(showBoxId, showBoxId1, false);
        showTogg = 0
        document.getElementById(buttun).classList.remove("is-show");
    };
};

function togg(showBoxId){

    for (let myClass of document.getElementsByClassName("showBoxClass")) {
        myClass.style.display = 'none';
    }

    document.getElementById(showBoxId).style.display = 'flex';
};

function offToggAll(){

    for (let id of execTogg2) {
        multiTogg(id, "site", true)
    }
    execTogg2 = []
    numTogg = 0
};

function multiTogg(showBoxId, showBoxId1, ifButtun){

    togg(showBoxId1)

    var isTogg = document.getElementById(showBoxId).style.display

    for (let myClass of document.getElementsByClassName("showClass")) {
        myClass.classList.remove("iframeFois4");
        myClass.classList.remove("iframeFois3");
        myClass.classList.remove("iframeFois2");
        myClass.classList.remove("inShowBoxClass");
    }

    if(isTogg == 'none'){
        if (numTogg < 4) {
            onTogg(showBoxId);
            numTogg ++
            execTogg2.push(showBoxId);
            if (ifButtun) {
                document.getElementById(showBoxId + "Menu").classList.add("is-show");
            }
        }
    }
    else {
        if (execTogg.indexOf(showBoxId) !== -1) {
            offTogg(showBoxId);
            numTogg --
            if (ifButtun) {
                document.getElementById(showBoxId + "Menu").classList.remove("is-show");
            }
        }
        else {
            if (numTogg < 4) {
                onTogg(showBoxId);
                execTogg.push(showBoxId);
                execTogg2.push(showBoxId);
                numTogg ++
                if (ifButtun) {
                    document.getElementById(showBoxId + "Menu").classList.add("is-show");
                }
            };
        };
    };

    if (numTogg == 0){
        document.getElementById("page").style.display = 'none';
    } else if (numTogg == 1){
        document.getElementById("page").style.display = 'block';
        for (let myClass of document.getElementsByClassName("showClass")) {
            myClass.classList.add("inShowBoxClass");
        }
    } else if (numTogg == 2){
        for (let myClass of document.getElementsByClassName("showClass")) {
            myClass.classList.add("iframeFois2");
        }
    } else if (numTogg == 3){
        for (let myClass of document.getElementsByClassName("showClass")) {
            myClass.classList.add("iframeFois3");
        }
    } else if (numTogg == 4){
        for (let myClass of document.getElementsByClassName("showClass")) {
            myClass.classList.add("iframeFois4");
        }
    }
};

function onTogg(showBoxId){
    document.getElementById(showBoxId).style.display = 'flex';
};

function offTogg(showBoxId){
    document.getElementById(showBoxId).style.display = 'none';
};