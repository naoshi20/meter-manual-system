let questions = document.getElementsByClassName("questionBox");
for (let i = 1; i < questions.length; i++) {
    questions[i].classList.add("inactive");
}

let solutions = document.getElementsByClassName("solutionBox");
for (let i = 0; i < solutions.length; i++) {
    solutions[i].classList.add("inactive");
}

let sendButton = document.getElementsByClassName("sendButton")[0];
sendButton.classList.add("inactive");

let works = {};
const valueChange = (event) => {
    // 履歴として表示するための文を作成
    let text;
    text =
        "質問" +
        event.currentTarget.name +
        "の回答は" +
        event.currentTarget.value +
        "です";
    console.log(text);

    // 履歴を表示
    const history = document.createElement("p");
    const history_content = document.createTextNode(text);
    history.appendChild(history_content);
    const history_box = document.getElementById("history_box");
    history_box.appendChild(history);

    // デバッグ用に質問と回答の組みや解決策をコンソール上に表示
    works[event.currentTarget.name] = event.currentTarget.value;
    console.log(works);

    // 現在表示している質問を非表示
    let currentQuestion = document.getElementById(
        "question_" + event.currentTarget.name
    );
    currentQuestion.classList.add("inactive");

    // 次に表示したい質問を表示
    // 次の質問があり、解決策はない場合、次の質問を表示
    if (
        event.currentTarget.dataset.nextquestion != -1 &&
        event.currentTarget.dataset.nextsolution == -1
    ) {
        let nextQuestion = document.getElementById(
            "question_" + event.currentTarget.dataset.nextquestion
        );
        nextQuestion.classList.remove("inactive");
    }
    // 次の質問がなく、解決策はがある場合、次の解決策を表示
    else if (
        event.currentTarget.dataset.nextquestion == -1 &&
        event.currentTarget.dataset.nextsolution != -1
    ) {
        let nextSolution = document.getElementById(
            "solution_" + event.currentTarget.dataset.nextsolution
        );
        nextSolution.classList.remove("inactive");
        sendButton.classList.remove("inactive");

        works["solution"] = event.currentTarget.dataset.nextsolution;
        console.log(works);

        // 解決策として表示するための文を作成
        let text;
        text =
            "解決策は" +
            nextSolution.getAttribute("data-solutionname") +
            "です";
        console.log(text);

        // 解決策を表示
        const history = document.createElement("p");
        const history_content = document.createTextNode(text);
        history.appendChild(history_content);
        const history_box = document.getElementById("history_box");
        history_box.appendChild(history);
    }
    // その他の場合はデータ不整合
    else {
        console.log("データが正しく登録されていない可能性があります。");
    }
};

// 全てのラジオボタンにイベントリスナーを追加
const radioButtons = document.getElementsByClassName("radioButton");
for (let i = 0; i < radioButtons.length; i++) {
    radioButtons[i].addEventListener("change", valueChange, true);
}
