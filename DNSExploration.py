

import dns
import dns.resolver
import socket

def ReverseDNS(ip):
	try:
		result = socket.gethostbyaddr(ip)
	except:
		return []
	return [result[0]]+result[1]

def DNSRequest(domain):
	try:
		result = dns.resolver.resolve(domain, 'A')
		if result:
			print(domain)
			for answer in result:
				print(answer)
				print("Domain Name: %s" % ReverseDNS(answer.to_text()))
	except (dns.resolver.NXDOMAIN, dns.exception.Timeout):
		return

def SubdomainSearch(domain, dictionary, nums):
	for word in dictionary:
		if not word:
			continue
		subdomain = word + "." + domain
	#	print("Trying subdomain:", subdomain)  
		DNSRequest (subdomain)
		if nums:
			for i in range (0,10):
				s = word+str(i)+"."+domain
				#print("Trying sundomain:" , s)
				DNSRequest(s)


domain = "google.com"
d = "/home/kali/workplace/Projects/subdomain.txt"
dictionary = []
with open(d,"r") as f:
	dictionary = f.read().splitlines()



SubdomainSearch (domain,dictionary,True)
