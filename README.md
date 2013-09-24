# Non-interactive captcha proof-of-concept

## Description

A quick proof-of-concept for captcha-like system involving Javascript use but no user interaction at all.

It is intended to protect from automatic spambots and simple reverse-engineering techniques.

Its workflow is the following:
 1. Javascript requests token from API server.
 2. Javascript does some processing with the token (optional).
 3. Javascript sets some form field to the processed token which is then checked by server to be correct.

The strength of the approach depends on complexity of step 2.
It can be as simple as skipping the step and passing the obtained token unchanged to step 3 or as complex
as involving some custom-made cryptographic techniques to generate processed token.

If you write the second step to be complex and use obfuscation at the same time there are chances that
lazy attacker will not do enough reverse-engineering to understand the algorithm and implement it later in his bot.

The idea is a natural expansion of [honeypot](http://haacked.com/archive/2007/09/11/honeypot-captcha.aspx) or
[checkbox](http://uxmovement.com/forms/captchas-vs-spambots-why-the-checkbox-captcha-wins/) captcha alternatives.


## Installation

You need to have python and easy_install installed.
```bash
easy_install pyramid
```

## Running

```bash
./server.py
```

Open http://localhost:8080 in browser

## Usage

Python server exposes several locations:

* `/generate` -- generates some random token
* `/check/XXXXXXX/unencoded` -- checks if the token is correct. It matches the generated token with no additional processing.
* `/check/XXXXXXX` -- checks if the processed token is correct. The processing in the example is bitwise XOR with each character of the secret.

## Experimental status

This is solely proof of concept and should not be used in production.

I don't know Javascript/JQuery and have only a brief experience with Python so you probably should
not use my code as a reference in coding style but only as a proof of concept.

## License and author

* Author:: Timur Batyrshin <erthad@gmail.com>
* License:: MIT
