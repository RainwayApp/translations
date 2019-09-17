const leetspeak = require('leetspeak')
const toZalgo = require('to-zalgo')
const fs = require('fs')

const json = require('./en-US.json')
const speak = {}
const zalgo = {}
const paramRegex = /{{.*}}/
const tagRegex = /<.*>/

Object.entries(json).forEach(entry => {
    const [key, value] = entry
    speak[key] = value.split(' ').map(word =>
        (word.match(paramRegex) || word.match(tagRegex))
            ? word
            : leetspeak(word)).join(' ')

    zalgo[key] = value.split(' ').map(word =>
        (word.match(paramRegex) || word.match(tagRegex))
            ? word
            : toZalgo(word)).join(' ')
})

fs.writeFile('en-US-x-leet.json', JSON.stringify(speak), 'utf8', () => console.log('output to leetspeek.json'))
fs.writeFile('en-US-x-zalgo.json', JSON.stringify(zalgo), 'utf8', () => console.log('output to zalgo.json'))
