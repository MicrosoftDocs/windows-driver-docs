---
title: Register an OEM Application during the Imaging Process via Universal Orchestrator Framework
description: Provides information on registering an OEM application during the imaging process via Universal Orchestrator framework.
ms.date: 10/27/2025
ms.topic: how-to
---

# Register an OEM application during the imaging process

>[!IMPORTANT]
> Universal Orchestrator provides functionality for OEMs to register an application during the imaging process to perform a one-time expedited install or update. This installation happens within 30 minutes of a user logging into a new device. Expediting an application might have a negative performance impact to the out of box experience for new devices.
>
> This functionality is only available on Windows 11 23H2 - KB5046732 (OS Build 22631.4541) and later.

## Requirements

To plug into the expedited app framework, the app must meet the following requirements:

- It must be a Store packaged app in MSIX format
- It must have a valid Product Family Name (PFN)

## Registration

Registration files are ASCII JSON files that contain metadata with information on the desired expedited flow and any custom client-side targeting that needs to be performed.

Expedited apps support two mechanisms to update / acquire an app:

1. From the Microsoft Store using a ProductId *(Recommended)*
1. From a URL that contains an MSIX package or bundle. This package must contain a Store packaged app with a valid Package Family Name (PFN). The OEM or App Owner is responsible for maintaining this URL.

Each registration file must contain the following required JSON properties:

| Key | Type | Description |
|--|--|--|
| PFN | String | The Package Family Name of the app (Example: Microsoft.WindowsStore_8wekyb3d8bbwe) |
| OEMName | String | String to represent the OEM creating this registration |
| UpdaterName | String | Unique name to track this expedited registration |
| RegistrationVersion | Number | The version of this app registration |
| Source | String | Allowed values:<br><br>Store &#124; CustomURL<br><br>Store - searches for the app directly from the Microsoft Store<br><br>CustomURL - searches for the app from a URL specified in the app registration's "Endpoint" value |
| Scenario | String | Allowed values:<br><br>Update &#124; Acquisition &#124; StubAcquisition<br><br>Update - (Not supported for CustomURL flows) attempts to update an existing app to its latest available version. No work is done if the app isn't present<br><br>Acquisition - attempts to acquire the latest version of an app.<br><br>StubAcquisition - attempts to acquire a "stub" of the app (if it's available). Acquires the full app if the stub isn't available. |
| ProductId | String | (Only required for Store scenarios)<br><br>The ProductId of the desired Store app |
| Endpoint | String | (Only required for CustomURL scenarios)<br><br>A string URI pointing to a location hosting an MSIX package. Must be an SSL URI that begins with 'https'. |

Additionally, the following optional properties can be specified to modify the behavior of the expedited app installation, or to target the expedited flow to occur only under certain conditions.

| Key | Type | Default | Description |
|--|--|--|--|
| AllowedInOobe | Boolean | False | Whether this expedited app should run during user OOBE.<br><br>**Important:** Use caution when setting to true, since this might create resource constraints on a device during the Out of Box Experience flow and negatively impact user perceived performance. |
| MaxRetryCount | Number | 1 | The number of times this updater is allowed to retry after failure.<br><br>Maximum allowed value is: 5 |
| TimeoutDurationInMinutes | Number | 15 | The duration in minutes to wait for this updater to complete work.<br><br>Maximum allowed value is: 30 |
| Architecture | String | No restriction | Allowed values:<br><br> "amd64" &#124; "arm64"<br><br>Specifies whether the expedited work should only occur for a specific architecture. |
| MinimumAllowedBuildVersion | Number | No restriction | Minimum Windows build versions where the expedited work is allowed.<br><br>For example, if set to 22631, expedited work is allowed for Windows 11 23H2 (10.0.22631.x), but blocked for Windows 11 22H2 (10.0.22621.x) |
| HonorDeprovisioning | Boolean | False | (Only applicable for Acquisition scenarios)<br><br> If the app was previously deprovisioned, don't attempt to acquire it again. |
| SkipIfPresent | Boolean | False | (Only applicable for Acquisition scenarios)<br><br>Don't perform the expedited work if any version of the app is already present. |
| Priority | Number | 100 | A numeric value from 1 - 100 to indicate relative priority of this application update.<br><br>Lower values indicate a higher relative priority to other expedited apps. |
| ExcludedRegions | Array (String) | No restrictions | A JSON array of strings for regions where this app should NOT be expedited.<br><br>Each entry in the array corresponds to the two letter ISO 3166-1 country code of the desired region.<br><br>Example: `["US", "MX"]` would prevent this flow on devices where the region is United States or Mexico.<br><br>This value can't be used with *IncludedRegions*. |
| IncludedRegions | Array (String) | No restrictions | A JSON array of strings that indicate an allowlist of regions where this app should be expedited.<br><br>Each entry in the array corresponds to the two letter ISO 3166-1 country code of the desired region.<br><br>Example: `["US", "MX"]` would allow this flow only on devices where the region is United States or Mexico.<br><br>This value can't be used with *ExcludedRegions*. |
| IncludedEditions | Array (Number) | No restrictions | A JSON array of numbers that indicate an allowlist of Editions where this app should be expedited.<br><br>Each entry in the array corresponds to the Edition code retrieved by the [GetProductInfo API](/windows/win32/api/sysinfoapi/nf-sysinfoapi-getproductinfo).<br><br>Example: `[121, 122]` to include only Education and EducationN Editions<br><br>This value can't be used with *ExcludedEditions*. |
| ExcludedEditions | Array (Number) | No restrictions | A JSON array of numbers for Editions where this app should NOT be expedited.<br><br>Each entry in the array corresponds to the Edition code retrieved by the [GetProductInfo API](/windows/win32/api/sysinfoapi/nf-sysinfoapi-getproductinfo).<br><br> Example: `[121, 122]` to exclude Education and EducationN Editions.<br><br>This value can't be used with *IncludedEditions*. |

## Samples

**Store-based stub acquisition, only in US and Mexico, to execute during OOBE**

```json
{  
    "OEMName": "Contoso",
    "UpdaterName": "OEMApp1",
    "RegistrationVersion":1,  
    "Source": "Store",  
    "Scenario": "StubAcquisition",  
    "PFN": "FakePackageFamilyName",  
    "ProductId": "StoreProductId",  
    "HonorDeprovisioning": true,  
    "AllowedInOobe": true,  
    "IncludedRegions": ["US", "MX"],  
    "Priority": 50  
}
```

**URL-based app acquisition on amd64 devices, excluding Education and EducationN editions, on Windows 11 23H2 only `(not Windows 11 22H2)`**

```json
{  
    "OEMName": "Contoso",
    "UpdaterName": "OEMApp1",
    "RegistrationVersion":2,  
    "Source": "CustomURL",  
    "Scenario": "Acquisition",  
    "PFN": "FakePackageFamilyName",  
    "Endpoint": "https://<SSL_URI>",   
    "ExcludedEditions": [121, 122],   
    "Architecture": "amd64",   
    "MinimumAllowedBuildVersion": 22631,  
    "Priority": 60 
}
```

## Tools  

To facilitate the registration process and provide actionable feedback on the registration metadata, OEMs need to use the **AppOrchestration** PowerShell scripts from the following location:
  
[microsoft/ms-update-universalorchestrator: Scripts and tools to onboard to Universal Orchestrator based update flows](https://github.com/microsoft/ms-update-universalorchestrator)

The scripts perform basic validation and stage the registration to the appropriate location on the device. On any failures, the scripts throw an exception with the specific failure details.  

To use the scripts:

1. Download the scripts to your device. From the GitHub repo page, you can select to download as a ZIP file and extract to your device
1. In a PowerShell window, run \"Import-Module \<PathToScripts>\scripts\AppOrchestration.psd1\"

> [!NOTE]
> These scripts require the user to have administrative privileges on the device, and must be executed from an elevated console.

There are four main cmdlets used for the registration flow:

**Test-UpdaterRegistration \<PathToRegistrationFile>**  
Purpose: Validate contents of a proposed registration file (without performing registration). Allows OEM to iterate on the registration file payload without affecting the device.

**Add-UpdaterRegistration \<PathToRegistrationFile>**  
Purpose: Validate and stage the contents of a registration file to the appropriate location, to onboard to the expedited app flow.

**Get-UpdaterRegistration \<OEMName> \<UpdaterName>**  
Purpose: If OEMName and UpdaterName are provided, return a summary of an existing registration that matches those values. If those inputs are omitted, return a summary of all the current registrations present on the device.

**Remove-UpdaterRegistration \<OEMName> \<UpdaterName>**  
Purpose: Unstage any registration that matches the OEMName and UpdaterName values.

## Execution

The Universal Orchestrator framework automatically invokes each of the registered apps, in sequence based on relative priority, within the first 30 minutes of a user reaching the Desktop on a new device (or during User OOBE if AllowedInOobe is set to true). Each registered application added by the OEM registration process will be attempted until either:  

- It's successfully installed  
- It surpasses the maximum number of failures specified in MaxRetryCount. After each failure, the app will enter a cool down period of 30 minutes before it's attempted again.

The Universal Orchestrator framework won't perform expedited attempts if any of the following conditions are true:

- Device doesn't have internet access.
- Device is on a metered network.  
- Device is on battery, and battery saver is enabled.  
- Device is configured with a [Windows Update Restricted Network Traffic policy](/windows/privacy/manage-connections-from-windows-operating-system-components-to-microsoft-services#bkmk-wu).  
- Device is configured with a [CTA policy](/windows-hardware/customize/desktop/unattend/microsoft-windows-deviceaccess-setregionspecificprivacyaccesspolicy) that isn't set for AutoApprove.

In each of these cases, the Universal Orchestrator framework keeps the registrations in place until the device configuration allows expedited attempts to proceed.

If the app registration contains optional values that block the expedited flow (for example, due to edition type), the Universal Orchestrator framework considers this registration request fulfilled and won't attempt it again, even if those conditions might later change on a device.

> [!IMPORTANT]
> Exercise caution when opting to expedite apps via this framework, as the update operations occur when the device might be in use and can cause a negative performance impact of the user experience on a new device.
