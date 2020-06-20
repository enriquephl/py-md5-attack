import urllib
import pymd5
import sys

if __name__ == "__main__" :
  if len(sys.argv) < 3:
    print ("Usage: ", sys.argv[0], " <known message> <md5 digest> <string to append> [length of secret]")
    sys.exit()

  original_message = sys.argv[1]
  original_digest = sys.argv[2]
  appended_message = sys.argv[3]
  secret_length = int(sys.argv[4])

  # Performing the hash length extension.
  # We set the md5 state to the first block's hash value.
  # This is the MAC value we got from the cookie
  extended_hash = pymd5.md5(state=original_digest.decode("hex"), count=512)
  extended_hash.update(appended_message)
  extended_digest = extended_hash.hexdigest()

  # This just shows that the HLE produced the same digest as
  # secret | message | padding | message_2
  secret="welcome"
  full_message_hash = pymd5.md5()
  full_message_hash.update(secret + original_message + pymd5.padding((len(original_message)+secret_length) * 8) + appended_message)
  full_message_digest = full_message_hash.hexdigest()

  print "Original message digest: " + original_digest
  print "Extended message digest: " + extended_digest
  print "Full message digest: " + full_message_digest + "\n"
  print "Original message: " + original_message
  print "Modified message: " + original_message + urllib.quote(pymd5.padding((len(original_message)+secret_length) * 8)) + appended_message