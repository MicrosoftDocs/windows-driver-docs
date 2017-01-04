---
title: Create a production device submission
description: Create a production device submission
MS-HAID:
- 'p\_dashboard.create\_a\_production\_device\_submission'
- 'hw\_dashboard.create\_a\_production\_device\_submission'
MSHAttr:
- 'PreferredSiteName:MSDN'
- 'PreferredLib:/library/windows/hardware'
ms.assetid: bf7a4e6b-852a-49a9-beb7-9818aea9cae4
---

# Create a production device submission


**Important**  The dashboard submission REST APIs will no longer be available for use as of the end of October 2016. APIs for driver submissions are under consideration for a future release.

 

You can build certification and file signing submissions into your existing development and deployment framework using your organization's service account and file signing services.

## <span id="To_create_a_production_device_submission_request"></span><span id="to_create_a_production_device_submission_request"></span><span id="TO_CREATE_A_PRODUCTION_DEVICE_SUBMISSION_REQUEST"></span>To create a production device submission request


1.  Get the service account credentials of your organization by following the steps in [Manage your service account credentials](https://msdn.microsoft.com/library/windows/hardware/dn800655.aspx#get-account-credentials). If you do not have a service account, follow the steps in [Manage your service account credentials](https://msdn.microsoft.com/library/windows/hardware/dn800655.aspx#new-account). You will use the service account credentials in the **client\_secret** value in the next step.

2.  Get an authentication token from Azure Access Control service (ACS). For more information, see [How to Request SWT Token from ACS](http://go.microsoft.com/fwlink/p/?linkid=507704). Use the following code in the client requesting the token.

    ``` syntax
    string realm = "https://devicesigningservice.cloudapp.net";
    string acsNameSpace = "https://sysdevacs.accesscontrol.windows.net";
    var client = new HttpClient();
    client.BaseAddress = new Uri(acsNameSpace);
    List<KeyValuePair<string, string>> values = new List<KeyValuePair<string, string>>();
    values.Add(new KeyValuePair<string, string>("grant_type", "client_credentials"));
    values.Add(new KeyValuePair<string, string>("client_id", "Fabrikam"));
    values.Add(new KeyValuePair<string, string>("client_secret", "Contoso"));
    values.Add(new KeyValuePair<string, string>("scope", realm));
    var content = new FormUrlEncodedContent(values);
    var responseMessage = client.PostAsync("v2/OAuth2-13", content).Result;
    var jss = new JavaScriptSerializer();
    dynamic responseString = jss.Deserialize<dynamic>(responseMessage.Content.ReadAsStringAsync().Result);
    string token = responseString["access_token"] as string;
    ```

3.  Create a [Dashboard submission objects](https://msdn.microsoft.com/library/windows/hardware/dn800651.aspx#signingrequest) object using the [Create a request](https://msdn.microsoft.com/library/windows/hardware/dn800659.aspx) operation and the authentication token from step 2. The authentication token must be in the header. This initiates the request and returns a Shared Access Signature (SAS) URI.

    ``` syntax
    var json = CreateSubmissionMetadata(new {
    ProductName = "Test",
    MarketingNames = new object[]{
    new {
    Name = "Testing Name",
    Locale = new object[]{
    "English"
    }
    }
    },
    AnnouncementDate = DateTime.Now.AddDays(4).ToString("s"),
    PublishingDate = DateTime.Now.AddDays(6).ToString("s"),
    OSSelections = new object[]{
    new {
    OS = "Windows 8",
    ProductType = "Printer",
    QualificationLevel = "Signature Only"
    }
    },
    InitialUploadFileSize = 1,
    TestHarnessType = "HLK"
    });
     
            static dynamic CreateSubmissionMetadata(dynamic json)
            {
                var SysdevEndpoint = "https://devicesigningservice.cloudapp.net/api/signing/devices";
                HttpRequestMessage createRequest = new HttpRequestMessage()
                {
                    Method = HttpMethod.Post,
                    RequestUri = new Uri(SysdevEndpoint),
                    Content = new StringContent(new JavaScriptSerializer().Serialize(json).ToString())
                };
                createRequest.Content.Headers.ContentType = new MediaTypeHeaderValue("application/json");
                HttpResponseMessage response = null;
                TimeAction("Creating an azure submission took {0} ms", () => { response = SendRequest(createRequest); });
                
                var submissionUrl = response.Headers.Location.ToString();
                var sasUrl = response.Content.ReadAsStringAsync().Result;
     
                return new
                {
                    SasUrl = sasUrl.Substring(1, sasUrl.Length - 2),
                    SubmissionGuid = GetFirstGuidFromUrl(submissionUrl)
                };
            }
            static HttpResponseMessage SendRequest(HttpRequestMessage message)
            {
                Trace.WriteLine("Sending request to " + message.RequestUri);
                using (HttpClient client = new HttpClient())
                {
                    //Trace.WriteLine("Set Bearer header to " + AuthToken);
                    client.DefaultRequestHeaders.Authorization = new AuthenticationHeaderValue("Bearer", AuthToken);
     
                    var resp = client.SendAsync(message).Result;
                    if(resp.IsSuccessStatusCode)
                    {
                        return resp;
                    }
                    else
                    {
                        throw new HttpRequestException("The request failed with status code response: " + resp.StatusCode.ToString());
                    }
                }
            }
    ```

4.  Using the SAS URI from step 3, use the [Azure Storage API](http://go.microsoft.com/fwlink/p/?linkid=507705) to upload your Hardware Certification Kit (HCK) package.

    ``` syntax
    /// <summary>
            /// Uploads the given file using the SAS Url provided. This method can be replaced with a call to the Azure Storage Client API
            /// </summary>
            /// <param name="sasUrl">Sas Url returned from the Sysdev API</param>
            /// <param name="filepath">Path to the file that will be uploaded</param>
            static void UploadFile(string sasUrl, string filepath)
            {
                using (var client = new HttpClient())
                {
                    client.DefaultRequestHeaders.Add("x-ms-version", Version);
                    client.DefaultRequestHeaders.Add("x-ms-client-request-id", SessionGuid);
     
                    StringBuilder sb = new StringBuilder("<?xml version=\"1.0\" encoding=\"utf-8\"?><BlockList>");
     
                    foreach (byte[] chunk in GetFileChunks(filepath))
                    {
                        var blockid = GetHash(chunk);
                        HttpRequestMessage chunkMessage = new HttpRequestMessage()
                        {
                            Method = HttpMethod.Put,
                            RequestUri = new Uri(sasUrl + "&timeout=90&comp=block&blockid=" + WebUtility.UrlEncode(blockid)),
                            Content = new ByteArrayContent(chunk)
                        };
                        chunkMessage.Headers.Add("x-ms-blob-type", "BlockBlob");
                        chunkMessage.Content.Headers.Add("MD5-Content", blockid);
     
                        TimeAction("Uploading chunk " + blockid + " took {0} ms", () =>
                        {
                            var response = client.SendAsync(chunkMessage).Result;
                        });
                        sb.Append("<Latest>");
                        sb.Append(blockid);
                        sb.Append("</Latest>");
                    }
                    sb.Append("</BlockList>");
     
                    Trace.WriteLine(sb.ToString());
     
                    HttpRequestMessage commitMessage = new HttpRequestMessage()
                    {
                        Method = HttpMethod.Put,
                        RequestUri = new Uri(sasUrl + "&timeout=90&comp=blocklist"),
                        Content = new StringContent(sb.ToString())
                    };
                    TimeAction("Commiting the blocks took {0} ms", () =>
                    {
                        var commit = client.SendAsync(commitMessage).Result;
                    });
                }
            }
    ```

5.  After uploading is complete, start the submission process by setting the **UpdateComplete** flag to **true** in the [Update an existing submission](https://msdn.microsoft.com/library/windows/hardware/dn800650.aspx) operation. This notifies Microsoft to start the backend processing.

    ``` syntax
    static void UpdateSubmission(string guid, dynamic json)
            {
                HttpRequestMessage update = new HttpRequestMessage()
                {
                    Method = new HttpMethod("PATCH"),
                    RequestUri = new Uri(SysdevEndpoint + "/" + guid),
                    Content = new StringContent(new JavaScriptSerializer().Serialize(json))
                };
                update.Content.Headers.ContentType = new MediaTypeHeaderValue("application/json");
     
                TimeAction("Updating the information for submission " + guid, () => { var response = SendRequest(update); });
            }
    ```

6.  To poll for status, use the [Get metadata for an existing submission](https://msdn.microsoft.com/library/windows/hardware/dn800658.aspx) operation and evaluate the **Status** value in the response for **Approved**, **Manual Review**, or **Rejected**. Processing can take from 10 minutes to 24 hours.

    ``` syntax
    Trace.WriteLine("Begin waiting for the submission to finish");
                    //Poll for the status of the submission in our system
                    //Give up checking after an hour
                    for (int retryCount = 0; ; retryCount++)
                    {
                        Thread.Sleep(60 * 1000);
                        var submission = GetSubmission(resp.SubmissionGuid);
                        if (String.Compare(submission["Status"], "Completed") == 0)
                        {
                            //Once the submission is finished processing, loop through the signed files and download them
                            foreach (var asset in submission["Assets"])
                            {
                                if (String.Compare(asset["AssetType"], "SignedFile") == 0)
                                {
                                    //Download the signed files from the azure storage blob
                                    DownloadFile(resp.SubmissionGuid, asset["DeviceSigningAssetID"], Path.Combine(outputDirectory, asset["Name"]));
                                }
                            }
                            break;
                        }
                        if (retryCount == 60)
                        {
                            throw new ApplicationException("Submission is taking a long time to process, last status: " + submission["Status"]);
                        }
    ```

## <span id="download"></span><span id="DOWNLOAD"></span>Download an asset


When processing is completed, do the following to download your signed files, the URL to certification verification reports, or the Driver Update Acceptable (DUA) shell package:

1.  If your token is expired, get a new authentication token from ACS.

2.  Retrieve the [Dashboard submission objects](https://msdn.microsoft.com/library/windows/hardware/dn800651.aspx#signingrequestinfo) using the [Get metadata for an existing submission](https://msdn.microsoft.com/library/windows/hardware/dn800658.aspx) operation.

    ``` syntax
    static dynamic GetSubmission(string guid)
            {
                HttpRequestMessage update = new HttpRequestMessage()
                {
                    Method = HttpMethod.Get,
                    RequestUri = new Uri(SysdevEndpoint + "/" + guid)
                };
     
                HttpResponseMessage response = null;
               TimeAction("Getting information for submission "+guid, () => { response = SendRequest(update); });
     
                JavaScriptSerializer jss = new JavaScriptSerializer();
     
                return jss.Deserialize<dynamic>(response.Content.ReadAsStringAsync().Result);
            }
    ```

3.  Use the [Dashboard submission objects](https://msdn.microsoft.com/library/windows/hardware/dn800651.aspx#asset) from the [Dashboard submission objects](https://msdn.microsoft.com/library/windows/hardware/dn800651.aspx#signingrequestinfo) and retrieve the SAS URI using the [Get a specific asset within a submission](https://msdn.microsoft.com/library/windows/hardware/dn800656.aspx) operation.

    ``` syntax
    static Uri GetSasUrlForAsset(string submissionGuid, string assetGuid)
            {
                HttpRequestMessage asset = new HttpRequestMessage()
                {
                    Method = HttpMethod.Get,
                    RequestUri = new Uri(SysdevEndpoint + "/" + submissionGuid + "/assets/" + assetGuid)
                };
     
                HttpResponseMessage get = null;
                TimeAction("Getting the sas url for "+submissionGuid +"/"+assetGuid + "took {0} ms", ()=>{SendRequest(asset);});
     
                return get.Headers.Location;
            }
    ```

4.  Use the [Azure Storage API](http://go.microsoft.com/fwlink/p/?linkid=507706) to download your requested asset.

    ``` syntax
    static void DownloadFile(string submissionGuid, string assetGuid, string filepath, Uri sasUrl)
            {
              using (var client = new HttpClient())
                {
                    client.DefaultRequestHeaders.Add("x-ms-version", Version);
                    client.DefaultRequestHeaders.Add("x-ms-client-request-id", SessionGuid);
     
                    HttpRequestMessage download = new HttpRequestMessage()
                    {
                        Method = HttpMethod.Get,
                        RequestUri = sasUrl
                    };
     
                    using (FileStream fs = new FileStream(filepath, FileMode.CreateNew))
                    {
                        using (var stream = client.SendAsync(download).Result.Content.ReadAsStreamAsync().Result)
                        {
                            byte[] buffer = new byte[ChunkSize];
                            int size = 0;
                            while ((size = stream.Read(buffer, 0, ChunkSize)) > 0)
                            {
                                fs.Write(buffer, 0, size);
                            }
                        }
                    }
                }
            }
    ```

## <span id="related_topics"></span>Related topics


[Dashboard submission REST API reference](https://msdn.microsoft.com/library/windows/hardware/dn800654.aspx)

[Dashboard submission objects](https://msdn.microsoft.com/library/windows/hardware/dn800651.aspx)

[Manage your service account credentials](https://msdn.microsoft.com/library/windows/hardware/dn800655.aspx)

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bhw_dashboard\hw_dashboard%5D:%20Create%20a%20production%20device%20submission%20%20RELEASE:%20%281/3/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")





