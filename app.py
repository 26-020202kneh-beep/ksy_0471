import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(
    page_title="2202 김태윤 오목 게임",
    page_icon="⚫",
    layout="centered"
)

html_code = """
<!DOCTYPE html>
<html lang="ko">
<head>
<meta charset="UTF-8">

<style>
* {
    box-sizing: border-box;
}

body {
    margin: 0;
    padding: 10px;
    font-family: Arial, "Malgun Gothic", sans-serif;
    background: #f5d76e;
}

.game {
    max-width: 700px;
    margin: auto;
    text-align: center;
}

h1 {
    margin: 10px 0 20px;
    color: #222;
}

.info {
    display: flex;
    justify-content: space-between;
    margin-bottom: 15px;
    font-weight: bold;
    font-size: 18px;
}

#board {
    width: 100%;
    max-width: 620px;
    height: auto;
    background: #dcb35c;
    border: 5px solid #5b3718;
    cursor: pointer;
}

button {
    margin-top: 20px;
    padding: 12px 25px;
    border: none;
    border-radius: 10px;
    background: #222;
    color: white;
    font-size: 17px;
    font-weight: bold;
    cursor: pointer;
}

button:hover {
    background: #555;
}

.rule {
    margin-top: 20px;
    padding: 15px;
    background: rgba(255,255,255,0.7);
    border-radius: 10px;
    text-align: left;
}

.rule h2 {
    text-align: center;
}

</style>
</head>

<body>

<div class="game">

<h1>⚫ 2202 김태윤 오목 게임 ⚪</h1>

<div class="info">
    <div id="turn">현재 차례: 흑돌 ⚫</div>
    <div id="status">게임 시작!</div>
</div>

<canvas id="board" width="620" height="620"></canvas>

<br>

<button onclick="restartGame()">🔄 다시 시작</button>

<div class="rule">
    <h2>게임 방법</h2>
    <p>⚫ 흑돌부터 시작합니다.</p>
    <p>⚪ 흑돌과 백돌을 번갈아 놓습니다.</p>
    <p>가로, 세로, 대각선으로 5개의 돌을 먼저 연결하면 승리합니다.</p>
</div>

</div>

<script>

const canvas = document.getElementById("board");
const ctx = canvas.getContext("2d");

const turnText = document.getElementById("turn");
const statusText = document.getElementById("status");

const SIZE = 15;
const CELL = canvas.width / SIZE;

let board;
let currentPlayer;
let gameOver;


// ======================
// 게임 초기화
// ======================

function restartGame() {

    board = [];

    for (let y = 0; y < SIZE; y++) {

        let row = [];

        for (let x = 0; x < SIZE; x++) {
            row.push(0);
        }

        board.push(row);
    }

    currentPlayer = 1;
    gameOver = false;

    turnText.textContent = "현재 차례: 흑돌 ⚫";
    statusText.textContent = "게임 시작!";

    drawBoard();
}


// ======================
// 바둑판 그리기
// ======================

function drawBoard() {

    ctx.clearRect(
        0,
        0,
        canvas.width,
        canvas.height
    );

    // 바둑판 배경
    ctx.fillStyle = "#dcb35c";

    ctx.fillRect(
        0,
        0,
        canvas.width,
        canvas.height
    );


    // 바둑판 선
    ctx.strokeStyle = "#513415";
    ctx.lineWidth = 1;


    for (let i = 0; i < SIZE; i++) {

        let p = (i + 0.5) * CELL;

        // 세로선
        ctx.beginPath();

        ctx.moveTo(
            p,
            CELL / 2
        );

        ctx.lineTo(
            p,
            canvas.height - CELL / 2
        );

        ctx.stroke();


        // 가로선
        ctx.beginPath();

        ctx.moveTo(
            CELL / 2,
            p
        );

        ctx.lineTo(
            canvas.width - CELL / 2,
            p
        );

        ctx.stroke();
    }


    // 화점
    drawStar(3, 3);
    drawStar(3, 11);
    drawStar(7, 7);
    drawStar(11, 3);
    drawStar(11, 11);


    // 돌
    for (let y = 0; y < SIZE; y++) {

        for (let x = 0; x < SIZE; x++) {

            if (board[y][x] !== 0) {

                drawStone(
                    x,
                    y,
                    board[y][x]
                );
            }
        }
    }
}


// ======================
// 화점
// ======================

function drawStar(x, y) {

    const px = (x + 0.5) * CELL;
    const py = (y + 0.5) * CELL;

    ctx.beginPath();

    ctx.arc(
        px,
        py,
        4,
        0,
        Math.PI * 2
    );

    ctx.fillStyle = "#222";
    ctx.fill();
}


// ======================
// 돌 그리기
// ======================

function drawStone(x, y, player) {

    const px = (x + 0.5) * CELL;
    const py = (y + 0.5) * CELL;

    const radius = CELL * 0.42;


    // 그림자
    ctx.beginPath();

    ctx.arc(
        px + 2,
        py + 2,
        radius,
        0,
        Math.PI * 2
    );

    ctx.fillStyle = "rgba(0,0,0,0.3)";
    ctx.fill();


    // 돌
    ctx.beginPath();

    ctx.arc(
        px,
        py,
        radius,
        0,
        Math.PI * 2
    );


    if (player === 1) {

        const gradient =
            ctx.createRadialGradient(
                px - 5,
                py - 5,
                2,
                px,
                py,
                radius
            );

        gradient.addColorStop(
            0,
            "#555"
        );

        gradient.addColorStop(
            1,
            "#000"
        );

        ctx.fillStyle = gradient;

    } else {

        const gradient =
            ctx.createRadialGradient(
                px - 5,
                py - 5,
                2,
                px,
                py,
                radius
            );

        gradient.addColorStop(
            0,
            "#ffffff"
        );

        gradient.addColorStop(
            1,
            "#cccccc"
        );

        ctx.fillStyle = gradient;
    }

    ctx.fill();

    ctx.strokeStyle = "#333";
    ctx.stroke();
}


// ======================
// 클릭
// ======================

canvas.addEventListener(
    "click",
    function(event) {

        if (gameOver) {
            return;
        }


        const rect =
            canvas.getBoundingClientRect();


        const scaleX =
            canvas.width / rect.width;

        const scaleY =
            canvas.height / rect.height;


        const mouseX =
            (event.clientX - rect.left)
            * scaleX;

        const mouseY =
            (event.clientY - rect.top)
            * scaleY;


        const x =
            Math.floor(mouseX / CELL);

        const y =
            Math.floor(mouseY / CELL);


        if (
            x < 0 ||
            x >= SIZE ||
            y < 0 ||
            y >= SIZE
        ) {
            return;
        }


        // 이미 돌이 있으면 무시
        if (board[y][x] !== 0) {
            return;
        }


        // 돌 놓기
        board[y][x] = currentPlayer;

        drawBoard();


        // 승리
        if (checkWin(x, y)) {

            gameOver = true;

            if (currentPlayer === 1) {

                turnText.textContent =
                    "⚫ 흑돌 승리!";

            } else {

                turnText.textContent =
                    "⚪ 백돌 승리!";
            }

            statusText.textContent =
                "🎉 게임 종료!";

            return;
        }


        // 무승부
        if (isDraw()) {

            gameOver = true;

            turnText.textContent =
                "🤝 무승부";

            statusText.textContent =
                "더 이상 놓을 곳이 없습니다.";

            return;
        }


        // 차례 변경
        if (currentPlayer === 1) {

            currentPlayer = 2;

            turnText.textContent =
                "현재 차례: 백돌 ⚪";

        } else {

            currentPlayer = 1;

            turnText.textContent =
                "현재 차례: 흑돌 ⚫";
        }

    }
);


// ======================
// 승리 판정
// ======================

function checkWin(x, y) {

    const directions = [

        [1, 0],   // 가로

        [0, 1],   // 세로

        [1, 1],   // 대각선

        [1, -1]   // 반대 대각선

    ];


    for (let direction of directions) {

        const dx = direction[0];
        const dy = direction[1];

        let count = 1;


        count += countStone(
            x,
            y,
            dx,
            dy
        );


        count += countStone(
            x,
            y,
            -dx,
            -dy
        );


        if (count >= 5) {
            return true;
        }
    }


    return false;
}


// ======================
// 같은 돌 개수 확인
// ======================

function countStone(
    x,
    y,
    dx,
    dy
) {

    let count = 0;

    let nx = x + dx;
    let ny = y + dy;


    while (

        nx >= 0 &&
        nx < SIZE &&
        ny >= 0 &&
        ny < SIZE &&
        board[ny][nx] === currentPlayer

    ) {

        count++;

        nx += dx;
        ny += dy;
    }


    return count;
}


// ======================
// 무승부
// ======================

function isDraw() {

    for (let y = 0; y < SIZE; y++) {

        for (let x = 0; x < SIZE; x++) {

            if (board[y][x] === 0) {
                return false;
            }
        }
    }

    return true;
}


// ======================
// 시작
// ======================

restartGame();

</script>

</body>
</html>
"""

st.title("⚫ 2202 김태윤 오목 게임")

components.html(
    html_code,
    height=900,
    scrolling=False
)
