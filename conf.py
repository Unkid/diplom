import configparser

 
def createConfig(path):
    """
    Create a config file
    """
    config = configparser.ConfigParser()
    config.add_section("Settings")
    config.set("Settings", "outpath", "output/")
    config.set("Settings", "format", "avi")
    config.set("Settings", "width","1000")
    config.set("Settings", "result","1")
    config.set("Settings", "name", "Y_m_d_H_M_S")
    config.set("Settings", "brightness", '0')
    config.set("Settings", "contrast", '1')
    
    with open(path, "w") as config_file:
        config.write(config_file)
 
 
if __name__ == "__main__":
    path = "settings.ini"
    createConfig(path)