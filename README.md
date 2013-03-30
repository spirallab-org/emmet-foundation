# emmet-foundation

Emmet ( http://emmet.io/ ) extension for Zurb Foundation 4 ( http://foundation.zurb.com/ )

## Features
* Grid: large, small and large-small
* Block Grid: large, small and large-small

## How to

### Grid

#### Row
d:r
&rarr;
```html
<div class="row"></div>
```

#### Large Columns
d:r>d:l4
&rarr;
```html
<div class="row">
	<div class="large-4 columns"></div>
</div>  
```
#### Small Columns
d:r>d:s2
&rarr;
```html
<div class="row">
	<div class="small-2 columns"></div>
</div>  
```
#### Large and Small Columns
d:r>d:l4s2
&rarr;
```html
<div class="row">
	<div class="large-4 small-2 columns"></div>
</div> 
```
### Block Grid
#### Large Block Grid
u:l4
&rarr;
```html
<ul class="large-block-grid-4"></ul>
```
#### Small Block Grid
u:s1
&rarr;
```html
<ul class="small-block-grid-1"></ul>
```
#### Large and Small Block Grid
u:l4s1
&rarr;
```html
<ul class="large-block-grid-4 small-block-grid-1"></ul> 
```
#### Large and Small Block Grid with li
u:l4s1>li*4
&rarr;
```html
<ul class="large-block-grid-4 small-block-grid-1">
	<li></li>
	<li></li>
	<li></li>
	<li></li>
</ul> 
```
