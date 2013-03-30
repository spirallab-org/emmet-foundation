# emmet-foundation

Emmet ( http://emmet.io/ ) extension for Zurb Foundation 4 ( http://foundation.zurb.com/ )

## Features
* Grid: large, small and large-small
* Block Grid: large, small and large-small

## How to

### Grid

#### Row
<pre><code>
	d:r
	
	<div class="row"></div>
</code></pre>

#### Large Columns
<pre><code>
	d:r>d:l4
	
	<div class="row">
		<div class="large-4 columns"></div>
	</div>  
</code></pre>

#### Small Columns
<pre><code>
	d:r>d:s2
	
	<div class="row">
		<div class="small-2 columns"></div>
	</div>  
</code></pre>

#### Large and Small Columns
<pre><code>
	d:r>d:l4s2
	
	<div class="row">
		<div class="large-4 small-2 columns"></div>
	</div> 
</code></pre>

### Block Grid
#### Large Block Grid
<pre><code>
	u:l4
	
	<ul class="large-block-grid-4"></ul>
</code></pre>

#### Small Block Grid
<pre><code>
	u:s1
	
	<ul class="small-block-grid-1"></ul>
</code></pre>

#### Large and Small Block Grid
<pre><code>
	u:l4s1
	
	<ul class="large-block-grid-4 small-block-grid-1"></ul> 
</code></pre>

#### Large and Small Block Grid with li
<pre><code>
	u:l4s1>li*4
	
	<ul class="large-block-grid-4 small-block-grid-1">
		<li></li>
		<li></li>
		<li></li>
		<li></li>
	</ul> 
</code></pre>
