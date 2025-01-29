using NetCord;
using NetCord.Gateway;

class Program
{
    public static string? TokenReal;
    static async Task Main()
    {
        ReadToken();

        if (TokenReal == null)
        {
            Console.WriteLine("Token is missing! Exiting...");
            return; 
        }

        GatewayClient client = new(new BotToken(TokenReal!));

        client.Log += message =>
        {
            Console.WriteLine(message);
            return default;
        };

        Yahoo.SpeakNOW();

        await client.StartAsync();
        await Task.Delay(-1);
    }

    static void ReadToken()
    {
        TokenReal = File.ReadAllText("config.txt");
        Console.WriteLine("Connected on " + TokenReal);
    }
}

class Yahoo
{
    public static void SpeakNOW()
    {
         Console.WriteLine("Hello!!!!");
         return;
    }
}