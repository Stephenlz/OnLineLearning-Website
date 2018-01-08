from users.models import EmailVerifyRecord
from random import Random
from django.core.mail import send_mail
from DjangoLearning.settings import EMAIL_FROM


def sendRegisterEmail(email, sendType="register"):
    emailRecord = EmailVerifyRecord()
    emailRecord.code = generateRandomStr(16)
    emailRecord.email = email
    emailRecord.sendType = sendType
    emailRecord.save()

    emailTitle = ""
    emailBody = ""

    if sendType == "register":
        emailTitle = "onLineLearning website register"
        emailBody = "please click the link to active your account: http://127.0.0.1:8000/active/{0}".format(
            emailRecord.code)
        send_status = send_mail(emailTitle, emailBody, EMAIL_FROM, [email])
        if send_status:
            pass
    elif sendType == "forget":
        emailTitle = "onLineLearning website password reset"
        emailBody = "please click the link to reset your password: http://127.0.0.1:8000/reset/{0}".format(
            emailRecord.code)
        send_status = send_mail(emailTitle, emailBody, EMAIL_FROM, [email])
        if send_status:
            pass


def generateRandomStr(randomLength=8):
    str = ''
    chars = 'AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz01234567890'
    length = len(chars)
    random = Random()
    for i in range(randomLength):
        str += chars[random.randint(0, length - 1)]
    return str
