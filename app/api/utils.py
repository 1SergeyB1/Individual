def config_parser(config_path):
    with open('config.txt','r') as config_file:
        config = dict()
        lines = config_file.readlines()
        for line in lines:
            k, v = line.split(' = ')
            config[k] = v.removesuffix('\n')
        return  config
