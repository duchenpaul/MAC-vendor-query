import requests
import bs4 as bs

MAC = '4C-57-CA-1A-D1-DF'

def vendor_query(MAC):
	'''Returns the vendor of MAC addr'''
	s = requests.Session()
	# Due to my network env, I have to use proxy to get the website
	s.proxy = {"http": "127.0.0.1:1080"}
	resp = s.get('https://hwaddress.com/?q=' + MAC )
	query_page = resp.text
	# with open('./1.html', 'w') as f:
	# 	f.write(query_page)

	# with open('./1.html', 'r') as f:
	# 	query_page = f.read()

	soup = bs.BeautifulSoup(query_page, 'lxml')
	vendor_name = soup.select('body > div > div[class="table-responsive"] > table > tr > td > a')[0].get_text()
	return vendor_name

if __name__ == '__main__':
	mac_list = {
				'38-21-87-B8-AA-5F',
				'B8-27-EB-B1-DA-D8',
				'F0-B4-79-BB-7A-58',
				'C0-EE-FB-B0-0A-1A',
				'B4-EF-FA-B3-2A-A8',
				'00-1E-65-BB-9A-A2',
				'4C-57-CA-BA-DA-DF',
				'50-3A-A0-BC-1A-28',
				}
	for MAC in mac_list:
		print('Querying ' + MAC)
		# print(vendor_query(MAC))
		print('\n')

# print(vendor_query(MAC))