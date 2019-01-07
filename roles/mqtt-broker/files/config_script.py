import json

def update_config(filename):
    config=json.loads(open(filename).read())
    plt_config = {
        'platform': 'mqtt',
        'name': 'mqtt',
        'url': 'tcp://localhost',
        'port': '1883',
        'topic_type': 'multiple',
        'topic_prefix': 'homebridge'
    }
    updated = False
    for i, acc in enumerate(config['platforms']):
        if acc['platform'] == 'mqtt':
            config['platforms'][i] = plt_config
            updated = True
    if not updated:
        config['platforms'].append(plt_config)
    f = open('config.json','w')
    f.write(json.dumps(config))
    f.close()

update_config('config.json')
print('successfully wrote config')
