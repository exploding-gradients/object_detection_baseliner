import glob
import ujson 
import os
import re
import sys

def write_json(readpath, grep_pattern="*.jpeg", write_metadata=True):
    """
    readpath: the location of the dataset. We expect to see jpegs and corresponding human annotations in a json file
    grep_pattern: "*.jpeg" pulls all jpegs in the first level. Do "*/*.jpeg" if your data is structured as "product_type"/"*.jpeg"
    write_metadata: Decorates each jpeg with available metadata. Expects each jpeg to have a -metadata.json
    """
    anns = []
    files = glob.glob('{}/{}'.format(readpath,grep_pattern))
    for f in files:
        f_dict = {"filepath": f}
        
        # get the corresponding annotations
        annpath = re.sub(".jpeg", "-annotation.json", f)
        if not os.path.exists("{}".format(annpath)):
            print("Warning: Annotation does not exist for {}".format(f))
            continue
        with open(annpath,'r') as af:
            f_dict["annotations"] = ujson.load(af)
            
        # get the corresponding metadata
        metapath = re.sub(".jpeg", "-metadata.json", f)
        if write_metadata and os.path.exists("{}".format(metapath)):
            with open(metapath, 'r') as mf:
                f_dict["metadata"] = ujson.load(mf)[0]
        anns.append(f_dict)
    return anns

