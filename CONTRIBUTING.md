# Contributing
Thank you for wanting to contribute to Velvet Oblivion!
At this time, only select individuals are able to help with the main parts of the game, but submitting things in Issues still helps!

For those individuals,

## Before You Start

- Discuss major changes with the project owner before implementing them.

- Check existing GitHub Issues before starting new work.

- If you are unsure about something, ask before making changes.

- Be respectful of everyone's ideas and contributions.

## Branching Rules

- Never commit directly to main.

- Create a separate branch for each feature, fix, or contribution.

- Use semi-descriptive branch names.
### Examples:
```
feature/new-character

story/route-brainstorm

fix/dialogue-bug

assets/character-sprites
```

## Pull Requests

All changes MUST be submitted through a Pull Request (PR).
When opening a PR,
- Explain what you changed and why.

- Link any related GitHub Issues.

- List any important files that were added, removed, or modified.

- Wait for the project owner to review and approve the changes.
Again, **Do not merge your own Pull Requests into main.**
The project owner has final approval over changes merged into the main branch.

## Story and Writing Contributions
- Discuss significant plot changes before implementing them.
  
- Do not rewrite or delete existing story content without approval.
  
- Label new ideas, dialogue, character concepts, and route proposals clearly.

- Respect established character personalities and world-building.

## Code Contributions

- Keep changes focused on the task you are working on.
- Test your changes before submitting a PR.
- Do not commit API keys, passwords, private credentials, or other secrets.

## Art and Other Assets
- At the moment, assets used are being used as placeholders. Only contribute assets you created yourself or have permission to use.
- Include attribution and licensing information where required.
- Use consistent filenames and formats.

# Setup

## Before you start

You'll need:
- A **GitHub account** that's been invited to this repo (accept the invite from your email or github.com/notifications)
- **Git**: [[Download]](https://git-scm.com/downloads) (the default options in the installer are fine)
- **VS Code** (or any editor you like, but VS Code is highly recommended): [[Download]](https://code.visualstudio.com/)

> [!NOTE]
> If you are looking to work with the story building or any other note related part of the project, make sure to install Obsidian alongside these in order to edit some specific files. [[Download]](https://obsidian.md/)

> [!TIP]
> To check Git is working, open a terminal and run:
> ```bash
> git --version
> ```
> If it prints a version number, you're good.

## Getting set up

1. Open VS Code and press `Ctrl+Shift+P` (`Cmd+Shift+P` on Mac) to open the Command Palette
2. Type **Git: Clone** and press Enter
3. Paste this link and press Enter:
```
https://github.com/EnderBlaze7879/Velvet-Oblivion.git
```
4. Pick a folder on your computer to save the project in, then click **Open** when VS Code asks

> [!NOTE]
> VS Code will most likely ask you to sign in to GitHub, so make sure to do so!

## Create your branch

Never work directly on `master`. Please make your own branch first:
1. Click the branch name (it says `master`) in the **bottom-left corner** of VS Code
2. Choose **Create new branch...**
3. Type a name for the branch according to the branch name guidelines, and press Enter

## Making changes

1. Edit your files as normal and save them
2. Click the **Source Control** icon in the left sidebar or press `Ctrl+Shift+G`. Your changed files are listed here
3. Hover over **Changes** and click the **+** to stage everything. This will mark it to be saved
4. Type a short message about what you did to the code in the box at the top.
5. Click **Commit**.
6. Click **Publish Branch** to upload your branch to GitHub. After the first time doing this step, the button says **Sync Changes** instead.

## Staying up to date

If `master` has changed while you were working:

1. Press `Ctrl+Shift+P` and run **Git: Fetch**.
2. Press `Ctrl+Shift+P` again and run **Git: Merge Branch...**
3. Choose **origin/master**.

