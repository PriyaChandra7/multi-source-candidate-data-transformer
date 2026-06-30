import json

def load_config(config_path):

    with open(config_path, "r") as file:
        config = json.load(file)

    return config

def project_profile(candidate, config):
        output = {}
        for field in config["fields"]:

          output_name = field["path"]

          source = field.get("from", output_name)
        
          if source.endswith("[0]"):

            key = source[:-3]

            if key in candidate and candidate[key]:

              output[output_name] = candidate[key][0]

            else:

              output[output_name] = None
          else:

            output[output_name] = candidate.get(source)

        if config["include_confidence"]:

         output["overall_confidence"] = candidate["overall_confidence"]

        return output
        
        
