---
title: Windows Inbox Smart Card Minidriver
description: Windows Inbox Smart Card Minidriver
ms.date: 05/08/2023
---

# Windows Inbox Smart Card Minidriver

Beginning with Windows 7 with Service Pack 1 (SP1), an inbox generic class minidriver is provided that supports PIV-compliant smart cards and cards that implement the GIDS card edge.

PIV-compliant smart cards and cards that implement the GIDS card edge. For more information about PIV, see [Personal Identity Verification (PIV) of Federal Employees and Contractors](https://www.nist.gov/publications/personal-identity-verification-piv-federal-employees-and-contractors).

For more information about GIDS, see the [Generic Identity Device Specification](/previous-versions/windows/hardware/design/dn642100(v=vs.85)) web page.

When a smart card is inserted into the reader and the Base CSP/KSP calls [**CardAcquireContext**](/previous-versions/dn468701(v=vs.85)), the class minidriver performs the following discovery process to mark the associated card as either PIV- or GIDS-compliant:

1. A SELECT command is issued to locate the PIV AID. If the command succeeds, Windows considers the card to be a PIV device and the discovery process stops.
2. If the command fails, a SELECT command is issued to locate the GIDS AID. If the command succeeds, Windows considers the card to be an GIDS device and the discovery process stops.
3. If the command fails with a status code that indicates neither AID exists on the smart card, Windows still proceeds as if the card is an GIDS device. If the command fails with any other error, Windows considers the card to be an unknown device.

## Electrical Profile for GIDS cards with the Microsoft Generic Profile

For Smart Cards that implement the GIDS card edge, they must be pre-provisioned with an electrical profile that enables them for provisioning with the inbox class minidriver. The information in this section requires deep understanding of APDUs, data model and the card edge as specified in the GIDS specification.

The subsections given here must be followed in the order listed before the card can be used for personalization. Please refer to section 11 of the GIDS specification for more information on APDUs referenced in this section.

### GIDS Application Metadata

The DOs described in this section are managed by GIDS and can be retrieved only in the response data field of the SELECT command. This metadata can only be created when the application is in the “creation” state. Please refer to section 6 of the GIDS specification for more information on the GIDS Life Cycle Management.

Note that the metadata provided below only include what is required to be present exactly as described (unless otherwise noted). There are other fields that may be optional, or are customizable by the card application vendor.

### File Control Information (DF FCI)

|Tag|Len|Value|
|----|----|----|
|64|Var.|Application Template Data Object</br></br>Tag</br>4F</br>Len</br>Var.</br>Value</br>Application AID =</br></br>A0 00 00 03 97 42 54 46 59 xx yy</br><ul><li>**XX** = GIDS specification revision number that is either 01 or 02.</li><li>**YY** = Reserved for the card application.</li></ul>|

### File Management Data (DF FMD)

|Tag|Len|Value|
|----|----|----|
|64|Var.|FMD Template</br></br>Tag</br>5F2F</br>Len</br>Var.</br>Value</br>PIN usage policy (see “PIN Usage Policy”) =</br></br>Either 40 or 60<ul><li>**40** – Application PIN is present and may be used to satisfy CHV.</li><li>**60** – Application and Global PINs are both present and may be used to satisfy CHV.</li></ul>|

### File Control Parameters (DF FCP)

|Tag|Len|Value|
|----|----|----|
|62|Var.|FCP Template</br></br>Tag</br>82</br>Len</br>01</br>Value</br>File descriptor byte: 38 (“not shareable-DF”)</br></br>Tag</br>8C</br>Len</br>03</br>Value</br>Security attribute in compact format =</br></br>03 30 30</br><ul><li>**40** – Following bytes specify requirements for CREATE FILE for EFs and DELETE FILE for EFs (and in that order).</li><li>**60** – User Authentication OR External Authentication satisfy requirements to create EFs.</li><li>**60** – User Authentication OR External Authentication satisfy requirements to delete EFs.</li></ul>
<div class="alert">
<strong>Note</strong>  The security attribute does not have to exactly match this, but allowing User Authentication OR External Authentication to both create and delete EFs is required.
</div>|

Once the DF FCP has been created, the card shall transition to the “initialization” state, which is the state required for creating the objects listed in the following sections.

### PIN Creation

To create a PIN, a CHANGE REFERENCE DATA APDU for the application password must be sent to the card:

**CLA**: 00

**INS**: 24

**P1**: 01

**P2**: 80

**Lc**: Length of command data field

**Data Field**: &lt;password&gt;

**Le**: Absent

For example, to set the PIN to 12345678, the following APDU must be sent to the card:

``` syntax
00 24 01 80 08 31 32 33 34 35 36 37 38
```

### Pin Unblock Key (PUK) Creation

A PUK is used to unblock and/or reset the PIN in the cases where the card becomes blocked or the PIN is forgotten. If admin key challenge/response is to be used instead, DO NOT create a PUK.

To create a PUK, a CHANGE REFERENCE DATA APDU for the application resetting password must be sent to the card:

**CLA**: 00

**INS**: 24

**P1**: 01

**P2**: 81

**Lc**: Length of command data field

**Data Field**: &lt;password&gt;

**Le**: Absent

For example, to set the PUK to 12345678, the following APDU must be sent to the card:

``` syntax
00 24 01 81 08 31 32 33 34 35 36 37 38
```

### ACL Creation

ACLs must be created using the CREATE FILE APDU:

**CLA**: 00

**INS**: E0

**P1-P2**: 00 00

**Lc**: Length of data field

**Data Field**: FCP template for EF

**Le**: Absent

The ACLs mentioned in the table below must be created. Each ACL creation APDU must be followed by ActivateFile APDU (00 44 00 00 00)

| ACL| APDU|
|-----|----|
| UserCreateDeleteDirAc    | 00 E0 00 00 0E 62 0C 82 01 39 83 02 A0 00 8C 03 03 30 00 |
| EveryoneReadUserWriteAc  | 00 E0 00 00 0E 62 0C 82 01 39 83 02 A0 10 8C 03 03 30 00 |
| UserWriteExecuteAc       | 00 E0 00 00 0E 62 0C 82 01 39 83 02 A0 11 8C 03 03 30 FF |
| EveryoneReadAdminWriteAc | 00 E0 00 00 0E 62 0C 82 01 39 83 02 A0 12 8C 03 03 20 00 |
| UserReadWriteAc          | 00 E0 00 00 0E 62 0C 82 01 39 83 02 A0 13 8C 03 03 30 30 |
| AdminReadWriteAc         | 00 E0 00 00 0E 62 0C 82 01 39 83 02 A0 14 8C 03 03 20 20 |

### Create EF for Admin Key

EF for Admin key must be created using the CREATE FILE APDU:

**CLA**: 00

**INS**: E0

**P1-P2**: 00 00

**Lc**: Length of data field

**Data Field**: FCP template for EF (EFID = B080 and KeyID=80)

**Le**: Absent

The following APDU must be sent to the card to create the EF for a Triple-DES three-key Admin Key:

``` syntax
00 E0 00 00 1C 62 1A 82 01 18 83 02 B0 80 8C 04 87 00 20 FF A5 0B A4 09 80 01 02 83 01 80 95 01 C0
```

The command mentioned above must be followed by an ActivateFile APDU:

``` syntax
00 44 00 00 00
```

### Inject Admin Key

The Admin Key must be injected onto the card using the PUT KEY APDU:

**CLA**: 00

**INS**: DB

**P1-P2**: 3F FF

**Lc**: Length of data field

**Data Field**: Key Usage Template

**Le**: Absent

The following APDU must be sent to the card to inject the Admin key into KeyID 80:

``` syntax
00 DB 3F FF 26 70 24 84 01 80 A5 1F 87 18 01 02 03 04 05 06 07 08 01 02 03 04 05 06 07 08 01 02
03 04 05 06 07 08 88 03 B0 73 DC
```

In the example mentioned above injects the admin key with the following value:

``` syntax
01 02 03 04 05 06 07 08 01 02 03 04 05 06 07 08 01 02 03 04 05 06 07 08
```

### Set Operational State

To transition the card from the “initialization” state to the “operational” state, a SELECT DF with EFID followed an ACTIVATE FILE command needs to be sent to the card.

First, send a SELECT APDU for the DF:

**CLA**: 00

**INS**: A4

**P1-P2**: 00 0C

**Lc**: 02

**Data Field**: 3F FF

**Le**: Absent

Secondly, use the ACTIVATE FILE APDU to change the state of the DF to “operational”:

**CLA**: 00

**INS**: 44

**P1-P2**: 00 00

**Lc**: 00

**Data Field**: Absent

**Le**: Absent

The following APDU must be sent to the card to bring it to operational state:

``` syntax
00 A4 00 0C 02 3F FF
00 44 00 00 00
```

After this step, the card is ready for placing the file system as described in file system specification section and is considered a “blank card”. Follow the steps for card “creation” to place the filesystem on the card using the minidriver API. Alternatively, follow the steps in the next section to place the filesystem on the card using APDUs.

### Data objects on a GIDS card after the filesystem is created

For cards compliant with GIDS specification with Microsoft Generic Profile, the following table describes the data objects and their corresponding EFIDs after the mandatory objects are created as per the section on card “creation”. Place each of the data objects from the table below onto the card using the PUT DATA APDU as specified in the GIDS specification if the minidriver API is not being used for creating the filesystem.

<table>
<colgroup>
<col width="25%" />
<col width="25%" />
<col width="25%" />
<col width="25%" />
</colgroup>
<thead>
<tr class="header">
<th align="left">EFID</th>
<th align="left">DO Tag</th>
<th align="left">Contents</th>
<th align="left">Friendly Name</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td align="left">A000</td>
<td align="left">DF1F</td>
<td align="left"><pre class="syntax"><code>01 6d 73 63 70 00 00 00 00 00 00 00 00 00 00 00
00 00 00 00 00 00 00 00 00 00 a0 00 00 00 00 00
00 00 00 00 00 00 63 61 72 64 69 64 00 00 00 00
00 20 df 00 00 12 a0 00 00 00 00 00 00 00 00 00
00 00 63 61 72 64 61 70 70 73 00 00 00 21 df 00
00 10 a0 00 00 00 00 00 00 00 00 00 00 00 63 61
72 64 63 66 00 00 00 00 00 22 df 00 00 10 a0 00
00 6d 73 63 70 00 00 00 00 00 63 6d 61 70 66 69
6c 65 00 00 00 23 df 00 00 10 a0 00 00</code></pre></td>
<td align="left">Master file system table</td>
</tr>
<tr class="even">
<td align="left">A010</td>
<td align="left">DF21</td>
<td align="left"><pre class="syntax"><code>6d 73 63 70 00 00 00 00</code></pre></td>
<td align="left">\cardapps</td>
</tr>
<tr class="odd">
<td align="left">A010</td>
<td align="left">DF22</td>
<td align="left"><pre class="syntax"><code>00 00 00 00 00 00</code></pre></td>
<td align="left">\cardcf</td>
</tr>
<tr class="even">
<td align="left">A010</td>
<td align="left">DF23</td>
<td align="left"><pre class="syntax"><code>&lt;empty 0-byte data object&gt;</code></pre></td>
<td align="left">mscp\cmapfile</td>
</tr>
<tr class="odd">
<td align="left">A012</td>
<td align="left">DF20</td>
<td align="left"><pre class="syntax"><code>&lt;random 16-byte value&gt;</code></pre></td>
<td align="left">\cardid</td>
</tr>
</tbody>
</table>

## INF Sample to re-brand inbox class minidriver

Smart card vendors can use the inbox minidriver without the need to ship a driver package. To add branding information to the Plug and Play experience for such cards, vendors can provide INF files that override various strings to provide branding information. These strings include the following:

- ProviderName
- CardDeviceName
- SmartCardName

The following is a sample INF file that can be used with the inbox minidriver. This INF file is decorated for installation in x86 and amd64 CPU platforms.

```inf
;
;FabrikamVendor Smartcard Minidriver for an x86 and x64 based package.
;

[Version]
Signature="$Windows NT$"
Class=SmartCard
ClassGuid={990A2BD7-E738-46c7-B26F-1CF8FB9F1391}
Provider=%ProviderName%
CatalogFile=delta.cat
DriverVer=10/03/2009,10.0.0.1
PnpLockdown=1

[Manufacturer]
%ProviderName%=Minidriver,NTamd64,NTamd64.6.1,NTx86,NTx86.6.1

[Minidriver.NTamd64]
%CardDeviceName%=Minidriver64_Install,SCFILTER\CID_51FF0800

[Minidriver.NTx86]
%CardDeviceName%=Minidriver32_Install,SCFILTER\CID_51FF0800

[Minidriver.NTamd64.6.1]
%CardDeviceName%=Minidriver64_61_Install,SCFILTER\CID_51FF0800

[Minidriver.NTx86.6.1]
%CardDeviceName%=Minidriver32_61_Install,SCFILTER\CID_51FF0800

[DefaultInstall]
CopyFiles=x86_CopyFiles
AddReg=AddRegDefault

[DefaultInstall.ntamd64]
CopyFiles=amd64_CopyFiles
CopyFiles=wow64_CopyFiles
AddReg=AddRegWOW64
AddReg=AddRegDefault

[DefaultInstall.NTx86]
CopyFiles=x86_CopyFiles
AddReg=AddRegDefault

[DefaultInstall.ntamd64.6.1]
AddReg=AddRegWOW64
AddReg=AddRegDefault

[DefaultInstall.NTx86.6.1]
AddReg=AddRegDefault

[SourceDisksFiles]
msclmd64.dll=1
msclmd.dll=1

[SourceDisksNames]
1 = %MediaDescription%

[Minidriver64_Install.NT]
CopyFiles=amd64_CopyFiles
CopyFiles=wow64_CopyFiles
AddReg=AddRegWOW64
AddReg=AddRegDefault

[Minidriver64_61_Install.NT]
AddReg=AddRegWOW64
AddReg=AddRegDefault
Include=umpass.inf
Needs=UmPass

[Minidriver32_Install.NT]
CopyFiles=x86_CopyFiles
AddReg=AddRegDefault

[Minidriver32_61_Install.NT]
AddReg=AddRegDefault
Include=umpass.inf
Needs=UmPass

[Minidriver64_61_Install.NT.Services]
Include=umpass.inf
Needs=UmPass.Services

[Minidriver32_61_Install.NT.Services]
Include=umpass.inf
Needs=UmPass.Services


[Minidriver64_61_Install.NT.HW]
Include=umpass.inf
Needs=UmPass.HW

[Minidriver64_61_Install.NT.CoInstallers]
Include=umpass.inf
Needs=UmPass.CoInstallers


[Minidriver64_61_Install.NT.Interfaces]
Include=umpass.inf
Needs=UmPass.Interfaces


[Minidriver32_61_Install.NT.HW]
Include=umpass.inf
Needs=UmPass.HW

[Minidriver32_61_Install.NT.CoInstallers]
Include=umpass.inf
Needs=UmPass.CoInstallers


[Minidriver32_61_Install.NT.Interfaces]
Include=umpass.inf
Needs=UmPass.Interfaces


[amd64_CopyFiles]
msclmd.dll,msclmd64.dll

[x86_CopyFiles]
msclmd.dll

[wow64_CopyFiles]
msclmd.dll

[AddRegWOW64]
HKLM, %SmartCardNameWOW64%,"ATR",0x00000001,3b,04,51,ff,08,00
HKLM, %SmartCardNameWOW64%,"ATRMask",0x00000001,ff,ff,ff,ff,ff,ff
HKLM, %SmartCardNameWOW64%,"Crypto Provider",0x00000000,"Microsoft Base Smart Card Crypto Provider"
HKLM, %SmartCardNameWOW64%,"Smart Card Key Storage Provider",0x00000000,"Microsoft Smart Card Key Storage Provider"
HKLM, %SmartCardNameWOW64%,"80000001",0x00000000,%SmartCardCardModule%

[AddRegDefault]
HKLM, %SmartCardName%,"ATR",0x00000001,3b,04,51,ff,08,00
HKLM, %SmartCardName%,"ATRMask",0x00000001,ff,ff,ff,ff,ff,ff
HKLM, %SmartCardName%,"Crypto Provider",0x00000000,"Microsoft Base Smart Card Crypto Provider"
HKLM, %SmartCardName%,"Smart Card Key Storage Provider",0x00000000,"Microsoft Smart Card Key Storage Provider"
HKLM, %SmartCardName%,"80000001",0x00000000,%SmartCardCardModule%

[DestinationDirs]
amd64_CopyFiles=10,system32
x86_CopyFiles=10,system32
wow64_CopyFiles=10,syswow64


; =================== Generic ==================================

[Strings]
ProviderName ="FabrikamVendor"
MediaDescription="FabrikamVendor Smart Card Minidriver Installation Disk"
CardDeviceName="FabrikamVendor Minidriver for Smart Card"
SmartCardName="SOFTWARE\Microsoft\Cryptography\Calais\SmartCards\Fabrikam"
SmartCardNameWOW64="SOFTWARE\Wow6432Node\Microsoft\Cryptography\Calais\SmartCards\Fabrikam"
SmartCardCardModule="msclmd.dll"
```

The following are required for this type of INF file:

- The hardware ID that is specified by the %FabrikamCardDeviceName% string must either be the ATR historical bytes of the device or the decoded value of the device’s smart card framework identifier. For more information about this identifier, see the “Windows Smart Card Framework Card Identifier” section in [Discovery Process](discovery-process.md).
- The **DefaultInstall** section is mandatory in INF files for smart card minidriver packages.
- The **DriverVer** directive in the INF file must have a value that is greater than the version and timestamp value in the inbox driver’s INF file. Otherwise, the system does not install the device by using the vendor’s INF file.

    The **DriverVer** directive has the following syntax.

    ``` syntax
    DriverVer=mm/dd/yyyy[,w.x.y.z]
    ```

    We recommend that you follow these guidelines when setting the value for the **DriverVer** directive:

  - Specify a date value that is far enough into the future so as to avoid conflicts with Windows service pack updates.
  - Although the 4-digit version number is optional, you must specify a version that is significantly higher than the current version that is specified in the inbox driver’s INF file.

For more information on INF files and syntax, see [Device and Driver Installation Design Guide](../install/overview-of-device-and-driver-installation.md).
