function click_show() {
    let sm_btn = document.querySelectorAll('[id="show_more_btn"]');
    for (let i = 0; i < sm_btn.length; i++) {
        let number = i;
        sm_btn[i].addEventListener(
        'click',
        function show() {
            let about_book = document.querySelectorAll('[id=about_book]');
            if (about_book[number].style.display == 'none') {
              about_book[number].style.display = "block";
            }
            else {
                about_book[number].style.display = "none";
            }
        });
    }
}

click_show()
