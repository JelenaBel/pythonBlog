

<?php
session_start();


?>
<!DOCTYPE html>


<html>
<head>
<meta charset = "UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<link rel="stylesheet" href="CSSKasityoshop.css">
<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css">

<title>Handy shop</title>

</head>
<body>
    <div class = "mainHeader">

        <h1>Handy shop</h1>

        </div>

	<section class="sectionMenu">


<div  class="topnav" id="myTopnav">
	<a  href="index.php">
	Etusivu
</a>

<a  href="CatalogKasityoshop.php">
	Online-shop
</a>


<a  href="Myyjalle.php">
	Myyjälle
</a>

<a  href="Tietoa-meista.php">
	Meistä
</a>

<a href="Yhteytä.php">
	Yhteyttä
</a>
<a id = "rekisteroidu" href="Kirjaudu.php">
	Kirjaudu
	</a>
	<a href="javascript:void(0);" class="icon" onclick="myFunction()">
		<i class="fa fa-bars"></i>
	  </a>


	  <a class = "iLoveMyBasket" href = "ShoppingCard.php"><i class="fa fa-shopping-basket" style="font-size:25px;color:black; position: relative; padding-top: 0px; padding-left: 0px;" ></i></a>

      <?php
     if (isset($_SESSION['currentUserNameMyyjat'])) {
  echo "<a  href='AddProduct.php'>Add Product</a>";
  echo "<a href='OmaProfiliiniMyyja.php'>Oma Profiliini</a>";

}

if (isset ($_SESSION['currentUserName'])){
echo "<a href='OmaProfiliini.php'>Oma profiilini</a>";
echo "<a  href='Logout.php'> Logout </a>";
}


  ?>
</div>
<script>
	function myFunction() {
	  var x = document.getElementById("myTopnav");
	  if (x.className === "topnav") {
		x.className += " responsive";
	  } else {
		x.className = "topnav";
	  }
	}
	</script>

</section>

<a href="#" class="fa fa-facebook"></a>
<a href="#" class="fa fa-twitter"></a>

<br>
<span  class = "msgcurretnUserName">
            <?php
            if (isset($_SESSION['currentUserNameMyyjat'])) {

                  echo $_SESSION['currentUserNameMyyjat'];

                }

            ?>

</span>

<br><br>

	<br>
	<h2 class = "headerCatalog">Meidän uutiset</h2>



	<section class = "sectionUutiset">

		<div class = "uutisetBoxes">

	<article class= "uutisetFrontPage">

	<div class = "uutisetImage">
		<img class = "display-imgnews" src="Kyntiloita.jpg"  >
	</div>

	<div class = "uutisetBody">

	<h2 class= "titleUutiset"> Hyvää uutta vuotta! Uuden vuoden kunniaksi myymälöissämme upeita tarjouksia.    </h2><br>
    <h2 class= "titleUutiset"> 2.1.2016 </h2>

	</div>


</article>

<article class= "uutisetFrontPage">
	<div class = "uutisetImage">
		<img class = "display-imgnews" src="HomeDecorations.png"  >
	</div>


	 <div class = "uutisetBody">

	<h2 class= "titleUutiset">  Joulukukat edullisesti meiltä. Myymälöissämme myös kattava ja edullinen valikoima joulukuusia.</h2><br>
	<h2 class= "titleUutiset">  14.12.2015 </h2>

	</div>

</article>

	<article class= "uutisetFrontPage">
		<div class = "uutisetImage">
			<img class = "display-imgnews" src="ForKids.png"  >
		</div>

	 <div class = "uutisetBody">

	<h2 class= "titleUutiset"> Nyt on hyvä aika aloittaa puutarhan valmistelu talven lepokautta varten. Meiltä löydät kaikki työkalut ja tarvikkeet. </h2>
	<br><h2 class= "titleUutiset"> 1.9.2015 </h2>
</div>


</article>
</div>




</section>


</body>

</html>
