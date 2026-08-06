console.log("Student JS Loaded");

const music = new Audio("/assets/practice_app/sound/ping.mp3");

frappe.after_ajax(() => {

    $("body").append(`
        <button id="play"
            style="
                position: fixed;
                bottom: 20px;
                right: 20px;
                z-index: 9999;
                padding: 10px 20px;
                background: #0d6efd;
                color: white;
                border: none;
                border-radius: 6px;
                cursor: pointer;">
            ▶ Play Music
        </button>
    `);

    $("#play").click(function () {

        if (music.paused) {
            music.play();
            $(this).text("⏸ Pause Horn");
        } else {
            music.pause();
            $(this).text("▶ Play Horn");
        }

    });

});