# A Website for Sol

## Initial Setup

### Getting the Code

Open up a Terminal application and navigate whichever folder you want to
store the *folder with the code for the site*. Please note that a separate
folder will be created as a result of running this download command:

```sh
git clone https://github.com/marlago/website.git
```

After you have downloaded the code for the site, go to the folder where you
have it using your favorite Terminal application.
The rest of this guide assumes you are in this folder in your Terminal.

### Setting up a Conda environment.

Use conda to recreate the environment. This is needed so as to cleanly separate
the python version you have running on your system (we don't want to mess with that!)
from the python version and modules that your site needs to compile.

```sh
conda env create -f conda_environment.yml
```

Now whenver you want to work on your site, use the following command to activate
the environment:

```sh
source activate sol_site
```

Another benefit of this setup aside from separating it from your OS python is
that you shouldn't ever need to bother with figuring out which packages to
install. All the settings are loaded automatically with the environment which
you can recreate anytime from `conda_environment.yml`.
Whenever you are done for the day, you can either close the terminal or run
the following command to deactivate the website environment.

```sh
source deactivate
```

### Building the Site for the First Time

Note that when you download this repo for the first time you will only have
the source files for the site, so we have to build it before we can see it locally.
We use a program called [Fabric](http://www.fabfile.org/)
(or `fab` in the terminal) to build the site. We will also use it for any other
maintenance-related tasks.

In the root folder for this repo run the following:

```sh
fab build
```

## Development

There are several things we need to start developing with this server.
First, we need the conda environment to be activated and the site
has to be built (see above).

If a pull request has been recently merged on the github website, the files on the local computer should be updated first by doing:

```sh
git pull origin master
```

Then we need to make sure our changes are tracked in real time and our updates
to the site can be seen simply by reloading it. This can be achieved with the following command:

```sh
fab rebuild && fab regenerate
```

Last but not least, we need to start up a basic web server that will make our
files accessible to web browsers like Firefox and Google Chrome.

First, open a a new terminal tab or window (but still in the root of this project). After activating the website environment again in the next tab, run the following command:

```sh
fab serve
```

This should print something to the effect of `Serving on port NNN`, where `NNN`
is most likely `8000` (but could differ!).
Provided this ran with no hiccups you can go to <http://localhost:8000> and
rejoice (hopefully!) at the sight of your site!


## Writing Content

A collection of tips/FAQ that deal with various challenges you'll run into when
writing new pages or posts.

### Blog Post Dates

If you publish a blogpost without specifying a date, Pelican will just use the date
your file was last modified as the post date. This is fragile and can lead to entries
appearing as "published" much later than they actually were, simply because the
corresponding text file was modified for whatever reason.

It is thus best to manually specify the date of your post.
In Markdown, make sure the meta-data of your post (the stuff on top of the file
enclosed in `---`, like `Title`, etc) contains the following line:
```
Date: YYYY-MM-DD
```
You could also include a time if you happen to be publishing two articles in
one day, but it's not needed otherwise.

In RST, according to
[Pelican Documentation](http://docs.getpelican.com/en/3.6.3/content.html#file-metadata)
you'd need to write this to add a date to a post:
```
:date: YYYY-MM-DD
```
Note the colons, they are important to include!

It is possible that the date format described above is not the only one
understood by Pelican. However, this we know to work and there was no time
to test others at the moment. Maybe we'll get to it later.

### Embedding Images in Markdown

Use the following syntax to embed an image in your markdown posts:

```
![alt_text]({filename}/images/name_of_image.jpg){:align="left"}
```

Note that `alt_text` can be any text and that you can replace "left" with "right"
for the `align` property. If you don't want to specify any alignment at all,
just drop everything in the curly brackets.
