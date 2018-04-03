# Get product data

Use the following methods in *Microsoft Hardware APIs* to get data for hardware products registered to your Dev Center Account. For an introduction to Microsoft Hardware APIs, including prerequisites for using the API, see [Manage hardware submissions using APIs](TBD).

<!-- https://manage.devcenter.microsoft.com/api/v1.0/my/hardware/products/-->

Before you can use these methods, the product must already exist in your
Dev Center account. To create or manage submissions for products, see
the methods in [Manage product submissions](TBD)

| Method                | URI                   | Description           |
|-|-|-|
| GET | `https://manage.devcenter.microsoft.com/api/v1.0/hardware/products`|[Get data for all your products](TBD) |
| GET                   | `https://manage.devcenter.microsoft.com/api/v1.0/hardware/products/`**{productID}** | [Get data for a specific product](TBD)
| GET                   | `https://manage.devcenter.microsoft.com/api/v1.0/hardware/products/`**{productID}**`/submissions` | [Get data for all submissions of a product](TBD) |
| GET                   | `https://manage.devcenter.microsoft.com/api/v1.0/hardware/products/`**{productID}**`/submissions/`**{submissionId}** | [Get data for a specific submission of a product](TBD) |

## Prerequisites

If you have not done so already, complete all the [prerequisites](dashboard-api.md) for the Microsoft Hardware APIs before trying to use any of these methods.

## Data resources

The Microsoft Hardware APIs methods for getting product data use the
following JSON data resources:

### Product resource

This resource represents a hardware product (driver) that is registered
to your account

```
JSON

{
"id": 9007199267351834,
"sharedProductId": 1152921504606971100,
"links": [
{
"href": "https://manage.devcenter.microsoft.com/api/v1.0/hardware/products/9007199267351834\",
"rel": "self",
"method": "GET"
},
{
"href": "https://manage.devcenter.microsoft.com/api/v1.0/hardware/products/9007199267351834/submissions\",
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

<table>
	<thead>
		<tr>
			<th class="x-hidden-focus">Value</th>
			<th>Type</th>
			<th>Description</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td>ID</td>
			<td>Long</td>
			<td>The private product ID of the product</td>
        </tr>
		<tr>
			<td>sharedProductId</td>
			<td>Long</td>
			<td>The shared product ID of the product</td>
		</tr>
		<tr>
			<td>Links</td>
			<td>arrays of objects</td>
			<td>See [Link object](TBD) for more details</td>
        </tr>
		<tr>
			<td>isCommitted</td>
			<td>Boolean</td>
			<td>Indicates whether the product has at least one committed submission</td>
        </tr>
		<tr>
			<td> isExtensionInf</td>
			<td>Boolean</td>
			<td>Indicates whether the product is an extension driver</td>
        </tr>
		<tr>
			<td>deviceMetadataIds</td>
			<td>array of GUIDs</td>
			<td>GUIDs which map device metadata submissions to the driver</td>
        </tr>
		<tr>
			<td>deviceType  </td>
			<td>String</td>
			<td>Indicates the type of device. Possible values are:
                <ul>
                    <li><strong>internal</strong> - An internal component. The device is part of a system and connects inside the PC.</li> 
                    <li><strong>external</strong> - An external component. The device is an external device (peripheral) that connects to a PC.</li>
                    <li><strong>internalExternal</strong> - Both. The device can be connected internally (inside a PC) and externally (peripheral).</li>
                    <li><strong>notSet</strong> - No data available.</li>
                </ul>
            </td>
        </tr>
		<tr>
			<td>isTestSign</td>
			<td>Boolean</td>
			<td>Indicates whether the product is a test signed driver. For more information about test-signing driver packages, see <a href="https://docs.microsoft.com/en-us/windows-hardware/drivers/install/whql-test-signature-program">WHQL Test Signature Program</a></td>
        </tr>
		<tr>
			<td></td>
			<td></td>
			<td></td>
        </tr>
	</tbody>
</table>

   |
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