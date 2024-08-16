

//PROJECT :       BANKING SYSTEM 
//
// MEMBER :
//	BITF15A530			
// USMAN MEHBOOB



# include "iostream"
# include "windows.h"
# include "cstdlib"
# include "fstream"
# include "iomanip"
# include "cctype"

using namespace std;

void main_menu();
void warning();
void create_account(int);
void show_data();
void blnc_inq();
void dpst_amnt();
void witdrw_amnt();
void blnc_inq();
void acnt_lst();
void acnt_del();
void acnt_mdfy();
void exit();


int x=1000;
const int size=20 , u=2;

struct account
{
    char name[20];
	
	int age;
	
	char actype[u];
	int amnt;
	int acno;
};


int main()
{
	const WORD colors[]=
	{
		0x1A, 0xB2,0x3C,0x4D,0x5E
    };

	
    HANDLE ass = GetStdHandle(STD_OUTPUT_HANDLE);

    CONSOLE_FONT_INFOEX font;
    GetCurrentConsoleFontEx(ass, false, &font);
    font.dwFontSize.X=15 ;
    font.dwFontSize.Y =35 ;
    SetCurrentConsoleFontEx(ass, false, &font);
    
    SetConsoleTextAttribute(ass , 0x0C);
	
	{
    std::cout << "*******************************************************************************"<<endl;
	Sleep(1000);
	std::cout << "\n\n\n\n\n\n\n \t\t\t ";
	std::cout << "\t BANKING SYSTEM \n\n\n"<<endl;
	Sleep(1000);
	std::cout << "\n\n\n\n\n\n";
    
	system("Pause");
	main_menu();
	}

}

void main_menu()
{


	int avi=0;
	fstream outf;
	outf.open("accounts.dat",ios::in);
	account user;
	while(outf.read(reinterpret_cast<char *>(&user),sizeof(account)) )
	{
	avi++;

	}
	outf.close();

	x=(5*avi)+1000;

	system ("color 5E");
	int a=0;
	do
	{
		system ("cls");
		cout<<"\n\n\n********************************************************************************"<<endl;
	    Sleep(350);
		cout<<"\n\n\t\t\t  MAIN MENU \t \t"<<endl;
		Sleep(350);
		cout<<"\n********************************************************************************\n";
		cout<<"\n\t1.\t\t New Account\n";
		Sleep(150);
	    cout<<"\t2.\t\t Deposite Amount\n";
		Sleep(150);
		cout<<"\t3.\t\t Withdraw Amount\n";
		Sleep(150);
		cout<<"\t4.\t\t Balance Enquiry\n";
		Sleep(150);
		cout<<"\t5.\t\t All Accounts Holders List\n";
		Sleep(150);
		cout<<"\t6.\t\t Close An Account\n";
		Sleep(150);
		cout<<"\t7.\t\t Modify an Account\n";
		Sleep(150);
		cout<<"\t8.\t\t EXIT\n";
		Sleep(150);
		cout<<endl;
		cout<<"\t\tselect your choice from (1-8)"<<endl;
		cin>>a;
		system ("cls");
		switch(a)
		{
			
		case 1:
			x+=5;
			if (x==user.acno)
			{
				x+=5;
			}
			create_account(x);
			
			break;
		
		case 2:
			dpst_amnt();
			break;
		case 3:
			witdrw_amnt();
			break;
		case 4:
			blnc_inq();
			break;
		case 5:
			acnt_lst();
			break;

		case 6:
			acnt_del();
			break;
		case 7:
			acnt_mdfy();
			break;

		case 8:
			exit();
			break;
		

		}	
		
	}
	while(a>8);
	{
		
		warning();
	}

}

void warning()
{
	cout<<"please enter within range of 1-8 "<<endl<<endl;
	cout<<"program closing "<<endl; 
	system("pause");

}


void create_account(int y)
{
	
	system("color 6E");
	fstream outf("accounts.dat", ios::out | ios::app | ios::binary);
	if(!outf)
	{
		cout<<"file coul'nt be created"<<endl;
	}
	account user;
	cin.ignore();
	cout<<"Enter Your Name"<<endl;
	cin.getline(user.name, size);
	cout<<"Enter Your Age"<<endl;
	cin>>user.age;
	if (user.age<18)
	{
		cout<<"You Are Not Eligible To Open An Account"<<endl;
		system("pause");
		main_menu();
	}
	
	cout<<"Enter The Amount To Be Deposited"<<endl;
	cin>>user.amnt;
	if(user.amnt<500)
	{
		cout<<"Please Deposite Amount Greater Than 500"<<endl;
		system("pause");
		main_menu();
	}
	
	
	cout<<"Enter Account Type C/S"<<endl;
	cin>>user.actype;
	
	cout<<"Your Account Is Sucessfully Created "<<endl;
	cout<<"Your Account Nmber Is "<<y<<endl;
	user.acno=y;
	cout<<"  Thanks For Creating Account  "<<endl;
	
	outf.write(reinterpret_cast<char*>(&user),sizeof(account));
	outf.close();

	system("pause");
	main_menu();

}


void dpst_amnt()
{
	system("color fd");
	int x=0, a=0;
	cout<<"Enter Account Number : ";
	cin>>a;
	account user;
	
	bool check=false;
  int h=0,s=0;
	fstream outf("accounts.dat",ios:: in | ios::out | ios::binary);
	while(outf.read(reinterpret_cast<char*>(&user),sizeof(account)))
	{
		if(user.acno==a)
		{
			check=true;
			cout<<"Your Current Balance is "<<user.amnt<<endl;
			cout<<endl;
			cout<<"Enter The Amount You Want To Deposite "<<endl;
			cin>>x;

			break;

		}


	}

	
	
	user.amnt += x;

	outf.seekg(-36,ios::cur);
	

	outf.write(reinterpret_cast<char *>(&user),sizeof(account));
	
	
	
	
	cout<<"New Balance Is "<<user.amnt<<endl;
	outf.close();
	system("pause");
	main_menu();
}

void witdrw_amnt()
{
	system("color 4E");
	int x=0, a=0;
	cout<<"enter account number : ";
	cin>>a;
	account user;
	
	
	fstream outf("accounts.dat",ios:: in | ios::out | ios::binary);
	while(outf.read(reinterpret_cast<char*>(&user),sizeof(account)))
	{
		if(user.acno==a)
		{
			
			cout<<"Your Current Balance Is "<<user.amnt<<endl;
			cout<<endl;
			cout<<"Enter The Amount You Want To Withdraw "<<endl;
			cin>>x;

			break;

		}


	}

	user.amnt -= x;

	outf.seekg(-36,ios::cur);
	

	outf.write(reinterpret_cast<char *>(&user),sizeof(account));
	
	
	cout<<"new balance is "<<user.amnt<<endl;
	outf.close();

	system("pause");
	main_menu();
}

void blnc_inq()
{
	system ("color A9");
	int  a=0;
	cout<<"enter account number : ";
	cin>>a;
	account user;
	
  
	fstream outf("accounts.dat",ios:: in | ios::binary);
	outf.seekp(0,ios::beg);
	while(outf.read(reinterpret_cast<char*>(&user),sizeof(account)))
	{
		
		if(user.acno==a)
		{
			cout<<"depositor name "<<user.name<<endl;
			cout<<"your current balance is "<<user.amnt<<endl;
			cout<<"Your Age: "<<user.age<<endl;

			system ("pause");
			system("cls");

			cout<<endl<<endl;

			cout<<"your receipt has been generated"<<endl;
			cout<<endl;
			cout<<"please collect it from the counter"<<endl<<endl;
			
			

			break;

		}


	}
	 
	outf.close();
	system("pause");
	main_menu();
}


void acnt_lst()
{
	system("color B5");
	int x=0;
	
	account user;

	fstream outf("accounts.dat",ios:: in | ios::out | ios::binary);
	outf.read(reinterpret_cast<char*>(&user),sizeof(account));
	cout<<endl<<"\t  Account holder list: \n";
	cout<<"_________________________________________\n";
	cout<<"\tDepositers"<<"\tType of account"<<endl;
	outf.seekp(0,ios:: beg);
	while(outf.read(reinterpret_cast<char *>(&user),sizeof(account)) )
	{
		cout<<"\t"<<user.name<<"\t\t\t"<<user.actype<<endl;
	}

	
		

	system("pause");
	main_menu();

}

void acnt_del()
{
	system("color D8");
	
	int x=0, a=0;
	cout<<"enter account number : ";
	cin>>a;
	account user;
	
	bool check=false;
  int h=0,s=0;
	fstream outf, outf2;

		outf.open("accounts.dat",ios:: in | ios::out | ios::binary);
	    outf2.open("accounts2.dat",ios:: in | ios::out | ios::binary);
	while(outf.read(reinterpret_cast<char*>(&user),sizeof(account)))
	{
		if(user.acno!=a)
		{
			outf2.write(reinterpret_cast<char *>(&user),sizeof(account));
			
		}

	}

	
	outf.close();
	cout<<endl;
	cout<<"\t your account is successfully deleted "<<endl;
	
	outf.open("accounts.dat",ios::out | ios::trunc | ios:: binary );
	
	outf2.seekg(0,ios::beg);
	account user1;
	while(outf2.read(reinterpret_cast<char *>(&user1),sizeof(account)))
	{
	outf.write(reinterpret_cast<char *>(&user1),sizeof(account));
	}
	
	outf.close();

	outf2.close();
	outf2.open("accounts2.dat",ios::out | ios::trunc | ios :: binary );
	outf2.close();

	system("pause");
	main_menu();

}

void acnt_mdfy()
{
	system("color 3E");
	account user;
	int s=0, a=0,d=0,f=0;
	char sio[20];
	
	cout<<"enter your account number "<<endl;
	cin>>a;

	fstream outf("accounts.dat",ios:: out | ios:: in |  ios::binary);
	outf.seekp(0,ios::beg);

	while(outf.read(reinterpret_cast<char*>(&user),sizeof(account)))
	{
		
		if(user.acno==a)
		{
			cout<<"what do you want to edit ?"<<endl;
			cout<<"1. NAME \n 2. AGE "<<endl;
			cout<<"chosse by entering 1 or 2 "<<endl;
			cin>>s;
			
			switch (s)
			{
			case 1:

				cout<<"your name is "<<user.name<<endl<<endl;
				cout<<"enter your new name "<<endl;
				cin>>sio;
				for (int i=0;i<20;i++)
				{
					user.name[i]=sio[i];
	
				}
				outf.seekg(-36 , ios:: cur );

	
		outf.write(reinterpret_cast<char *>(&user),sizeof(account));
	
		cout<<"Your new name is: "<<user.name<<endl<<endl;
		
		cout<<"your account has been modified "<<endl;
		outf.close();
		
		system("pause");
		main_menu();
				
					break;

			
			case 2 :
			    cout<<"your age was "<<user.age<<endl<<endl;
				cout<<"enter your new age "<<endl;
				cin>>d;
	
				user.age = d;

				outf.seekg(-36 , ios:: cur );

	
				outf.write(reinterpret_cast<char *>(&user),sizeof(account));
	
				cout<<"your new age is "<<user.age<<endl<<endl;
				cout<<"your account has been modified "<<endl;

	
				outf.close();
	
	
				system("pause");
	
				main_menu();			
					
				break;
			}


		}
	
	}
	
}

void exit()
{
	system("color F8");
	cout<<endl;
	cout<<"\n\n\n";
	
		Sleep(1000);
		cout<<"\n\n\t\t *********  thanks for using  ************ "<<endl;
		
	cout<<"\n\n\n";
		
		exit(0);
	
	
}
