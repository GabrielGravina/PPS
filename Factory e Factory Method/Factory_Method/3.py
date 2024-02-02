from abc import ABC

class ConfigReader(ABC):
    def read_config(self, file_path):
        pass

class JSONConfigReader(ConfigReader):
    def read_config(self, file_path):
        print(f"Lendo configuração do arquivo JSON: {file_path}")

class XMLConfigReader(ConfigReader):
    def read_config(self, file_path):
        print(f"Lendo configuração do arquivo XML: {file_path}")

class YAMLConfigReader(ConfigReader):
    def read_config(self, file_path):
        print(f"Lendo configuração do arquivo YAML: {file_path}")

class ConfigReaderFactory(ABC):
    def create_reader(self):
        pass

class JSONConfigReaderFactory(ConfigReaderFactory):
    def create_reader(self):
        return JSONConfigReader()

class XMLConfigReaderFactory(ConfigReaderFactory):
    def create_reader(self):
        return XMLConfigReader()

class YAMLConfigReaderFactory(ConfigReaderFactory):
    def create_reader(self):
        return YAMLConfigReader()

class ConfigurationManager:
    def __init__(self, config_reader_factory):
        self.config_reader = config_reader_factory.create_reader()

    def load_config(self, file_path):
        self.config_reader.read_config(file_path)

if __name__ == "__main__":
    json_reader_factory = JSONConfigReaderFactory()
    xml_reader_factory = XMLConfigReaderFactory()
    yaml_reader_factory = YAMLConfigReaderFactory()

    config_manager_json = ConfigurationManager(json_reader_factory)
    config_manager_xml = ConfigurationManager(xml_reader_factory)
    config_manager_yaml = ConfigurationManager(yaml_reader_factory)

    config_manager_json.load_config("config.json")
    config_manager_xml.load_config("config.xml")
    config_manager_yaml.load_config("config.yaml")
