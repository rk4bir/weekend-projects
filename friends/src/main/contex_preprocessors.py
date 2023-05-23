from accounts.models import Account
from notifications.models import Notification


def ACCOUNTS(request):
 	ACCOUNTS = Account.objects.all().filter(is_active=True)
 	return {'ACCOUNTS': ACCOUNTS}

def NOTFS(request):
	if request.user.is_authenticated and not request.user.is_superuser:
		account = Account.objects.get(user=request.user)
		NOTFS = Notification.objects.all().filter(account=account)
		no = Notification.objects.all().filter(account=account).filter(is_seen=False)
		NOTFS_COUNT = no.count
	else:
		NOTFS = None
		NOTFS_COUNT = 0
	return {"NOTFS": NOTFS, "NOTFS_COUNT": NOTFS_COUNT}