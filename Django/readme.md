# Django Project
<h1>Django Project Setup Notes</h1>
<h2>Python and Virtual Environment</h2>
<div class="codehilite">
<pre><span></span><code>&gt;<span class="w"> </span>python<span class="w">
</span>--version
&gt;<span class="w"> </span>python<span class="w"> </span>-m<span class="w">
</span>venv<span class="w"> </span>env<span class="w"> </span>
<span class="c1"># -m ~ module</span>
<span class="c1"># venv ~ virtual env</span>
<span class="c1"># env ~ folder name</span>
<span class="c1"># To enable the virtualenv</span>
&gt;<span class="w"> </span>env<span class="se">\S</span>cripts<span
class="se">\a</span>ctivate.bat
<span class="c1"># or go inside env/scripts/activate to open virtualenv</span>
</code></pre>
</div>
<h2>Install Django</h2>
<div class="codehilite">
<pre><span></span><code>&gt;<span class="w"> </span>python<span class="w">
</span>-m<span class="w"> </span>pip<span class="w"> </span>install<span class="w">
</span>Django
&gt;<span class="w"> </span>django-admin<span class="w"> </span>--version
<span class="c1"># or</span>
&gt;<span class="w"> </span>pip<span class="w"> </span>list
</code></pre>
</div>
<h2>Create Project</h2>
<div class="codehilite">
<pre><span></span><code>&gt;<span class="w"> </span>django-admin<span class="w">
</span>startproject<span class="w"> </span>projectOne
&gt;<span class="w"> </span>python<span class="w"> </span>manage.py<span class="w">
</span>runserver
</code></pre>
</div>
<h2>Create Application</h2>
<div class="codehilite">
<pre><span></span><code>&gt;<span class="w"> </span>django-admin<span class="w">
</span>startapp<span class="w"> </span>appOne
</code></pre>
</div>
Django Project README
<p>In <code>settings.py</code>:
- Add <code>"appOne"</code> to <code>INSTALLED_APPS</code></p>
<h2>Views and URLs</h2>
<p>In <code>appOne/views.py</code>:</p>
<div class="codehilite">
<pre><span></span><code><span class="kn">from</span><span class="w"> </span><span
class="nn">django.http</span><span class="w"> </span><span class="kn">import</span>
<span class="n">HttpResponse</span>
<span class="k">def</span><span class="w"> </span><span
class="nf">LandingPage</span><span class="p">(</span><span class="n">request</span><span
class="p">):</span>
 <span class="k">return</span> <span class="n">HttpResponse</span><span
class="p">(</span><span class="s2">&quot;hello world&quot;</span><span
class="p">)</span>
</code></pre>
</div>
<p>In <code>appOne/urls.py</code>:</p>
<div class="codehilite">
<pre><span></span><code><span class="kn">from</span><span class="w"> </span><span
class="nn">django.urls</span><span class="w"> </span><span class="kn">import</span>
<span class="n">path</span>
<span class="kn">from</span><span class="w"> </span><span class="nn">.</span><span
class="w"> </span><span class="kn">import</span> <span class="n">views</span>
<span class="n">urlpatterns</span> <span class="o">=</span> <span class="p">[</span>
 <span class="n">path</span><span class="p">(</span><span
class="s1">&#39;LandingPage/&#39;</span><span class="p">,</span> <span
class="n">views</span><span class="o">.</span><span class="n">LandingPage</span><span
class="p">,</span> <span class="n">name</span><span class="o">=</span><span
class="s2">&quot;Landing Page&quot;</span><span class="p">)</span>
<span class="p">]</span>
</code></pre>
</div>
<p>In <code>projectOne/urls.py</code>:</p>
<div class="codehilite">
<pre><span></span><code><span class="kn">from</span><span class="w"> </span><span
class="nn">django.urls</span><span class="w"> </span><span class="kn">import</span>
<span class="n">include</span><span class="p">,</span> <span class="n">path</span>
<span class="n">urlpatterns</span> <span class="o">=</span> <span class="p">[</span>
 <span class="n">path</span><span class="p">(</span><span
class="s1">&#39;&#39;</span><span class="p">,</span> <span class="n">include</span><span
class="p">(</span><span class="s1">&#39;appOne.urls&#39;</span><span class="p">))</span>
Django Project README
<span class="p">]</span>
</code></pre>
</div>
<h2>Templates and Authentication</h2>
<p>To connect a file like <code>register.html</code> to <code>base.html</code>:</p>
<div class="codehilite">
<pre><span></span><code><span class="cp">{%</span> <span class="k">extends</span> <span
class="s2">&quot;base.html&quot;</span> <span class="cp">%}</span>
<span class="cp">{%</span> <span class="k">block</span> <span class="nv">content</span>
<span class="cp">%}</span>
<span class="x">&lt;div&gt;ABCD&lt;/div&gt;</span>
<span class="cp">{%</span> <span class="k">endblock</span> <span class="cp">%}</span>
</code></pre>
</div>
<p>Make a <code>registerView</code> function in <code>views.py</code> to render the
<code>register.html</code> template.<br />
Create a path in <code>urls.py</code> to execute the <code>registerView</code>
function.</p>
<h2>Creating Forms</h2>
<p>In <code>appOne/forms.py</code>:</p>
<div class="codehilite">
<pre><span></span><code><span class="kn">from</span><span class="w"> </span><span
class="nn">django</span><span class="w"> </span><span class="kn">import</span> <span
class="n">forms</span>
<span class="k">class</span><span class="w"> </span><span
class="nc">RegisterForm</span><span class="p">(</span><span class="n">forms</span><span
class="o">.</span><span class="n">ModelForm</span><span class="p">):</span>
 <span class="n">username</span> <span class="o">=</span> <span
class="n">forms</span><span class="o">.</span><span class="n">CharField</span><span
class="p">(</span><span class="n">max_length</span><span class="o">=</span><span
class="mi">20</span><span class="p">,</span> <span class="n">required</span><span
class="o">=</span><span class="kc">True</span><span class="p">)</span>
 <span class="n">email</span> <span class="o">=</span> <span
class="n">forms</span><span class="o">.</span><span class="n">EmailField</span><span
class="p">(</span><span class="n">max_length</span><span class="o">=</span><span
class="mi">40</span><span class="p">,</span> <span class="n">required</span><span
class="o">=</span><span class="kc">True</span><span class="p">)</span>
 <span class="n">password</span> <span class="o">=</span> <span
class="n">forms</span><span class="o">.</span><span class="n">CharField</span><span
class="p">(</span><span class="n">max_length</span><span class="o">=</span><span
class="mi">30</span><span class="p">,</span> <span class="n">required</span><span
class="o">=</span><span class="kc">True</span><span class="p">)</span>
 <span class="n">confirm_password</span> <span class="o">=</span> <span
class="n">forms</span><span class="o">.</span><span class="n">CharField</span><span
Django Project README
class="p">(</span><span class="n">max_length</span><span class="o">=</span><span
class="mi">30</span><span class="p">,</span> <span class="n">required</span><span
class="o">=</span><span class="kc">True</span><span class="p">)</span>
 <span class="k">class</span><span class="w"> </span><span
class="nc">Meta</span><span class="p">:</span>
 <span class="n">model</span> <span class="o">=</span> <span
class="n">Register</span>
 <span class="n">fields</span> <span class="o">=</span> <span
class="p">(</span><span class="s2">&quot;&quot;</span><span class="p">,)</span>
 <span class="k">def</span><span class="w"> </span><span class="nf">clean</span><span
class="p">(</span><span class="bp">self</span><span class="p">):</span>
 <span class="c1"># validate password match here</span>
 <span class="k">pass</span>
</code></pre>
</div>
<p>To use MySQL:</p>
<div class="codehilite">
<pre><span></span><code>&gt;<span class="w"> </span>python<span class="w">
</span>-m<span class="w"> </span>pip<span class="w"> </span>install<span class="w">
</span>mysqlclient
&gt;<span class="w"> </span>python<span class="w"> </span>manage.py<span class="w">
</span>makemigrations
</code></pre>
</div>
<h2>Login View Logic</h2>
<div class="codehilite">
<pre><span></span><code><span class="k">def</span><span class="w"> </span><span
class="nf">LoginPage</span><span class="p">(</span><span class="n">request</span><span
class="p">):</span>
 <span class="n">form</span> <span class="o">=</span> <span
class="n">LoginForm</span><span class="p">(</span><span class="n">request</span><span
class="o">.</span><span class="n">POST</span><span class="p">)</span>
 <span class="k">if</span> <span class="n">request</span><span
class="o">.</span><span class="n">method</span> <span class="o">==</span> <span
class="s2">&quot;POST&quot;</span><span class="p">:</span>
 <span class="n">form</span> <span class="o">=</span> <span
class="n">LoginForm</span><span class="p">(</span><span class="n">request</span><span
class="o">.</span><span class="n">POST</span><span class="p">)</span>
 <span class="k">if</span> <span class="n">form</span><span
class="o">.</span><span class="n">is_valid</span><span class="p">():</span>
 <span class="n">un</span> <span class="o">=</span> <span
class="n">form</span><span class="o">.</span><span class="n">cleaned_data</span><span
class="p">[</span><span class="s1">&#39;username&#39;</span><span class="p">]</span>
 <span class="n">pwd</span> <span class="o">=</span> <span
class="n">form</span><span class="o">.</span><span class="n">cleaned_data</span><span
Django Project README
class="p">[</span><span class="s1">&#39;password&#39;</span><span class="p">]</span>
 <span class="n">user</span> <span class="o">=</span> <span
class="n">authenticate</span><span class="p">(</span><span class="n">request</span><span
class="p">,</span> <span class="n">username</span><span class="o">=</span><span
class="n">un</span><span class="p">,</span> <span class="n">password</span><span
class="o">=</span><span class="n">pwd</span><span class="p">)</span>
 <span class="k">if</span> <span class="n">user</span> <span
class="ow">is</span> <span class="ow">not</span> <span class="kc">None</span><span
class="p">:</span>
 <span class="n">login</span><span class="p">(</span><span
class="n">request</span><span class="p">,</span> <span class="n">user</span><span
class="p">)</span>
 <span class="n">messages</span><span class="o">.</span><span
class="n">success</span><span class="p">(</span><span class="n">request</span><span
class="p">,</span> <span class="s1">&#39;Login Successful&#39;</span><span
class="p">)</span>
 <span class="k">return</span> <span class="n">redirect</span><span
class="p">(</span><span class="s1">&#39;dashboardPage&#39;</span><span
class="p">)</span>
 <span class="k">else</span><span class="p">:</span>
 <span class="n">messages</span><span class="o">.</span><span
class="n">warning</span><span class="p">(</span><span class="n">request</span><span
class="p">,</span> <span class="s1">&#39;Login Unsuccessful&#39;</span><span
class="p">)</span>
 <span class="k">return</span> <span class="n">render</span><span
class="p">(</span><span class="n">request</span><span class="p">,</span> <span
class="s1">&#39;login.html&#39;</span><span class="p">,</span> <span
class="p">{</span><span class="s1">&#39;form&#39;</span><span class="p">:</span> <span
class="n">form</span><span class="p">})</span>
 <span class="k">else</span><span class="p">:</span>
 <span class="k">return</span> <span class="n">render</span><span
class="p">(</span><span class="n">request</span><span class="p">,</span> <span
class="s1">&#39;login.html&#39;</span><span class="p">,</span> <span
class="p">{</span><span class="s1">&#39;form&#39;</span><span class="p">:</span> <span
class="n">form</span><span class="p">})</span>
 <span class="k">return</span> <span class="n">render</span><span
class="p">(</span><span class="n">request</span><span class="p">,</span> <span
class="s1">&#39;login.html&#39;</span><span class="p">,</span> <span
class="p">{</span><span class="s1">&#39;form&#39;</span><span class="p">:</span> <span
class="n">form</span><span class="p">})</span>
</code></pre>
</div>
<h2>Middleware Logic</h2>
<div class="codehilite">
<pre><span></span><code><span class="k">if</span> <span class="n">user</span><span
class="o">.</span><span class="n">is_authenticated</span> <span class="ow">and</span>
<span class="n">path</span> <span class="ow">in</span> <span class="p">[</span><span
class="n">reverse</span><span class="p">(</span><span
class="s1">&#39;login&#39;</span><span class="p">),</span> <span
Django Project README
class="n">reverse</span><span class="p">(</span><span
class="s1">&#39;register&#39;</span><span class="p">)]:</span>
 <span class="k">return</span> <span class="n">redirect</span><span
class="p">(</span><span class="s1">&#39;dashboard&#39;</span><span class="p">)</span>
<span class="n">protected_paths</span> <span class="o">=</span> <span
class="p">[</span><span class="n">reverse</span><span class="p">(</span><span
class="s1">&#39;dashboard&#39;</span><span class="p">)]</span>
<span class="k">if</span> <span class="ow">not</span> <span class="n">user</span><span
class="o">.</span><span class="n">is_authenticated</span> <span class="ow">and</span>
<span class="n">path</span> <span class="ow">in</span> <span
class="n">protected_paths</span><span class="p">:</span>
 <span class="k">return</span> <span class="n">redirect</span><span
class="p">(</span><span class="s1">&#39;home&#39;</span><span class="p">)</span>
<span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span
class="n">get_response</span><span class="p">(</span><span class="n">request</span><span
class="p">)</span>
</code></pre>
</div>