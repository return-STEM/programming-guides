# Return STEM Programming Guides

## Editing

Download [Obsidian](https://obsidian.md/) and open `guide/` as a vault.

For each course, go to `metadata.json` and find the `href` of the lesson you are writing. Create a markdown file called `{href}.md`. If your file needs resources (images, etc.), create a folder with the same name as your markdown file.

For example, if I'm writing *Control Structures: Conditionals* for *Intro to C++*, my folder structure will look like this:

```
guide/
    ...
    introcpp/
        ...
        conditionals/
            image1.png
        conditionals.md
        ...
        metadata.json
    ...
```

Therefore, your images in markdown will look like this:
```markdown
![](conditionals/image1.png)
```


# Known Issues
For block quotes, a blank line needs to be placed in between newlines for them to render as actual newlines:
**This is not consistent with obsidian!**

```markdown
Text

> First line
>
> Second line
>
> Third line
```
