

# Manage hardware submissions using APIs

Use the *Microsoft Hardware APIs* to programmatically query and create
submissions for hardware products within your organization's Windows
Dev Center account. These APIs are useful if your account manages many
products, and you want to automate and optimize the submission process
for these assets. These APIs use Azure Active Directory (Azure AD) to
authenticate the calls from your app or service.

Note the following important steps. They are a necessary part of the end-to-end process for using the Microsoft Hardware API.

- These APIs can only be used by developer accounts that belong to the  [Windows Hardware Dev Center program](https://msdn.microsoft.com/windows/hardware/drivers/dashboard/get-started-with-the-hardware-dashboard).

- You must complete all of the prerequisites.

- Before you call a method in the Microsoft Hardware API, [obtain an
Azure AD access token](#ObtainAADToken). After you obtain a token, you have 60 minutes to use this token in calls to the Microsoft Store submission API before the token expires. After the token expires, you can generate a new token.

- Call the Microsoft Store submission API].

## Step 1: Complete prerequisites for using the Microsoft Hardware API

Before you start writing code to call the Microsoft Hardware API, make
sure that you have completed the following prerequisites.

-   You (or your organization) must have an Azure AD directory and you
    must have [Global
    administrator](http://go.microsoft.com/fwlink/?LinkId=746654)
    permission for the directory. If you already use Office 365 or other
    business services from Microsoft, you already have Azure AD
    directory. Otherwise, you can [create a new Azure AD in Dev
    Center](https://docs.microsoft.com/en-us/windows/uwp/publish/associate-azure-ad-with-dev-center#create-a-brand-new-azure-ad-to-associate-with-your-dev-center-account)
    at no additional charge.

-   You must [associate an Azure AD application with your Windows Dev
    Center account](https://docs.microsoft.com/en-us/windows/uwp/monetize/create-and-manage-submissions-using-windows-store-services#associate-an-azure-ad-application-with-your-windows-dev-center-account) and obtain your tenant ID, client ID and key. You need these values to obtain an Azure AD access token, which you will use in calls to the Microsoft Hardware API.

### How to associate an Azure AD application with your Windows Dev Center account

Before you use the Microsoft Hardware API, you must associate an
Azure AD application with your Dev Center account, retrieve the tenant
ID and client ID for the application and generate a key. The Azure AD
application represents the app or service from which you want to call
the Microsoft Hardware API. You need the tenant ID, client ID and key to
obtain an Azure AD access token that you pass to the API.

1.  In Dev Center, go to your **Account settings**, click **Manage
    users**, and [associate your organization's Dev Center account with
    your organization's Azure AD directory](https://docs.microsoft.com/en-us/windows/uwp/publish/associate-azure-ad-with-dev-center).

2.  In the **Manage users** page, click **Add Azure AD applications**,
    add the Azure AD application that represents the app or service that
    you will use to access submissions for your Dev Center account, and
    assign it the **Manager** role. If this application already exists
    in your Azure AD directory, you can select it on the **Add Azure AD
    applications** page to add it to your Dev Center account. Otherwise,
    you can create a new Azure AD application on the **Add Azure AD
    applications** page. For more information, see [Add Azure AD applications to your Dev Center account](https://docs.microsoft.com/en-us/windows/uwp/publish/add-users-groups-and-azure-ad-applications#azure-ad-applications).

3.  Return to the **Manage users** page, click the name of your Azure AD
    application to go to the application settings, and copy down the
    **Tenant ID** and **Client ID** values.

4.  Click **Add new key**. On the following screen, copy down the
    **Key** value. You won't be able to access this info again after
    you leave this page. For more information, see [Manage keys for an
    Azure AD application](https://docs.microsoft.com/en-us/windows/uwp/publish/add-users-groups-and-azure-ad-applications#manage-keys).

## Step 2: Obtain an Azure AD access token

Before you call any of the methods in the Microsoft Store submission
API, you must first obtain an Azure AD access token that you pass to the
**Authorization** header of each method in the API. After you obtain an
access token, you have 60 minutes to use it before it expires. After the
token expires, you can refresh the token, so you can continue to use it
in further calls to the API.

To obtain the access token, follow the instructions in [Service to
Service Calls Using Client Credentials](https://azure.microsoft.com/documentation/articles/active-directory-protocols-oauth-service-to-service/) to send an HTTP POST to the `https://login.microsoftonline.com/`**<tenant_id>**`/oauth2/token endpoint`.
The following is a sample request.

```
POST https://login.microsoftonline.com/<tenant_id>/oauth2/token
HTTP/1.1

Host: login.microsoftonline.com

Content-Type: application/x-www-form-urlencoded; charset=utf-8

grant\_type=client\_credentials

&client\_id=\<your\_client\_id\>

&client\_secret=\<your\_client\_secret\>

&resource=https://manage.devcenter.microsoft.com
```

For the *tenant\_id* value in the POST URI and the *client\_id* and
*client\_secret* parameters, specify the tenant ID, client ID and the
key for your application that you retrieved from Dev Center in the
previous section. For the *resource* parameter, you must specify
`https://manage.devcenter.microsoft.com`.

After your access token expires, you can refresh it by following the
instructions in [Refreshing the access token](https://azure.microsoft.com/documentation/articles/active-directory-protocols-oauth-code/#refreshing-the-access-tokens).

## Step 3: Use the Microsoft Hardware API

After you have an Azure AD access token, you can call methods in the
Microsoft Hardware API. The API includes many methods that are grouped
into scenarios. To create or update submissions, you typically call
multiple methods in the Microsoft Hardware API in a specific order. For
information about each scenario and the syntax of each method, see the
articles in the following table.


| Scenario     | Description        |
|-|-|
| Drivers      | Get, create and update drivers registered to your Dev Center Account. For more information about these methods, see the following topics: - [Get product data](TBD)
- [Manage product submissions](TBD) |
| | |

## Code examples

You can find detailed C# code examples that demonstrate how to use the Microsoft Hardware API at [submissions for apps, add-ons, and flights](https://docs.microsoft.com/en-us/windows/uwp/monetize/csharp-code-examples-for-the-windows-store-submission-api)

## Additional help

If you have questions about the Microsoft Store submission API or need assistance managing your submissions with this API, visit the [support
    page](https://developer.microsoft.com/en-us/dashboard/account/help?returnUri=https://developer.microsoft.com/en-us/dashboard/hardware)
    and request help.

[]{#GetASubmission .anchor}Get a submission

Use this method in the Microsoft Hardware API to retrieve data for a
specific submission of a product.

[]{#_Toc510098078 .anchor}Prerequisites

If you have not done so already, complete all the
[[prerequisites]{.underline}](#ManageHWUsingAPI) for the Microsoft
Hardware APIs before trying to use any of these methods.

[]{#_Toc510098079 .anchor}Request

This method has the following syntax. See the following sections for
usage examples and descriptions of the header and request body.

  Method   Request URI
  -------- -----------------------------------------------------------------------------------------------------------
  GET      https://manage.devcenter.microsoft.com/ api/v1.0/hardware/products/{productID}/submissions/{submissionID}

[]{#_Toc510098080 .anchor}Request header

  Header          Type     Description
  --------------- -------- ------------------------------------------------------------------------------
  Authorization   string   Required. The Azure AD access token in the form **Bearer** *\<token\>*.
  accept          string   Optional. Specifies the type of content. Allowed value is "application/json"

[]{#_Toc510098081 .anchor}Request parameters

Do not provide request parameters for this method.

[]{#_Toc510098082 .anchor}Request body

Do not provide a request body for this method.

[]{#_Toc510098083 .anchor}Request examples

The following example demonstrates how to retrieve information about all
submissions of a product.

Copy

GET https://manage.devcenter.microsoft.com/api/v1.0/hardware/products/
13635057453741329/submissions/1152921504621441930 HTTP/1.1

Authorization: Bearer \<your access token\>

[]{#_Toc510098084 .anchor}Response

The following example demonstrates the JSON response body returned by a
successful request for a specific submission of a product. For more
details about the values in the response body, see the following
section.

JSON Copy

{

\"id\": 1152921504621442000,

\"productId\": 13635057453741328,

\"workflowStatus\": {

\"currentStep\": \"finalizeIngestion\",

\"state\": \"completed\",

\"messages\": \[\]

},

\"downloads\": {

\"items\": \[

{

\"type\": \"initialPackage\",

\"url\":
\"https://ingestionpackagesint1.blob.core.windows.net/ingestion/dc55b8c6-a01c-40b6-b815-cac8bc08812a?sv=2016-05-31&sr=b&sig=ipjW3RsVC75lZrcEZRh9JmTX89L4gTIKkxwqv9F8Axs%3D&se=2018-03-12T15:32:10Z&sp=rl\"

},

{

\"type\": \"derivedPackage\",

\"url\":
\"https://ingestionpackagesint1.blob.core.windows.net/ingestion/6bd77dbf-a851-46d2-b703-29ea4efae006?sv=2016-05-31&sr=b&sig=O5XQf%2FzMbI2FFt5WwSUJWL1JbWY4JXXPRkCKAnX7IRs%3D&se=2018-03-12T15:32:10Z&sp=rl&rscd=attachment%3B
filename%3DShell\_1152921504621441930.hlkx\"

},

{

\"type\": \"signedPackage\",

\"url\":
\"https://ingestionpackagesint1.blob.core.windows.net/ingestion/0b83a294-c1d1-4136-82a1-dd52f51841e3?sv=2016-05-31&sr=b&sig=zTfxKJmaTwpbFol%2FpAKG0QuXJTTxm5aZ0F2wQQI8whc%3D&se=2018-03-12T15:32:10Z&sp=rl\"

},

{

\"type\": \"certificationReport\",

\"url\": \"https://
manage.devcenter.microsoft.com/en-us/dashboard/hardware/Driver/DownloadCertificationReport/29963920/13635057453741329/1152921504621441930\"

}

\],

\"messages\": \[\]

},

\"links\": \[

{

\"href\":
\"https://manage.devcenter.microsoft.com/api/v1/hardware/products/13635057453741329/submissions/1152921504621441930\",

\"rel\": \"self\",

\"method\": \"GET\"

},

{

\"href\":
\"https://manage.devcenter.microsoft.com/api/v1/hardware/products/13635057453741329/submissions/1152921504621441930\",

\"rel\": \"update\_submission\",

\"method\": \"PATCH\"

}

\],

\"name\": \"HARRY-Duatest2\",

\"type\": \"initial\"

}

[]{#_Toc510098085 .anchor}Response body

Refer [submission resource](#SubmissionResource) for more details

[]{#_Toc510098086 .anchor}Error codes

Refer [error codes](#ErrorCodes) for details.

[]{#ManageDriverSubmissions .anchor}Manage Product Submissions

Use the following methods in *Microsoft Hardware APIs* to manage
submissions for your products and for getting them signed by Microsoft.
For an introduction to Microsoft Hardware APIs, including prerequisites
for using the API, see [Manage hardware submissions using
APIs](#ManageHWUsingAPI).

https://manage.devcenter.microsoft.com/api/v1.0/my/hardware/products/

[]{#_Toc510098088 .anchor}Methods for managing product submissions

+-----------------------+-----------------------+-----------------------+
| Method                | URI                   | Description           |
+=======================+=======================+=======================+
| GET                   | https://manage.devcen | [Get status/data for  |
|                       | ter.microsoft.com/    | a specific            |
|                       | api/v1.0/hardware/pro | product](#GetADriver) |
|                       | ducts/{productID}     |                       |
+-----------------------+-----------------------+-----------------------+
| GET                   | https://manage.devcen | [Get status/data for  |
|                       | ter.microsoft.com/    | a specific submission |
|                       | api/v1.0/hardware/pro | of a                  |
|                       | ducts/{productID}/sub | product](#GetASubmiss |
|                       | missions/             | ion)                  |
|                       |                       |                       |
|                       | {submissionId}        |                       |
+-----------------------+-----------------------+-----------------------+
| POST                  | https://manage.devcen | [Create a new         |
|                       | ter.microsoft.com/    | product](#CreateNewDr |
|                       | api/v1.0/hardware/pro | iver)                 |
|                       | ducts                 |                       |
+-----------------------+-----------------------+-----------------------+
| POST                  | https://manage.devcen | [Create a new         |
|                       | ter.microsoft.com/    | submission for a      |
|                       | api/v1.0/hardware/pro | product](#CreateNewSu |
|                       | ducts/{productID}/sub | bmissionForDriver)    |
|                       | missions/             |                       |
+-----------------------+-----------------------+-----------------------+
| POST                  | https://manage.devcen | [Commit a product     |
|                       | ter.microsoft.com/    | submission](#CommitDr |
|                       | api/v1.0/hardware/pro | iverSubmission)       |
|                       | ducts/{productID}/sub |                       |
|                       | missions/             |                       |
|                       |                       |                       |
|                       | {submissionId}/commit |                       |
+-----------------------+-----------------------+-----------------------+
| PUT                   |                       | Update product data   |
+-----------------------+-----------------------+-----------------------+
| PUT                   |                       | Update submission     |
|                       |                       | data                  |
+-----------------------+-----------------------+-----------------------+

[]{#_Toc510098089 .anchor}Create and submit a product for signing

1.  If you have not done so already, complete all the
    [[prerequisites]{.underline}](#ManageHWUsingAPI) for the Microsoft
    Hardware APIs.

2.  [Obtain an Azure AD access token](#ObtainAADToken). You must pass
    this access token to the methods in the Microsoft Store submission
    API. After you obtain an access token, you have 60 minutes to use it
    before it expires. After the token expires, you can obtain a new
    one.

3.  [Create a new product](#CreateNewDriver) by executing the following
    method in the Microsoft Hardware API. This creates a new in-progress
    product and allows you to submit packages for this product.

    https://manage.devcenter.microsoft.com/api/v1.0/my/hardware/products/

    The response body contains a [product resource](#ProductResource)
    that includes the ID of this product.

4.  [Create a submission](#CreateNewSubmissionForDriver) for this
    product by executing the following method in the Microsoft Hardware
    API. Use the ProductID created in the step above.

    https://manage.devcenter.microsoft.com/api/v1.0/my/hardware/products/{productID}/submissions/

    The response body contains a [submission
    resource](#SubmissionResource) which includes the ID of the
    submission, the shared access signature (SAS) URI for uploading the
    product (driver) package for the submission to Azure Blob storage.
    \[!NOTE\] \> A SAS URI provides access to a secure resource in Azure
    storage without requiring account keys. For background information
    about SAS URIs and their use with Azure Blob storage, see [Shared
    Access Signatures, Part 1: Understanding the SAS
    model](https://azure.microsoft.com/documentation/articles/storage-dotnet-shared-access-signature-part-1)
    and [Shared Access Signatures, Part 2: Create and use a SAS with
    Blob
    storage](https://azure.microsoft.com/documentation/articles/storage-dotnet-shared-access-signature-part-2/).

5.  **Upload your package** to the Azure Blob storage at the location
    specified by the SAS URI in the previous step.

    The following C\# code example demonstrates how to upload a package
    to Azure Blob storage using the
    [CloudBlockBlob](https://msdn.microsoft.com/library/azure/microsoft.windowsazure.storage.blob.cloudblockblob.aspx)
    class in the Azure Storage Client Library for .NET. This example
    assumes that the package has already been written to a stream
    object.

> C\# Copy
>
> string sasUrl =
> \"https://productingestionbin1.blob.core.windows.net/ingestion/26920f66-b592-4439-9a9d-fb0f014902ec?sv=2014-02-14&sr=b&sig=usAN0kNFNnYE2tGQBI%2BARQWejX1Guiz7hdFtRhyK%2Bog%3D&se=2016-06-17T20:45:51Z&sp=rwl\";
>
> Microsoft.WindowsAzure.Storage.Blob.CloudBlockBlob blockBob =
>
> new Microsoft.WindowsAzure.Storage.Blob.CloudBlockBlob(new
> System.Uri(sasUrl));
>
> await blockBob.UploadFromStreamAsync(stream);

6.  [Commit the product submission](#CommitDriverSubmission) by
    executing the following method. This will alert Hardware Dev Center
    that you are done with your product submission and validation will
    be started for the submission.

    https://manage.devcenter.microsoft.com/api/v1.0/my/hardware/products/{productID}/submissions/{submissionId}/commit

7.  Check on the commit status by executing the following method to [get
    the status of the product submission](#GetASubmission).

    https://manage.devcenter.microsoft.com/api/v1.0/my/hardware/products/{productID}/submissions/{submissionId}

    To confirm the submission status, review the *commitStatus* value in
    the response body. This value should change from *commitReceived* to
    *commitCompleted* if the request succeeds or to *commitFailed* if
    there are errors in the request. If there are errors, the *error*
    field contains further details about the error.

[]{#_Toc510098090 .anchor}Code examples

The following articles provide detailed code examples that demonstrate
how to use the Microsoft Hardware API:

-   [C\# sample: \<link
    > TBD\>](https://docs.microsoft.com/en-us/windows/uwp/monetize/csharp-code-examples-for-the-windows-store-submission-api)

[]{#_Toc510098091 .anchor}Data resources

The Microsoft Hardware APIs methods for creating and managing product
data use the following JSON data resources:

-   [Product resource](#ProductResource)

-   [Submission resource](#SubmissionResource)

[]{#CreateNewDriver .anchor}Create a new product

Use this method in the Microsoft Hardware API to create a new hardware
product.

[]{#_Toc510098093 .anchor}Prerequisites

If you have not done so already, complete all the
[[prerequisites]{.underline}](#ManageHWUsingAPI) for the Microsoft
Hardware APIs before trying to use any of these methods.

[]{#_Toc510098094 .anchor}Request

This method has the following syntax. See the following sections for
usage examples and descriptions of the header and request body.

  Method   Request URI
  -------- --------------------------------------------------------------------
  POST     https://manage.devcenter.microsoft.com/ api/v1.0/hardware/products

[]{#_Toc510098095 .anchor}Request header

  Header          Type     Description
  --------------- -------- ------------------------------------------------------------------------------
  Authorization   string   Required. The Azure AD access token in the form **Bearer** *\<token\>*.
  accept          string   Optional. Specifies the type of content. Allowed value is "application/json"

[]{#_Toc510098096 .anchor}Request parameters

Do not provide request parameters for this method.

[]{#_Toc510098097 .anchor}Request body

The following example demonstrates the JSON request body for creating a
new product. For more details about the values in the request body, see
the table below the json.

JSON Copy

{

\"ProductName\": \"Test\_Network\_Product2-R\",

\"TestHarness\": \"Attestation\",

\"announcementDate\": \"2018-01-01T00:00:00\",

\"deviceMetadataIds\": \[\],

\"firmwareVersion\": \"980\",

\"deviceType\": \"external\",

\"isTestSign\": false,

\"marketingNames\": \[\],

\"productName\": \"VST\_apdevtest1\",

\"selectedProductTypes\": {

\"windows\_v100\_RS3\": \"Unclassified\"

},

\"requestedSignatures\": \[

\"WINDOWS\_v100\_RS3\_FULL\",

\"WINDOWS\_v100\_X64\_RS3\_FULL\",

\"WINDOWS\_VISTA\"

\],

\"additionalAttributes\": {},

\"packageType\": \"HLK\"

}

For details on the fields in the request, refer [product
resource](#ProductResource)

[]{#_Toc510098098 .anchor}Request examples

The following example demonstrates how to create a new product.

Copy

POST https://manage.devcenter.microsoft.com/api/v1.0/hardware/products
HTTP/1.1

Authorization: Bearer \<your access token\>

[]{#_Toc510098099 .anchor}Response

The following example demonstrates the JSON response body returned by a
successful request for creating a product. For more details about the
values in the response body, see the following section.

JSON Copy

{

\"id\": 14631253285588838,

\"sharedProductId\": 1152921504607010608,

\"links\": \[

{

\"href\": \"https://
manage.devcenter.microsoft.com/api/v1/hardware/products/14631253285588838\",

\"rel\": \"self\",

\"method\": \"GET\"

},

{

\"href\": \"https://
manage.devcenter.microsoft.com/api/v1/hardware/products/14631253285588838/submissions\",

\"rel\": \"get\_submissions\",

\"method\": \"GET\"

}

\],

\"isCommitted\": false,

\"isExtensionInf\": false,

\"announcementDate\": \"2018-01-01T00:00:00\",

\"deviceMetadataIds\": \[\],

\"firmwareVersion\": \"980\",

\"deviceType\": \"external\",

\"isTestSign\": false,

\"marketingNames\": \[\],

\"productName\": \"VST\_apdevtest1\",

\"selectedProductTypes\": {

\"windows\_v100\_RS3\": \"Unclassified\"

},

\"requestedSignatures\": \[

\"WINDOWS\_v100\_RS3\_FULL\",

\"WINDOWS\_v100\_X64\_RS3\_FULL\",

\"WINDOWS\_VISTA\"

\],

\"additionalAttributes\": {},

\"testHarness\": \"attestation\"

}

[]{#_Toc510098100 .anchor}Response body

Refer [product resource](#ProductResource) for more details

[]{#_Toc510098101 .anchor}Error codes

Refer [error codes](#ErrorCodes) for details.

[]{#CreateNewSubmissionForDriver .anchor}Create a new submission for a
product

Use this method in the Microsoft Hardware API to create a new submission
for a product. Prior to using this method ensure you have created a new
product. For details, see [create a new product](#CreateNewDriver).

[]{#_Toc510098103 .anchor}Prerequisites

If you have not done so already, complete all the
[[prerequisites]{.underline}](#ManageHWUsingAPI) for the Microsoft
Hardware APIs before trying to use any of these methods.

[]{#_Toc510098104 .anchor}Request

This method has the following syntax. See the following sections for
usage examples and descriptions of the header and request body.

  Method   Request URI
  -------- --------------------------------------------------------------------------------------------
  POST     https://manage.devcenter.microsoft.com/ api/v1.0/hardware/products/{productID}/submissions

The productId in the method is the product for which the submission is
intended.

[]{#_Toc510098105 .anchor}Request header

  Header          Type     Description
  --------------- -------- ------------------------------------------------------------------------------
  Authorization   String   Required. The Azure AD access token in the form **Bearer** *\<token\>*.
  Accept          String   Optional. Specifies the type of content. Allowed value is "application/json"

[]{#_Toc510098106 .anchor}Request parameters

Do not provide request parameters for this method.

[]{#_Toc510098107 .anchor}Request body

The following example demonstrates the JSON request body for creating a
new submission.

JSON Copy

{

\"name\": \"VST\_apdevtest1\_init\",

\"type\": \"initial\"

}

For details on the fields in the request, refer [submission
resource](#SubmissionResource)

[]{#_Toc510098108 .anchor}Request examples

The following example demonstrates how to create a new submission.

Copy

POST
https://manage.devcenter.microsoft.com/api/v1.0/hardware/products/14631253285588838/submissions
HTTP/1.1

Authorization: Bearer \<your access token\>

[]{#_Toc510098109 .anchor}Response

The following example demonstrates the JSON response body returned by a
successful request for creating a new submission for a product. For more
details about the values in the response body, see the following
section.

JSON Copy

{

\"id\": 1152921504621465124,

\"productId\": 14631253285588838,

\"downloads\": {

\"items\": \[

{

\"type\": \"initialPackage\",

\"url\":
\"https://ingestionpackagesint1.blob.core.windows.net/ingestion/38c19eaf-7377-4834-893c-28d5791f7896?sv=2017-04-17&sr=b&sig=SlD5j5e067oA4Y3hdk1sPW3UycTSUVlIp80WbWvj4A8%3D&se=2018-03-20T05:00:14Z&sp=rwl\"

}

\],

\"messages\": \[\]

},

\"links\": \[

{

\"href\":
\"https://manage.devcenter.microsoft.com/api/v1/hardware/products/14631253285588838/submissions/1152921504621465124\",

\"rel\": \"self\",

\"method\": \"GET\"

},

{

\"href\":
\"https://manage.devcenter.microsoft.com/api/v1/hardware/products/14631253285588838/submissions/1152921504621465124\",

\"rel\": \"update\_submission\",

\"method\": \"PATCH\"

}

\],

\"commitStatus\": \"commitPending\",

\"name\": \"VST\_apdevtest1\_init\",

\"type\": \"initial\"

}

[]{#_Toc510098110 .anchor}Response body

Refer [submission resource](#SubmissionResource) for more details

[]{#_Toc510098111 .anchor}Error codes

Refer [error codes](#ErrorCodes) for details.

[]{#CommitDriverSubmission .anchor}Commit a product submission

Use this method in the Microsoft Hardware API to commit a new submission
to Hardware Dev Center. This will alert Hardware Dev Center that you are
done with your product submission and validation will be started for the
submission.

[]{#_Toc510098113 .anchor}Prerequisites

If you have not done so already, complete all the
[[prerequisites]{.underline}](#ManageHWUsingAPI) for the Microsoft
Hardware APIs before trying to use any of these methods.

Another prerequisite to commit a submission is to complete the upload of
the driver package to the SAS URI provided while [creating a new
submission](#CreateNewSubmissionForDriver). For more information about
how the commit operation fits into the process of submitting a product
app by using the Microsoft Hardware API, see [manage product
submissions](#ManageDriverSubmissions).

[]{#_Toc510098114 .anchor}Request

This method has the following syntax. See the following sections for
usage examples and descriptions of the header and request body.

  Method   Request URI
  -------- ------------------------------------------------------------------------------------------------------------------
  POST     https://manage.devcenter.microsoft.com/ api/v1.0/hardware/products/{productID}/submissions/{submissionID}/commit

The productId in the method is the product for which the submission is
intended. The submssionID in the method is the submission which is being
committed.

[]{#_Toc510098115 .anchor}Request header

  Header          Type     Description
  --------------- -------- ------------------------------------------------------------------------------
  Authorization   String   Required. The Azure AD access token in the form **Bearer** *\<token\>*.
  accept          String   Optional. Specifies the type of content. Allowed value is "application/json"

[]{#_Toc510098116 .anchor}Request parameters

Do not provide request parameters for this method.

[]{#_Toc510098117 .anchor}Request body

Do not provide request body for this method.

[]{#_Toc510098118 .anchor}Request examples

The following example demonstrates how to commit a submission.

Copy

POST
https://manage.devcenter.microsoft.com/api/v1.0/hardware/products/14631253285588838/submissions/
1152921504621465124/commit HTTP/1.1

Authorization: Bearer \<your access token\>

[]{#_Toc510098119 .anchor}Response

The following example demonstrates the JSON response body returned by a
successful request for creating a new submission for a product. For more
details about the values in the response body, see the following
section.

JSON Copy

{

\"commitStatus\": \"commitStarted\",

}

[]{#_Toc510098120 .anchor}Response body

  Value          Type     Description
  -------------- -------- -------------------------------------------------------------------------
  commitStatus   string   The status of the submission. The value returned would be CommitStarted

After this step, use the method [get submission
details](#GetASubmission) to get the status of the submission.

[]{#_Toc510098121 .anchor}Error codes

Refer [error codes](#ErrorCodes) for details.
