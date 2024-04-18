from rest_framework.decorators import api_view
from rest_framework.response import Response
from .api.serializers import UserSerializer
from rest_framework import status
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.authentication import SessionAuthentication, TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from .models import Image
from .api.serializers import ImageSerializer
import random
from django.db.models.signals import post_save
from django.dispatch import receiver
@api_view(['POST'])
def login(request):
    user = get_object_or_404(User, username=request.data['username'])
    if not user.check_password(request.data['password']):
        return Response("missing user")
    token, _ = Token.objects.get_or_create(user=user)
    serializer = UserSerializer(user)
    return Response({'token': token.key, 'user': serializer.data})
# @api_view(['POST'])
# def signup(request):
#     serializer = UserSerializer(data=request.data)
#     if serializer.is_valid():
#         serializer.save()
#         user = User.objects.get(username=request.data['username'])
#         user.set_password(request.data['password'])
#         user.save()
#         token = Token.objects.create(user=user)
#         return Response({'token': token.key, 'user': serializer.data})
#     return Response(serializer.errors, status=status.HTTP_200_OK)
@api_view(['POST'])
def signup(request):
    serializer = UserSerializer(data=request.data)
    if serializer.is_valid():
        user = serializer.save()
        user.set_password(request.data['password'])
        user.save()
        token = Token.objects.create(user=user)
        image_urls = [
            "https://res.cloudinary.com/dnmy80tpe/image/upload/v1713296870/wfwqchnkidel2tmr1ukw.png",
            "https://res.cloudinary.com/dnmy80tpe/image/upload/v1713296871/wjmilcylzsc60lmmlqpe.png",
            "https://res.cloudinary.com/dnmy80tpe/image/upload/v1713296872/nkzskbp6ce637jivrf2o.png",
            "https://res.cloudinary.com/dnmy80tpe/image/upload/v1713296873/vcisszysmr8ujqzol96w.png",
            "https://res.cloudinary.com/dnmy80tpe/image/upload/v1713296874/wkylbleuor6vw3yndwbh.png",
            "https://res.cloudinary.com/dnmy80tpe/image/upload/v1713296875/yhq3n8kudojp6izee2bz.png",
            "https://res.cloudinary.com/dnmy80tpe/image/upload/v1713296876/y6wc9k0zun4jpvw6krlu.png",
            "https://res.cloudinary.com/dnmy80tpe/image/upload/v1713296877/fevsx3yg56j756gnu3lg.png",
            "https://res.cloudinary.com/dnmy80tpe/image/upload/v1713296878/svwzom0fydmhba0v1xrs.png",
            "https://res.cloudinary.com/dnmy80tpe/image/upload/v1713296879/xly0jhlwb5jfj5btvavn.png",
            "https://res.cloudinary.com/dnmy80tpe/image/upload/v1713296880/vhbieq8xtxmtzn6f6zyv.png",
            "https://res.cloudinary.com/dnmy80tpe/image/upload/v1713296880/mxiteqm1owkcjo6w2v7a.png",
            "https://res.cloudinary.com/dnmy80tpe/image/upload/v1713296881/sm3f9wfjtkevpaiekhyy.png",
            "https://res.cloudinary.com/dnmy80tpe/image/upload/v1713296882/qvjqrvle5l5rr72jqasn.png",
            "https://res.cloudinary.com/dnmy80tpe/image/upload/v1713296883/rj0dqmoqbqopn1urk1cs.png",
            "https://res.cloudinary.com/dnmy80tpe/image/upload/v1713296884/pkdawc7mtuxkxu2k7tud.png",
            "https://res.cloudinary.com/dnmy80tpe/image/upload/v1713296884/asdicjwlxdbi1y4bnafp.png",
            "https://res.cloudinary.com/dnmy80tpe/image/upload/v1713296885/o0azzwraptct1k56loc9.png",
            "https://res.cloudinary.com/dnmy80tpe/image/upload/v1713296886/nokhbttbxxbtihbs9wjg.png",
            "https://res.cloudinary.com/dnmy80tpe/image/upload/v1713296886/nrka5opffsxq5mcdoyat.png",
        ]
        images_data = []
        for url in image_urls:
            image = Image.objects.create(
                user=user,
                urll=url,
                type=1,  # Assuming type is always 0
                generated=1,  # Assuming generated is always 1
                question1=None,  # Set other question fields as needed
                question2=None,
                question3=None,
                question4=None,
                grade=0
            )
            image.save()
            image_serializer = ImageSerializer(image)
            images_data.append(image_serializer.data)
        image_urls = [
            "https://res.cloudinary.com/dnmy80tpe/image/upload/v1713297284/ajhb1pdkdbcagfxvcdnb.png",
            "https://res.cloudinary.com/dnmy80tpe/image/upload/v1713297284/xcatf8xcuumsgizanzwi.png",
            "https://res.cloudinary.com/dnmy80tpe/image/upload/v1713297285/uy5mthlfmpqrbvrqafhj.png",
            "https://res.cloudinary.com/dnmy80tpe/image/upload/v1713297286/xwnlqajsyanzvtcmzw7m.png",
            "https://res.cloudinary.com/dnmy80tpe/image/upload/v1713297287/mt4szya80ufoda27od0v.png",
            "https://res.cloudinary.com/dnmy80tpe/image/upload/v1713297288/ytfyhgbvwfu1d0zgw4fi.png",
            "https://res.cloudinary.com/dnmy80tpe/image/upload/v1713297288/inc0dotftkauazrrwotl.png",
            "https://res.cloudinary.com/dnmy80tpe/image/upload/v1713297289/ddx3mthjjytgaebwaimu.png",
            "https://res.cloudinary.com/dnmy80tpe/image/upload/v1713297290/dcjglwcgsyzjhzcn3ark.png",
            "https://res.cloudinary.com/dnmy80tpe/image/upload/v1713297290/stcnclgyf7wjss7mihs7.png",
            "https://res.cloudinary.com/dnmy80tpe/image/upload/v1713297291/fzlrpa6hwygmoxk3succ.png",
            "https://res.cloudinary.com/dnmy80tpe/image/upload/v1713297292/xzq459zrwstbgcpja82e.png",
            "https://res.cloudinary.com/dnmy80tpe/image/upload/v1713297293/vvee6pa7uzjf0d7swhea.png",
            "https://res.cloudinary.com/dnmy80tpe/image/upload/v1713297293/hsclui8kfaezmabuqk0n.png",
            "https://res.cloudinary.com/dnmy80tpe/image/upload/v1713297294/fcqzax0shqubxzthnox3.png",
            "https://res.cloudinary.com/dnmy80tpe/image/upload/v1713297295/txzpafnkl3lceaqvm7ji.png",
            "https://res.cloudinary.com/dnmy80tpe/image/upload/v1713297296/gptklxudua1kw0xc18zs.png",
            "https://res.cloudinary.com/dnmy80tpe/image/upload/v1713297296/zeyhzb6pjzi4mjqvjek6.png",
            "https://res.cloudinary.com/dnmy80tpe/image/upload/v1713297297/xng2wvmqk0uqczzflied.png",
            "https://res.cloudinary.com/dnmy80tpe/image/upload/v1713297298/slgw3tvmglwblab4vvtt.png"
        ]
        for url in image_urls:
            image = Image.objects.create(
                user=user,
                urll=url,
                type=0,  # Assuming type is always 0
                generated=1,  # Assuming generated is always 1
                question1=None,  # Set other question fields as needed
                question2=None,
                question3=None,
                question4=None,
                grade=0
            )
            image.save()
            image_serializer = ImageSerializer(image)
            images_data.append(image_serializer.data)
        return Response({'token': token.key, 'user': serializer.data, 'images': images_data }, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
@api_view(['GET'])
@authentication_classes([SessionAuthentication, TokenAuthentication])
@permission_classes([IsAuthenticated])
def test_token(request):
    return Response(request.user.username)
@api_view(['POST'])
def createImage(request):
    try:
        userr = request.data.get('user')  # Assuming user_id is passed in the request
        user = User.objects.get(id=userr)  # Assuming you have a User model
        # images_data = []
        # image_urls = [
        #     "https://res.cloudinary.com/dnmy80tpe/image/upload/v1713297413/c8tx348nnvtgddl1izwi.jpg",
        #     # "https://res.cloudinary.com/dnmy80tpe/image/upload/v1713297414/pi3sluai0jtlvdalvmej.jpg",
        #     # "https://res.cloudinary.com/dnmy80tpe/image/upload/v1713297415/rgy8amqb9ylxbyxzusnu.jpg",
        #     # "https://res.cloudinary.com/dnmy80tpe/image/upload/v1713297415/ofonkw7hxz6r8m3hl4ys.jpg",
        #     # "https://res.cloudinary.com/dnmy80tpe/image/upload/v1713297416/fd2qjasmar4w59pxjrab.jpg",
        #     # "https://res.cloudinary.com/dnmy80tpe/image/upload/v1713297417/ozov0yailazhqxuoyozc.jpg",
        #     # "https://res.cloudinary.com/dnmy80tpe/image/upload/v1713297417/azkxr4ywmubewtpbfmil.jpg",
        #     # "https://res.cloudinary.com/dnmy80tpe/image/upload/v1713297418/s52zuobblfxyadc5cd1e.jpg",
        #     # "https://res.cloudinary.com/dnmy80tpe/image/upload/v1713297419/uw5qhbbnmw9q6ryybm9x.jpg",
        #     # "https://res.cloudinary.com/dnmy80tpe/image/upload/v1713297419/vs3qfqerqnwcfykwsd0r.jpg",
        #     # "https://res.cloudinary.com/dnmy80tpe/image/upload/v1713297420/gmhge8iyvettv4qsj0cp.jpg",
        #     # "https://res.cloudinary.com/dnmy80tpe/image/upload/v1713297421/omadqkkcw78ltf4jm4il.jpg",
        #     # "https://res.cloudinary.com/dnmy80tpe/image/upload/v1713297421/rx9abex9i8nukq3t42hz.jpg",
        #     # "https://res.cloudinary.com/dnmy80tpe/image/upload/v1713297422/qn74kkynngv996atewmz.jpg",
        #     # "https://res.cloudinary.com/dnmy80tpe/image/upload/v1713297423/uul6djfsgxskblhrat61.jpg",
        #     # "https://res.cloudinary.com/dnmy80tpe/image/upload/v1713297423/sp9m1vetvtoyhkwytgxz.jpg",
        #     # "https://res.cloudinary.com/dnmy80tpe/image/upload/v1713297424/ueo5w41om1ypk7jhx3hz.jpg",
        #     # "https://res.cloudinary.com/dnmy80tpe/image/upload/v1713297425/j8vzjcub3n3va3gs5pvu.jpg",
        #     # "https://res.cloudinary.com/dnmy80tpe/image/upload/v1713297426/y6sozredrlijf9jbrhe2.jpg",
        #     # "https://res.cloudinary.com/dnmy80tpe/image/upload/v1713297427/oyurfqckedpslzrpcx64.jpg"
        # ]
        # for url in image_urls:
        #     image = Image.objects.create(
        #         user=user,
        #         urll=url,
        #         type=1,
        #         generated=0,
        #         question1=None,
        #         question2=None,
        #         question3=None,
        #         question4=None,
        #         grade=0
        #     )
        #     image.save()
        #     image_serializer = ImageSerializer(image)
        #     images_data.append(image_serializer.data)
        # image_urls = [
        #     "https://res.cloudinary.com/dnmy80tpe/image/upload/v1713297515/hpdtmmzvd4qr6uyyad19.jpg",
        #     # "https://res.cloudinary.com/dnmy80tpe/image/upload/v1713297516/btmt4zrubwv6y9pzla0n.jpg",
        #     # "https://res.cloudinary.com/dnmy80tpe/image/upload/v1713297517/te2lxqlbc7xe9vdsw8uo.jpg",
        #     # "https://res.cloudinary.com/dnmy80tpe/image/upload/v1713297517/xidrjqldcdtqcgk5tz2d.jpg",
        #     # "https://res.cloudinary.com/dnmy80tpe/image/upload/v1713297518/uum01amdwjatddiadlcy.jpg",
        #     # "https://res.cloudinary.com/dnmy80tpe/image/upload/v1713297519/bipquhlcpxwtssllf3dj.jpg",
        #     # "https://res.cloudinary.com/dnmy80tpe/image/upload/v1713297520/o5xrn96azfhxn2twtude.jpg",
        #     # "https://res.cloudinary.com/dnmy80tpe/image/upload/v1713297520/oi2itoqqpmxtvnhoywip.jpg",
        #     # "https://res.cloudinary.com/dnmy80tpe/image/upload/v1713297521/k7gb4syzinmjri19dzic.jpg",
        #     # "https://res.cloudinary.com/dnmy80tpe/image/upload/v1713297522/kay76hpckkrcktw289lw.jpg",
        #     # "https://res.cloudinary.com/dnmy80tpe/image/upload/v1713297523/a9bvhtq2hdjkldqpgug9.jpg",
        #     # "https://res.cloudinary.com/dnmy80tpe/image/upload/v1713297523/s0m4lpu5xifkdhjswkkn.jpg",
        #     # "https://res.cloudinary.com/dnmy80tpe/image/upload/v1713297524/ncw3dzofjduhtxvpqozt.jpg",
        #     # "https://res.cloudinary.com/dnmy80tpe/image/upload/v1713297525/kvidj9or8j0dxbhf0i8y.jpg",
        #     # "https://res.cloudinary.com/dnmy80tpe/image/upload/v1713297526/pklf3ehraiezljb92q7k.jpg",
        #     # "https://res.cloudinary.com/dnmy80tpe/image/upload/v1713297528/ee9sefdkpqf9f0o3zwas.jpg",
        #     # "https://res.cloudinary.com/dnmy80tpe/image/upload/v1713297529/zbgjwijat54ivzaakqea.jpg",
        #     # "https://res.cloudinary.com/dnmy80tpe/image/upload/v1713297529/q4maklr2cwqt2rmqhcgx.jpg",
        #     # "https://res.cloudinary.com/dnmy80tpe/image/upload/v1713297530/phlpmlmdggad4iqkv63m.jpg",
        #     # "https://res.cloudinary.com/dnmy80tpe/image/upload/v1713297531/acmtvsn9j9i0115ffn0x.jpg"
        # ]
        # for url in image_urls:
        #     image = Image.objects.create(
        #         user=user,
        #         urll=url,
        #         type=0,
        #         generated=0,
        #         question1=None,
        #         question2=None,
        #         question3=None,
        #         question4=None,
        #         grade=0
        #     )
        #     image.save()
        #     image_serializer = ImageSerializer(image)
        #     images_data.append(image_serializer.data)

        return Response({'user': user }, status=status.HTTP_201_CREATED)
    except Exception as e:
        return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
@api_view(['POST'])
def userImages(request):
    if 'user_id' not in request.data:
        return Response({'error': 'User ID is required'}, status=status.HTTP_400_BAD_REQUEST)
    try:
        user = User.objects.get(id=request.data['user_id'])
    except User.DoesNotExist:
        return Response({'error': 'User not found'}, status=status.HTTP_404_NOT_FOUND)
    if not user.is_authenticated:
        return Response({'error': 'Authentication required'}, status=status.HTTP_401_UNAUTHORIZED)
    images = Image.objects.filter(user=user)
    shuffled_images = list(images)
    random.shuffle(shuffled_images)
    serializer = ImageSerializer(shuffled_images, many=True)    
    return Response(serializer.data, status=status.HTTP_200_OK)
@api_view(['PUT'])
def updateImage(request):
    try:
        image_id = request.data.get('id')
        user = request.data.get('user')
        image = Image.objects.get(id=image_id, user=user)
    except Image.DoesNotExist:
        return Response({'error': 'Image not founddd'}, status=status.HTTP_404_NOT_FOUND)
    if request.method == 'PUT':
        serializer = ImageSerializer(image, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)