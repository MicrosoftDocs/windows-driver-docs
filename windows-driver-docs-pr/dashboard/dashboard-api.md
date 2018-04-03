

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

[]{#GetDriverData .anchor}Get product data

Use the following methods in *Microsoft Hardware APIs* to get data for
hardware products registered to your Dev Center Account. For an
introduction to Microsoft Hardware APIs, including prerequisites for
using the API, see [Manage hardware submissions using
APIs](#ManageHWUsingAPI).

https://manage.devcenter.microsoft.com/api/v1.0/my/hardware/products/

Before you can use these methods, the product must already exist in your
Dev Center account. To create or manage submissions for products, see
the methods in [Manage product submissions](#ManageDriverSubmissions)

+-----------------------+-----------------------+-----------------------+
| Method                | URI                   | Description           |
+=======================+=======================+=======================+
| GET                   | https://manage.devcen | [Get data for all     |
|                       | ter.microsoft.com/    | your                  |
|                       | api/v1.0/hardware/pro | products](#GetAllDriv |
|                       | ducts/                | ers)                  |
+-----------------------+-----------------------+-----------------------+
| GET                   | https://manage.devcen | [Get data for a       |
|                       | ter.microsoft.com/    | specific              |
|                       | api/v1.0/hardware/pro | product](#GetADriver) |
|                       | ducts/{productID}     |                       |
+-----------------------+-----------------------+-----------------------+
| GET                   | https://manage.devcen | [Get data for all     |
|                       | ter.microsoft.com/    | submissions of a      |
|                       | api/v1.0/hardware/pro | product](#GetAllSubmi |
|                       | ducts/{productID}/sub | ssions)               |
|                       | missions              |                       |
+-----------------------+-----------------------+-----------------------+
| GET                   | https://manage.devcen | [Get data for a       |
|                       | ter.microsoft.com/    | specific submission   |
|                       | api/v1.0/hardware/pro | of a                  |
|                       | ducts/{productID}/sub | product](#GetASubmiss |
|                       | missions/             | ion)                  |
|                       |                       |                       |
|                       | {submissionId}        |                       |
+-----------------------+-----------------------+-----------------------+

[]{#_Toc510098036 .anchor}Prerequisites

If you have not done so already, complete all the
[[prerequisites]{.underline}](#ManageHWUsingAPI) for the Microsoft
Hardware APIs before trying to use any of these methods.

[]{#_Toc510098037 .anchor}Data resources

The Microsoft Hardware APIs methods for getting product data use the
following JSON data resources

[]{#ProductResource .anchor}Product resource

This resource represents a hardware product (driver) that is registered
to your account

JSON

{

\"id": 9007199267351834,

"sharedProductId": 1152921504606971100,

"links": \[

{

"href\": \"https://
manage.devcenter.microsoft.com/api/v1.0/hardware/products/9007199267351834\",

\"rel\": \"self\",

\"method\": \"GET\"

},

{

\"href\": \"https://
manage.devcenter.microsoft.com/api/v1.0/hardware/products/9007199267351834/submissions\",

\"rel\": \"get\_submissions\",

\"method\": \"GET\"

}

\],

\"isCommitted\": true,

\"isExtensionInf\": false,

\"deviceMetadataIds\": \[\],

\"deviceType\": \"notSet\",

\"isTestSign\": false,

\"marketingNames\": \[

\"marketing name 1\",

\" marketing name 2\"

\],

\"productName\": \"product name\",

\"selectedProductTypes\": {

\"windows\_v100Server\": \"Unclassified\",

\"windows\_v100\": \"Unclassified\"

},

\"requestedSignatures\": \[

 \"WINDOWS\_v100\_X64\_TH1\_FULL\",

\"WINDOWS\_v63\_X64\"

\],

\"additionalAttributes\": {},

\"testHarness\": \"hlk\",

\" announcementDate \": \"2016-10-22T00:00:00Z\",

}

This resource has the following values

+-----------------------+-----------------------+-----------------------+
| Value                 | Type                  | Description           |
+=======================+=======================+=======================+
| Id                    | Long                  | The private product   |
|                       |                       | ID of the product     |
+-----------------------+-----------------------+-----------------------+
| sharedProductId       | Long                  | The shared product ID |
|                       |                       | of the product        |
+-----------------------+-----------------------+-----------------------+
| Links                 | array of objects      | Refer [link           |
|                       |                       | object](#LinkResource |
|                       |                       | )                     |
|                       |                       | for more details      |
+-----------------------+-----------------------+-----------------------+
| isCommitted           | Boolean               | Indicates whether the |
|                       |                       | product has at least  |
|                       |                       | one committed         |
|                       |                       | submission            |
+-----------------------+-----------------------+-----------------------+
| isExtensionInf        | Boolean               | Indicates whether the |
|                       |                       | product is an         |
|                       |                       | extension driver      |
+-----------------------+-----------------------+-----------------------+
| deviceMetadataIds     | array of GUIDs        | GUIDs which map       |
|                       |                       | device metadata       |
|                       |                       | submissions to the    |
|                       |                       | driver                |
+-----------------------+-----------------------+-----------------------+
| deviceType            | String                | Indicates the type of |
|                       |                       | device. Possible      |
|                       |                       | values are:           |
|                       |                       |                       |
|                       |                       | -   "internal" - An   |
|                       |                       |     internal          |
|                       |                       |     component, device |
|                       |                       |     is part of a      |
|                       |                       |     system and        |
|                       |                       |     connects inside   |
|                       |                       |     the PC            |
|                       |                       |                       |
|                       |                       | -   "external" - An   |
|                       |                       |     external          |
|                       |                       |     component, device |
|                       |                       |     is an external    |
|                       |                       |     device            |
|                       |                       |     (peripheral) that |
|                       |                       |     connects to a PC  |
|                       |                       |                       |
|                       |                       | -   "internalExternal |
|                       |                       | " -                   |
|                       |                       |     Both, device can  |
|                       |                       |     be connected      |
|                       |                       |     internally        |
|                       |                       |     (inside a PC) and |
|                       |                       |     externally        |
|                       |                       |     (peripheral)      |
|                       |                       |                       |
|                       |                       | -   "notSet" -- no    |
|                       |                       |     data available    |
+-----------------------+-----------------------+-----------------------+
| isTestSign            | Boolean               | Indicates whether the |
|                       |                       | product is a test     |
|                       |                       | signed driver. For    |
|                       |                       | more information      |
|                       |                       | about test-signing    |
|                       |                       | driver packages, see  |
|                       |                       | [WHQL Test Signature  |
|                       |                       | Program](https://docs |
|                       |                       | .microsoft.com/en-us/ |
|                       |                       | windows-hardware/driv |
|                       |                       | ers/install/whql-test |
|                       |                       | -signature-program)   |
+-----------------------+-----------------------+-----------------------+
| marketingNames        | array of strings      | Marketing names or    |
|                       |                       | aliases of the        |
|                       |                       | product               |
+-----------------------+-----------------------+-----------------------+
| productName           | String                | The name of the       |
|                       |                       | driver as specified   |
|                       |                       | during creation       |
+-----------------------+-----------------------+-----------------------+
| selectedProductTypes  | dictionary            | Key value pair where  |
|                       |                       | both are strings.     |
|                       |                       |                       |
|                       |                       | **Key** represents    |
|                       |                       | the Operating System  |
|                       |                       | Family Code. For a    |
|                       |                       | list of Operating     |
|                       |                       | System Family Codes,  |
|                       |                       | see [list of OS       |
|                       |                       | family                |
|                       |                       | codes](#OSFamilyCodes |
|                       |                       | ).                    |
|                       |                       |                       |
|                       |                       | **Value** represents  |
|                       |                       | the type of the       |
|                       |                       | product. For a list   |
|                       |                       | of type of products,  |
|                       |                       | see [product          |
|                       |                       | types](#DriverTypes). |
+-----------------------+-----------------------+-----------------------+
| requestedSignatures   | array of strings      | List of operating     |
|                       |                       | system signatures for |
|                       |                       | which product is      |
|                       |                       | certified. For a list |
|                       |                       | of all Operating      |
|                       |                       | systems, see [list of |
|                       |                       | OS codes](#OSCodes)   |
+-----------------------+-----------------------+-----------------------+
| additionalAttributes  | Object                | Refer [additional     |
|                       |                       | attributes            |
|                       |                       | object](#additionalAt |
|                       |                       | tributesObject)       |
|                       |                       | for more details.     |
+-----------------------+-----------------------+-----------------------+
| testHarness           | string                | The type of package   |
|                       |                       | which has been        |
|                       |                       | submitted. Possible   |
|                       |                       | values are            |
|                       |                       |                       |
|                       |                       | -   hlk               |
|                       |                       |                       |
|                       |                       | -   hck               |
|                       |                       |                       |
|                       |                       | -   attestation       |
|                       |                       |                       |
|                       |                       | -   notset            |
+-----------------------+-----------------------+-----------------------+
| announcementDate      | datetime              | The date when the     |
|                       |                       | product will get      |
|                       |                       | included on the       |
|                       |                       | Windows Server        |
|                       |                       | Catalog               |
+-----------------------+-----------------------+-----------------------+

[]{#SubmissionResource .anchor}Submission resource

This resource represents a submission of a product.

JSON

{

\"id\": 1152921504621442000,

\"productId\": 13635057453741328,

\"links\": \[

{

\"href\": \"https://
manage.devcenter.microsoft.com/api/v1.0/hardware/products/13635057453741329/submissions/1152921504621441944\",

\"rel\": \"self\",

\"method\": \"GET\"

}

\],

\"name\": \"HARRY-Duatest2\",

\"type\": \"derived\"

}

This resource has the following values

+-----------------------+-----------------------+-----------------------+
| Value                 | Type                  | Description           |
+=======================+=======================+=======================+
| Id                    | long                  | The ID of the         |
|                       |                       | submission            |
+-----------------------+-----------------------+-----------------------+
| Productid             | long                  | The private product   |
|                       |                       | ID to which this      |
|                       |                       | submission is         |
|                       |                       | associated            |
+-----------------------+-----------------------+-----------------------+
| Links                 | array of objects      | Refer [link           |
|                       |                       | object](#LinkResource |
|                       |                       | )                     |
|                       |                       | for more details      |
+-----------------------+-----------------------+-----------------------+
| Name                  | string                | The name of the       |
|                       |                       | submission            |
+-----------------------+-----------------------+-----------------------+
| Type                  | string                | Indicates whether the |
|                       |                       | submission is an      |
|                       |                       | initial or derived    |
|                       |                       | submission. Possible  |
|                       |                       | values are            |
|                       |                       |                       |
|                       |                       | -   initial           |
|                       |                       |                       |
|                       |                       | -   derived           |
+-----------------------+-----------------------+-----------------------+
| workflowstatus        | object                | This is available     |
|                       |                       | only when retrieving  |
|                       |                       | details of a specific |
|                       |                       | submission. This      |
|                       |                       | object depicts the    |
|                       |                       | status of the         |
|                       |                       | workflow for this     |
|                       |                       | submission. Refer     |
|                       |                       | [workflow status      |
|                       |                       | object](#wokflowstatu |
|                       |                       | sresource)            |
|                       |                       | for more details      |
+-----------------------+-----------------------+-----------------------+
| downloads             | object                | This is available     |
|                       |                       | only when retrieving  |
|                       |                       | details of a specific |
|                       |                       | submission only. This |
|                       |                       | object depicts the    |
|                       |                       | downloads available   |
|                       |                       | for the submission.   |
|                       |                       | Refer [download       |
|                       |                       | object](#downloadobje |
|                       |                       | ct)                   |
|                       |                       | for more details.     |
+-----------------------+-----------------------+-----------------------+

[]{#wokflowstatusresource .anchor}Workflow Status object

This object represents the status of workflow for a given entity

JSON

{

"currentStep\": \" finalizeIngestion\",

\" state\": \" completed\",

\" messages\": \[\]

}

This object has the following values

+-----------------------+-----------------------+-----------------------+
| Value                 | Type                  | Description           |
+=======================+=======================+=======================+
| currentStep           | string                | The name of the       |
|                       |                       | current step in the   |
|                       |                       | overall workflow for  |
|                       |                       | this entity.          |
|                       |                       |                       |
|                       |                       | For ingestion/package |
|                       |                       | submission the        |
|                       |                       | possible values are   |
|                       |                       | (*description in      |
|                       |                       | parenthesis*):        |
|                       |                       |                       |
|                       |                       | -   packageInfoValida |
|                       |                       | tion                  |
|                       |                       |     (*Validating      |
|                       |                       |     Package metadata  |
|                       |                       |     and contents*)    |
|                       |                       |                       |
|                       |                       | -   preparation       |
|                       |                       |     (*Getting package |
|                       |                       |     ready for         |
|                       |                       |     processing*)      |
|                       |                       |                       |
|                       |                       | -   scanning          |
|                       |                       |     (*Scanning        |
|                       |                       |     package contents  |
|                       |                       |     for Malware*)     |
|                       |                       |                       |
|                       |                       | -   validation        |
|                       |                       |     (*Validation of   |
|                       |                       |     test results*)    |
|                       |                       |                       |
|                       |                       | -   catalogCreation   |
|                       |                       |     (*Creating a      |
|                       |                       |     security catalog  |
|                       |                       |     for package*)     |
|                       |                       |                       |
|                       |                       | -   manualReview      |
|                       |                       |     (*Undergoing      |
|                       |                       |     Manual Review*)   |
|                       |                       |                       |
|                       |                       | -   signing (*Signing |
|                       |                       |     the binaries*)    |
|                       |                       |                       |
|                       |                       | -   finalizeIngestion |
|                       |                       |     (*Completing the  |
|                       |                       |     ingestion and     |
|                       |                       |     getting signed    |
|                       |                       |     files ready to    |
|                       |                       |     download or       |
|                       |                       |     publish*)         |
+-----------------------+-----------------------+-----------------------+
| State                 | string                | The state of the      |
|                       |                       | current step.         |
|                       |                       | Possible values are:  |
|                       |                       |                       |
|                       |                       | -   notStarted        |
|                       |                       |                       |
|                       |                       | -   started           |
|                       |                       |                       |
|                       |                       | -   failed            |
|                       |                       |                       |
|                       |                       | -   completed         |
+-----------------------+-----------------------+-----------------------+
| Messages              | array                 | -   An array of       |
|                       |                       |     strings to        |
|                       |                       |     provide messages  |
|                       |                       |     about current     |
|                       |                       |     step (especially  |
|                       |                       |     in case of        |
|                       |                       |     failure)          |
+-----------------------+-----------------------+-----------------------+

[]{#downloadobject .anchor}Download object

This object represents the downloads for a given submission.

JSON

{

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

}

This object has the following values

+-----------------------+-----------------------+-----------------------+
| Value                 | Type                  | Description           |
+=======================+=======================+=======================+
| Items                 | array                 | An array of download  |
|                       |                       | types and the URL for |
|                       |                       | each. Please refer    |
|                       |                       | below for details     |
+-----------------------+-----------------------+-----------------------+
| Type                  | string                | The type of package   |
|                       |                       | available for         |
|                       |                       | download. Possible    |
|                       |                       | values are:           |
|                       |                       |                       |
|                       |                       | -   "initialPackage"  |
|                       |                       |     -- package        |
|                       |                       |     uploaded by user  |
|                       |                       |     (in case of new   |
|                       |                       |     submission, it    |
|                       |                       |     points to the SAS |
|                       |                       |     URI for uploading |
|                       |                       |     the package)      |
|                       |                       |                       |
|                       |                       | -   "derivedPackage"  |
|                       |                       |     -- shell for      |
|                       |                       |     derived           |
|                       |                       |     submissions       |
|                       |                       |                       |
|                       |                       | -   "signedPackage"   |
|                       |                       |     -- package signed |
|                       |                       |     by Microsoft      |
|                       |                       |                       |
|                       |                       | -   "certificationRep |
|                       |                       | ort"                  |
|                       |                       |     -- certification  |
|                       |                       |     report for the    |
|                       |                       |     signed product    |
+-----------------------+-----------------------+-----------------------+
| Messages              | array                 | An array of strings   |
|                       |                       | to provide messages   |
|                       |                       | about the             |
|                       |                       | downloadable files    |
+-----------------------+-----------------------+-----------------------+

[]{#LinkResource .anchor}Link object

This object represents a list of helpful links for the containing entity

JSON

{

"href\": \"https://
manage.devcenter.microsoft.com/api/v1.0/hardware/products/9007199267351834\",

\"rel\": \"self\",

\"method\": \"GET\"

}

This object has the following values

+-----------------------+-----------------------+-----------------------+
| Value                 | Type                  | Description           |
+=======================+=======================+=======================+
| Href                  | String                | The URL to access the |
|                       |                       | resource via API      |
+-----------------------+-----------------------+-----------------------+
| Rel                   | String                | Type of the resource. |
|                       |                       | Possible values are:  |
|                       |                       |                       |
|                       |                       | -   self -- Link      |
|                       |                       |     points to itself  |
|                       |                       |                       |
|                       |                       | -   next\_link --     |
|                       |                       |     Link points to    |
|                       |                       |     next resource     |
|                       |                       |     typically used    |
|                       |                       |     for pagination    |
|                       |                       |                       |
|                       |                       | -   get\_submissions  |
|                       |                       |     -- link points to |
|                       |                       |     all submissions   |
|                       |                       |     of a product      |
|                       |                       |                       |
|                       |                       | -   commit\_submissio |
|                       |                       | n                     |
|                       |                       |     -- link points to |
|                       |                       |     commit of a       |
|                       |                       |     submission        |
|                       |                       |                       |
|                       |                       | -   update\_submissio |
|                       |                       | n                     |
|                       |                       |     -- link points to |
|                       |                       |     update of the     |
|                       |                       |     submission        |
+-----------------------+-----------------------+-----------------------+
| Method                | String                | Type of the http      |
|                       |                       | method to be used     |
|                       |                       | when invoking the     |
|                       |                       | URL. Possible values  |
|                       |                       | are                   |
|                       |                       |                       |
|                       |                       | -   GET               |
|                       |                       |                       |
|                       |                       | -   POST              |
|                       |                       |                       |
|                       |                       | -   PATCH             |
+-----------------------+-----------------------+-----------------------+

[]{#additionalAttributesObject .anchor}Additional Attribute object

This object provides additional attributes about the product if it is of
type RAID controller, Storage Controller or Server Virtualization
Validation program (SVVP). It can contain one of three types of objects
-- StorageController, RaidController or SVVP.

**StorageController Object**

  Value                  Type      Description
  ---------------------- --------- ------------------------------------------------------------------------------------------------------------------------
  biosVersion            string    ROM Bios Version
  firmwareVersion        string    Firmware Version
  driverVersion          string    Driver Version
  driverName             string    Driver Name
  deviceVersion          string    Device Version
  chipsetName            string    Chipset Name
  usedProprietary        boolean   Multi-pathing supported through proprietary driver. If true, then proprietaryName and proprietaryVersion are madatory
  proprietaryName        string    Multi-path software name
  proprietaryVersion     string    Multi-path software version
  usedMicrosoft          boolean   Microsoft MPIO supported through device-specific module. If true, then microsoftName and microsoftVersion are madatory
  microsoftName          string    Multi-path software name
  microsoftVersion       string    Multi-path software version
  usedBootSupport        boolean   Boot Support
  usedBetterBoot         boolean   Boot \>2.2TB support. If true, then Supported UEFI version and Supported ACPI version are mandatory
  uefiVersion            string    Supported UEFI version
  acpiVersion            string    Supported ACPI version
  supportsSector4K512E   boolean   Support sector size of 4K/512e
  supportsSector4K4K     boolean   Support sector size of 4K/4K
  supportsDifferential   boolean   Differential (high-voltage differential)

**RaidController Object**

  Value                Type      Description
  -------------------- --------- -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  firmwareVersion      string    Firmware Version
  filterVersion        string    Driver Version
  driverVersion        string    Filter Version
  usedProprietary      boolean   Multi-pathing supported through proprietary driver. If true, then proprietaryName and proprietaryVersion are mandatory
  proprietaryName      string    Multi-path software name
  proprietaryVersion   string    Multi-path software version
  usedMicrosoft        boolean   Microsoft MPIO supported through device-specific module. If true, then microsoftName and microsoftVersion are mandatory
  microsoftName        string    Multi-path software name
  microsoftVersion     string    Multi-path software version
  isThirdPartyNeeded   boolean   Third party non-Microsoft driver needed for connectivity
  isSES                boolean   SES (SCSI Enclosure Services). Indicates if a SES is included. SCSI is the standard term for a service bus that connects devices on a system, originally Small Computer System Interface. SES is short for SCSI Enclosure Services.
  isSAFTE              boolean   SAF-TE (ANBll Specification). Indicates if a SAF-TE is included. ANBll an industry specification. SAF-TE is short for SCSI Accessed Fault Tolerant Enclosures. SCSI is the standard term for a service bus that connects devices on a system, originally Small Computer System Interface.
  additionalInfo       string    Additonal Information

**SVVP Object**

+-----------------------+-----------------------+-----------------------+
| Value                 | Type                  | Description           |
+=======================+=======================+=======================+
| productVersion        | string                | Product Version       |
+-----------------------+-----------------------+-----------------------+
| supportLink           | string                | Support URL           |
+-----------------------+-----------------------+-----------------------+
| guestOs               | string                | Guest OS. Possible    |
|                       |                       | values are:           |
|                       |                       |                       |
|                       |                       | -   Windows Server    |
|                       |                       |     2008              |
|                       |                       |                       |
|                       |                       | -   Windows Server    |
|                       |                       |     2008 Release 2    |
|                       |                       |                       |
|                       |                       | -   Windows Server    |
|                       |                       |     2012              |
|                       |                       |                       |
|                       |                       | -   Windows Server    |
|                       |                       |     2012 R2           |
+-----------------------+-----------------------+-----------------------+
| processorArchitecture | string                | Hardware Processor    |
|                       |                       | Architecture.         |
|                       |                       | Possible values are:  |
|                       |                       |                       |
|                       |                       | -   Xeon              |
|                       |                       |                       |
|                       |                       | -   Opteron           |
|                       |                       |                       |
|                       |                       | -   Itanium 2         |
+-----------------------+-----------------------+-----------------------+
| maxProcessors         | integer               | Max Processors in VM  |
+-----------------------+-----------------------+-----------------------+
| maxMemory             | integer               | Max memory in VM (in  |
|                       |                       | GB)                   |
+-----------------------+-----------------------+-----------------------+

[]{#DriverTypes .anchor}List of Product Types

A product can be of the following types. This information is used along
with the Operating system to identify applicability

-   All In One

-   All In One with Touch

-   Audio Device

-   Bluetooth Controller

-   Bluetooth Controller Non USB

-   Convertible Tablet

-   Desktop

-   Digital Media Renderer

-   Digital Media Server

-   Digital Still Cameras

-   Digital Video Cameras

-   Distribution Scan Management Enabled Devices

-   Enterprise WSD Multi-Function Printer

-   Finger Print Reader

-   Game Controller

-   Generic Controller

-   Generic Portable Device

-   Graphics Adapter WDDM1.0

-   Graphics Adapter WDDM1.1

-   Graphics Adapter WDDM1.2

-   Graphics Adapter WDDM1.2 DisplayOnly

-   Graphics Adapter WDDM1.2 RenderOnly

-   Graphics Tablet

-   Hard Drive

-   Keyboard

-   Keyboard Video Mouse Switch

-   LAN

-   LAN (Server)

-   LAN CS

-   LAN Virtual Machine (Server)

-   Laptop

-   Laptop with Touch

-   LCD

-   Light Sensor

-   Location Sensor

-   Media Player

-   Mobile Broadband CDMA

-   Mobile Broadband GSM

-   Mobile Phone

-   Monitor

-   Motherboard

-   Motion Sensor Fusion

-   Multi-Function Printer

-   Near Field Proximity

-   Network Media Device

-   Optical Drive

-   Pen Digitizer

-   Pointing Drawing

-   Presence Sensor

-   Printer

-   Projector

-   Removable Storage

-   Router

-   Scanner

-   SDIO Controller

-   Server

-   Server Virtualization Validation Program

-   Signature Tablet

-   Smart Cards

-   Smartcard Reader

-   Storage Array

-   Storage Controller

-   Storage Spaces Adapter

-   Storage Spaces Drive

-   Tablet

-   Touch

-   Touch Monitor

-   Ultra-Mobile PC

-   Ultra-Mobile PC with Touch

-   USB Controller

-   USB Hub

-   WebCam

-   WLAN

-   WLAN CSB

-   WSD Multi-Function Printer

-   WSD Printer

-   WSD Scanner

[]{#OSFamilyCodes .anchor}List of Operating System Family Codes

Given below is a list of Operating system Family Codes and their
description

  **OS Family Code**                                     **Description**
  ------------------------------------------------------ -------------------------------
  WindowsMe                                              Windows Me
  Windows2000                                            Windows 2000
  Windows98                                              Windows 98
  WindowsNT40                                            Windows NT 4.0
  WindowsXP                                              Windows XP
  WindowsServer2003                                      Windows Server 2003
  WindowsVista                                           Windows Vista
  Windows2008Server                                      Windows Server 2008
  WindowsHomeServer                                      Windows Home Server
  Windows7                                               Windows 7
  Windows2008ServerR2                                    Windows Server 2008 Release 2
  WindowsServerSolutions                                 Windows Server Solutions
  Windows8                                               Windows 8
  Windows8Server                                         Windows Server 2012
  Windows81                                              Windows 8.1
  Windows81Server                                        Windows Server 2012 R2
  Windows\_v100\_TH1                                     Windows Threshold 1
  Windows\_v100\_TH2                                     Windows Threshold 2
  Windows\_v100\_RS1                                     Windows 10 Anniversary Update
  Windows\_v100Server\_RS1                               Windows Server 2016
  Windows\_v100\_RS2                                     Windows 10 RS2 Update
  Windows\_v100Server\_RS2                               Windows Server RS2
  Windows\_v100\_RS3                                     Windows 10 RS3 Update
  Windows\_v100Server\_RS3                               Windows Server RS3
  WINDOWS\_v100\_ARM64\_RS3\_FULL\_PRE\_RELEASE\_CLOUD   Windows 10 RS3 Update

[]{#OSCodes .anchor}List of Operating System Codes

Given below is a list of Operating System Codes and their description

  **OS Code**                                            **Description**
  ------------------------------------------------------ ----------------------------------------------
  WindowsMe                                              Windows Me
  Windows2000                                            Windows 2000
  Windows98                                              Windows 98
  WindowsNT40                                            Windows NT 4.0
  WindowsXP\_X86                                         Windows XP
  WindowsXP\_IA64                                        Windows XP IA64
  WindowsXP\_X64                                         Windows XP X64
  WindowsXPMediaCenter                                   Windows XP Media Center
  WindowsServer2003\_X86                                 Windows Server 2003
  WindowsServer2003\_IA64                                Windows Server 2003 IA64
  WindowsServer2003\_X64                                 Windows Server 2003 X64
  WindowsVista\_X86                                      Windows Vista Client
  WindowsVista\_X64                                      Windows Vista Client X64
  Windows2008Server\_X86                                 Windows Server 2008
  Windows2008Server\_IA64                                Windows Server 2008 IA64
  Windows2008Server\_X64                                 Windows Server 2008 X64
  WindowsHomeServer                                      Windows Home Server
  Windows7\_X86                                          Windows 7 Client
  Windows7\_X64                                          Windows 7 Client x64
  Windows2008ServerR2\_IA64                              Windows Server 2008 Release 2 IA64
  Windows2008ServerR2\_X64                               Windows Server 2008 Release 2 x64
  WindowsServerSolutions\_X64                            Windows Server Solutions x64
  Windows8\_X86                                          Windows 8 Client
  Windows8\_X64                                          Windows 8 Client x64
  Windows8\_ARM                                          Windows 8 Client RT
  Windows8Server\_X64                                    Windows Server 2012
  Windows81\_X86                                         Windows 8.1 Client
  Windows81\_X64                                         Windows 8.1 Client x64
  Windows81\_ARM                                         Windows 8.1 Client RT
  Windows63Server\_X64                                   Windows Server 2012 R2 x64
  Windows\_v100\_X86\_TH1\_Full                          Windows 10 Client versions 1506 and 1511
  Windows\_v100\_X64\_TH1\_Full                          Windows 10 Client versions 1506 and 1511 x64
  Windows\_v100Server\_X64\_TH1\_Full                    Windows Server 2016 x64
  Windows\_v100\_X86\_TH2\_Full                          Windows 10 Client versions 1506 and 1511
  Windows\_v100\_X64\_TH2\_Full                          Windows 10 Client versions 1506 and 1511 x64
  Windows\_v100Server\_X64\_TH2\_Full                    Windows Server 2016 x64
  Windows\_v100\_X86\_RS1\_Full                          Windows 10 Client version 1607
  Windows\_v100\_X64\_RS1\_Full                          Windows 10 Client version 1607 x64
  Windows\_v100Server\_X64\_RS1\_Full                    Windows Server 2016 x64
  Windows\_v100\_X86\_RS2\_Full                          Windows 10 RS2 Client
  Windows\_v100\_X64\_RS2\_Full                          Windows 10 RS2 Client x64
  Windows\_v100Server\_X64\_RS2\_Full                    Windows Server RS2 x64
  Windows\_v100\_X86\_RS3\_Full                          Windows 10 RS3 Client
  Windows\_v100\_X64\_RS3\_Full                          Windows 10 RS3 Client x64
  Windows\_v100\_ARM64\_RS3\_Full                        Windows 10 RS3 Client ARM64
  Windows\_v100Server\_x64\_RS3\_Full                    Windows Server RS3 x64
  WINDOWS\_v100\_ARM64\_RS3\_FULL\_PRE\_RELEASE\_CLOUD   Windows 10 S RS3 Client ARM64 Pre Release

[]{#ErrorCodes .anchor}Error codes

These error codes are applicable to all web methods of the API.

If the request cannot be successfully completed, the response will
contain one of the following HTTP error codes.

  HTTP Status                    Description
  ------------------------------ -------------------------------------------------------------------------------------------------------------------------
  400 -- Bad Request             Request not well formed (e.g., malformed request syntax, invalid request message framing, or deceptive request routing)
  401 -- Unauthorized            Authentication failed or not provided
  403 -- Forbidden               Forbidden to access a resource
  404 -- Not Found               Entity requested for is not found.
  415 - Unsupported Media Type   Payload is in a format not supported by this method on the target resource.
  422 - Unprocessable Entity     Validation failures.
  500 - Internal Server Error    Unrecoverable error occurred at the API server.

If there are functional validation failures, the response body will
contain one of the following functional error codes.

  Error Code                      Error Message                                                                 Description
  ------------------------------- ----------------------------------------------------------------------------- ----------------------------------------------------------------------------------------------------------------------------
  InvalidInput                                                                                                  Returned when an input validation fails
  RequestInvalidForCurrentState   Only pending submissions can be committed                                     Returned when a commit is applied on a submission which is not in pending state
  RequestInvalidForCurrentState   Initial submission already exists                                             Returned when an initial submission is created for a driver which already has an initial submission
  RequestInvalidForCurrentState   Cannot create derived submission since no initial submission created          Returned when a derived submission is created for a driver which does not have an initial submission
  UpdateUnauthorized              Not authorized to update the product                                          Returned when trying to update a product that was shared (resold) since shared products cannot be updated
  UpdateUnauthorized              Cannot update product without an initial submission                           Returned when trying to update a product which does not have an initial submission
  UpdateUnauthorized              Cannot update product because the workflow has failed                         Returned when trying to update a product which has a failed workflow
  UpdateUnauthorized              Announcement Date cannot be updated after the ingestion process is finished   Returned when announcement date is updated after ingestion is completed
  UpdateUnauthorized              Product Name cannot be updated at this time. Please re-try                    
  UpdateUnauthorized              Not authorized to update the submission                                       Returned when trying to update a submission for a product that was shared (resold) since shared products cannot be updated
  UpdateUnauthorized              Cannot update the submission since the workflows have failed                  Returned when trying to update a submission which has a failed workflow
  EntityNotFound                  No submission found                                                           Returned when trying to commit for a submission which does not exist
  EntityNotFound                  Product not found                                                             Returned when trying to create a submission for which a product does not exist

[]{#GetAllDrivers .anchor}Get all products

Use this method in the Microsoft Hardware API to retrieve data for all
the products registered to your Windows Dev Center account.

[]{#_Toc510098049 .anchor}Prerequisites

If you have not done so already, complete all the
[[prerequisites]{.underline}](#ManageHWUsingAPI) for the Microsoft
Hardware APIs before trying to use any of these methods.

[]{#_Toc510098050 .anchor}Request

This method has the following syntax. See the following sections for
usage examples and descriptions of the header and request body.

  Method   Request URI
  -------- -----------------------------------------------------------------------
  GET      https://manage.devcenter.microsoft.com/api/v1.0/my/hardware/products/

[]{#_Toc510098051 .anchor}Request header

  Header          Type     Description
  --------------- -------- ------------------------------------------------------------------------------
  Authorization   string   Required. The Azure AD access token in the form **Bearer** *\<token\>*.
  accept          string   Optional. Specifies the type of content. Allowed value is "application/json"

[]{#_Toc510098052 .anchor}Request parameters

Do not provide request parameters for this method.

[]{#_Toc510098053 .anchor}Request body

Do not provide a request body for this method.

[]{#_Toc510098054 .anchor}Request examples

The following example demonstrates how to retrieve information about all
products that are registered to your account.

Copy

GET
https://manage.devcenter.microsoft.com/api/v1.0/my/hardware/products/
HTTP/1.1

Authorization: Bearer \<your access token\>

[]{#_Toc510098055 .anchor}Response

The following example demonstrates the JSON response body returned by a
successful request for all the products that are registered to a
developer account. For brevity, this example only shows the data for the
first two products returned by the request. For more details about the
values in the response body, see the following section.

JSON Copy

{

\"value\": \[

{

\"id\": 9007199267351834,

\"sharedProductId\": 1152921504606971100,

\"links\": \[

{

\"href\":
\"https://manage.devcenter.microsoft.com/api/v1/hardware/products/9007199267351834\",

\"rel\": \"self\",

\"method\": \"GET\"

},

{

\"href\":
\"https://manage.devcenter.microsoft.com/api/v1/hardware/products/9007199267351834/submissions\",

\"rel\": \"get\_submissions\",

\"method\": \"GET\"

}

\],

\"isCommitted\": true,

\"isExtensionInf\": false,

\"deviceMetadataIds\": \[\],

\"deviceType\": \"notSet\",

\"isTestSign\": false,

\"marketingNames\": \[\],

\"productName\": \"NewDriverHacked\",

\"selectedProductTypes\": {},

\"requestedSignatures\": \[

\"WINDOWS\_v100\_X64\_TH1\_FULL\",

\"WINDOWS\_v63\_X64\"

\],

\"additionalAttributes\": {},

\"testHarness\": \"hlk\"

},

{

\"id\": 9007199267351836,

\"sharedProductId\": 1152921504606971100,

\"links\": \[

{

\"href\":
\"https://manage.devcenter.microsoft.com/api/v1/hardware/products/9007199267351835\",

\"rel\": \"self\",

\"method\": \"GET\"

},

{

\"href\":
\"https://manage.devcenter.microsoft.com/api/v1/hardware/products/9007199267351835/submissions\",

\"rel\": \"get\_submissions\",

\"method\": \"GET\"

}

\],

\"isCommitted\": true,

\"isExtensionInf\": false,

\"announcementDate\": \"2016-10-22T00:00:00Z\",

\"deviceMetadataCategory\": \"Input.Digitizer.Multitouch\",

\"deviceMetadataIds\": \[\],

\"deviceType\": \"internalExternal\",

\"isTestSign\": false,

\"marketingNames\": \[

\"MEU\"

\],

\"productName\": \"Mew2?\",

\"selectedProductTypes\": {

\"windows\_v100\": \"Touch\",

\"windows81\": \"Unclassified\"

},

\"requestedSignatures\": \[

\"WINDOWS\_v100\_X64\_TH1\_FULL\",

\"WINDOWS\_v63\_X64\"

\],

\"additionalAttributes\": {},

\"testHarness\": \"hlk\"

}

\],

\"links\": \[

{

\"href\":
\"https://manage.devcenter.microsoft.com/api/v1/hardware/products?pageSize=50\",

\"rel\": \"self\",

\"method\": \"GET\"

},

{

\"href\":
\"https://manage.devcenter.microsoft.com/api/v1/hardware/products?pageSize=50&continuationToken=PD94bWwgdmVyc2lvbj0iMS4wIiBlbmNvZGluZz0idXRmLTE2Ij8%2BPENvbnRpbnVhdGlvblRva2VuPjxWZXJzaW9uPjIuMDwvVmVyc2lvbj48VHlwZT5UYWJsZTwvVHlwZT48TmV4dFBhcnRpdGlvbktleT4xITQ4IWNIVmliR2x6YUdWeWN5MHdNREF3TURBd01EQXdNREF3TURBd01ESTVPVFl6T1RJdzwvTmV4dFBhcnRpdGlvbktleT48TmV4dFJvd0tleT4xITk2IWRYTmxjaTFrWld4bGRHVmtMVEF0SUNBZ0lDQWdTR0Z5WkhkaGNtVkVjbWwyWlhJdGNISnZaSFZqZEhNdE1EQXdNREF3TURBd09UQXdOekU1T1RJMk56TTNNakUyTkEtLTwvTmV4dFJvd0tleT48VGFyZ2V0TG9jYXRpb24%2BUHJpbWFyeTwvVGFyZ2V0TG9jYXRpb24%2BPC9Db250aW51YXRpb25Ub2tlbj4%3D\",

\"rel\": \"next\_link\",

\"method\": \"GET\"

}

\]

}

[]{#_Toc510098056 .anchor}Response body

  Value   Type    Description
  ------- ------- ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  value   array   An array of objects that contain information about each product that is registered to your account. For more information about the data in each object, see [Product resource](#ProductResource).
  links   array   An array of objects with helpful links about the containing entity. Refer [link object](#LinkResource) for more details

[]{#_Toc510098057 .anchor}Error codes

Refer [error codes](#ErrorCodes) for details.

[]{#GetADriver .anchor}Get a product

Use this method in the Microsoft Hardware API to retrieve data for a
specific product registered to your Windows Dev Center account.

[]{#_Toc510098059 .anchor}Prerequisites

If you have not done so already, complete all the
[[prerequisites]{.underline}](#ManageHWUsingAPI) for the Microsoft
Hardware APIs before trying to use any of these methods.

[]{#_Toc510098060 .anchor}Request

This method has the following syntax. See the following sections for
usage examples and descriptions of the header and request body.

  Method   Request URI
  -------- ----------------------------------------------------------------------------------
  GET      https://manage.devcenter.microsoft.com/api/v1.0/my/hardware/products/{productID}

[]{#_Toc510098061 .anchor}Request header

  Header          Type     Description
  --------------- -------- ------------------------------------------------------------------------------
  authorization   string   Required. The Azure AD access token in the form **Bearer** *\<token\>*.
  accept          string   Optional. Specifies the type of content. Allowed value is "application/json"

[]{#_Toc510098062 .anchor}Request parameters

Do not provide request parameters for this method

[]{#_Toc510098063 .anchor}Request body

Do not provide a request body for this method.

[]{#_Toc510098064 .anchor}Request examples

The following example demonstrates how to retrieve information about a
specific product registered to your account.

Copy

GET
https://manage.devcenter.microsoft.com/api/v1.0/my/hardware/products/14039471039847257
HTTP/1.1

Authorization: Bearer \<your access token\>

[]{#_Toc510098065 .anchor}Response

The following example demonstrates the JSON response body returned by a
successful request for a specific product registered to a developer
account. For more details about the values in the response body, see the
following section.

JSON Copy

{

\"id\": 9007199267351834,

\"sharedProductId\": 1152921504606971100,

\"links\": \[

{

\"href\":
\"https://manage.devcenter.microsoft.com/api/v1/hardware/products/9007199267351834\",

\"rel\": \"self\",

\"method\": \"GET\"

},

{

\"href\":
\"https://manage.devcenter.microsoft.com/api/v1/hardware/products/9007199267351834/submissions\",

\"rel\": \"get\_submissions\",

\"method\": \"GET\"

}

\],

\"isCommitted\": true,

\"isExtensionInf\": false,

\"deviceMetadataIds\": \[\],

\"deviceType\": \"notSet\",

\"isTestSign\": false,

\"marketingNames\": \[\],

\"productName\": \"NewDriverHacked\",

\"selectedProductTypes\": {},

\"requestedSignatures\": \[

\"WINDOWS\_v100\_X64\_TH1\_FULL\",

\"WINDOWS\_v63\_X64\"

\],

\"additionalAttributes\": {},

\"testHarness\": \"hlk\"

}

[]{#_Toc510098066 .anchor}Error codes

Refer [error codes](#ErrorCodes) for details.

[]{#GetAllSubmissions .anchor}Get all submissions

Use this method in the Microsoft Hardware API to retrieve data for all
submissions of a product.

[]{#_Toc510098068 .anchor}Prerequisites

If you have not done so already, complete all the
[[prerequisites]{.underline}](#ManageHWUsingAPI) for the Microsoft
Hardware APIs before trying to use any of these methods.

[]{#_Toc510098069 .anchor}Request

This method has the following syntax. See the following sections for
usage examples and descriptions of the header and request body.

  Method   Request URI
  -------- --------------------------------------------------------------------------------------------
  GET      https://manage.devcenter.microsoft.com/ api/v1.0/hardware/products/{productID}/submissions

[]{#_Toc510098070 .anchor}Request header

  Header          Type     Description
  --------------- -------- ------------------------------------------------------------------------------
  Authorization   string   Required. The Azure AD access token in the form **Bearer** *\<token\>*.
  accept          string   Optional. Specifies the type of content. Allowed value is "application/json"

[]{#_Toc510098071 .anchor}Request parameters

Do not provide request parameters for this method.

[]{#_Toc510098072 .anchor}Request body

Do not provide a request body for this method.

[]{#_Toc510098073 .anchor}Request examples

The following example demonstrates how to retrieve information about all
submissions of a product.

Copy

GET https://manage.devcenter.microsoft.com/ api/v1.0/hardware/products/
13635057453741329/submissions HTTP/1.1

Authorization: Bearer \<your access token\>

[]{#_Toc510098074 .anchor}Response

The following example demonstrates the JSON response body returned by a
successful request for all the submissions of a product. For brevity,
this example only shows the data for the first two submissions returned
by the request. For more details about the values in the response body,
see the following section.

JSON Copy

{

\"value\": \[

{

\"id\": 1152921504621442000,

\"productId\": 13635057453741328,

\"links\": \[

{

\"href\":
\"https://manage.devcenter.microsoft.com/api/v1/hardware/products/13635057453741329/submissions/1152921504621441944\",

\"rel\": \"self\",

\"method\": \"GET\"

},

{

\"href\":
\"https://manage.devcenter.microsoft.com/api/v1/hardware/products/13635057453741329/submissions/1152921504621441944\",

\"rel\": \"update\_submission\",

\"method\": \"PATCH\"

}

\],

\"name\": \"HARRY-Duatest2\",

\"type\": \"derived\"

},

{

\"id\": 1152921504621442000,

\"productId\": 13635057453741328,

\"workflowStatus\": {

\"currentStep\": \"finalizeIngestion\",

\"state\": \"completed\",

\"messages\": \[\]

},

\"links\": \[

{

\"href\":
\"https://manage.devcenter.microsoft.com/api/v1/hardware/products/13635057453741329/submissions/1152921504621441946\",

\"rel\": \"self\",

\"method\": \"GET\"

},

{

\"href\":
\"https://manage.devcenter.microsoft.com/api/v1/hardware/products/13635057453741329/submissions/1152921504621441946\",

\"rel\": \"update\_submission\",

\"method\": \"PATCH\"

}

\],

\"name\": \"updated-1\",

\"type\": \"derived\"

},

{

\"id\": 1152921504621442000,

\"productId\": 13635057453741328,

\"workflowStatus\": {

\"currentStep\": \"finalizeIngestion\",

\"state\": \"completed\",

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

\],

\"links\": \[

{

\"href\":
\"https://manage.devcenter.microsoft.com/api/v1/hardware/products/13635057453741329/submissions\",

\"rel\": \"self\",

\"method\": \"GET\"

}

\]

}

[]{#_Toc510098075 .anchor}Response body

  Value   Type    Description
  ------- ------- --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  value   array   An array of objects that contain information about each submission of a product. For more information about the data in each object, see [Submission resource](#SubmissionResource).
  links   array   An array of objects with helpful links about the containing entity. Refer [link object](#LinkResource) for more details

[]{#_Toc510098076 .anchor}Error codes

Refer [error codes](#ErrorCodes) for details.

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
