'use strict'

var { default: satori } = require('satori');
var { Resvg } = require('@resvg/resvg-js');
var express = require('express');
var fs = require('fs');

express.urlencoded({ extended: true })

var app = express()
app.set('views', './views')
app.set('view engine', 'ejs')

app.use(express.static('public'));

const fontArrayBuffer = fs.readFileSync('./GenShinGothic-Bold.ttf').buffer;

async function renderOGPImage(title) {
    const svg = await satori(
        {
            type: 'div',
            props: {
                children: title,
                style: {
                    display: 'flex',
                    alignItems: 'center',
                    justifyContent: 'center',
                    width: '100%',
                    height: '100%',
                    padding: '4em',
                    color: 'black', backgroundColor: 'white',
                    fontSize: '3em',
                    background: "linear-gradient(lightblue, pink)"
                },
            },
        },
        {
            width: "1200px",
            height: "630px",
            fonts: [
                {
                    name: 'genshin-gothic-bold',
                    data: fontArrayBuffer,
                    weight: 400,
                    style: 'normal',
                },
            ],
        }
    );
    const renderer = new Resvg(svg, {
        fitTo: {
            mode: 'width',
            value: 1200,
        },
    })
    const buffer = await renderer.render();
    return buffer.asPng();
}

app.get('/ogp', async function (req, res) {
    try {
        const { title } = req.query;
        res.setHeader('Content-Type', 'image/png');
        res.send(await renderOGPImage(title));
    } catch (e) {
        console.error(e);
        res.status(500).send('Internal Server Error');
    }
});


const articleTitles = [
    'OGP（Open Graph Protocol）って何？知らないとヤバいですよ！',
    'NodeJSに使われていないか？使いこなすための現代NodeJS入門',
]


app.get('/article/:id', function (req, res) {
    try {
        const id = Number(req.params.id);
        if (id < 0 || id >= articleTitles.length) {
            res.status(404).send('Not Found');
            return;
        }

        res.render('article', {
            ogpimage: `https://${req.hostname}/ogp?title=${articleTitles[id]}`,
            title: articleTitles[id],
            content_path: `articles/${id}.ejs`,
        });
    } catch (e) {
        console.error(e);
        res.status(500).send('Internal Server Error');
    }
})

app.listen(3000);
console.log('Express started on port 3000');

