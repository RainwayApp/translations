# translations
Translations for Rainway user interfaces. 

## Status
Check the status of our existing translations [here](https://rainway.com/translation-status)!

## How to contribute
Here's how to help us translate Rainway into your language:
1. [Create a GitHub account](https://github.com/join), if you haven't yet.
2. Download [`en-US.json`](https://raw.githubusercontent.com/RainwayApp/translations/master/src/en-US.json) to your computer.
3. Look up your [language's code](http://www.langtag.net/registries/lsr-language-utf8.txt) (and if necessary, your [region code](http://www.langtag.net/registries/lsr-region.txt)) and rename the file. For example, `is.json` is Icelandic; `ar-EG.json` is Arabic as spoken in Egypt.
4. Translate all the text in the file. Make sure the `{{template-names}}` and `<1>`tag numbers`</1>` are preserved. You can move them around to suit your language's grammar, but Rainway needs them to know where to insert variable text and formatting.
   > When translating something like `hours-played` and `hours-played_plural`, the right approach depends on your language's rules for plurals. You can use [this tool](https://jsfiddle.net/sm9wgLze) to verify which suffixes your language needs: type the language code into where it says _Enter a language code_ in the bottom-right box, then check the _Suffixes_ and _Sampling counts_ outputs.
   >
   > For example, a `ru` (Russian) translation might need three different translations, that inflect the word _ча́с_ (hour) three different ways: `hours-played_0` (for numbers ending in 0/5/6/7/8/9), `hours-played_1` (for numbers ending in 1) and `hours-played_2` (for numbers ending in 2/3/4). But a `ja` (Japanese) translation can just get rid of the `_plural` translation, because there are no plurals in Japanese.
   >
   > If this is confusing, don't worry too much about getting it right: we can probably help you figure it out once you submit your translation.
   
   You can also use the translation editor built into the Rainway Dashboard and Web Client. Open it from the language settings page, select the appropriate language and you can import a translation file you're currently working on and see your edits show up in the UI instantly. Your changes are saved to your account, so you can switch between the Dashboard and Web Client as you work. When you're done, just use the button to export back to JSON.
5. Go [here](https://github.com/RainwayApp/translations/tree/master/src) and click “Add file” → “Create new file”.
6. GitHub will show you an editor to paste your translation into. Don't forget the file name (`xx.json` or `xx-YY.json`)!
7. At the bottom of the page, click “Propose new file”, and then “Create pull request” on the next screen.
8. Write comments for us in the “Leave a comment” field, then confirm by clicking “Create pull request”.
9. Once we check and accept your work, your translation will be in Rainway.
