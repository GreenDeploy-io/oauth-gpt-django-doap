# OAuth Protected Endpoints for your custom GPT in OpenAI's GPT Store

| Attribute | Details         |
|-----------|-----------------|
| Author    | Kimsia          |
| Date      | 2023-12-10 Sunday |
| Version   | 0.0.1           |



## Table of Contents

- **[Why This?](#why-this)**
- **[Roadmap](#roadmap)**
  - **[Committed Plans](#committed-plans)**
  - **[Not Committed Plans](#not-committed-plans)**
- **[Footnotes](#footnotes)**


## Why This?

I created this GitHub repository to show how to implement the hello-world, canonical example of
implementing OAuth protected endpoints for custom GPTs in OpenAI's GPT Store.

This repository uses micro Django and DigitalOcean App Platform to implement.

For more details about the larger mission, check out the parent repository[^1] for this.

## Who is This For?

This is for people who meet all the requirements:

- You're already building custom GPT in OpenAI
- You're comfortable with Python code
- You're comfortable with experimenting with DigitalOcean
- You're comfortable with googling (or asking ChatGPT) how to setup Python virtual environment to
  test locally
- You can figure out how to install Postman on your machine.

## Stages of Progression

I will onboard you in stages. You cannot skip stages else it's very hard to troubleshoot.

1. You setup a OAuth protected endpoint locally using this repository and Postman as the client.
2. Same as Stage 1 except the OAuth protected endpoint is now on DigitalOcean.
3. Same as Stage 2 except you're using a test GPT as the client.


The objective of this repo is to get you to:

- have OAuth protected endpoints on DigitalOcean App Platform,
- have your test GPT call your endpoints correctly, and
- learn how to do basic troubleshooting


### Stage 1: Local OAuth protected endpoint with Postman as client

I'm sorry that I'm macOS-first. In future, I will make it convenient for Windows-based developers.

Linux developers, you're on your own. 😊

#### Stage 1 Steps

1. Create a new repo using this repo as template repo set it as private

Because then it's easier to know where you last stopped and you need to store some env secrets.

Best to keep your repo as private.

2. Make a separate branch from `main` and call it `develop`.

Easier to experiment if you keep your experiment on separate branch.

I expect to update `main` branch in future, so you can setup upstream to pull the latest changes
from this repo as well.

4. Download and install Postman if you haven't already done so on your machine.

Go to https://www.postman.com/downloads/

5. Setup a virtual environment for this Django installation.

This is a tricky step as different OS will have different sub-steps.

For macOS developers, follow the instructions under `.infrastructure/.macos/.venv-scripts/README.md`

For windows developers, stay patient. I will have one for you soon.

My early research shows me I have to use https://github.com/pyenv-win/pyenv-win


6. Install dependencies and make sure the django app can run hello world

I have compiled the whole thing as a loom video here.

[![Video Title or Description](https://link-to-your-screenshot.jpg)](https://www.loom.com/share/your-video-id)

7. Get a managed postgres database on DigitalOcean

[![DigitalOcean Referral Badge](https://web-platforms.sfo2.cdn.digitaloceanspaces.com/WWW/Badge%203.svg)](https://www.digitalocean.com/?refcode=1be9f5a28874&utm_campaign=Referral_Invite&utm_medium=Referral_Program&utm_source=badge)

Click on the above to get $200 credit over the next 60 days if you don't already have an account.

I have compiled the whole thing as a loom video here.

[![Video Title or Description](https://link-to-your-screenshot.jpg)](https://www.loom.com/share/your-video-id)

8. Update the .env with your database settings
9. Uncomment the database settings in `manage.py`




### Stage 2: OAuth protected endpoint on DigitalOcean App Platform with Postman as client

Once you have Stage 1 working, it's time to have your endpoints working on the internet.

#### Stage 2 Steps

1. Register an account with DigitalOcean

If you click on this, you will get $200 credit over the next 60 days.

[![DigitalOcean Referral Badge](https://web-platforms.sfo2.cdn.digitaloceanspaces.com/WWW/Badge%203.svg)](https://www.digitalocean.com/?refcode=1be9f5a28874&utm_campaign=Referral_Invite&utm_medium=Referral_Program&utm_source=badge)

Which is more than enough for an exercise.

2. If you already have an account, you need to setup two things: App, and Database.

Both are meant to be managed services by DigitalOcean.

In this demo, I will choose the absolute cheapest tier. Then, when you're done, you can just shut down. And you will only be charged on pro-rated costs.

I have compiled the whole thing as a loom video here.

[![Video Title or Description](https://link-to-your-screenshot.jpg)](https://www.loom.com/share/your-video-id)


### Stage 3: OAuth protected endpoint on DigitalOcean App Platform with custom GPT

1. Create your own GPT
2. Create your own privacy page using Termly
3. Add the OAuth protected endpoints to the GPT

I have compiled the whole thing as a loom video here.

[![Video Title or Description](https://link-to-your-screenshot.jpg)](https://www.loom.com/share/your-video-id)


## Todo

- [ ] Make Stage 1 Windows-friendly



I divide my roadmap into [committed plans](#committed-plans) and
[uncommitted plans](#not-committed-plans).

Both committed and un-committed plans do not come with a committed timeline.

They will be done when they are done. And in no particular order.

If you want to get updated, you can create a GitHub issue and tell me your preferred method of
getting updates. I am leaning towards a Substack for such purposes. Majority wins.

### Committed Plans

- [ ] A copy-and-paste, hello-world, canonical example[^2] using micro Django and DigitalOcean App
Platform to set up OAuth-protected endpoints for custom GPT.

- [ ] A Loom video tutorial on how to use micro Django and DigitalOcean App Platform to set up
OAuth-protected endpoints for custom GPT.

- [ ] A more polished and edited YouTube video tutorial on using micro Django and DigitalOcean App
Platform.

- [ ] A technology-agnostic guide outlining abstract principles, enabling developers to use other
technologies (like Laravel, TypeScript, etc.) and infrastructure providers (AWS, Heroku, etc.).

- [ ] A subscription option (likely a Substack) for updates on any OpenAI changes impacting the
implementation of OAuth-protected endpoints.

### Not Committed Plans

- A directory listing community projects that implement the canonical example using different
technologies and infrastructures.

## FAQs

1. Is this production-ready?

No, this is meant to demonstrate how to setup OAuth protected endpoints using actual cloud hosting.

But, it's not too hard to make a few changes to make this production ready.

Changes such as changing environmental variables like DEBUG from True to False, upgrading the DigitalOcean App Platform hosting resources, etc.

2. Any unit tests?

No. It's not on the roadmap as well.

But, if it's important to you, open an issue. I might bump it higher on my roadmap.

3. Why is your Django app just a single file?

I am most familiar with Django but its strength (being comprehensive) is also its weakness (looks 'heavy').

I found this O'Reilly chapter called The World's Smallest Django Project[^3]. It basically turns Django into a single python file.

I extended that for use here since this is meant to demonstrate a concept.

I call this way of making Django as lightweight as possible -- micro Django. I have a soft spot for rhymes. 😊


[^1]: [GreenDeploy-io/oauth-gpt: Resources and howto for making oauth for your custom gpt in OpenAI's GPT Builder (github.com)](https://github.com/GreenDeploy-io/oauth-gpt-django-doap) last commit on
2023-12-10 Sunday
[^2]: [Setting repository visibility - GitHub Docs](https://docs.github.com/en/repositories/managing-your-repositorys-settings-and-features/managing-repository-settings/setting-repository-visibility) last accessed on 2023-12-10 Sunday
[^3]: [1. The World’s Smallest Django Project - Lightweight Django [Book] (oreilly.com)](https://www.oreilly.com/library/view/lightweight-django/9781491946275/ch01.html) last accessed on 2023-12-10 Sunday

