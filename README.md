# Artur Rios - Personal Blog

> [!NOTE]
> This is the real, open-source code of personal-blog. Its home is Forgejo, at
> https://git.techcraftsmen.net/artur-rios/personal-blog; the copy on GitHub is a read-only mirror, for viewing only, and
> its issues and pull requests are not followed. If you want to contribute, email me at
> arturdev@duck.com.

This is the repository of my personal blog, published at **<https://blog.artur-rios.tech/>**. Built with
[Hugo](https://gohugo.io/), using the theme [Rusty Typewriter](https://github.com/artur-rios/hugo-theme-rusty-typewriter).  
The comment section is powered by [Giscus](https://giscus.app/).

> **Where this lives:** the repository is at <https://git.techcraftsmen.net/artur-rios/personal-blog>. The GitHub
> repository is a read-only mirror of it.

## Running it locally

Requires Hugo **extended** 0.158 or later.

The theme is not a submodule: the image fetches it, pinned by commit in the [`Dockerfile`](Dockerfile). To run Hugo on
your machine, clone it into `themes/rusty-typewriter` at that commit (the folder is git-ignored). Without the theme Hugo
builds an empty site.

```sh
git clone https://git.techcraftsmen.net/artur-rios/personal-blog.git
cd personal-blog
git clone https://github.com/artur-rios/hugo-theme-rusty-typewriter.git themes/rusty-typewriter
git -C themes/rusty-typewriter checkout a7d91728156fc3d7bb0ab5d401efc940f5e1b187
hugo server
```

## Deploy

Pushing to `main` deploys the blog: [yggdrasil](https://git.techcraftsmen.net/artur-rios/yggdrasil) builds the
`Dockerfile` and serves it with [static-web-server](https://static-web-server.net/) at `blog.artur-rios.tech`. Hugo's
`baseURL` comes from the address the image is built for (from `PUBLIC_HOST` and `PUBLIC_PATH`, root-relative when they are empty), so `hugo.toml` sets none. To try the image:

```sh
docker build --tag personal-blog .
docker run --rm -p 8080:8080 personal-blog
```

To use another theme commit, set `RUSTY_TYPEWRITER_COMMIT` in the `Dockerfile`.
