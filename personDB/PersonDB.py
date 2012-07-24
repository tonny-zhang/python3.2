import sys,shelve

#personDB['1'] = {'name':'test','age':10}

def storePerson (db):
	pid = input('enter person ID:');
	name = input('enter your name:');
	age = input('enter your age:');
	db[pid] = {'name':name,'age':age}
	print('store success!');

def  seachPerson(db):
	condition = input('enter seach conditioin(pid,name,age)["q" for quit]:');

	if(condition == 'pid'):
		pid = input('enter pid:');
		try:
			print(db[pid]);
		except:
			print('have no info!');
			seachPerson(db);
	elif(condition == 'q'):
		return;
	else:
		print('please enter right command!');
		seachPerson(db);

def enterCommand ():
	cmd = input('enter you command(? for help):');
	return cmd.strip().lower();

def cmd_help ():
	print('	store	store info to DB!');
	print('	seach	seach info from DB!');
	print('	quit	quite sys!');
	pass;
def main ():
	personDB = shelve.open('E:/python/personDB/person.dat');
	for(k,v) in personDB.items():
		print(k,v);
	for k in personDB.keys():
		print(k);

	try:
		while(True):
			cmd = enterCommand();
			if(cmd == 'store'):
				storePerson(personDB);
			elif(cmd == 'seach'):
				seachPerson(personDB);
			elif(cmd == 'quit'):
				return;
			elif(cmd == '?'):
				cmd_help();
			else:
				cmd_help();
	finally:
		personDB.close();

if(__name__ == '__main__'):
	main();
