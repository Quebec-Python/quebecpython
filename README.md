# Québec-Python

Québec-Python's website.

Built with [Pelican](http://getpelican.com)

## Dependencies

* <= Python 3.3
* See *requirements.txt* file for Pelican's dependencies.
* Node.js / NPM / Grunt for the theme

## Development environment setup

There are 2 ways to run our website on your machine:

### 1. The virtualenv way

    $ cd app
    $ virtualenv venv
    $ source venv/bin/activate
    $ pip install -r requirements.txt
    $ make devserver

Type [http://localhost:8000](http://localhost:8000) in your browser to see the website

### 2. The VirtualBox/Vagrant way when the virtualenv way fails

Install the [latest VirtualBox](https://www.virtualbox.org/) and [Vagrant](http://www.vagrantup.com/)

    # Then hop into the vagrant folder:
    $ cd vagrant
    $ vagrant up

    # Get into the VM by typing:
    $ vagrant ssh

    # You're now in the VM at /home/vagrant
    # Go into the folder where the project is
    $ cd quebecpython

    # Install Pelican's dependencies
    $ sudo pip install -r requirements.txt

    # Run the following command in the project's folder:
    $ make devserver

Type [http://localhost:8000](http://localhost:8000) in your browser to see the website

## FAQ

### How can I stop Pelican's webserver ?

You need to run the make script with the following option:

    $ make stopserver

### How can I add an article ?

1. Navigate in the *app/content* folder
2. Copy and paste the latest file there
3. Save the new file with a unexistent filename
4. Open that file and edit the metadata at the top
5. Start writing in Markdown below the metadata
6. Use the ```make devserver``` command to see how your article will look like

### How can I add/edit a page ?

1. Navigate in the *app/content/pages* folder
2. Follow the instructions for an article !

### How can I edit the theme ?

#### *static* folder

You need to install ```Grunt``` in the this folder for live ```LessCSS``` compilation & minification as you edit those ```less``` files.

Take a look at the ```themes/quebecpython/static/css/src/main.less``` file to see that it is
based on [Bootstrap](http://getbootstrap.com/) and [Bootswatch's Yeti theme](http://bootswatch.com/yeti/).

I only added a background image taken from [Subtlepatterns](http://subtlepatterns.com/) and a fixed sidebar.

#### *templates* folder

Templates in Pelican are based on [Jinja2](http://jinja.pocoo.org/docs/).

All html files here inherits from *base.html*:

<table>
    <thead>
        <tr>
            <th>Page</th>
            <th>Role</th>
            <th>Modification scope</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>base.html</td>
            <td>The base html file every other html file inherits from</td>
            <td>Global (ex: header, footer, sidebar)</td>
        </tr>
        <tr>
            <td>index.html</td>
            <td>The welcome page</td>
            <td>The articles list, the partners and sponsors at the bottom</td>
        </tr>
        <tr>
            <td>page.html</td>
            <td>A regular page html structure</td>
            <td>A regular page like *à propos* or *présentations*</td>
        </tr>
        <tr>
            <td>article.html</td>
            <td>An article html structure</td>
            <td>An article page</td>
        </tr>
    </tbody>
</table>
