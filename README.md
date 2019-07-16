# translations
Repository of language translation files for the Rainway Client and Dashboard.

# How to contribute
Know a second language? We need your help! Here's how to help us translate Rainway into your language:
1. Fork this repository.
2. Clone your copy to your computer.
3. Copy the `en.json` file in the `src` directory and rename it to your own language's language or locale code.
4. Change the "en" in the file to your language or locale code and get started translating the english strings contained within into your target language. Ensure that the double-bracketed `{{templates}}` are preserved as they are, as they'll be filled in with language agnostic information on the app-side. Put them in the correct place for your language's grammatical structure, but don't change their contents.
5. When you're finished, make a pull request back to this repository with your changes. Once it's accepted, the new language file will be deployed to our server and will be made available to the Rainway Client and Dashboard. 