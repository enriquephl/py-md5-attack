# This is an example of hash length extension attacks (and why you don't roll your own crypto!!!)
# In this case, an attacker, Malice, intercepts a message ("to=12345&amt=103.53&note=Thanks!")
# that has been "authenticated" using a poorly constructed MAC (message authentication code).
# This MAC has been created using the following method: md5(secret | message).
# Ideally, since the attacker, Malice, doesn't have the secret, he should be unable to craft a new
# message that is also authenticated. However, because of how the mac was created, we can use 
# Hash Length Extensions. We'll be using the pymd5 library as found on upenn's website via google cache:
# https://webcache.googleusercontent.com/search?q=cache:yyvXXyVKuYYJ:https://www.cis.upenn.edu/~cis331/project1/pymd5.py+&cd=3&hl=en&ct=clnk&gl=us

import urllib
from pymd5 import md5, padding

secret = "p@ssw0rd"
original_message = "to=12345&amt=103.54&note=Thanks!"
appended_message = "&to=98765&amt=1000.00"

# Creating the original MAC
original_hash = md5()
original_hash.update(secret + original_message)
original_digest = original_hash.hexdigest()

# Performing the hash length extension.
# We set the md5 state to the first block's hash value.
# This is the MAC value we got from the cookie
extended_hash = md5(state=original_digest.decode("hex"), count=512)
extended_hash.update(appended_message)
extended_digest = extended_hash.hexdigest()

# This just shows that the HLE produced the same digest as
# secret | message | padding | message_2
full_message_hash = md5()
full_message_hash.update(secret + original_message + padding(len(secret + original_message) * 8) + appended_message)
full_message_digest = full_message_hash.hexdigest()

print "Original message digest: " + original_digest
print "Extended message digest: " + extended_digest
print "Full message digest: " + full_message_digest + "\n"
print "Original message: " + original_message
print "Modified message: " + original_message + urllib.quote(padding(len(secret + original_message) * 8)) + appended_message