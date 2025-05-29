import requests

url = "https://airtable.com/v0.3/view/viwN3RMGptp84mfag/readSharedViewData?stringifiedObjectParams=%7B%22shouldUseNestedResponseFormat%22%3Atrue%7D&accessPolicy=%7B%22allowedActions%22%3A%5B%7B%22modelClassName%22%3A%22view%22%2C%22modelIdSelector%22%3A%22viwN3RMGptp84mfag%22%2C%22action%22%3A%22readSharedViewData%22%7D%2C%7B%22modelClassName%22%3A%22view%22%2C%22modelIdSelector%22%3A%22viwN3RMGptp84mfag%22%2C%22action%22%3A%22getMetadataForPrinting%22%7D%2C%7B%22modelClassName%22%3A%22view%22%2C%22modelIdSelector%22%3A%22viwN3RMGptp84mfag%22%2C%22action%22%3A%22readSignedAttachmentUrls%22%7D%2C%7B%22modelClassName%22%3A%22row%22%2C%22modelIdSelector%22%3A%22rows%20*%5BdisplayedInView%3DviwN3RMGptp84mfag%5D%22%2C%22action%22%3A%22createDocumentPreviewSession%22%7D%2C%7B%22modelClassName%22%3A%22view%22%2C%22modelIdSelector%22%3A%22viwN3RMGptp84mfag%22%2C%22action%22%3A%22downloadCsv%22%7D%2C%7B%22modelClassName%22%3A%22view%22%2C%22modelIdSelector%22%3A%22viwN3RMGptp84mfag%22%2C%22action%22%3A%22downloadICal%22%7D%2C%7B%22modelClassName%22%3A%22row%22%2C%22modelIdSelector%22%3A%22rows%20*%5BdisplayedInView%3DviwN3RMGptp84mfag%5D%22%2C%22action%22%3A%22downloadAttachment%22%7D%5D%2C%22shareId%22%3A%22shroKsHx3SdYYOzeh%22%2C%22applicationId%22%3A%22app1PaujS9zxVGUZ4%22%2C%22generationNumber%22%3A0%2C%22expires%22%3A%222025-06-19T00%3A00%3A00.000Z%22%2C%22signature%22%3A%221dfa86e01fd2a094e5fc44efd441955c420023307f1afd2448afcda703be714d%22%7D"

payload = {}
headers = {
  'accept': '*/*',
  'accept-language': 'en-US,en;q=0.9',
  'cache-control': 'no-cache',
  'dnt': '1',
  'x-airtable-application-id': 'app1PaujS9zxVGUZ4',
  'x-requested-with': 'XMLHttpRequest',
  'x-time-zone': 'Asia/Calcutta',
  'Cookie': 'AWSALBTG=+bfzZqspm8bJoBPw0fTts8wNaXL11hiGUeVPJSNYfao5qXCr794ZLCqz/v8hnvxo1LLOnZRae2G6kRSnEj5QJELQSqkECsEKfTFBW9ewftfksQuocwi2dCul+YYW9+4k2+AgbekExg+GWRZVHTdj5DWn3lWAS1T6bR5pdOms+VB13QHNWko=; AWSALBTGCORS=+bfzZqspm8bJoBPw0fTts8wNaXL11hiGUeVPJSNYfao5qXCr794ZLCqz/v8hnvxo1LLOnZRae2G6kRSnEj5QJELQSqkECsEKfTFBW9ewftfksQuocwi2dCul+YYW9+4k2+AgbekExg+GWRZVHTdj5DWn3lWAS1T6bR5pdOms+VB13QHNWko=; __Host-airtable-session=eyJzZXNzaW9uSWQiOiJzZXNyR2NUWFRhNmRzc3VOTyJ9; __Host-airtable-session.sig=06QUr5PknVPO9no-A0VOv9F3m630AP9ggByur8K2qy4; brw=brwOuBQlY60BSTezo; brwConsent=opt-in'
}

def get_response():
    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        data = response.json()
        return data
    except Exception as e:
        print("Error fetching or parsing data:", e)
        return []
      
