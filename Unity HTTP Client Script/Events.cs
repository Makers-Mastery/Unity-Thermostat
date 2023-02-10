using UnityEngine;
using UnityEngine.UI;

using Valve.VR.InteractionSystem;
using CI.HttpClient;









public class Events : MonoBehaviour
{
    public int localTemp = 70;
    public void OnUpPress(Hand hand)
    {
        localTemp = localTemp + 1;
        Debug.Log("SteamVR Up Button pressed!");
        Debug.Log("local temp = " + localTemp.ToString());

        var client = new HttpClient();

        client.Put(new System.Uri("http://192.168.137.142:8000"), new StringContent(localTemp.ToString()), HttpCompletionOption.AllResponseContent, (r) =>
        {
            // Raised either when the download completes or periodically depending on the HttpCompletionOption
        }, (u) =>
        {
            // Raised periodically when uploading, this callback does not need to be specified
        });

        System.Net.ServicePointManager.ServerCertificateValidationCallback += (o, certificate, chain, errors) =>
        {
            return true;
        };
    }
    public void OnDownPress(Hand hand)
    {
        localTemp = localTemp - 1;
        // StringContent stringContent = new StringContent(localTemp.ToString(), Encoding.UTF8, "text/plain");
        Debug.Log("SteamVR Down Button pressed!");
        Debug.Log("local temp = " + localTemp.ToString());

        var client = new HttpClient();

        client.Put(new System.Uri("http://192.168.137.142:8000"), new StringContent(localTemp.ToString()), HttpCompletionOption.AllResponseContent, (r) =>
        {
            // Raised either when the download completes or periodically depending on the HttpCompletionOption
        }, (u) =>
        {
            // Raised periodically when uploading, this callback does not need to be specified
        });

        System.Net.ServicePointManager.ServerCertificateValidationCallback += (o, certificate, chain, errors) =>
        {
            return true;
        };
    }

    [SerializeField]
    public Text _text;
    public void OnCustomButtonPress()
    {
        
        Debug.Log("We pushed our custom button!");
        //string textUp = ToString(localTemp);
        _text.text = localTemp.ToString();
    }
}
