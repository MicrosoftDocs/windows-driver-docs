---
title: Manage product submissions
description: Manage hardware dashboard submissions for your products and get them signed by Microsoft
ms.topic: article
ms.date: 03/31/2022
---

# Manage Product Submissions

Use the following methods in *Microsoft Hardware APIs* to manage submissions for your products and for getting them signed by Microsoft. For an introduction to Microsoft Hardware APIs, including prerequisites for using the API, see [hardware dashboard API](dashboard-api.md).

```cpp      
https://manage.devcenter.microsoft.com/v2.0/my/hardware/products/
```

Methods for managing product submissions

| Method | URI | Description |
|:-|:-|:-|
| GET | `https://manage.devcenter.microsoft.com/v2.0/my/hardware/products/{productID}` | [Get status/data for a specific product](get-a-product.md) |
| GET | `https://manage.devcenter.microsoft.com/v2.0/my/hardware/products/{productID}/submissions/{submissionId}` | [Get status/data for a specific submission of a product](get-a-submission.md) |
| POST | `https://manage.devcenter.microsoft.com/v2.0/my/hardware/products` | [Create a new product](create-a-new-product.md) |
| POST | `https://manage.devcenter.microsoft.com/v2.0/my/hardware/products/{productID}/submissions/` | [Create a new submission for a product](create-a-new-submission-for-a-product.md) |
| POST | `https://manage.devcenter.microsoft.com/v2.0/my/hardware/products/{productID}/submissions/{submissionId}/commit` | [Commit a product submission](commit-a-product-submission.md) |

## Create and submit a product for signing

1. If you have not done so already, complete all the [prerequisites](dashboard-api.md) for the Microsoft Hardware APIs.

1. [Obtain an Microsoft Entra ID access token](dashboard-api.md#obtain-a-microsoft-entra-id-access-token). You must pass this access token to the methods in the Microsoft Store submission API. After you obtain an access token, you have 60 minutes to use it before it expires. After the token expires, you can obtain a new one.

1. [Create a new product](create-a-new-product.md)  by executing the following method in the Microsoft Hardware API. This creates a new in-progress product and allows you to submit packages for this product.

    ```cpp
    https://manage.devcenter.microsoft.com/v2.0/my/hardware/products/
    ```

    The response body contains a [Product resource](get-product-data.md#product-resource) that includes the ID of this product.

1. [Create a submission](create-a-new-submission-for-a-product.md)  for this product by executing the following method in the Microsoft Hardware API.  Use the ProductID created in the step above.

    ```cpp
    https://manage.devcenter.microsoft.com/v2.0/my/hardware/products/{productID}/submissions/
    ```

    The response body contains a [Submission resource](get-product-data.md#submission-resource) which includes the ID of the submission, the shared access signature (SAS) URI for uploading the product (driver) package for the submission to Azure Blob Storage. [!NOTE] > A SAS URI provides access to a secure resource in Azure storage without requiring account keys. For background information about SAS URIs and their use with Azure Blob Storage, see [Shared Access Signatures, Part 1: Understanding the SAS model](/azure/storage/common/storage-sas-overview)  and [Shared Access Signatures, Part 2: Create and use a SAS with Blob storage](/azure/storage/common/storage-sas-overview) .

1. **Upload your package** to the Azure Blob Storage at the location specified by the SAS URI in the previous step.
The following C# code example demonstrates how to upload a package to Azure Blob Storage using the [CloudBlockBlob](/dotnet/api/microsoft.azure.storage.blob.cloudblockblob/) class in the Azure Storage Client Library for .NET. This example assumes that the package has already been written to a stream object.

    ```json
    string sasUrl = "https://productingestionbin1.blob.core.windows.net/ingestion/26920f66-b592-4439-9a9d-fb0f014902ec?sv=2014-02-14&sr=b&sig=usAN0kNFNnYE2tGQBI%2BARQWejX1Guiz7hdFtRhyK%2Bog%3D&se=2016-06-17T20:45:51Z&sp=rwl";
    Microsoft.WindowsAzure.Storage.Blob.CloudBlockBlob blockBob =
        new Microsoft.WindowsAzure.Storage.Blob.CloudBlockBlob(new System.Uri(sasUrl));
    await blockBob.UploadFromStreamAsync(stream);
    ```

1. [Commit the product submission](commit-a-product-submission.md)  by executing the following method. This will alert Hardware Dev Center that you are done with your product submission and validation will be started for the submission.

    ```cpp
    https://manage.devcenter.microsoft.com/v2.0/my/hardware/products/{productID}/submissions/{submissionId}/commit
    ```

1. Check on the commit status by executing the following method to [get the status of the product submission](get-a-submission.md).

    ```cpp
    https://manage.devcenter.microsoft.com/v2.0/my/hardware/products/{productID}/submissions/{submissionId}
    ```

    To confirm the submission status, review the **commitStatus** value in the response body. This value should change from **CommitReceived** to **CommitComplete** if the request succeeds or to **CommitFailed** if there are errors in the request.

   >[!NOTE]
   >The main Search page refreshes about every 10 minutes. To view all of your results as you create them, click **Driver List Page (all)**, at the top of the **Drivers** page of the Partner Center. Although the page takes some time to process and load if you have a lot of submissions, both successful and unsuccessful submissions should be listed when it does load. For more info, see [Find a hardware submission](./hardware-submissions-view.md).

## Code examples

The following code examples demonstrates how to use the Microsoft Hardware API:

- [C# sample](https://download.microsoft.com/download/C/F/4/CF404E53-87A0-4204-BA13-A64B09A237C1/HardwareApiCSharpSample.zip)

## Data resources

The Microsoft Hardware APIs methods for creating and managing product data use the following JSON data resources:

- [Product resource](get-product-data.md#product-resource)
- [Submission resource](get-product-data.md#submission-resource)

## See also

- [hardware dashboard API samples (GitHub)](https://aka.ms/hpc_async_api_samples)
