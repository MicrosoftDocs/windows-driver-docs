---
title: Get product data
description: These methods from the Microsoft Hardware APIs get data for hardware products registered to your Dev Center Account.
author: balapv
ms.author: balapv
ms.topic: article
ms.date: 04/05/2018
ms.localizationpriority: medium
---

# Get product data

Use the following methods in *Microsoft Hardware APIs* to get data for hardware products registered to your Dev Center Account. For an introduction to Microsoft Hardware APIs, including prerequisites for using the API, see [Manage hardware submissions using APIs](dashboard-api.md).

```cpp
https://manage.devcenter.microsoft.com/v1.0/my/hardware/products/
```
Before you can use these methods, the product must already exist in your Dev Center account. To create or manage submissions for products, see the methods in [Manage product submissions](manage-product-submissions.md).

| Method | URI | Description |
|-|-|-|
|GET |	`https://manage.devcenter.microsoft.com/v1.0/hardware/products/`	|[Get data for all your products](get-all-products.md)|
|GET |	`https://manage.devcenter.microsoft.com/v1.0/hardware/products/{productID}`	|[Get data for a specific product](get-a-product.md)|
|GET |	`https://manage.devcenter.microsoft.com/v1.0/hardware/products/{productID}/submissions`	|[Get data for all submissions of a product](get-all-submissions.md)|
|GET |	`https://manage.devcenter.microsoft.com/v1.0/hardware/products/{productID}/submissions/{submissionId}`	|[Get data for a specific submission of a product](get-a-submission.md)|

## Prerequisites

If you have not done so already, complete all the [prerequisites](dashboard-api.md) for the Microsoft Hardware APIs before trying to use any of these methods.

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
  "isExtensionInf": false, "_comment": "THis field is deprecated and moved to submission resource",
  "deviceMetadataIds": [],
  "deviceType": "notSet",
  "isTestSign": false,
  "isFlightSign": false,
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
| Links | array of objects | Refer to [link object](#link-object)  for more details |
| isCommitted | Boolean | Indicates whether the product has at least one committed submission  |
| isExtensionInf | Boolean | (DEPRECATED) Indicates whether the product is an extension driver. This field is deprecated and should no longer be used. isExtensionInf has been moved to submission level property. |
| deviceMetadataIds | array of GUIDs | GUIDs which map device metadata submissions to the driver |
| deviceType | String | Indicates the type of device. Possible values are:<ul><li>“internal” - An internal component, device is part of a system and connects inside the PC</li><li>“external” - An external component, device is an external device (peripheral) that connects to a PC</li><li>“internalExternal” - Both, device can be connected internally (inside a PC) and externally (peripheral)</li><li>“notSet” – no data available</li></ul>|
| isTestSign | Boolean | Indicates whether the product is a test signed driver. For more information about test-signing driver packages, see [WHQL Test Signature Program](https://docs.microsoft.com/windows-hardware/drivers/install/whql-test-signature-program)  |
| isFlightSign | Boolean | Indicates whether the product is a flight signed driver. Flight signed drivers are test drivers which can be published via Windows Update. They can be published/installed only on machines which have signed up for Windows Insider Program. They can be installed on machines without disbaling secure boot. They cannot be installed on retail machines which are not part of Windows Insider Program.|
| marketingNames | array of strings | Marketing names or aliases of the product |
| productName | String | The name of the driver as specified during creation |
| selectedProductTypes | dictionary  | Key value pair where both are strings. <ul><li>**Key** represents the Operating System Family Code. For a list of Operating System Family Codes, see [list of OS family codes](#list-of-operating-system-family-codes).</li><li>**Value** represents the type of the product. For a list of type of products, see [product types](#list-of-product-types).</li></ul>|
| requestedSignatures | array of strings | List of operating system signatures for which product is certified. For a list of all Operating systems, see [list of OS codes](#list-of-operating-system-codes)  |
| additionalAttributes | Object | Refer [additional attributes object](#additional-attribute-object)  for more details. |
| testHarness | string | The type of package which has been submitted. Possible values are <ul><li>hlk<li>hck</li><li>attestation</li><li>notset</li></ul>|
| announcementDate | datetime | The date when the product will get included on the Windows Server Catalog |



### Submission resource

This resource represents a submission of a product.

```json
{
  "id": 1152921504621442000,
  "productId": 13635057453741328,
   "workflowStatus": {
      “currentStep": " finalizeIngestion",
      " state": " completed",
      " messages": []
    },
  "links": [
    {
      "href": "https:// manage.devcenter.microsoft.com/api/v1.0/hardware/products/13635057453741329/submissions/1152921504621441944",
      "rel": "self",
      "method": "GET"
    }
  ],
  "commitStatus": "commitPending",
  "isExtensionInf": true,
  "isUniversal": true,
  "isDeclarativeInf": true,
  "name": "HARRY-Duatest2",
  "type": "derived"
}
```

This resource has the following values

| Value | Type | Description |
|:--|:--|:--|
| Id | long | The ID of the submission |
| Productid | long | The private product ID to which this submission is associated |
| Links | array of objects | Refer to [link object](#link-object)  for more details |
| Name | string | The name of the submission |
| Type | string | Indicates whether the submission is an initial or derived submission. Possible values are <ul><li>initial</li><li>derived</li></ul> |
| isExtensionInf | Boolean | Indicates whether the submission is an extension driver |
| isUniversal | Boolean | Indicates whether the submission passes the Universal API test. A driver is DCHU compliant if it is Decalarative and Universal |
| isDeclarativeInf | Boolean | Indicates whether the submission passes the Declarative INVerif test. A driver is DCHU compliant if it is Decalarative and Universal |
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
| currentStep | string | The name of the current step in the overall workflow for this entity. <br>For ingestion/package submission the possible values are (description in parenthesis):<ul><li>packageInfoValidation (*Validating Package metadata and contents*)</li><li>preparation (*Getting package ready for processing*)</li><li>scanning (*Scanning package contents for Malware*)</li><li>validation (*Validation of test results*)</li><li>catalogCreation (*Creating a security catalog for package*)</li><li>manualReview (*Undergoing Manual Review*)</li><li>signing (*Signing the binaries*)</li><li>finalizeIngestion (*Completing the ingestion and getting signed files ready to download or publish*)</li></ul>|
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
      "url": "https:// manage.devcenter.microsoft.com/dashboard/hardware/Driver/DownloadCertificationReport/29963920/13635057453741329/1152921504621441930"
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
| Rel | String | Type of the resource. Possible values are:<ul><li>self – Link points to itself</li><li>next_link – Link points to next resource typically used for pagination</li><li>get_submissions – link points to all submissions of a product</li><li>commit_submission – link points to commit of a submission </li><li>update_submission – link points to update of the submission </li><li>update_shippinglabel – link points to update of the shipping label  </li><li>driverMetadata - link points to a file which allows to download of driver metadata. For more details refer [driver package metadata](driver-package-metadata.md).</li></ul>|
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

A product can be of the following types. This information is used along with the Operating system to identify applicability.

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

The following table lists Operating system Family Codes and their descriptions.

| OS Family Code | Description |
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
| Windows_v100 | Windows 10 Threshold |
| Windows_v100Server | Windows Server Threshold |
| Windows_v100_RS1 | Windows 10 Anniversary Update |
| Windows_v100Server_RS1 | Windows Server 2016 |
| Windows_v100_RS2 | Windows 10 RS2 Update |
| Windows_v100Server_RS2 | Windows Server RS2 |
| Windows_v100_RS3 | Windows 10 RS3 Update |
| Windows_v100Server_RS3 | Windows Server RS3 |
| Windows_v100_RS4 | Windows 10 RS4 Update |
| Windows_v100Server_RS4 | Windows Server RS4 |

### List of Operating System Codes

The following table lists Operating System Codes and their descriptions.

| OS Code | Description |
|:--|:--|
|WINDOWS_ME|Windows Me|
|WINDOWS_98|Windows 98|
|WINDOWS_2000|Windows 2000|
|WINDOWS_NT40|Windows NT 4.0|
|WINDOWS_XP|Windows XP|
|WINDOWS_XP_IA64|Windows XP IA64|
|WINDOWS_XP_X64|Windows XP X64|
|WINDOWS_XP_MEDIA_CENTER|Windows XP Media Center|
|WINDOWS_2003|Windows Server 2003|
|WINDOWS_2003_IA64|Windows Server 2003 IA64|
|WINDOWS_2003_X64|Windows Server 2003 X64|
|WINDOWS_VISTA|Windows Vista Client|
|WINDOWS_VISTA_X64|Windows Vista Client X64|
|WINDOWS_2008_SERVER|Windows Server 2008|
|WINDOWS_2008_SERVER_IA64|Windows Server 2008 IA64|
|WINDOWS_2008_SERVER_X64|Windows Server 2008 X64|
|WINDOWS_HOME_SERVER|Windows Home Server|
|WINDOWS_7|Windows 7 Client|
|WINDOWS_7_X64|Windows 7 Client x64|
|WINDOWS_2008_SERVER_R2_IA64|Windows Server 2008 Release 2 IA64|
|WINDOWS_2008_SERVER_R2_X64|Windows Server 2008 Release 2 x64|
|WINDOWS_SERVER_SOLUTIONS_X64|Windows Server Solutions x64|
|WINDOWS_8|Windows 8 Client|
|WINDOWS_8_X64|Windows 8 Client x64|
|WINDOWS_8_ARM|Windows 8 Client RT|
|WINDOWS_8_SERVER_X64|Windows Server 2012|
|WINDOWS_v63|Windows 8.1 Client|
|WINDOWS_v63_X64|Windows 8.1 Client x64|
|WINDOWS_v63_ARM|Windows 8.1 Client RT|
|WINDOWS_v63_SERVER_X64|Windows Server 2012 R2 x64|
|WINDOWS_v100_TH1_FULL|Windows 10 Client versions 1506 and 1511 (TH1)|
|WINDOWS_v100_X64_TH1_FULL|Windows 10 Client versions 1506 and 1511 x64 (TH1)|
|WINDOWS_v100_SERVER_X64_TH1_FULL|Windows Server 2016 x64 (TH1)|
|WINDOWS_v100_TH2_FULL|Windows 10 Client versions 1506 and 1511 (TH2)|
|WINDOWS_v100_X64_TH2_FULL|Windows 10 Client versions 1506 and 1511 x64 (TH2)|
|WINDOWS_v100_SERVER_X64_TH2_FULL|Windows Server 2016 x64 (TH2)|
|WINDOWS_v100_RS1_FULL|Windows 10 Client version 1607|
|WINDOWS_v100_X64_RS1_FULL|Windows 10 Client version 1607 x64|
|WINDOWS_v100_SERVER_X64_RS1_FULL|Windows Server 2016 x64 (RS1)|
|WINDOWS_v100_RS2_FULL|Windows 10 RS2 Client|
|WINDOWS_v100_X64_RS2_FULL|Windows 10 RS2 Client x64|
|WINDOWS_v100_RS3_FULL|Windows 10 RS3 Client|
|WINDOWS_v100_X64_RS3_FULL|Windows 10 RS3 Client x64|
|WINDOWS_v100_ARM64_RS3_FULL|Windows 10 RS3 Client ARM64|
|WINDOWS_v100_SERVER_X64_RS3_FULL|Windows Server RS3 x64|
|WINDOWS_v100_RS4_FULL|Windows 10 RS4 Client|
|WINDOWS_v100_X64_RS4_FULL|Windows 10 RS4 Client x64|
|WINDOWS_v100_ARM64_RS4_FULL|Windows 10 RS4 Client ARM64|
|WINDOWS_v100_SERVER_X64_RS4_FULL|Windows 10 RS4 Server x64|
|WINDOWS_v100_SERVER_ARM64_RS4_FULL|Windows 10 RS4 Server ARM64|


## Error codes

The error codes are applicable to all web methods of the API. If the request cannot be successfully completed, the response will contain one of the following HTTP error codes.

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
| InvalidInput | Extension drivers must be published as an Automatic update. Either of isAutoInstallDuringOSUpgrade or isAutoInstallOnApplicableSystems must be true. | Returned when a windows update shipping label for an extension INF is created without choosing isAutoInstallDuringOSUpgrade or isAutoInstallOnApplicableSystems |
| InvalidInput | Chids are allowed only when HardwareIds are for operating systems Windows10 & Above. | Returned when a shipping label targeting OS less than windows 10 is created with CHID targeting. CHID targeting is applicable only for Windows 10 and above. |
| InvalidInput | Cannot update the shipping label when another workflow is in progress. Please retry. | Returned when a shipping label is updated when a previous workflow is still in progress. |
| RequestInvalidForCurrentState | Cannot create Publishing shipping label for inbox or system type. One can only share the shipping label. | Returned when windows update Shipping label is created on an inbox driver or a system. |
| RequestInvalidForCurrentState | Submission is not yet ready to create shipping label. Please retry after some time. | Returned when a shipping label is created without waiting for preparation or pre-processing to complete. |

## See also

- [Hardware dashboard API samples (GitHub)](https://aka.ms/hpc_async_api_samples)
