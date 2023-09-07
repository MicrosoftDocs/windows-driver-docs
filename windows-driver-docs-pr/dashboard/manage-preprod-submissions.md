---
title: Manage Preprod submissions
description: Manage Preprod driver submissions to Hardware Dev Center to get them signed for preproduction testing.
ms.date: 08/04/2022
---

# Manage Preprod Submissions

Use the following methods in *Microsoft Hardware APIs* to manage preprod submissions and for getting your driver packages signed by Microsoft for preproduction testing use. For an introduction to Microsoft Hardware APIs, including prerequisites for using the API, see [Hardware dashboard API](dashboard-api.md).

```csharp
https://manage.devcenter.microsoft.com/v2.0/my/hardware/products/
```

Methods for managing product submissions

| Method | URI | Description |
|:--|:--|:--|
| PUT | `https://manage.devcenter.microsoft.com/v2.0/my/hardware/preprod/packages/` | Submit a package for preprod signing |
| GET | `https://manage.devcenter.microsoft.com/v2.0/my/hardware/preprod/packages/{packageId}` | Get package metadata for a preprod submission |
| GET | `https://manage.devcenter.microsoft.com/v2.0/my/hardware/preprod/packages/{packageId}/assets` | Get available assets for a preprod submission  |
| GET | `https://manage.devcenter.microsoft.com/v2.0/my/hardware/preprod/packages/{packageId}/assets/{assetId}` | Get asset metadata for a single asset |
| GET | `https://manage.devcenter.microsoft.com/v2.0/my/hardware/preprod/packages/{packageId}/assets/{assetId}/download` | Download an asset for a given preprod submission |

Package Metadata Resource

| ID | Unique identifier of the package |
|:--|:--|
| signingStatus | <ul><li> NotStarted</li><li> Processing</li><li> Succeeded</li><li> Failed</li></ul> |
| Error | Errors encountered during package processing |

Asset Metadata Resource

| ID | Unique identifier of the asset |
|:--|:--|
| packageID | Identifier of the package that this asset belongs to |
| assetType | The type of asset available for download. Possible values are: <ul><li> “SignedFilesZip”: package signed by Microsoft.</li></ul> |
| contentHash | SHA-256 hash of the content |

## Create and submit a product for signing

1. If you have not done so already, complete all the [prerequisites](dashboard-api.md) for the Microsoft Hardware APIs.

2. [Obtain an Azure Entra Identity access token](dashboard-api.md). You must pass this access token to the methods in the Microsoft Store submission API. After you obtain an access token, you have 60 minutes to use it before it expires. After the token expires, you can obtain a new one.

3. Create a new submission by executing the following method in the Microsoft Hardware API. The request body should contain your package stream as "application/octet-stream". This will creates a new in-progress preprod submission with HDC. Ensure that the package is signed in the same way you would for [attestation](code-signing-attestation.md) submissions before uploading.

    ```
    PUT https://manage.devcenter.microsoft.com/v2.0/my/hardware/preprod/packages/
    ```

    The response body contains the **id** of the package which will be the packageId for subsequent steps.
    ```json
    {
        "id": "string",
        "etag": "string",
        "lastModified": "2022-03-28T23:31:17.014Z",
        "signingStatus": "NotStarted",
        "error": 
        {
            "message": "string"
        }
    }
    ```


4. Check on the status by executing the following method to get the package metadata.

    ```
    GET https://manage.devcenter.microsoft.com/v2.0/my/hardware/preprod/packages/{packageId}
    ```

    To confirm the package status, review the **signingStatus** value in the response body. This value should change from **Processing** to **Succeeded** if the submission succeeds, or to **Failed** if there are errors in the request. If there are errors, the *error* field contains further details about the error.

    If the **signingStatus** is **Succeeded** a signed package should be available in the assets field.

    ```json
    {
    "id": "string",
    "etag": "string",
    "lastModified": "2022-03-28T23:45:25.501Z",
    "signingStatus": "NotStarted",
    "error": {
        "message": "string"
    },
    "assets": [
        {
        "id": "string",
        "packageId": "string",
        "assetType": "string",
        "createdDate": "2022-03-28T23:45:25.501Z",
        "contentHash": "string"
        }
    ],
    "assetsContinuationToken": "string"
    }
    ```


5. Download your preprod signed package by using the following method to download an asset once **signingStatus** is **Succeeded**. Use the id for the signed asset from the metadata retrieved in step 4 as your assetId in the request. The downloaded package will include the signed driver files as a zip. 
    ```
    GET https://manage.devcenter.microsoft.com/v2.0/my/hardware/preprod/packages/{packageId}/assets/{assetId}/download
    ```

## Example Submit Package for Preprod Signing Code
```csharp
    var httpClient = new HttpClient();
    httpClient.BaseAddress = new Uri(https://manage.devcenter.microsoft.com/v2.0/my/hardware/);
    httpClient.DefaultRequestHeaders.Accept.Clear();
    httpClient.DefaultRequestHeaders.Accept.Add(
        new MediaTypeWithQualityHeaderValue("*/*"));

    httpClient.DefaultRequestHeaders.Authorization = new AuthenticationHeaderValue("bearer", token);

    var driverPackage = File.ReadAllBytes(@"C:\cabfile.cab");
    Task<HttpResponseMessage> response = httpClient.PutAsync("preprod/packages", new ByteArrayContent(driverPackage));
    var jsonResponse = response.Result.Content.ReadFromJsonAsync<object>().Result as JsonElement?;
    var packageId = jsonResponse?.GetProperty("id").ToString();

```
