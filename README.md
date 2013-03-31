# emmet-foundation

Emmet ( http://emmet.io/ ) extension for Zurb Foundation 4 ( http://foundation.zurb.com/ )

## Features
* Grid:
	* Sizes: large, small and large-small
	* Centered: large, small and large-small
* Block Grid: large, small and large-small

## How to use

### Grid

#### Row
d:r
&rarr;
```html
<div class="row"></div>
```
#### Small Columns
d:r>d:s2
&rarr;
```html
<div class="row">
	<div class="small-2 columns"></div>
</div>  
```
#### Large Columns
d:r>d:l4
&rarr;
```html
<div class="row">
	<div class="large-4 columns"></div>
</div>  
```
#### Small and Large Columns
d:r>d:s2l4
&rarr;
```html
<div class="row">
	<div class="small-2 large-4 columns"></div>
</div> 
```
#### Small Columns Centered
d:r>d:s2c
&rarr;
```html
<div class="row">
	<div class="small-2 small-centered columns"></div>
</div>  
```
#### Large Columns
d:r>d:l4c
&rarr;
```html
<div class="row">
	<div class="large-4 large-centered columns"></div>
</div>  
```
#### Small and Large Columns Centered
d:r>d:s2cl4c
&rarr;
```html
<div class="row">
	<div class="small-2 small-centered large-4 large-centered columns"></div>
</div> 
```
### Block Grid
#### Small Block Grid
u:s1
&rarr;
```html
<ul class="small-block-grid-1"></ul>
```
#### Large Block Grid
u:l4
&rarr;
```html
<ul class="large-block-grid-4"></ul>
```
#### Small and Large Block Grid
u:s1l4
&rarr;
```html
<ul class="small-block-grid-1 large-block-grid-4"></ul> 
```
#### Small and Large Block Grid with li
u:s1l4>li*4
&rarr;
```html
<ul class="small-block-grid-1 large-block-grid-4">
	<li></li>
	<li></li>
	<li></li>
	<li></li>
</ul> 
```
