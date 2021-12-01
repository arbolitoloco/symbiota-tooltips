<!-- 
  1. Include the DocsUtilities class
  2. Output $relFilePath variable using getFilePath method
  3. Make sure page includes the title of the page as the first available h1 inside #innertext (it will be tagged by JS to add a page-level tooltip whenever available in the API)
 -->

<?php
include_once('../../config/symbini.php');
include_once($SERVER_ROOT.'/classes/DocsUtilities.php');
header("Content-Type: text/html; charset=".$CHARSET);

$docs = new DocsUtilities();
$relFilePath = $docs->getFilePath(__FILE__, $SERVER_ROOT);
?>
<html>
 <head>...</head>

  <body>
    <?php
    $displayLeftMenu = (isset($taxa_admin_taxonomydisplayMenu)?$taxa_admin_taxonomydisplayMenu:'false');
    include($SERVER_ROOT.'/includes/header.php');
    ?>
    <div class="navpath">
      <a href="../../index.php">Home</a> &gt;&gt;
      <a href="taxonomydisplay.php"><b>Taxonomic Tree Viewer</b></a>
    </div>
    <!-- This is inner text! -->
    <div id="innertext">
      ...
      <div>
        <?php '<h1>Title of Page</h1>' ?>
      ...
  </body>

</html>