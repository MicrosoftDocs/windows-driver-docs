---
title: Get product data
description: These methods from the Microsoft Hardware APIs get data for hardware products registered to your Dev Center Account.
ms.author: windowsdriverdev
ms.date: 04/05/2018
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Manage hardware submissions using APIs

Use the *Microsoft Hardware APIs* to programmatically query and create submissions for hardware products within your organization's Windows Dev Center account. These APIs are useful if your account manages many products, and you want to automate and optimize the submission process for these assets. These APIs use Azure Active Directory (Azure AD) to authenticate the calls from your app or service.
The following steps describe the end-to-end process of using the Microsoft Hardware API:
1.	These APIs can only be used by developer accounts that belong to the [Windows Hardware Dev Center program](https://msdn.microsoft.com/windows/hardware/drivers/dashboard/get-started-with-the-hardware-dashboard).
2.	Make sure that you have completed all the [prerequisites](#complete-prerequisites-for-using-the-microsoft-hardware-api).
3.	Before you call a method in the Microsoft Hardware API, [obtain an Azure AD access token](#obtain-an-azure-ad-access-token). After you obtain a token, you have 60 minutes to use this token in calls to the Microsoft Store submission API before the token expires. After the token expires, you can generate a new token.
4.	[Call the Microsoft Store submission API](#use-the-microsoft-hardware-api).



## Complete prerequisites for using the Microsoft Hardware API
Before you start writing code to call the Microsoft Hardware API, make sure that you have completed the following prerequisites.

*	You (or your organization) must have an Azure AD directory and you must have [Global administrator](http://go.microsoft.com/fwlink/?LinkId=746654)  permission for the directory. If you already use Office 365 or other business services from Microsoft, you already have Azure AD directory. Otherwise, you can [create a new Azure AD in Dev Center](https://docs.microsoft.com/en-us/windows/uwp/publish/associate-azure-ad-with-dev-center#create-a-brand-new-azure-ad-to-associate-with-your-dev-center-account)  for no additional charge.

*	You must [associate an Azure AD application with your Windows Dev Center account](https://docs.microsoft.com/en-us/windows/uwp/monetize/create-and-manage-submissions-using-windows-store-services#associate-an-azure-ad-application-with-your-windows-dev-center-account)  and obtain your tenant ID, client ID and key. You need these values to obtain an Azure AD access token, which you will use in calls to the Microsoft Hardware API.

### How to associate an Azure AD application with your Windows Dev Center account
Before you can use the Microsoft Hardware API, you must associate an Azure AD application with your Dev Center account, retrieve the tenant ID and client ID for the application and generate a key. The Azure AD application represents the app or service from which you want to call the Microsoft Hardware API. You need the tenant ID, client ID and key to obtain an Azure AD access token that you pass to the API.
1.	In Dev Center, go to your **Account** settings, click **Manage** users, and [associate your organization's Dev Center account with your organization's Azure AD directory](https://docs.microsoft.com/en-us/windows/uwp/publish/associate-azure-ad-with-dev-center) .
2.	In the **Manage users** page, click **Add Azure AD** applications, add the Azure AD application that represents the app or service that you will use to access submissions for your Dev Center account, and assign it the **Manager** role. If this application already exists in your Azure AD directory, you can select it on the **Add Azure AD applications** page to add it to your Dev Center account. Otherwise, you can create a new Azure AD application on the **Add Azure AD applications** page. For more information, see [Add Azure AD applications to your Dev Center account](https://docs.microsoft.com/en-us/windows/uwp/publish/add-users-groups-and-azure-ad-applications#azure-ad-applications) .
3.	Return to the **Manage users** page, click the name of your Azure AD application to go to the application settings, and copy down the **Tenant ID** and **Client ID** values.
4.	Click **Add new** key. On the following screen, copy down the **Key** value. You won't be able to access this info again after you leave this page. For more information, see [Manage keys for an Azure AD application](https://docs.microsoft.com/en-us/windows/uwp/publish/add-users-groups-and-azure-ad-applications#manage-keys).

## Obtain an Azure AD access token


Before you call any of the methods in the Microsoft Store submission API, you must first obtain an Azure AD access token that you pass to the **Authorization** header of each method in the API. After you obtain an access token, you have 60 minutes to use it before it expires. After the token expires, you can refresh the token, so you can continue to use it in further calls to the API.
To obtain the access token, follow the instructions in [Service to Service Calls Using Client Credentials](https://azure.microsoft.com/documentation/articles/active-directory-protocols-oauth-service-to-service/)  to send an HTTP POST to the https://login.microsoftonline.com/<tenant_id>/oauth2/token endpoint. Here is a sample request.

```
POST https://login.microsoftonline.com/<tenant_id>/oauth2/token HTTP/1.1
Host: login.microsoftonline.com
Content-Type: application/x-www-form-urlencoded; charset=utf-8

grant_type=client_credentials
&client_id=<your_client_id>
&client_secret=<your_client_secret>
&resource=https://manage.devcenter.microsoft.com
```

For the *tenant_id* value in the POST URI and the *client_id* and *client_secret* parameters, specify the tenant ID, client ID and the key for your application that you retrieved from Dev Center in the previous section. For the *resource* parameter, you must specify https://manage.devcenter.microsoft.com.

After your access token expires, you can refresh it by following the instructions [here](https://azure.microsoft.com/documentation/articles/active-directory-protocols-oauth-code/#refreshing-the-access-tokens) .

## Use the Microsoft Hardware API

After you have an Azure AD access token, you can call methods in the Microsoft Hardware API. The API includes many methods that are grouped into scenarios. To create or update submissions, you typically call multiple methods in the Microsoft Hardware API in a specific order. For information about each scenario and the syntax of each method, see the articles in the following table.

| Scenario | Description |
|:--|:--|
| Drivers | Get, create and update drivers registered to your Dev Center Account. For more information about these methods, see the following articles:<ul><li>[Get product data](#get-product-data)</li><li>[Manage product submissions](#manage-product-submissions)</li></ul>|


## Code examples

The following articles provide detailed code examples that demonstrate how to use the Microsoft Hardware API:

*	[C# sample: <link TBD>](https://docs.microsoft.com/en-us/windows/uwp/monetize/csharp-code-examples-for-the-windows-store-submission-api)

## Additional help

If you have questions about the Microsoft Store submission API or need assistance managing your submissions with this API, use the following resources:
•	Visit our [support page](https://developer.microsoft.com/en-us/dashboard/account/help?returnUri=https://developer.microsoft.com/en-us/dashboard/hardware)  and request for help.

## Get product data

Use the following methods in *Microsoft Hardware APIs* to get data for hardware products registered to your Dev Center Account. For an introduction to Microsoft Hardware APIs, including prerequisites for using the API, see [Manage hardware submissions using APIs](#manage-hardware-submissions-using-apis).

```
https://manage.devcenter.microsoft.com/api/v1.0/my/hardware/products/
```
Before you can use these methods, the product must already exist in your Dev Center account. To create or manage submissions for products, see the methods in [Manage product submissions](#manage-product-submissions)

| Method | URI | Description |
|:--|:--|:--|
|GET	https://manage.devcenter.microsoft.com/api/v1.0/hardware/products/	|[Get data for all your products](#get-all-products)|
|GET	https://manage.devcenter.microsoft.com/api/v1.0/hardware/products/{productID}	|[Get data for a specific product](#get-a-product)|
|GET	https://manage.devcenter.microsoft.com/api/v1.0/hardware/products/{productID}/submissions	|[Get data for all submissions of a product](#get-all-submissions)|
|GET	https://manage.devcenter.microsoft.com/api/v1.0/hardware/products/{productID}/submissions/{submissionId}	|[Get data for a specific submission of a product](#get-a-submission)|

## Prerequisites

If you have not done so already, complete all the [prerequisites](#manage-hardware-submissions-using-apis) for the Microsoft Hardware APIs before trying to use any of these methods.

## Data resources

The Microsoft Hardware APIs methods for getting product data use the following JSON data resources

### Product resource

This resource represents a hardware product (driver) that is registered to your account.


```json
{
  "id”: 9007199267351834,
  “sharedProductId”: 1152921504606971100,
  “links”: [
    {
      “href": "https:// manage.devcenter.microsoft.com/api/v1.0/hardware/products/9007199267351834",
      "rel": "self",
      "method": "GET"
    },
    {
      "href": "https:// manage.devcenter.microsoft.com/api/v1.0/hardware/products/9007199267351834/submissions",
      "rel": "get_submissions",
      "method": "GET"
    }
  ],
  "isCommitted": true,
  "isExtensionInf": false,
  "deviceMetadataIds": [],
  "deviceType": "notSet",
  "isTestSign": false,
  "marketingNames": [
    "marketing name 1",
    " marketing name 2"
],
  "productName": "product name",
  "selectedProductTypes": {
    "windows_v100Server": "Unclassified",
    "windows_v100": "Unclassified"
},
  "requestedSignatures": [
    "WINDOWS_v100_X64_TH1_FULL",
    "WINDOWS_v63_X64"
  ],
  "additionalAttributes": {},
  "testHarness": "hlk",
  " announcementDate ": "2016-10-22T00:00:00Z",
}
```

This resource has the following values

| Value | Type | Description |
|:--|:--|:--|
| Id | Long | The private product ID of the product |
| sharedProductId | Long | The shared product ID of the product |
| Links | array of objects | Refer [link object](#link-object)  for more details |
| isCommitted | Boolean | Indicates whether the product has at least one committed submission  |
| isExtensionInf | Boolean | Indicates whether the product is an extension driver |
| deviceMetadataIds | array of GUIDs | GUIDs which map device metadata submissions to the driver |
| deviceType | String | Indicates the type of device. Possible values are:<ul><li>“internal” - An internal component, device is part of a system and connects inside the PC</li><li>“external” - An external component, device is an external device (peripheral) that connects to a PC</li><li>“internalExternal” - Both, device can be connected internally (inside a PC) and externally (peripheral)</li><li>“notSet” – no data available</li></ul>|
| isTestSign | Boolean | Indicates whether the product is a test signed driver. For more information about test-signing driver packages, see [WHQL Test Signature Program](https://docs.microsoft.com/en-us/windows-hardware/drivers/install/whql-test-signature-program)  |
| marketingNames | array of strings | Marketing names or aliases of the product |
| productName | String | The name of the driver as specified during creation |
| selectedProductTypes | dictionary  | Key value pair where both are strings. <ul><li>**Key** represents the Operating System Family Code. For a list of Operating System Family Codes, see [list of OS family codes](#list-of-operating-system-family-codes).</li><li>**Value** represents the type of the product. For a list of type of products, see [product types](#list-of-product-types).</li></ul>|
| requestedSignatures | array of strings | List of operating system signatures for which product is certified. For a list of all Operating systems, see [list of OS codes](#list-of-operating-system-family-codes)  |
| additionalAttributes | Object | Refer [additional attributes object](#additional-attribute-object)  for more details. |
| testHarness | string | The type of package which has been submitted. Possible values are <ul><li>hlk<li>hck</li><li>attestation</li><li>notset</li></ul>|
| announcementDate | datetime | The date when the product will get included on the Windows Server Catalog |



### Submission resource

This resource represents a submission of a product.

```json
{
  "id": 1152921504621442000,
  "productId": 13635057453741328,
  "links": [
    {
      "href": "https:// manage.devcenter.microsoft.com/api/v1.0/hardware/products/13635057453741329/submissions/1152921504621441944",
      "rel": "self",
      "method": "GET"
    }
  ],
  "name": "HARRY-Duatest2",
  "type": "derived"
}
```

This resource has the following values

| Value | Type | Description |
|:--|:--|:--|
| Id | long | The ID of the submission |
| Productid | long | The private product ID to which this submission is associated |
| Links | array of objects | Refer [link object](#link-object)  for more details |
| Name | string | The name of the submission |
| Type | string | Indicates whether the submission is an initial or derived submission. Possible values are <ul><li>initial</li><li>derived</li></ul> |
| workflowstatus | object | This is available only when retrieving details of a specific submission. This object depicts the status of the workflow for this submission. Refer [workflow status object](#workflow-status-object)  for more details  |
| downloads | object | This is available only when retrieving details of a specific submission only. This object depicts the downloads available for the submission. Refer [download object](#download-object)  for more details. |



### Workflow Status object

This object represents the status of workflow for a given entity

```json
{
      “currentStep": " finalizeIngestion",
      " state": " completed",
      " messages": []
    }
```

This object has the following values

| Value | Type | Description |
|:--|:--|:--|
| currentStep | string | The name of the current step in the overall workflow for this entity. <br>For ingestion/package submission the possible values are (description **in** parenthesis):<ul><li>packageInfoValidation (Validating **Package metadata and** contents)</li><li>preparation (Getting **package ready for** processing)</li><li>scanning (Scanning **package contents for** Malware)</li><li>validation (Validation **of test** results)</li><li>catalogCreation (Creating **a security catalog for** package)</li><li>manualReview (Undergoing **Manual** Review)</li><li>signing (Signing **the** binaries)</li><li>finalizeIngestion (Completing **the ingestion and getting signed files ready to download or** publish)</li></ul>|
| State | string | The state of the current step. Possible values are:<ul><li>notStarted</li><li>started</li><li>failed</li><li>completed</li></ul> |
| Messages | array | An array of strings to provide messages about current step (especially in case of failure) |


### Download object

This object represents the downloads for a given submission.

```json
{
  "items": [
    {
      "type": "initialPackage",
      "url": "https://ingestionpackagesint1.blob.core.windows.net/ingestion/dc55b8c6-a01c-40b6-b815-cac8bc08812a?sv=2016-05-31&sr=b&sig=ipjW3RsVC75lZrcEZRh9JmTX89L4gTIKkxwqv9F8Axs%3D&se=2018-03-12T15:32:10Z&sp=rl"
    },
    {
      "type": "derivedPackage",
      "url": "https://ingestionpackagesint1.blob.core.windows.net/ingestion/6bd77dbf-a851-46d2-b703-29ea4efae006?sv=2016-05-31&sr=b&sig=O5XQf%2FzMbI2FFt5WwSUJWL1JbWY4JXXPRkCKAnX7IRs%3D&se=2018-03-12T15:32:10Z&sp=rl&rscd=attachment%3B filename%3DShell_1152921504621441930.hlkx"
    },
    {
      "type": "signedPackage",
      "url": "https://ingestionpackagesint1.blob.core.windows.net/ingestion/0b83a294-c1d1-4136-82a1-dd52f51841e3?sv=2016-05-31&sr=b&sig=zTfxKJmaTwpbFol%2FpAKG0QuXJTTxm5aZ0F2wQQI8whc%3D&se=2018-03-12T15:32:10Z&sp=rl"
    },
    {
      "type": "certificationReport",
      "url": "https:// manage.devcenter.microsoft.com/en-us/dashboard/hardware/Driver/DownloadCertificationReport/29963920/13635057453741329/1152921504621441930"
    }
  ],
  "messages": []
}
```

This object has the following values

| Value | Type | Description |
|:--|:--|:--|
| Items | array | An array of download types and the URL for each. Please refer below for details |
| Type | string | The type of package available for download. Possible values are:<ul><li>“initialPackage” – package uploaded by user (in case of new submission, it points to the SAS URI for uploading the package)</li><li>“derivedPackage” – shell for derived submissions</li><li>“signedPackage” – package signed by Microsoft</li><li>“certificationReport” – certification report for the signed product</li></ul>|
| Messages | array | An array of strings to provide messages about the downloadable files |


### Link object

This object represents a list of helpful links for the containing entity

```json
{
      “href": "https:// manage.devcenter.microsoft.com/api/v1.0/hardware/products/9007199267351834",
      "rel": "self",
      "method": "GET"
    }
```

This object has the following values

| Value | Type | Description |
|:--|:--|:--|
| Href | String | The URL to access the resource via API |
| Rel | String | Type of the resource. Possible values are:<ul><li>self – Link points to itself</li><li>next_link – Link points to next resource typically used for pagination</li><li>get_submissions – link points to all submissions of a product</li><li>commit_submission – link points to commit of a submission </li><li>update_submission – link points to update of the submission </li></ul>|
| Method | String | Type of the http method to be used when invoking the URL. Possible values are<ul><li>GET</li><li>POST</li><li>PATCH</li></ul>|

### Additional Attribute object

This object provides additional attributes about the product if it is of type RAID controller, Storage Controller or Server Virtualization Validation program (SVVP). It can contain one of three types of objects – StorageController, RaidController or SVVP.

**StorageController Object**

| Value | Type | Description |
|:--|:--|:--|
| biosVersion | string | ROM Bios Version |
| firmwareVersion | string | Firmware Version |
| driverVersion | string | Driver Version |
| driverName | string | Driver Name |
| deviceVersion | string | Device Version |
| chipsetName | string | Chipset Name |
| usedProprietary | boolean | Multi-pathing supported through proprietary driver. If true, then proprietaryName and proprietaryVersion are madatory |
| proprietaryName | string | Multi-path software name |
| proprietaryVersion | string | Multi-path software version |
| usedMicrosoft | boolean | Microsoft MPIO supported through device-specific module. If true, then microsoftName and microsoftVersion are madatory |
| microsoftName | string | Multi-path software name |
| microsoftVersion | string | Multi-path software version |
| usedBootSupport | boolean | Boot Support |
| usedBetterBoot | boolean | Boot >2.2TB support.  If true, then Supported UEFI version and Supported ACPI version are mandatory |
| uefiVersion | string | Supported UEFI version |
| acpiVersion | string | Supported ACPI version |
| supportsSector4K512E | boolean | Support sector size of 4K/512e |
| supportsSector4K4K | boolean | Support sector size of 4K/4K |
| supportsDifferential | boolean | Differential (high-voltage differential) |


**RaidController Object**

| Value | Type | Description |
|:--|:--|:--|
| firmwareVersion | string | Firmware Version |
| filterVersion | string | Driver Version |
| driverVersion | string | Filter Version |
| usedProprietary | boolean | Multi-pathing supported through proprietary driver. If true, then proprietaryName and proprietaryVersion are mandatory |
| proprietaryName | string | Multi-path software name |
| proprietaryVersion | string | Multi-path software version |
| usedMicrosoft | boolean | Microsoft MPIO supported through device-specific module. If true, then microsoftName and microsoftVersion are mandatory |
| microsoftName | string | Multi-path software name |
| microsoftVersion | string | Multi-path software version |
| isThirdPartyNeeded | boolean | Third party non-Microsoft driver needed for connectivity |
| isSES | boolean | SES (SCSI Enclosure Services). Indicates if a SES is included. SCSI is the standard term for a service bus that connects devices on a system, originally Small Computer System Interface. SES is short for SCSI Enclosure Services. |
| isSAFTE | boolean | SAF-TE (ANBll Specification). Indicates if a SAF-TE is included. ANBll an industry specification. SAF-TE is short for SCSI Accessed Fault Tolerant Enclosures. SCSI is the standard term for a service bus that connects devices on a system, originally Small Computer System Interface. |
| additionalInfo | string | Additonal Information |


**SVVP Object**

| Value | Type | Description |
|:--|:--|:--|
| productVersion | string | Product Version |
| supportLink | string | Support URL |
| guestOs | string | Guest OS. Possible values are:<ul><li>Windows Server 2008</li><li>Windows Server 2008 Release 2</li><li>Windows Server 2012</li><li>Windows Server 2012 R2 </li></ul>|
| processorArchitecture | string | Hardware Processor Architecture. Possible values are:<ul><li>Xeon</li><li>Opteron</li><li>Itanium 2</li></ul>|
| maxProcessors | integer | Max Processors in VM |
| maxMemory | integer | Max memory in VM (in GB) |


### List of Product Types

A product can be of the following types. This information is used along with the Operating system to identify applicability

* All In One
* All In One with Touch
* Audio Device
* Bluetooth Controller
* Bluetooth Controller Non USB
* Convertible Tablet
* Desktop
* Digital Media Renderer
* Digital Media Server
* Digital Still Cameras
* Digital Video Cameras
* Distribution Scan Management Enabled Devices
* Enterprise WSD Multi-Function Printer
* Finger Print Reader
* Game Controller
* Generic Controller
* Generic Portable Device
* Graphics Adapter WDDM1.0
* Graphics Adapter WDDM1.1
* Graphics Adapter WDDM1.2
* Graphics Adapter WDDM1.2 DisplayOnly
* Graphics Adapter WDDM1.2 RenderOnly
* Graphics Tablet
* Hard Drive
* Keyboard
* Keyboard Video Mouse Switch
* LAN
* LAN (Server)
* LAN CS
* LAN Virtual Machine (Server)
* Laptop
* Laptop with Touch
* LCD
* Light Sensor
* Location Sensor
* Media Player
* Mobile Broadband CDMA
* Mobile Broadband GSM
* Mobile Phone
* Monitor
* Motherboard
* Motion Sensor Fusion
* Multi-Function Printer
* Near Field Proximity
* Network Media Device
* Optical Drive
* Pen Digitizer
* Pointing Drawing
* Presence Sensor
* Printer
* Projector
* Removable Storage
* Router
* Scanner
* SDIO Controller
* Server
* Server Virtualization Validation Program
* Signature Tablet
* Smart Cards
* Smartcard Reader
* Storage Array
* Storage Controller
* Storage Spaces Adapter
* Storage Spaces Drive
* Tablet
* Touch
* Touch Monitor
* Ultra-Mobile PC
* Ultra-Mobile PC with Touch
* USB Controller
* USB Hub
* WebCam
* WLAN
* WLAN CSB
* WSD Multi-Function Printer
* WSD Printer
* WSD Scanner


### List of Operating System Family Codes

Given below is a list of Operating system Family Codes and their description

| ****OS Family Code**** | ****Description**** |
|:--|:--|
| WindowsMe | Windows Me |
| Windows2000 | Windows 2000 |
| Windows98 | Windows 98 |
| WindowsNT40 | Windows NT 4.0 |
| WindowsXP | Windows XP |
| WindowsServer2003 | Windows Server 2003 |
| WindowsVista | Windows Vista |
| Windows2008Server | Windows Server 2008 |
| WindowsHomeServer | Windows Home Server |
| Windows7 | Windows 7 |
| Windows2008ServerR2 | Windows Server 2008 Release 2 |
| WindowsServerSolutions | Windows Server Solutions |
| Windows8 | Windows 8 |
| Windows8Server | Windows Server 2012 |
| Windows81 | Windows 8.1 |
| Windows81Server | Windows Server 2012 R2 |
| Windows_v100_TH1 | Windows Threshold 1 |
| Windows_v100_TH2 | Windows Threshold 2 |
| Windows_v100_RS1 | Windows 10 Anniversary Update |
| Windows_v100Server_RS1 | Windows Server 2016 |
| Windows_v100_RS2 | Windows 10 RS2 Update |
| Windows_v100Server_RS2 | Windows Server RS2 |
| Windows_v100_RS3 | Windows 10 RS3 Update |
| Windows_v100Server_RS3 | Windows Server RS3 |
| WINDOWS_v100_ARM64_RS3_FULL_PRE_RELEASE_CLOUD | Windows 10 RS3 Update |

### List of Operating System Codes

Given below is a list of Operating System Codes and their description

| ****OS Code**** | ****Description**** |
|:--|:--|
| WindowsMe | Windows Me |
| Windows2000 | Windows 2000 |
| Windows98 | Windows 98 |
| WindowsNT40 | Windows NT 4.0 |
| WindowsXP_X86 | Windows XP |
| WindowsXP_IA64 | Windows XP IA64 |
| WindowsXP_X64 | Windows XP X64 |
| WindowsXPMediaCenter | Windows XP Media Center |
| WindowsServer2003_X86 | Windows Server 2003 |
| WindowsServer2003_IA64 | Windows Server 2003 IA64 |
| WindowsServer2003_X64 | Windows Server 2003 X64 |
| WindowsVista_X86 | Windows Vista Client |
| WindowsVista_X64 | Windows Vista Client X64 |
| Windows2008Server_X86 | Windows Server 2008 |
| Windows2008Server_IA64 | Windows Server 2008 IA64 |
| Windows2008Server_X64 | Windows Server 2008 X64 |
| WindowsHomeServer | Windows Home Server |
| Windows7_X86 | Windows 7 Client |
| Windows7_X64 | Windows 7 Client x64 |
| Windows2008ServerR2_IA64 | Windows Server 2008 Release 2 IA64 |
| Windows2008ServerR2_X64 | Windows Server 2008 Release 2 x64 |
| WindowsServerSolutions_X64 | Windows Server Solutions x64 |
| Windows8_X86 | Windows 8 Client |
| Windows8_X64 | Windows 8 Client x64 |
| Windows8_ARM | Windows 8 Client RT |
| Windows8Server_X64 | Windows Server 2012 |
| Windows81_X86 | Windows 8.1 Client |
| Windows81_X64 | Windows 8.1 Client x64 |
| Windows81_ARM | Windows 8.1 Client RT |
| Windows63Server_X64 | Windows Server 2012 R2 x64 |
| Windows_v100_X86_TH1_Full | Windows 10 Client versions 1506 and 1511 |
| Windows_v100_X64_TH1_Full | Windows 10 Client versions 1506 and 1511 x64 |
| Windows_v100Server_X64_TH1_Full | Windows Server 2016 x64 |
| Windows_v100_X86_TH2_Full | Windows 10 Client versions 1506 and 1511 |
| Windows_v100_X64_TH2_Full | Windows 10 Client versions 1506 and 1511 x64 |
| Windows_v100Server_X64_TH2_Full | Windows Server 2016 x64 |
| Windows_v100_X86_RS1_Full | Windows 10 Client version 1607 |
| Windows_v100_X64_RS1_Full | Windows 10 Client version 1607 x64 |
| Windows_v100Server_X64_RS1_Full | Windows Server 2016 x64 |
| Windows_v100_X86_RS2_Full | Windows 10 RS2 Client |
| Windows_v100_X64_RS2_Full | Windows 10 RS2 Client x64 |
| Windows_v100Server_X64_RS2_Full | Windows Server RS2 x64 |
| Windows_v100_X86_RS3_Full | Windows 10 RS3 Client |
| Windows_v100_X64_RS3_Full | Windows 10 RS3 Client x64 |
| Windows_v100_ARM64_RS3_Full | Windows 10 RS3 Client ARM64 |
| Windows_v100Server_x64_RS3_Full | Windows Server RS3 x64 |
| WINDOWS_v100_ARM64_RS3_FULL_PRE_RELEASE_CLOUD | Windows 10 S RS3 Client ARM64 Pre Release |


## Error codes

These error codes are applicable to all web methods of the API.

If the request cannot be successfully completed, the response will contain one of the following HTTP error codes.

| HTTP Status | Description |
|:--|:--|
| 400 – Bad Request | Request not well formed (e.g., malformed request syntax, invalid request message framing, or deceptive request routing) |
| 401 – Unauthorized | Authentication failed or not provided |
| 403 – Forbidden | Forbidden to access a resource |
| 404 – Not Found | Entity requested for is not found. |
| 415 - Unsupported Media Type | Payload is in a format not supported by this method on the target resource. |
| 422 - Unprocessable Entity | Validation failures. |
| 500 - Internal Server Error | Unrecoverable error occurred at the API server. |


If there are functional validation failures, the response body will contain one of the following functional error codes.

| Error Code | Error Message | Description |
|:--|:--|:--|
| InvalidInput |  | Returned when an input validation fails |
| RequestInvalidForCurrentState | Only pending submissions can be committed | Returned when a commit is applied on a submission which is not in pending state |
| RequestInvalidForCurrentState | Initial submission already exists | Returned when an initial submission is created for a driver which already has an initial submission |
| RequestInvalidForCurrentState | Cannot create derived submission since no initial submission created | Returned when a derived submission is created for a driver which does not have an initial submission |
| UpdateUnauthorized | Not authorized to update the product | Returned when trying to update a product that was shared (resold) since shared products cannot be updated |
| UpdateUnauthorized | Cannot update product without an initial submission | Returned when trying to update a product which does not have an initial submission |
| UpdateUnauthorized | Cannot update product because the workflow has failed | Returned when trying to update a product which has a failed workflow |
| UpdateUnauthorized | Announcement Date cannot be updated after the ingestion process is finished | Returned when announcement date is updated after ingestion is completed |
| UpdateUnauthorized | Product Name cannot be updated at this time. Please re-try |  |
| UpdateUnauthorized | Not authorized to update the submission | Returned when trying to update a submission for a product that was shared (resold) since shared products cannot be updated |
| UpdateUnauthorized | Cannot update the submission since the workflows have failed | Returned when trying to update a submission which has a failed workflow |
| EntityNotFound | No submission found | Returned when trying to commit for a submission which does not exist |
| EntityNotFound | Product not found | Returned when trying to create a submission for which a product does not exist |