# in the_bank.py
from os import access


class Account(object):
	ID_COUNT = 1
	def __init__(self, name, **kwargs):
		self.__dict__.update(kwargs)

		self.id = self.ID_COUNT
		Account.ID_COUNT += 1
		self.name = name
		if not hasattr(self, "value"):
			self.value = 0

		if self.value < 0:
			raise AttributeError("Attribute value cannot be negative.")
		if not isinstance(self.name, str):
			raise AttributeError("Attribute name must be a str object.")
	def transfer(self, amount):
		self.value += amount


# in the_bank.py
class Bank(object):
	"""The bank"""
	def __init__(self):
		self.accounts = []

	def check_account_add(self, account):
		if (not isinstance(account, Account)):
			return False
		if (any(x.name == account.name for x in self.accounts)):
			return False
		return True

	def check_account_transfer(self, account):
		if (not isinstance(account, Account)):
			return False
		attr = dir(account)
		if (len(attr) % 2 == 0):
			return False
		if (any(att[0] == "b" for att in attr)):
			return False
		if (all(not (att.startswith("zip") or att.startswith("addr") ) for att in attr)):
			return False
		if (not set(["name", "id", "value"]).issubset(set(attr))):
			return False
		if (not isinstance(account.name, str)):
			return False
		if (not isinstance(account.id, int)):
			return False
		if (not (isinstance(account.value, int) or isinstance(account.value, float))):
			return False
		return True
	def add(self, new_account):
		""" Add new_account in the Bank
		@new_account: Account() new account to append
		@return True if success, False if an error occured
		"""
		if (not self.check_account_add(new_account)):
			return False
		self.accounts.append(new_account)
		return True

	def transfer(self, origin, dest, amount):
		"""" Perform the fund transfer
		@origin: str(name) of the first account
		@dest: str(name) of the destination account
		@amount: float(amount) amount to transfer
		@return True if success, False if an error occured
		"""
		account_origin = next((x for x in self.accounts if x.name == origin), None)
		account_dest = next((x for x in self.accounts if x.name == dest), None)

		if (not (self.check_account_transfer(account_origin) and self.check_account_transfer(account_dest))):
			return False
		if (amount < 0 or amount > account_origin.value):
			return False
		if (account_origin.name == account_dest.name):
			return True
		account_origin.transfer(-amount)
		account_dest.transfer(amount)
		return True


	def fix_account(self, name):
		""" fix account associated to name if corrupted
		@name: str(name) of the account
		@return True if success, False if an error occured
		"""
		if (not isinstance(name ,str) or all(account.name != name for account in self.accounts)):
			return False
		account = next((x for x in self.accounts if x.name == name), None)
		attr = dir(account)
		if (not isinstance(account, Account)):
			return False
		for att in attr:
			if (att[0] == "b"):
				delattr(account, att)
		if (all(not (att.startswith("zip") or att.startswith("addr") ) for att in attr)):
			setattr(account, "zip", "azerty")
		if (len(dir(account)) % 2 == 0):
			setattr(account, "odd", "odd")
		return True
