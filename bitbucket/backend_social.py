@csrf_exempt
def social_login(request):
    if request.method == 'POST':
        received_json_data=json.loads(request.body)
        code = received_json_data['code']
        client_id = received_json_data['client_id']
        redirect_uri = received_json_data['redirect_uri']
        secret = SocialApp.objects.values_list('secret',flat=True).get(provider="bitbucket_oauth2")

        # .objects.filter()
        # secret =''
        # for obj in secretobject:
        #     secret = obj.secret
        print("data",received_json_data)
        print('client_id',client_id)
        print("secret",secret)

        headers = {"Content-Type":"application/x-www-form-urlencoded"}
        data = {"grant_type":"authorization_code","code":code}
        response = requests.post("https://"+client_id+":"+secret+"@bitbucket.org/site/oauth2/access_token",headers=headers,data=data)
        content = response.content
        # content[redirect_uri] = redirect_uri
        print("content: ",content)
        return content
