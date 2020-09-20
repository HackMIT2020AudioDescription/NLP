import requests
import json

DENSE_CAP_API_KEY= "d946d749-f736-4643-b27f-502661cb7b7f"

def get_captions(path):
    r = requests.post( "https://api.deepai.org/api/densecap",
        files={
            'image': open(path, 'rb'),
            #'image':'https://cdnph.upi.com/svc/sv/upi/5711585753629/2020/1/8a65ca6bc7a15003a9b698a5d7788d0b/Wimbledon-tennis-tournament-canceled-2021-dates-announced.jpg'
        },
        headers={'api-key': DENSE_CAP_API_KEY})
    
    result=r.json()
    picture_captions=set()
    #print(result['output']['captions'])
    for caption_dict in result['output']['captions']:
        if caption_dict['confidence']>0.9:
            picture_captions.add(caption_dict['caption'])
    picture_captions_li=list(picture_captions)

    for i in range(len(picture_captions_li)):
        for j in range(i+1,len(picture_captions_li)):
            str1=picture_captions_li[i]
            str2=picture_captions_li[j]
            if get_jaccard_sim(str1, str2) >0.4:
                picture_captions.remove(str1)

    captions_str= ", ".join(picture_captions)
    res= "Captions: {}".format(captions_str)
    #print(res)
    return res


def get_jaccard_sim(str1, str2): 
    a = set(str1.split()) 
    b = set(str2.split())
    c = a.intersection(b)
    return float(len(c)) / (len(a) + len(b) - len(c))


captions_set= get_captions()
print(captions_set)