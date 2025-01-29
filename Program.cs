using NetCord;
using NetCord.Gateway;

GatewayClient client = new(new BotToken("MTIyNDQzNTM4NjAyNjI5NTMzNw.Gs_g8s.czVnzV8Vkwi-ETO1-Cs0aVlOpX8nyfRdSNz2sk"));

client.Log += message =>
{
    Console.WriteLine(message);
    return default;
};

await client.StartAsync();
await Task.Delay(-1);
