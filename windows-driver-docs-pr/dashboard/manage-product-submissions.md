---
title: Manage Product Submissions
description: Manage hardware dashboard submissions for your products and get them signed by Microsoft.
ms.topic: article
ms.date: 09/19/2024
---

# Manage product submissions

Use the following methods in *Microsoft Hardware APIs* to manage submissions for your products and for getting them signed by Microsoft. For an introduction to Microsoft Hardware APIs, including prerequisites for using the API, see [Hardware dashboard API](dashboard-api.md).

`https://manage.devcenter.microsoft.com/v2.0/my/hardware/products/`

Methods for managing product submissions

| Method | URI | Description |
|:-|:-|:-|
| GET | `https://manage.devcenter.microsoft.com/v2.0/my/hardware/products/{productID}` | [Get status/data for a specific product](get-a-product.md) |
| GET | `https://manage.devcenter.microsoft.com/v2.0/my/hardware/products/{productID}/submissions/{submissionId}` | [Get status/data for a specific submission of a product](get-a-submission.md) |
| POST | `https://manage.devcenter.microsoft.com/v2.0/my/hardware/products` | [Create a new product](create-a-new-product.md) |
| POST | `https://manage.devcenter.microsoft.com/v2.0/my/hardware/products/{productID}/submissions/` | [Create a new submission for a product](create-a-new-submission-for-a-product.md) |
| POST | `https://manage.devcenter.microsoft.com/v2.0/my/hardware/products/{productID}/submissions/{submissionId}/commit` | [Commit a product submission](commit-a-product-submission.md) |

## Create and submit a product for signing

1. Complete all the [prerequisites](dashboard-api.md) for the Microsoft Hardware APIs.

1. [Obtain a Microsoft Entra ID access token](dashboard-api.md#obtain-a-microsoft-entra-id-access-token). You must pass this access token to the methods in the Microsoft Store submission API. After you obtain an access token, you have 60 minutes to use it before it expires. After the token expires, you can obtain a new one.

1. [Create a new product](create-a-new-product.md) by executing the following method in the Microsoft Hardware API. This method creates a new in-progress product and allows you to submit packages for this product.

    `https://manage.devcenter.microsoft.com/v2.0/my/hardware/products/`

    The response body contains a [Product resource](get-product-data.md#product-resource) that includes the ID of this product.

1. [Create a submission](create-a-new-submission-for-a-product.md) for this product by executing the following method in the Microsoft Hardware API. Use the ProductID created in the previous step.

    `https://manage.devcenter.microsoft.com/v2.0/my/hardware/products/{productID}/submissions/`

    The response body contains a [Submission resource](get-product-data.md#submission-resource) which includes the ID of the submission, the shared access signature (SAS) URI for uploading the product (driver) package for the submission to Azure Blob Storage. [!NOTE] > A SAS URI provides access to a secure resource in Azure storage without requiring account keys. For background information about SAS URIs and their use with Azure Blob Storage, see [Grant limited access to Azure Storage resources using shared access signatures (SAS)](/azure/storage/common/storage-sas-overview).

1. **Upload your package** to the Azure Blob Storage at the location specified by the SAS URI in the previous step.
The following C# code example demonstrates how to upload a package to Azure Blob Storage using the [BlockBlobClient](/dotnet/api/azure.storage.blobs.specialized.blockblobclient/) class in the Azure Storage Blobs Library for .NET. This example assumes that the package is already written to a stream object.

    ```json
    string sasUrl = "<SAS URL from Hardware API>";
    Azure.Storage.Blobs.Specialized.BlockBlobClient blockBlobClient =
        new Azure.Storage.Blobs.Specialized.BlockBlobClient(new System.Uri(sasUrl));
    string filePath = "<Path to HLK package>";
    using (FileStream fileStream = File.OpenRead(filePath))
    { 
        await blockBlobClient.UploadAsync(fileStream);
    }
    ```

1. [Commit the product submission](commit-a-product-submission.md) by executing the following method. This method alerts Hardware Dev Center that you're done with your product submission and validation starts for the submission.

    `https://manage.devcenter.microsoft.com/v2.0/my/hardware/products/{productID}/submissions/{submissionId}/commit`

1. Check on the commit status by executing the following method to [get the status of the product submission](get-a-submission.md).

    `https://manage.devcenter.microsoft.com/v2.0/my/hardware/products/{productID}/submissions/{submissionId}`

    To confirm the submission status, review the **commitStatus** value in the response body. This value should change from **CommitReceived** to **CommitComplete** if the request succeeds or to **CommitFailed** if there are errors in the request.

   >[!NOTE]
   >The main Search page refreshes about every 10 minutes. To view all of your results as you create them, click **Driver List Page (all)**, at the top of the **Drivers** page of the Partner Center. Although the page takes some time to process and load if you have a lot of submissions, both successful and unsuccessful submissions should be listed when it does load. For more info, see [Find a hardware submission](./hardware-submissions-view.md).

## Code example

The following code example demonstrates how to use the Microsoft Hardware API:

- [C# sample](https://download.microsoft.com/download/C/F/4/CF404E53-87A0-4204-BA13-A64B09A237C1/HardwareApiCSharpSample.zip)

## Data resources

The Microsoft Hardware APIs methods for creating and managing product data use the following JSON data resources:

- [Product resource](get-product-data.md#product-resource)
- [Submission resource](get-product-data.md#submission-resource)

## See also

- [Hardware dashboard API samples (GitHub)](https://aka.ms/hpc_async_api_samples)
