# ScavengerHunt
picoCTF2021 Scavenger Hunt

**Let this script find the flag for you.**

**Solutions** :\
**Flag 1**

hit `CTRL + U` on the index.html page to view the source.

```html
<!doctype html>
<html>
  <head>
    <title>Scavenger Hunt</title>
    <link href="https://fonts.googleapis.com/css?family=Open+Sans|Roboto" rel="stylesheet">
    <link rel="stylesheet" type="text/css" href="mycss.css">
    <script type="application/javascript" src="myjs.js"></script>
  </head>

  <body>
    <div class="container">
      <header>
		<h1>Just some boring HTML</h1>
      </header>

      <button class="tablink" onclick="openTab('tabintro', this, '#222')" id="defaultOpen">How</button>
      <button class="tablink" onclick="openTab('tababout', this, '#222')">What</button>

      <div id="tabintro" class="tabcontent">
		<h3>How</h3>
		<p>How do you like my website?</p>
      </div>

      <div id="tababout" class="tabcontent">
		<h3>What</h3>
		<p>I used these to make this site: <br/>
		  HTML <br/>
		  CSS <br/>
		  JS (JavaScript)
		</p>
	<!-- Here's the first part of the flag: picoCTF{t -->
      </div>

    </div>

  </body>
</html>
```
We can see the first part of the flag in the comment.
```html
<!-- Here's the first part of the flag: picoCTF{t -->
```
**Flag 2**\
We got the second part in the css file.

```css
/* CSS makes the page look nice, and yes, it also has part of the flag. Here's part 2: h4ts_4_l0 */
```
**Flag 3**\
Similarly, let's check the javascript file.

`/* How can I keep Google from indexing my website? */`\
There is no flag but we got a hint.
The common way to Stop Google from indexing is disallow those on the robots.txt file.

We got our third part and a hint at robots.txt
```
User-agent: *
Disallow: /index.html
# Part 3: t_0f_pl4c
# I think this is an apache server... can you Access the next flag?
```
**Flag 4**\
Well, an `.htaccess` file is a directory-level configuration file supported by several web servers, used for configuration of website-access issues, such as URL redirection, URL shortening, access control, and more.
The fourth part is in the `.htaccess` file.
```
# Part 4: 3s_2_lO0k
# I love making websites on my Mac, I can Store a lot of information there.
```
**Flag 5**\
The word 'srore' is mentioned in the hint.
On Mac OS there is a auto created file called .DS_Store
It's stores system configuration details.we can access that
We got our fifth part
```
Congrats! You completed the scavenger hunt. Part 5: _7a46d25d}
```
