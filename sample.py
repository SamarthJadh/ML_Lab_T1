<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Landing page using html css</title>
    <link rel="stylesheet" href="style.css">
    <style>
        *{
            padding: 0;
            margin: 0;
            box-sizing: border-box;
        }
        header{
            width: 100%;
            height: 100vh;
            background:linear-gradient(rgba(0,0,0,0.8),rgba(0,0,0,0.2)) , url(12.jpg);
            background-size: cover;
            font-family: 'Poppins',sans-serif;
            position: relative;
        }
        .slider {
            width: 100%;
            height: 300px;
            background: #ccc;
            position: absolute;
            bottom: 0;
            left: 0;
        }
    </style>
</head>
<body>
    <header>
        <nav>
            <div class="logo">
                Shop Online
            </div>
            <div class="menu">
                <a href="#">Home</a>
                <a href="#">Products</a>
                <a href="#">Wishlist</a>
                <a href="#">Cart</a>
            </div>
            <div class="register">
                <a href="#">Sign in</a>
            </div>
        </nav>
        <section class="h-text">
            <span>Shop Well</span>
            <h1>Welcome to the World of Online Shopping...</h1>
            <br>
            <a href="#">Shop Now</a>
        </section>

        <div class="slider">
            <!-- Slider content goes here -->
        </div>
    </header>
</body>
</html>
