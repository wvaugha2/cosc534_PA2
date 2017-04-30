
Homework 2

Team: Coding Seahorses
Ellias Palcu
Sharon Soleman
Ty Vaughan

Answers

	Our answers are for the nodes given by running bootstrap.jar.  The 
	output from running bootstrap.jar with our team name as input can
	be found in the file bootstrap.txt.

	The answers to this assignment for each part are given in the 
	following csv files:
		Part1  ->  PART1_ANSWERS.csv
		Part2  ->  PART2_ANSWERS.csv
		Part3  ->  PART3_ANSWERS.csv

	The answers are also provided in this file, displaying the 
	probabilities associated with our answers.

Part 1:

	We ran our python script that performed our probabilistic disclosure
	attack, part1.py, with the input-rounds file provided on the course
	website, part1.txt using the command line prompt as follows:

		python part1.py part1.txt

	Our answers are below:
	a0 --> [('g5', 0.36), ('x7', 0.66)]
	b0 --> [('b2', 0.28), ('z7', 0.53)]
	c0 --> [('r5', 0.35), ('y9', 0.6)]
	d0 --> [('s3', 0.3), ('w2', 0.32)]
	e0 --> [('e6', 0.35), ('y0', 0.67)]
	f0 --> [('j5', 0.41), ('q3', 0.59)]
	g0 --> [('k4', 0.34), ('q6', 0.38)]
	h0 --> [('d8', 0.53), ('l2', 0.53)]
	i0 --> [('w2', 0.29), ('b7', 0.48)]
	j0 --> [('w2', 0.44), ('y5', 0.75)]
	k0 --> [('p9', 0.45), ('s3', 0.64)]
	l0 --> [('s7', 0.45), ('i8', 0.48)]
	m0 --> [('w2', 0.34), ('w4', 0.69)]
	n0 --> [('e2', 0.58), ('s9', 0.66)]
	o0 --> [('a2', 0.41), ('k1', 0.64)]
	p0 --> [('w6', 0.37), ('l6', 0.46)]
	q0 --> [('g0', 0.35), ('t8', 0.67)]
	r0 --> [('e4', 0.35), ('x3', 0.68)]
	s0 --> [('v6', 0.37), ('l6', 0.6)]
	t0 --> [('r9', 0.46), ('c6', 0.54)]
	u0 --> [('d7', 0.39), ('h5', 0.6)]
	v0 --> [('p4', 0.35), ('a9', 0.55)]
	w0 --> [('x7', 0.39), ('z5', 0.43)]
	x0 --> [('d7', 0.28), ('r6', 0.38)]
	y0 --> [('h6', 0.35), ('n9', 0.55)]
	z0 --> [('m9', 0.39), ('i5', 0.49)]

Gathering Rounds for Part 2/3:

	To gather rounds, we first ran priv_pub.py to obtain which nodes were
	public and which nodes were private.  This was done using the command
	line prompt below:
	
		python3 priv_pub.py > nodes.txt

	We then created a new, empty directory and placed nodes.txt and 
	gatherData.py into that directory. We then ran gatherData.py, which
	connected to all public nodes, created a file for each public node,
	and wrote each individual node’s traffic to its file for a period of 
	10 hours.  This was done using the command line prompt below:

		python gatherData.py

	At this point, we have 120 files named after the node whose traffic 
	it contains.  We move gatherData.py out of the directory and 
	make_send_rec_file.py into the directory.  By running this python
	script, we turn those node-traffic files into two files: 
		public_rounds.txt and 
		private_rounds.txt, 
	which contain the sender and receiver lists for all rounds for either 
	the public nodes or the private nodes. 

Part 2:

	To get our answer for part2, we ran part2.py with our public_rounds.txt
	file.  The command line prompt to do this is given below:
	
		python part2.py public_rounds.txt > public_results.txt

	Our answers are below:
	8033838d7157e4931fc64e426a930ead17ec1039fd5a2e48ba7987477d018c42 -->
	[('8015e43bc996a54c0b41963cc57b6121f9cadb68e45974d2a4c5d19aeb92c9e0', 0.44), 
	('80292158866c2107dda1c71987e3da44882eadeec59bdf8e55760ae6f5cb75c1', 0.49)]

	801078937affd4f219223684fef36f767cdf51d5e44329a90004db8e087f8f8c --> 	
	[('80ace5d2b36a63b4a41681155bd4446625a9d24199e37f4e32f2d870d404983f', 0.44),
	('80db34e8b2657a7ff43d37ba2069ca576e61b70f589aa4da8a20be3057639095', 0.45)]

	801f4c84e74280e0e7b751ae0421c284cd27b49e6cb30b3dbd766874bbd9a4e0 --> 
	[('808246ae5158b67891ab242ea4a8c0c42224a78d7d29d32d9b7977b4c42a3dfd', 0.23), 
	('809a857276dbe1798b57eec62032e8ac7b4960ff5f410bfb67704121fb4c11ac', 0.52)]

	807bad0c90c7c5fd16de41c739e24fb2ab32f3bdad6393f15b948e0620a7b840 --> 
	[('80275b8013b71095cc12403a4bf5d30553d1626aad0c197a732d8966e131b313', 0.22), 
	('80ec3120cfc443a2db1794e32a73fe6f3f3c85b15f55f6c61e1c73daeb74de7f', 0.49)]

	8063c492767fc09f29f601f35240652a375e7c9003ae92b3070cdc28077b65c9 --> 
	[('80ec3120cfc443a2db1794e32a73fe6f3f3c85b15f55f6c61e1c73daeb74de7f', 0.37), 
	('80e7a69705dbab7359a5ebc21770329eda376c67556b257b8c724ba7a46369f5', 0.57)]

Part 3:
	
	To get our answer for part3, we ran part3.py with our private_rounds.txt
	file.  The command line prompt to do this is given below:

		python part3.py public_rounds.txt > private_results.txt

	Our answers are below:
	804a74fecca6aabed86b2642ca5ddf91d03d1943a89c487a91a21bace9757ad3 --> 
	[('80430025357f50f44aaac39b6689b86dee16808bc4aa125f671be841eb603336', 0.35),
 	('80cd7028b270b1569d8703655aee8e07eb042b71ead034e941514d94a2a491f0', 0.36)]

	80c36eb1372ba2de9c3222748b9c2d5d0f59924a5f87da7e270c25758ae6da87 --> 
	[('8059ad64c403bc076ea9934f8bdb0722730aebad22e0d93a5407dcf649565c28', 0.28), 
	('80afa00f9e65c7cbb8611e30e3193fdf1ec629d7f6c9344139ba6e0a9e8f1865', 0.59)]

	80294dd94243cfec921c56685040765ffccdcd89677e7040e16733ff645c7a0c --> 
	[('80432f767a08499a490b6c531a2750f661ae25825b4603335f5537ce46b71ae2', 0.28), 
	('80ac687c25a326c0558014f3c734921d86780ca67ed6b6135febf6bc2fe111d4', 0.54)]

	806ca14119a98ecf4160e8e4c4c0f49d6feae0b21076bd412b93e0ef9263caf9 --> 
	[('802a0f91d5430889f275395aa0cf3e5b9236dc06fa8818ab9628d06838513fef', 0.38), 
	('80993ea8c53e71c2e84c9b6bd8651b296045f21be5e404162d20ba6e62a2b14e', 0.59)]

	80c0435f7fed4d24fb9bbf5915973a7d3cdec68f8ee66e935965238433c2cd45 --> 
	[('80a0ff5e2819ef24352369ed4b1ca0080001ce951a714923b16bb6f3372d1e3b', 0.45), 
	('80b546bd72dc8f402cba152c73e5356cb789b81028888825cd26424a140c0725', 0.54)]






	

	