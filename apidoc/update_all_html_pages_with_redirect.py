from glob import glob

html_content = \
"""
<h1>This page has been moved!</h1>
<h3>Redirecting you to <a href="https://developers.arcgis.com/python/api-reference/">developers.arcgis.com</a>.</h3>
<p>If you are not automatically redirected, click <a id="dynamic-redirect-link" href="https://developers.arcgis.com/python/api-reference/">here</a>.</p>
<script>
// Assemble the link
var currPathName = window.location.pathname;
var relPathNameFromRoot = currPathName.split("/html/")[1] + window.location.hash;
var newDomainRoot = "http://developers.arcgis.com/python/api-reference/"
var newAddress = newDomainRoot + relPathNameFromRoot;

var el = document.getElementById("dynamic-redirect-link");
if(el){
    el.href = newAddress;}
window.location.href = newAddress; //this will automatically bring us to the new page
</script>
"""

for path in glob("./html/**/*.html", recursive=True):
    with open(path, "w") as f:
        f.write(html_content)
