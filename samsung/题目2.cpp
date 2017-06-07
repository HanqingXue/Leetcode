#include<string>
#include<iostream>
using namespace std;

struct SRT {
	long   start_pos;
	long  max_length;
};

void expand_Palindrome(SRT& rt, string & str, long  left, long  right, long  length)
{
	while (left >= 0 && right < length && str[left] == str[right])
	{
		left -= 1;
		right += 1;
	}
	long  cur_maxlen = right - left - 1;
	if (cur_maxlen > rt.max_length)
	{
		rt.max_length = cur_maxlen;
		rt.start_pos = left + 2;
	}


}

void find_max_palindrome_length(SRT& rt, string & str, long  length)
{

	rt.max_length = 1;
	rt.start_pos = 1;
	
	if (length < 2)
	{
		return;
	}

	for (long  i = 0; i < length; i++)
	{
		expand_Palindrome(rt, str, i, i,length);

		expand_Palindrome(rt, str, i, i+1,length);
		
	}

	return;

}



int main()
{
	long  N;
	cin >> N;
	for (int i = 1; i <= N; i++)
	{
		long  length;
		string str;
		SRT rt;
		cin >> length >> str;	
		find_max_palindrome_length(rt, str, length);
		cout << "Case #" << i << endl<<rt.start_pos<<" "<<rt.max_length<<endl;
	}
	system("pause");
	return 0;
}

