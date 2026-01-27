using System.Net.Http.Json;
using Microsoft.AspNetCore.Components.Forms;

public class VideoService
{
    private readonly HttpClient _http;

    public VideoService(HttpClient http)
    {
        _http = http;
    }

    public async Task<(string original, string heatmap)> UploadVideo(IBrowserFile file)
    {
        var content = new MultipartFormDataContent();
        content.Add(
            new StreamContent(file.OpenReadStream(200_000_000)),
            "file",
            file.Name
        );

        var response = await _http.PostAsync("api/video/upload", content);
        response.EnsureSuccessStatusCode();

        var result = await response.Content.ReadFromJsonAsync<VideoResponse>();

        return (result!.original_video, result.heatmap_video);
    }

    public class VideoResponse
    {
        public string original_video { get; set; } = "";
        public string heatmap_video { get; set; } = "";
    }
}
