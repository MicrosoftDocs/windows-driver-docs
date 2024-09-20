---
title: Get product data
description: These methods from the Microsoft Hardware APIs retrieve data for hardware products registered to your Dev Center Account.
ms.topic: article
ms.date: 09/12/2024
---

# Get product data

Use the following methods in *Microsoft Hardware APIs* to retrieve data for hardware products registered to your Dev Center Account. For an introduction to Microsoft Hardware APIs, including prerequisites for using the API, see [Manage hardware submissions using APIs](dashboard-api.md).

`https://manage.devcenter.microsoft.com/v2.0/my/hardware/products/`

Before you can use these methods, the product must already exist in your Dev Center account. To create or manage submissions for products, see the methods in [Manage product submissions](manage-product-submissions.md).

| Method | URI | Description |
|--|--|--|
| GET | `https://manage.devcenter.microsoft.com/v2.0/my/hardware/products/` | [Get data for all your products](get-all-products.md) |
| GET | `https://manage.devcenter.microsoft.com/v2.0/my/hardware/products/{productID}` | [Get data for a specific product](get-a-product.md) |
| GET | `https://manage.devcenter.microsoft.com/v2.0/my/hardware/products/{productID}/submissions` | [Get data for all submissions of a product](get-all-submissions.md) |
| GET | `https://manage.devcenter.microsoft.com/v2.0/my/hardware/products/{productID}/submissions/{submissionId}` | [Get data for a specific submission of a product](get-a-submission.md) |

## Prerequisites

Complete all the [prerequisites](dashboard-api.md) for the Microsoft Hardware APIs before trying to use any of these methods.

## Data resources

The Microsoft Hardware APIs methods for getting product data use the following JSON data resources

### Product resource

This resource represents a hardware product (driver) that is registered to your account.

```json
{
  "id": 9007199267351834,
  "sharedProductId": 1152921504606971100,
  "links": [
    {
      "href": "https://manage.devcenter.microsoft.com/v2.0/my/hardware/products/9007199267351834",
      "rel": "self",
      "method": "GET"
    },
    {
      "href": "https://manage.devcenter.microsoft.com/v2.0/my/hardware/products/9007199267351834/submissions",
      "rel": "get_submissions",
      "method": "GET"
    }
  ],
  "isCommitted": true,
  "isExtensionInf": false, "_comment": "This field is deprecated and moved to submission resource",
  "deviceMetadataIds": [],
  "deviceType": "notSet",
  "isTestSign": false,
  "isFlightSign": false,
  "marketingNames": [
    "marketing name 1",
    "marketing name 2"
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
  "announcementDate": "2016-10-22T00:00:00Z",
}
```

This resource has the following values

| Value | Type | Description |
|:-|:-|:-|
| Id | Long | The private product ID of the product |
| sharedProductId | Long | The shared product ID of the product |
| Links | array of objects | Refer to [link object](#link-object)  for more details |
| isCommitted | Boolean | Indicates whether the product has at least one committed submission |
| isExtensionInf | Boolean | (DEPRECATED) Indicates whether the product is an extension driver. This field is deprecated and should no longer be used. isExtensionInf moved to a submission level property. |
| deviceMetadataIds | array of GUIDs | GUIDs which map device metadata submissions to the driver |
| deviceType | String | Indicates the type of device. Possible values are:<ul><li>"internal" - An internal component, device is part of a system and connects inside the PC<li>"external" - An external component, device is an external device (peripheral) that connects to a PC<li>"internalExternal" - Both, device can be connected internally (inside a PC) and externally (peripheral)<li>"notSet" – no data available |
| isTestSign | Boolean | Indicates whether the product is a test signed driver. For more information about test-signing driver packages, see [WHQL Test Signature Program](../install/whql-test-signature-program.md) |
| isFlightSign | Boolean | Indicates whether the product is a flight signed driver. Flight signed drivers are test drivers which can be published via Windows Update. They can be published/installed only on machines signed up for Windows Insider Program. They can be installed on machines without disabling secure boot. They can't be installed on retail machines which aren't part of Windows Insider Program. |
| marketingNames | array of strings | Marketing names or aliases of the product |
| productName | String | The name of the driver as specified during creation |
| selectedProductTypes | dictionary | Key value pair where both are strings. <ul><li>**Key** represents the operating system family code. For a list of operating system family codes, see [list of OS family codes](#list-of-operating-system-family-codes).<li>**Value** represents the type of the product. For a list of type of products, see [product types](#list-of-product-types). |
| requestedSignatures | array of strings | List of operating system signatures for which product is certified. For a list of all Operating systems, see [list of OS codes](#list-of-operating-system-codes). |
| additionalAttributes | Object |  For more information, see [additional attributes object](#additional-attribute-object). |
| testHarness | string | The type of package submitted. Possible values are: <ul><li>hlk<li>hck<li>attestation<li>notset |
| announcementDate | datetime | The date when the product gets included on the Windows Server Catalog. |

### Submission resource

This resource represents a submission of a product.

```json
{
  "id": 1152921504621442000,
  "productId": 13635057453741328,
   "workflowStatus": {
      "currentStep": "finalizeIngestion",
      "state": "completed",
      "messages": []
    },
  "links": [
    {
      "href": "https:// manage.devcenter.microsoft.com/api/v2.0/hardware/products/13635057453741329/submissions/1152921504621441944",
      "rel": "self",
      "method": "GET"
    }
  ],
  "commitStatus": "CommitPending",
  "isExtensionInf": true,
  "isUniversal": true,
  "isDeclarativeInf": true,
  "name": "HARRY-Duatest2",
  "type": "derived"
}
```

This resource has the following values:

| Value | Type | Description |
|:-|:-|:-|
| Id | long | The ID of the submission |
| Productid | long | The private product ID to which this submission is associated |
| workflowstatus | object | This is available only when retrieving details of a specific submission. This object depicts the status of the workflow for this submission. For more information, see [workflow status object](#workflow-status-object). |
| Links | array of objects | Refer to [link object](#link-object)  for more details |
| commitStatus | See [Manage Product Submissions](manage-product-submissions.md) for more details. |
| isExtensionInf | Boolean | Indicates whether the submission is an extension driver |
| isUniversal | Boolean | Indicates whether the submission passes the Universal API test. A driver is DCHU compliant if it's Declarative and Universal |
| isDeclarativeInf | Boolean | Indicates whether the submission passes the Declarative INVerif test. A driver is DCHU compliant if it's Declarative and Universal. |
| Name | string | The name of the submission. |
| Type | string | Indicates whether the submission is an initial or derived submission. Possible values are: <ul><li>initial<li>derived |
| downloads | object | This is available only when retrieving details of a specific submission only. This object depicts the downloads available for the submission. For more information, see [download object](#download-object). |

### Workflow Status object

This object represents the status of workflow for a given entity

```json
{
      "currentStep": "finalizeIngestion",
      "state": "completed",
      "messages": []
    }
```

This object has the following values

| Value | Type | Description |
|:-|:-|:-|
| currentStep | string | The name of the current step in the overall workflow for this entity. <br>For ingestion/package submission the possible values are (description in parenthesis):<ul><li>packageInfoValidation (*Validating Package metadata and contents*)<li>preparation (*Getting package ready for processing*)<li>scanning (*Scanning package contents for Malware*)<li>validation (*Validation of test results*)<li>catalogCreation (*Creating a security catalog for package*)<li>manualReview (*Undergoing Manual Review*)<li>signing (*Signing the binaries*)<li>finalizeIngestion (*Completing the ingestion and getting signed files ready to download or publish*) |
| State | string | The state of the current step. Possible values are:<ul><li>notStarted<li>started<li>failed<li>completed |
| Messages | array | An array of strings to provide messages about current step (especially if there's failure) |

### Download object

This object represents the downloads for a given submission.

```json
{
  "items": [
    {
      "type": "initialPackage",
      "url": "<SAS URL from Hardware API>"
    },
    {
      "type": "derivedPackage",
      "url": "<SAS URL from Hardware API>"
    },
    {
      "type": "signedPackage",
      "url": "<SAS URL from Hardware API>"
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
|:-|:-|:-|
| Items | array | An array of download types and the URL for each. |
| Type | string | The type of package available for download. Possible values are:<ul><li>"initialPackage" – package uploaded by user (for a new submission, it points to the SAS URI for uploading the package)<li>"derivedPackage" – shell for derived submissions<li>"signedPackage" – package signed by Microsoft<li>"certificationReport" – certification report for the signed product<li>driverMetadata - link points to a file which allows to download of driver metadata. For more information, see [driver package metadata](driver-package-metadata.md).<li>ExternalNotes<li>Unknown |
| Messages | array | An array of strings to provide messages about the downloadable files |

### Link object

This object represents a list of helpful links for the containing entity

```json
{
      "href": "https:// manage.devcenter.microsoft.com/api/v2.0/hardware/products/9007199267351834",
      "rel": "self",
      "method": "GET"
    }
```

This object has the following values

| Value | Type | Description |
|:-|:-|:-|
| Href | String | The URL to access the resource via API |
| Rel | String | Type of the resource. Possible values are:<ul><li>self – Link points to itself<li>next_link – Link points to next resource typically used for pagination<li>get_submissions – link points to all submissions of a product<li>commit_submission – link points to commit of a submission <li>update_submission – link points to update of the submission <li>update_shippinglabel – link points to update of the shipping label |
| Method | String | Type of the http method to be used when invoking the URL. Possible values are: <ul><li>GET<li>POST<li>PATCH |

### Additional Attribute object

This object provides more attributes about the product if it is of type RAID controller, Storage Controller, or Server Virtualization Validation program (SVVP). It can contain one of three types of objects – StorageController, RaidController, or SVVP.

#### StorageController Object

| Value | Type | Description |
|:-|:-|:-|
| biosVersion | string | ROM Bios Version |
| firmwareVersion | string | Firmware Version |
| driverVersion | string | Driver Version |
| driverName | string | Driver Name |
| deviceVersion | string | Device Version |
| chipsetName | string | Chipset Name |
| usedProprietary | boolean | Multi-pathing supported through proprietary driver. If true, then proprietaryName and proprietaryVersion are mandatory. |
| proprietaryName | string | Multi-path software name |
| proprietaryVersion | string | Multi-path software version |
| usedMicrosoft | boolean | Microsoft MPIO supported through device-specific module. If true, then microsoftName and microsoftVersion are mandatory. |
| microsoftName | string | Multi-path software name |
| microsoftVersion | string | Multi-path software version |
| usedBootSupport | boolean | Boot Support |
| usedBetterBoot | boolean | Boot > 2.2-TB support. If true, then Supported UEFI version and Supported ACPI version are mandatory |
| uefiVersion | string | Supported UEFI version |
| acpiVersion | string | Supported ACPI version |
| supportsSector4K512E | boolean | Support sector size of 4K/512e |
| supportsSector4K4K | boolean | Support sector size of 4K/4K |
| supportsDifferential | boolean | Differential (high-voltage differential) |

#### RaidController Object

| Value | Type | Description |
|:-|:-|:-|
| firmwareVersion | string | Firmware Version |
| filterVersion | string | Driver Version |
| driverVersion | string | Filter Version |
| usedProprietary | boolean | Multi-pathing supported through proprietary driver. If true, then proprietaryName and proprietaryVersion are mandatory |
| proprietaryName | string | Multi-path software name |
| proprietaryVersion | string | Multi-path software version |
| usedMicrosoft | boolean | Microsoft MPIO supported through device-specific module. If true, then microsoftName and microsoftVersion are mandatory |
| microsoftName | string | Multi-path software name |
| microsoftVersion | string | Multi-path software version |
| isThirdPartyNeeded | boolean | Non-Microsoft driver needed for connectivity |
| isSES | boolean | SES (SCSI Enclosure Services). Indicates if a SES is included. SCSI is the standard term for a service bus that connects devices on a system, originally Small Computer System Interface. SES is short for SCSI Enclosure Services. |
| isSAFTE | boolean | SAF-TE (ANBll Specification). Indicates if a SAF-TE is included. ANBll an industry specification. SAF-TE is short for SCSI Accessed Fault Tolerant Enclosures. SCSI is the standard term for a service bus that connects devices on a system, originally Small Computer System Interface. |
| additionalInfo | string | Additonal Information |

#### SVVP Object

| Value | Type | Description |
|:-|:-|:-|
| productVersion | string | Product Version |
| supportLink | string | Support URL |
| guestOs | string | Guest OS. Possible values are:<ul><li>Windows Server 2008<li>Windows Server 2008 Release 2<li>Windows Server 2012<li>Windows Server 2012 R2 |
| processorArchitecture | string | Hardware Processor Architecture. Possible values are:<ul><li>Xeon<li>Opteron<li>Itanium 2 |
| maxProcessors | integer | Max Processors in VM |
| maxMemory | integer | Max memory in VM (in GB) |

### List of Product Types

A product can be of the following types. Along with the operating system, this information is used to identify applicability.

- 3D Printer
- Accelerometer Sensor
- All In One
- All In One with Touch
- Audio Device
- Audio Processing Objects
- Bluetooth Controller
- Bluetooth Controller Non USB
- Camera
- Camera Sensor
- Cluster
- Compute Accelerator MCDM 2.7
- Compute Accelerator MCDM 3.1
- Compute Accelerator MCDM 3.2
- Convertible Tablet
- Desktop
- Digital Media Renderer
- Digital Media Server
- Digital Still Cameras
- Digital Video Cameras
- Distribution Scan Management Enabled Devices
- Enterprise WSD Multi-Function Printer
- Finger Print Reader
- Game Controller
- Generic Controller
- Generic Portable Device
- Graphics Adapter MCDM2.7
- Graphics Adapter MCDM2.8
- Graphics Adapter MCDM2.9
- Graphics Adapter MCDM3.0
- Graphics Adapter WDDM1.0
- Graphics Adapter WDDM1.1
- Graphics Adapter WDDM1.2
- Graphics Adapter WDDM1.2 DisplayOnly
- Graphics Adapter WDDM1.2 RenderOnly
- Graphics Adapter WDDM1.3
- Graphics Adapter WDDM1.3 DisplayOnly
- Graphics Adapter WDDM1.3 RenderOnly
- Graphics Adapter WDDM2.0
- Graphics Adapter WDDM2.0 Display Only
- Graphics Adapter WDDM2.0 Render Only
- Graphics Adapter WDDM2.1
- Graphics Adapter WDDM2.1 Display Only
- Graphics Adapter WDDM2.1 Render Only
- Graphics Adapter WDDM2.2
- Graphics Adapter WDDM2.2 Display Only
- Graphics Adapter WDDM2.2 Render Only
- Graphics Adapter WDDM2.3
- Graphics Adapter WDDM2.3 Display Only
- Graphics Adapter WDDM2.3 Render Only
- Graphics Adapter WDDM2.4
- Graphics Adapter WDDM2.4 Display Only
- Graphics Adapter WDDM2.4 Render Only
- Graphics Adapter WDDM2.4 VM
- Graphics Adapter WDDM2.5
- Graphics Adapter WDDM2.5 Display Only
- Graphics Adapter WDDM2.5 Render Only
- Graphics Adapter WDDM2.5 VM
- Graphics Adapter WDDM2.6
- Graphics Adapter WDDM2.6 Display Only
- Graphics Adapter WDDM2.6 Render Only
- Graphics Adapter WDDM2.6 VM
- Graphics Adapter WDDM2.7
- Graphics Adapter WDDM2.7 Display Only
- Graphics Adapter WDDM2.7 Render Only
- Graphics Adapter WDDM2.7 VM
- Graphics Adapter WDDM2.8
- Graphics Adapter WDDM2.8 Display Only
- Graphics Adapter WDDM2.8 Render Only
- Graphics Adapter WDDM2.8 VM
- Graphics Adapter WDDM2.9
- Graphics Adapter WDDM2.9 Display Only
- Graphics Adapter WDDM2.9 Render Only
- Graphics Adapter WDDM2.9 VM
- Graphics Adapter WDDM3.0
- Graphics Adapter WDDM3.0 Display Only
- Graphics Adapter WDDM3.0 Render Only
- Graphics Adapter WDDM3.0 VM
- Graphics Adapter WDDM3.1
- Graphics Adapter WDDM3.1 Display Only
- Graphics Adapter WDDM3.1 Render Only
- Graphics Adapter WDDM3.1 VM
- Graphics Adapter WDDM3.2
- Graphics Adapter WDDM3.2 Display Only
- Graphics Adapter WDDM3.2 Render Only
- Graphics Adapter WDDM3.2 VM
- Graphics Tablet
- Gyroscope Sensor
- Hard Drive
- Hardware Multifunction Transforms
- Keyboard
- Keyboard Video Mouse Switch
- LAN
- LAN (Server)
- LAN CS
- LAN Virtual Machine (Server)
- Laptop
- Laptop with Touch
- LCD
- Light Sensor
- Location Sensor
- Media Player
- Mobile Broadband CDMA
- Mobile Broadband GSM
- Mobile Phone
- Monitor
- Motherboard
- Motion Sensor Fusion
- Multi-Function Printer
- Near Field Proximity
- Network Media Device
- NFC
- NFC Smart Card Reader
- Optical Drive
- Pen Digitizer
- Pointing Drawing
- PrecisionTouchpad
- Presence Sensor
- Printer
- Projector
- Removable Storage
- Router
- Scanner
- SDIO Controller
- Server
- Server Virtualization Validation Program
- Signature Tablet
- Smart Cards
- Smartcard Reader
- Storage Array
- Storage Controller
- Storage Spaces Adapter
- Storage Spaces Drive
- Tablet
- Touch
- Touch Monitor
- TPM20
- Ultra-Mobile PC
- Ultra-Mobile PC with Touch
- USB Controller
- USB Hub
- WebCam
- WLAN
- WLAN CSB
- WSD Multi-Function Printer
- WSD Printer
- WSD Scanner

### List of operating system family codes

The following table lists Operating system Family Codes and their descriptions.

| OS Family Code | Description |
|:-|:-|
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
| Windows_v100Server_RS5 | Windows Server 2019 |
| Windows_v100_RS5 | Windows 10 RS5 x86 |
| Windows_v100_RS5 | Windows 10 RS5 x64 |
| Windows_v100_19H1 | Windows 10 19H1 Update |
| Windows_v100_VB | Windows 10 version 2004 |
| Windows_v100Server_FE | Windows - Server, version 21H2 |
| Windows_v100_CO | Windows - Client, version 21H2 |
| Windows_v100_NI | Windows 11 Client, version 22H2 |
| Windows_v100_GE | Windows 11 Client, version 24H2 |
| Windows_v100Server_GE | Windows Server 2025 |

### List of Operating System Codes

The following table lists Operating System Codes and their descriptions.

| OS Code | Description |
|:-|:-|
| WINDOWS_ME | Windows Me |
| WINDOWS_98 | Windows 98 |
| WINDOWS_2000 | Windows 2000 |
| WINDOWS_NT40 | Windows NT 4.0 |
| WINDOWS_XP | Windows XP |
| WINDOWS_XP_IA64 | Windows XP IA64 |
| WINDOWS_XP_X64 | Windows XP X64 |
| WINDOWS_XP_MEDIA_CENTER | Windows XP Media Center |
| WINDOWS_2003 | Windows Server 2003 |
| WINDOWS_2003_IA64 | Windows Server 2003 IA64 |
| WINDOWS_2003_X64 | Windows Server 2003 X64 |
| WINDOWS_VISTA | Windows Vista Client |
| WINDOWS_VISTA_X64 | Windows Vista Client X64 |
| WINDOWS_2008_SERVER | Windows Server 2008 |
| WINDOWS_2008_SERVER_IA64 | Windows Server 2008 IA64 |
| WINDOWS_2008_SERVER_X64 | Windows Server 2008 X64 |
| WINDOWS_HOME_SERVER | Windows Home Server |
| WINDOWS_7 | Windows 7 Client |
| WINDOWS_7_X64 | Windows 7 Client x64 |
| WINDOWS_2008_SERVER_R2_IA64 | Windows Server 2008 Release 2 IA64 |
| WINDOWS_2008_SERVER_R2_X64 | Windows Server 2008 Release 2 x64 |
| WINDOWS_SERVER_SOLUTIONS_X64 | Windows Server Solutions x64 |
| WINDOWS_8 | Windows 8 Client |
| WINDOWS_8_X64 | Windows 8 Client x64 |
| WINDOWS_8_ARM | Windows 8 Client RT |
| WINDOWS_8_SERVER_X64 | Windows Server 2012 |
| WINDOWS_v63 | Windows 8.1 Client |
| WINDOWS_v63_X64 | Windows 8.1 Client x64 |
| WINDOWS_v63_ARM | Windows 8.1 Client RT |
| WINDOWS_v63_SERVER_X64 | Windows Server 2012 R2 x64 |
| WINDOWS_v100_TH1_FULL | Windows 10 Client versions 1506 and 1511 (TH1) |
| WINDOWS_v100_X64_TH1_FULL | Windows 10 Client versions 1506 and 1511 x64 (TH1) |
| WINDOWS_v100_SERVER_X64_TH1_FULL | Windows Server 2016 x64 (TH1) |
| WINDOWS_v100_TH2_FULL | Windows 10 Client versions 1506 and 1511 (TH2) |
| WINDOWS_v100_X64_TH2_FULL | Windows 10 Client versions 1506 and 1511 x64 (TH2) |
| WINDOWS_v100_SERVER_X64_TH2_FULL | Windows Server 2016 x64 (TH2) |
| WINDOWS_v100_RS1_FULL | Windows 10 Client version 1607 |
| WINDOWS_v100_X64_RS1_FULL | Windows 10 Client version 1607 x64 |
| WINDOWS_v100_SERVER_X64_RS1_FULL | Windows Server 2016 x64 (RS1) |
| WINDOWS_v100_RS2_FULL | Windows 10 RS2 Client |
| WINDOWS_v100_X64_RS2_FULL | Windows 10 RS2 Client x64 |
| WINDOWS_v100_RS3_FULL | Windows 10 RS3 Client |
| WINDOWS_v100_X64_RS3_FULL | Windows 10 RS3 Client x64 |
| WINDOWS_v100_ARM64_RS3_FULL | Windows 10 RS3 Client Arm64 |
| WINDOWS_v100_RS4_FULL | Windows 10 RS4 Client |
| WINDOWS_v100_X64_RS4_FULL | Windows 10 RS4 Client x64 |
| WINDOWS_v100_ARM64_RS4_FULL | Windows 10 RS4 Client Arm64 |
| WINDOWS_v100_SERVER_X64_RS5_FULL | Windows Server 2019 |
| WINDOWS_v100_RS5_FULL | Windows 10 RS5 x86 |
| WINDOWS_v100_X64_RS5_FULL | Windows 10 RS5 Client x64 |
| WINDOWS_v100_19H1_FULL | Windows 19H1 Client x86 |
| WINDOWS_v100_X64_19H1_FULL | Windows 19H1 Client x64 |
| WINDOWS_v100_ARM64_19H1_FULL | Windows 19H1 Client Arm64 |
| WINDOWS_v100_VB_FULL | Windows 10 version 2004 Client x86 |
| WINDOWS_v100_X64_VB_FULL | Windows version 2004 Client x64 |
| WINDOWS_v100_ARM64_VB_FULL | Windows version 2004 Client Arm64 |
| WINDOWS_v100_SERVER_X64_FE_FULL | Windows - Server, version 21H2 x64 |
| WINDOWS_v100_SERVER_ARM64_FE_FULL | Windows - Server, version 21H2 Arm64 |
| WINDOWS_v100_X64_CO_FULL | Windows - Client, version 21H2 x64 |
| WINDOWS_v100_ARM64_CO_FULL | Windows - Client, version 21H2 Arm64 |
| WINDOWS_v100_X64_NI_FULL | Windows 11 Client, version 22H2 x64 |
| WINDOWS_v100_ARM64_NI_FULL | Windows 11 Client, version 22H2 Arm64 |
| WINDOWS_v100_X64_GE_FULL | Windows 11 Client, version 24H2 x64 |
| WINDOWS_v100_ARM64_GE_FULL | Windows 11 Client, version 24H2 ARM64 |
| WINDOWS_v100_SERVER_X64_GE_FULL | Windows Server 2025 x64 |
| WINDOWS_v100_SERVER_ARM64_GE_FULL | Windows Server 2025 ARM64 |

## Error codes

The error codes are applicable to all web methods of the API. If the request can't be successfully completed, the response contains one of the following HTTP error codes.

| HTTP Status | Description |
|:-|:-|
| 400 – Bad Request | Request not well formed (for example, malformed request syntax, invalid request message framing, or deceptive request routing) |
| 401 – Unauthorized | Authentication failed or not provided |
| 403 – Forbidden | Forbidden to access a resource. |
| 404 – Not Found | Requested entity isn't found. |
| 415 - Unsupported Media Type | Payload is in a format not supported by this method on the target resource. |
| 422 - Unprocessable Entity | Validation failures. |
| 429 - Too Many Requests | Too many requests are being sent. Calls are throttled and the backoff time is provided in the response. |
| 500 - Internal Server Error | Unrecoverable error occurred at the API server. |

If there are functional validation failures, the response body contains one of the following functional error codes.

| Error Code | Error Message | Description |
|:-|:-|:-|
| InvalidInput |  | Returned when an input validation fails. |
| RequestInvalidForCurrentState | Only pending submissions can be committed | Returned when a commit is applied on a submission which isn't in pending state. |
| RequestInvalidForCurrentState | Initial submission already exists | Returned when an initial submission is created for a driver which already has an initial submission. |
| RequestInvalidForCurrentState | Can't create derived submission since no initial submission created | Returned when a derived submission is created for a driver that doesn't have an initial submission. |
| UpdateUnauthorized | Not authorized to update the product | Returned when trying to update a product that was shared (resold) since shared products can't be updated. |
| UpdateUnauthorized | Can't update product without an initial submission | Returned when trying to update a product which doesn't have an initial submission. |
| UpdateUnauthorized | Can't update product because the workflow failed | Returned when trying to update a product which has a failed workflow. |
| UpdateUnauthorized | Announcement Date can't be updated after the ingestion process is finished | Returned when announcement date is updated after ingestion is completed. |
| UpdateUnauthorized | Product Name can't be updated at this time. Try again. |  |
| UpdateUnauthorized | Not authorized to update the submission | Returned when trying to update a submission for a product that was shared (resold) since shared products can't be updated. |
| UpdateUnauthorized | Can't update the submission since the workflows failed | Returned when trying to update a submission which has a failed workflow. |
| EntityNotFound | No submission found | Returned when trying to commit for a submission which doesn't exist. |
| EntityNotFound | Product not found | Returned when trying to create a submission for which a product doesn't exist. |
| InvalidInput | Extension drivers must be published as an Automatic update. Either of isAutoInstallDuringOSUpgrade or isAutoInstallOnApplicableSystems must be true. | Returned when a Windows update shipping label for an extension INF is created without choosing isAutoInstallDuringOSUpgrade or isAutoInstallOnApplicableSystems. |
| InvalidInput | CHIDs are allowed only when HardwareIds are for operating systems Windows 10 and later. | Returned when a shipping label targeting OS less than windows 10 is created with CHID targeting. CHID targeting is applicable only for Windows 10 and above. |
| InvalidInput | Can't update the shipping label when another workflow is in progress. Try again. | Returned when a shipping label is updated when a previous workflow is still in progress. |
| RequestInvalidForCurrentState | Can't create Publishing shipping label for inbox or system type. One can only share the shipping label. | Returned when windows update Shipping label is created on an inbox driver or a system. |
| RequestInvalidForCurrentState | Submission isn't yet ready to create shipping label. Retry after some time. | Returned when a shipping label is created without waiting for preparation or preprocessing to complete. |

## See also

- [Hardware dashboard API samples (GitHub)](https://aka.ms/hpc_async_api_samples)
