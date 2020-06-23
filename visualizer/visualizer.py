import json

def translation_keys(translation):
    return {k.split('_')[0] for k in translation.keys()}

def generate_table_rows(max_missing_keys_shown = 10):
    with open('../src/key.json') as f:
        languages = json.load(f)

    with open('../src/en-US.json') as f:
        en_us_keys = translation_keys(json.load(f))

    rows = []
    for l in languages:
        code = l['value']
        name = l['title']
        with open('../src/%s.json' % code) as f:
            translated_keys = translation_keys(json.load(f))
        missing_keys = en_us_keys - translated_keys
        missing_excerpt = ', '.join(sorted(missing_keys)[:max_missing_keys_shown]) + (', …' if len(missing_keys) > max_missing_keys_shown else '')
        rows.append((code, name, len(translated_keys), missing_excerpt))

    # Sort by translated keys, descending.
    rows.sort(key=lambda x: -x[2])

    return rows

def generate_html():
    print(r'''<!doctype html><html lang="en">
    <head>
        <meta charset="utf-8">
        <title>Rainway translation progress</title>
        <link href="https://fonts.googleapis.com/css?family=Lato:400,700" rel="stylesheet" type="text/css">
        <link rel="stylesheet" href="https://indestructibletype.com/fonts/Jost.css" type="text/css" charset="utf-8" />
        <style>
            a { color: #029aeb; }
            body { font-family: Lato, sans-serif; background-color: #050311; color: #F5F4FC; max-width: 750px; margin-left: auto; margin-right: auto; }
            h1 { font-family: Jost, sans-serif; }
            h1, h1+p { text-align: center; }
            table { border-collapse: collapse; }
            td, th { padding: 2px 8px; border-bottom: 1px solid #FFFFFF40; }
            td:nth-child(1) { width: 4em; font-family: 'DejaVu Sans Mono', 'Monaco', 'Consolas', monospace; }
            td:nth-child(3) { width: 100px; }
            td:nth-child(4) { font-size: 75%; opacity: 75%; }
        </style>
    </head>
    <body>
        <h1>Rainway translation progress</h1>
        <p>You can <a href="https://github.com/RainwayApp/translations">help translate Rainway</a> on GitHub.</p>
        <table>
        <thead><th>Code</th><th>Language</th><th>Completion</th><th>Missing keys</th></thead>
        <tbody>''')

    rows = generate_table_rows()
    total_key_count = rows[0][2]
    for row in rows:
        code, name, key_count, missing_keys = row
        percentage = key_count / total_key_count * 100
        print(
            f'<tr><td>{code}</td><td>{name}</td>'
            f'<td style="background:linear-gradient(90deg, #2F2D83 0%, #2F2D83 {percentage}%, #FFFFFF00 {percentage}%, #FFFFFF00 100%)">'
            f'{key_count} / {total_key_count}</td>'
            f'<td>{missing_keys}</tr>'
        )

    print(r'''</tbody>
        </table>
    </body>
</html>''')

if __name__ == '__main__':
    generate_html()
