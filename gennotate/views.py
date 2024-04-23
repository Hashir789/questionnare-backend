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
# from django.db.models.signals import post_save
# from django.dispatch import receiver
# import csv
# from django.http import HttpResponse
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
        images_data = []
        image_urls = [
            "https://res.cloudinary.com/dnmy80tpe/image/upload/v1713889094/ajx6juf4fquc5jnrqb4d.jpg",
            "https://res.cloudinary.com/dnmy80tpe/image/upload/v1713889095/b5su61lbdpzjwh2tqqij.jpg",
            "https://res.cloudinary.com/dnmy80tpe/image/upload/v1713889096/xelazmrqzeveqox6xxp8.jpg",
            "https://res.cloudinary.com/dnmy80tpe/image/upload/v1713889097/fpafqzzyqarqyfe3g0tp.jpg",
            "https://res.cloudinary.com/dnmy80tpe/image/upload/v1713889098/mvyvqx5knwaiwjqrp3op.jpg",
            "https://res.cloudinary.com/dnmy80tpe/image/upload/v1713889098/kahuvezng1qibqxrsjij.jpg",
            "https://res.cloudinary.com/dnmy80tpe/image/upload/v1713889099/htj0fiqz6ndc0nxerx49.jpg",
            "https://res.cloudinary.com/dnmy80tpe/image/upload/v1713889101/rogikpczo5hrcqs30afp.jpg",
            "https://res.cloudinary.com/dnmy80tpe/image/upload/v1713889102/qkrtbk35jcuqnl6himd5.jpg",
            "https://res.cloudinary.com/dnmy80tpe/image/upload/v1713889103/rjvd7di3chzeofnot4aa.jpg",
            "https://res.cloudinary.com/dnmy80tpe/image/upload/v1713889104/mbawwpxpyju7usgpznby.jpg",
            "https://res.cloudinary.com/dnmy80tpe/image/upload/v1713889104/o5bxvntj0ohgnbfzhaaj.jpg",
            "https://res.cloudinary.com/dnmy80tpe/image/upload/v1713889105/ks3zbsxguuoulv7rl3co.jpg",
            "https://res.cloudinary.com/dnmy80tpe/image/upload/v1713889106/mspuq1hqqdnx23vdx12z.jpg",
            "https://res.cloudinary.com/dnmy80tpe/image/upload/v1713889107/y8xhpyznn4rb2g3xzq0y.jpg",
            "https://res.cloudinary.com/dnmy80tpe/image/upload/v1713889107/syxuknfastpzl0llmaex.jpg",
            "https://res.cloudinary.com/dnmy80tpe/image/upload/v1713889108/tget9geb35l3rvunozeu.jpg",
            "https://res.cloudinary.com/dnmy80tpe/image/upload/v1713889109/ezbbitih8rnudiolecmm.jpg",
            "https://res.cloudinary.com/dnmy80tpe/image/upload/v1713889110/ikccputraynlmmfufjqf.jpg",
            "https://res.cloudinary.com/dnmy80tpe/image/upload/v1713889111/s8smvvcolxmq0qne3vfq.jpg",

        ]
        for url in image_urls:
            image = Image.objects.create(
                user=user,
                urll=url,
                type=1,
                generated=1,
                question1=None,
                question2=None,
                question3=None,
                question4=None,
                question5=None,
                grade=0
            )
            image.save()
            image_serializer = ImageSerializer(image)
            images_data.append(image_serializer.data)
        image_urls = [
            "https://res.cloudinary.com/dnmy80tpe/image/upload/v1713889176/kqyfp2ylogmdxplqkr7d.jpg",
            "https://res.cloudinary.com/dnmy80tpe/image/upload/v1713889177/lubhwjfem2cu2vjvpcvd.jpg",
            "https://res.cloudinary.com/dnmy80tpe/image/upload/v1713889178/qcxd9cppjdyrkxcce06v.jpg",
            "https://res.cloudinary.com/dnmy80tpe/image/upload/v1713889178/eqzdwnipu2uxxnrcgua9.jpg",
            "https://res.cloudinary.com/dnmy80tpe/image/upload/v1713889179/gvj6j3xrhjctzi5shvzf.jpg",
            "https://res.cloudinary.com/dnmy80tpe/image/upload/v1713889180/fcr5k09ycvcirhlsvaqn.jpg",
            "https://res.cloudinary.com/dnmy80tpe/image/upload/v1713889181/vc6pprpzwxbnqk8qpzsf.jpg",
            "https://res.cloudinary.com/dnmy80tpe/image/upload/v1713889182/et50pt8m2ckpzqotp1nz.jpg",
            "https://res.cloudinary.com/dnmy80tpe/image/upload/v1713889182/sglyotfckubf7erjklts.jpg",
            "https://res.cloudinary.com/dnmy80tpe/image/upload/v1713889183/zn89sybmz65csnkgq0u4.jpg",
            "https://res.cloudinary.com/dnmy80tpe/image/upload/v1713889184/fnnaq4peijd5yk4sbymz.jpg",
            "https://res.cloudinary.com/dnmy80tpe/image/upload/v1713889185/pvar4bev4c5scyigqg7u.jpg",
            "https://res.cloudinary.com/dnmy80tpe/image/upload/v1713889186/zvzlowwe18iux53muuqn.jpg",
            "https://res.cloudinary.com/dnmy80tpe/image/upload/v1713889187/dxqyxg2h31detguzdlxp.jpg",
        ]
        for url in image_urls:
            image = Image.objects.create(
                user=user,
                urll=url,
                type=2,
                generated=0,
                question1=None,
                question2=None,
                question3=None,
                question4=None,
                question5=None,
                grade=0
            )
            image.save()
            image_serializer = ImageSerializer(image)
            images_data.append(image_serializer.data)
        image_urls = [
            "https://res.cloudinary.com/dnmy80tpe/image/upload/v1713889231/d500g5lhomzx2cbv7w5a.png",
            "https://res.cloudinary.com/dnmy80tpe/image/upload/v1713889232/q4i02nsi83jxfmhgktmk.png",
            "https://res.cloudinary.com/dnmy80tpe/image/upload/v1713889233/z0vg7wuqfxxhwskcccpk.png",
            "https://res.cloudinary.com/dnmy80tpe/image/upload/v1713889234/xqe1e4n7igl8k7l8wj0a.png",
            "https://res.cloudinary.com/dnmy80tpe/image/upload/v1713889235/jimaapsxlumbmfjxwb5t.png",
            "https://res.cloudinary.com/dnmy80tpe/image/upload/v1713889236/lv5uoixjuqtecojr7yfj.png",
            "https://res.cloudinary.com/dnmy80tpe/image/upload/v1713889237/hw6zqonngjygjpplqb38.png",
            "https://res.cloudinary.com/dnmy80tpe/image/upload/v1713889239/iwnhtln4v4wauwzle47h.png",
            "https://res.cloudinary.com/dnmy80tpe/image/upload/v1713889240/fvf3mgqy2g5duc3wgblc.png",
            "https://res.cloudinary.com/dnmy80tpe/image/upload/v1713889241/rzvgchifjecmauih7u9r.png",
            "https://res.cloudinary.com/dnmy80tpe/image/upload/v1713889242/bhwgfgcavbybetdwrjys.png",
            "https://res.cloudinary.com/dnmy80tpe/image/upload/v1713889242/yepdjxr5udvddiskiywu.png",
            "https://res.cloudinary.com/dnmy80tpe/image/upload/v1713889243/gwt6j6azsequpm9goxx4.png",
            "https://res.cloudinary.com/dnmy80tpe/image/upload/v1713889244/o78ra2xd7jdxwj7r7d7d.png",
            "https://res.cloudinary.com/dnmy80tpe/image/upload/v1713889245/brqgkmzlbck4rcpex1bk.png",
            "https://res.cloudinary.com/dnmy80tpe/image/upload/v1713889246/zjmwlxj1efoz5xklaowo.png",
            "https://res.cloudinary.com/dnmy80tpe/image/upload/v1713889247/garkz3kaemw4t2odifop.png",
            "https://res.cloudinary.com/dnmy80tpe/image/upload/v1713889249/rfwxknzuadjtcncrup05.png",
            "https://res.cloudinary.com/dnmy80tpe/image/upload/v1713889249/ey0i9nrovj6mid8mqoao.png",
            "https://res.cloudinary.com/dnmy80tpe/image/upload/v1713889250/lcwzn25rcwjrx7orpsx9.png",
        ]
        for url in image_urls:
            image = Image.objects.create(
                user=user,
                urll=url,
                type=2,
                generated=1,
                question1=None,
                question2=None,
                question3=None,
                question4=None,
                question5=None,
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
        user_id = request.data.get('user')  # Assuming user_id is passed in the request
        user = User.objects.get(id=user_id)
        images_data = []
        image_urls = [
            "https://res.cloudinary.com/dnmy80tpe/image/upload/v1713888780/ge8rmbrks035pfyjlnwz.jpg",
            "https://res.cloudinary.com/dnmy80tpe/image/upload/v1713888781/ihlvhmxg6rwrfcj82i7n.jpg",
            "https://res.cloudinary.com/dnmy80tpe/image/upload/v1713888782/frmuqdvv1eh3lufgo3c4.jpg",
            "https://res.cloudinary.com/dnmy80tpe/image/upload/v1713888783/bok3ftzlj22fpshlnxja.jpg",
            "https://res.cloudinary.com/dnmy80tpe/image/upload/v1713888783/ezhmtvtfynftss9ofdg0.jpg",
            "https://res.cloudinary.com/dnmy80tpe/image/upload/v1713888784/bavrdqu9hxrx8mib218n.jpg",
            "https://res.cloudinary.com/dnmy80tpe/image/upload/v1713888785/xgvdaghav73wrfmgx8mb.jpg",
            "https://res.cloudinary.com/dnmy80tpe/image/upload/v1713888786/afe5xppk8aajevxyxks3.jpg",
            "https://res.cloudinary.com/dnmy80tpe/image/upload/v1713888786/xw9bf3ot75d4ulfctr3o.jpg",
            "https://res.cloudinary.com/dnmy80tpe/image/upload/v1713888787/xfcaanqn54t3kjxo1ir1.jpg",
            "https://res.cloudinary.com/dnmy80tpe/image/upload/v1713888788/upaearsaegh0qlsfwy4s.jpg",
            "https://res.cloudinary.com/dnmy80tpe/image/upload/v1713888789/yupiq0u2pcq2nhxnjcfr.jpg",
            "https://res.cloudinary.com/dnmy80tpe/image/upload/v1713888790/kalchynkq6j7ud1supmo.jpg",
        ]
        for url in image_urls:
            image = Image.objects.create(
                user=user,
                urll=url,
                type=0,
                generated=0,
                question1=None,
                question2=None,
                question3=None,
                question4=None,
                question5=None,
                grade=0
            )
            image.save()
            image_serializer = ImageSerializer(image)
            images_data.append(image_serializer.data)
        image_urls = [
            "https://res.cloudinary.com/dnmy80tpe/image/upload/v1713888853/hsnstayp6qno3aqjjt6i.png",
            "https://res.cloudinary.com/dnmy80tpe/image/upload/v1713888854/gk8kd0m4tt3jlsiyn1a0.png",
            "https://res.cloudinary.com/dnmy80tpe/image/upload/v1713888855/s79uehcqimpmxd4wdzqf.png",
            "https://res.cloudinary.com/dnmy80tpe/image/upload/v1713888856/h6ou3l2yvrblhni8auoy.png",
            "https://res.cloudinary.com/dnmy80tpe/image/upload/v1713888856/ewqw5juc6t8hkqpjvovd.png",
            "https://res.cloudinary.com/dnmy80tpe/image/upload/v1713888857/vrwie7oriuijgcnz2jke.png",
            "https://res.cloudinary.com/dnmy80tpe/image/upload/v1713888858/vxnde7daqtc3l3jfpgg0.png",
            "https://res.cloudinary.com/dnmy80tpe/image/upload/v1713888859/aucdhpvs7itvdeydnghj.png",
            "https://res.cloudinary.com/dnmy80tpe/image/upload/v1713888860/dzjnvhswsqtltojto1w9.png",
            "https://res.cloudinary.com/dnmy80tpe/image/upload/v1713888861/tvnnl32llcraf5vstjny.png",
            "https://res.cloudinary.com/dnmy80tpe/image/upload/v1713888862/rppoxhqfhollz15paaks.png",
            "https://res.cloudinary.com/dnmy80tpe/image/upload/v1713888862/hwdteq58wgmwnayqqivw.png",
            "https://res.cloudinary.com/dnmy80tpe/image/upload/v1713888863/fksqrvqctpzf9z4tw4wi.png",
            "https://res.cloudinary.com/dnmy80tpe/image/upload/v1713888864/i4hyks3pjf7nwqnudcxo.png",
            "https://res.cloudinary.com/dnmy80tpe/image/upload/v1713888865/jr1zyepvibr1ymhpra6v.png",
            "https://res.cloudinary.com/dnmy80tpe/image/upload/v1713888866/q94hreyli4ly96elxqvr.png",
            "https://res.cloudinary.com/dnmy80tpe/image/upload/v1713888867/pfurgvekxlvlcalesoev.png",
            "https://res.cloudinary.com/dnmy80tpe/image/upload/v1713888868/pkl83orbvy9fggutu5ip.png",
            "https://res.cloudinary.com/dnmy80tpe/image/upload/v1713888869/bonfwgvwb9ojqdrzzcxv.png",
            "https://res.cloudinary.com/dnmy80tpe/image/upload/v1713888870/nrjlhnf5hlkhonylvsuy.png",            
        ]
        for url in image_urls:
            image = Image.objects.create(
                user=user,
                urll=url,
                type=0,
                generated=1,
                question1=None,
                question2=None,
                question3=None,
                question4=None,
                question5=None,
                grade=0
            )
            image.save()
            image_serializer = ImageSerializer(image)
            images_data.append(image_serializer.data)
        image_urls = [
            "https://res.cloudinary.com/dnmy80tpe/image/upload/v1713888931/ji5mnoshwspeusi7eotr.jpg",
            "https://res.cloudinary.com/dnmy80tpe/image/upload/v1713888932/yc3qlob6ayhpffgkeipz.jpg",
            "https://res.cloudinary.com/dnmy80tpe/image/upload/v1713888933/xhkl3tdah0x6aaaqkx3y.jpg",
            "https://res.cloudinary.com/dnmy80tpe/image/upload/v1713888934/rpllsa2nzc5vqqtuegqu.jpg",
            "https://res.cloudinary.com/dnmy80tpe/image/upload/v1713888935/p34jbfmjkjsq4nfivsmk.jpg",
            "https://res.cloudinary.com/dnmy80tpe/image/upload/v1713888935/vh1dlmrlsdcfa57apxc9.jpg",
            "https://res.cloudinary.com/dnmy80tpe/image/upload/v1713888936/ri1aipdjyl8ycinzjufg.jpg",
            "https://res.cloudinary.com/dnmy80tpe/image/upload/v1713888937/lktpxumaotd4ygtfaicp.jpg",
            "https://res.cloudinary.com/dnmy80tpe/image/upload/v1713888938/tw0rlahpbjwpzlrwnugk.jpg",
            "https://res.cloudinary.com/dnmy80tpe/image/upload/v1713888938/ckhmlwiyxvpa7lorjtft.jpg",
            "https://res.cloudinary.com/dnmy80tpe/image/upload/v1713888939/e2urxiurojbxnqljgdvv.jpg",
            "https://res.cloudinary.com/dnmy80tpe/image/upload/v1713888940/f6edmftf6xvx9wdjp3qx.jpg",
            "https://res.cloudinary.com/dnmy80tpe/image/upload/v1713888940/litv8jy99xbchbql1ork.jpg",
        ]
        for url in image_urls:
            image = Image.objects.create(
                user=user,
                urll=url,
                type=1,
                generated=0,
                question1=None,
                question2=None,
                question3=None,
                question4=None,
                question5=None,
                grade=0
            )
            image.save()
            image_serializer = ImageSerializer(image)
            images_data.append(image_serializer.data)
        return Response({ "images": images_data }, status=status.HTTP_201_CREATED)
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
@api_view(['GET'])
def stats(request):
    op1 = Image.objects.filter(question1=1).count()
    op2 = Image.objects.filter(question1=2).count()
    op3 = Image.objects.filter(question1=3).count()
    op4 = Image.objects.filter(question1=4).count()
    op5 = Image.objects.filter(question1=5).count()
    q1 = [op1, op2, op3, op4, op5]
    op1 = Image.objects.filter(question2=1).count()
    op2 = Image.objects.filter(question2=2).count()
    q2 = [op1, op2]
    op1 = Image.objects.filter(question3=1).count()
    op2 = Image.objects.filter(question3=2).count()
    op3 = Image.objects.filter(question3=3).count()
    op4 = Image.objects.filter(question3=4).count()
    op5 = Image.objects.filter(question3=5).count()
    q3 = [op1, op2, op3, op4, op5]
    op1 = Image.objects.filter(question4=1).count()
    op2 = Image.objects.filter(question4=2).count()
    op3 = Image.objects.filter(question4=3).count()
    op4 = Image.objects.filter(question4=4).count()
    q4 = [op1, op2, op3, op4]
    return Response({ "question1": q1, "question2": q2, "question3": q3, "question4": q4 })
# @api_view(['GET'])
# def printCSV(request):
#     if request.method == 'GET':
#         unique_urls = Image.objects.values_list('urll', flat=True).distinct()
#         data = []
#         for url in unique_urls:
#             q1_option1_count = Image.objects.filter(question1=1, urll=url).count()
#             q1_option2_count = Image.objects.filter(question1=2, urll=url).count()
#             q1_option3_count = Image.objects.filter(question1=3, urll=url).count()
#             q2_option1_count = Image.objects.filter(question2=1, urll=url).count()
#             q2_option2_count = Image.objects.filter(question2=2, urll=url).count()
#             q2_option3_count = Image.objects.filter(question2=3, urll=url).count()
#             q3_option1_count = Image.objects.filter(question3=1, urll=url).count()
#             q3_option2_count = Image.objects.filter(question3=2, urll=url).count()
#             q3_option3_count = Image.objects.filter(question3=3, urll=url).count()
#             q4_option1_count = Image.objects.filter(question4=1, urll=url).count()
#             q4_option2_count = Image.objects.filter(question4=2, urll=url).count()
#             q4_option3_count = Image.objects.filter(question4=3, urll=url).count()
#             image_data = {
#                 'q1_option1_count': q1_option1_count,
#                 'q1_option2_count': q1_option2_count,
#                 'q1_option3_count': q1_option3_count,
#                 'q2_option1_count': q2_option1_count,
#                 'q2_option2_count': q2_option2_count,
#                 'q2_option3_count': q2_option3_count,
#                 'q3_option1_count': q3_option1_count,
#                 'q3_option2_count': q3_option2_count,
#                 'q3_option3_count': q3_option3_count,
#                 'q4_option1_count': q4_option1_count,
#                 'q4_option2_count': q4_option2_count,
#                 'q4_option3_count': q4_option3_count,
#             }
#             data.append(image_data)
#         return Response(data)
@api_view(['GET'])
def printCSV(request):
    if request.method == 'GET':
        unique_urls = Image.objects.values_list('urll', flat=True).distinct()
        data = []

        questions = ['question1', 'question2', 'question3', 'question4']
        options = [1, 2, 3]

        for url in unique_urls:
            image_data = {}

            for question in questions:
                for option in options:
                    count = Image.objects.filter(**{question: option, 'urll': url}).count()
                    key = f'{question}_option{option}_count'
                    image_data[key] = count

            data.append(image_data)

        return Response(data)