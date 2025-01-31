class Authenticator
{
    static void Main()
    {
        if (success == true)
        {
            goto stage1;
        }
    }
    static void stage1()
    {
        if (failed == true)
        {
            goto Main;
        }
        
        if (success == true)
        {
            goto stage2;
        }       
    }
    static void stage2()
    {
        if (failed == true)
        {
            goto Main;
        }

        if (success == true)
        {
            goto stage3;
        }
    }
    static void stage3()
    {
        if (failed == true)
        {
            goto Main;
        }

        if (success == true)
        {
            goto stage4;
        }
    }
    static void stage4()
    {
        if (failed == true)
        {
            goto Main;
        }

        if (success == true)
        {
            goto stage5;
        }
    }
    static void stage5()
    {
        if (failed == true)
        {
            goto Main;
        }
    }
}