#include <iostream>
#include <string>
using namespace std;

class Game
{
public:
    Game(string FirstUserName,int FirstUserChoose,string SecondUserName,int SecondUserChoose)
    {
        setFirstUserName(FirstUserName);
        setFirstUserChoose(FirstUserChoose);
        setSecondUserName(SecondUserName);
        setSecondUserChoose(SecondUserChoose);
        WhoWins();
    }
    ~Game()
    {
    }
    void setFirstUserName(string FirstUserName)
    {
        this->FirstUserName = FirstUserName;
    }
    void setSecondUserName(string SecondUserName)
    {
        this->SecondUserName = SecondUserName;
    }
    void setFirstUserChoose(int FirstUserChoose)
    {
        if (FirstUserChoose >= 0 && FirstUserChoose <=3)
        {
            this->FirstUserChoose = FirstUserChoose;
        }
        else
        {
            cout << "A wrong choice!" << endl;
        }
    }
    void setSecondUserChoose(int SecondUserChoose)
    {
        if (SecondUserChoose >= 0 && SecondUserChoose <=3)
        {
            this->SecondUserChoose = SecondUserChoose;
        }
        else
        {
            cout << "A wrong choice!" << endl;
        }
    }
    void WhoWins()
    {
        if (FirstUserChoose - SecondUserChoose == -1 || FirstUserChoose - SecondUserChoose == 2)
        {
            cout << FirstUserName << " Wins!" << endl;
        }
        else if (FirstUserChoose == SecondUserChoose)
        {
            cout << "Draw!!!" << endl;
        }
        else
        {
            cout << SecondUserName << " Wins!" << endl;
        }
    }
private:
    string FirstUserName = "Noname";
    string SecondUserName = "Noname";
    int FirstUserChoose = 0;
    int SecondUserChoose = 0;
};
int main()
{
    int FirstUserChoose;
    int SecondUserChoose;
    string FirstUserName;
    string SecondUserName;
    cout << "Player 1 enter your name: " << endl;
    cin >> FirstUserName;
    cout << "Player 1 choose your item (1 - Rock, 2 - Paper, 3 - Scissors): " << endl;
    cin >> FirstUserChoose;
    system("cls");
    cout << "Player 2 enter your name: " << endl;
    cin >> SecondUserName;
    cout << "Player 2 choose your item (1 - Rock, 2 - Paper, 3 - Scissors): " << endl;
    cin >> SecondUserChoose;
    system("cls");
    Game first(FirstUserName, FirstUserChoose, SecondUserName, SecondUserChoose);

}
