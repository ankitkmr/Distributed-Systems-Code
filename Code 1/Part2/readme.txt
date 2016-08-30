1.  Decide the number of servers available.
	Default number is set to 5 servers. Corresponding to that are 5 server{i}.py files with /localhost:800{i} corresponding address
	So  server1.py - /localhost:8001
		server2.py - /localhost:8002
		server3.py - /localhost:8003
		server4.py - /localhost:8004
		server5.py - /localhost:8005

	In case of more or less serves, use appropriate copies of server{i}.py files i.e 3 such files for 3 servers and 7 such files for 7 servers.
	Make sure to change the address in those new copies of server{i}.py file as /localhost:800{i}

2. Run All the server.py files in separate terminal each
3. Run the client.py file and Enter the number of servers that you decided and set up for as given in Step 1 and press Enter. 
   In case of Default Number of servers, simply press Enter without any number.

4. Get the sorted array printed on the client.py terminal