---
title: Authoring an update driver package
description: This topic provides information about authoring an update driver package and provides example INF file settings and configurations.
ms.assetid: 9018900A-3670-4C78-9094-1DDAB82847DD
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Authoring an update driver package


It is required that the update payload for each firmware resource described in the ESRT be bundled and distributed in its own driver package so as to allow it to maintain its own versioning scheme without being tied to other firmware resource updates that may not be updated at the same cadence.

The following example provides a sample driver package INF file definition for a firmware resource update that targets the {SYSTEM\_FIRMWARE} resource from the ESRT example in Table 2, updating it from version 1 to version 2. For reference purposes, let’s assume that the GUID assigned for the SYSTEM\_FIRMWARE resource is 6bd4efb9-23cc-4b4a-ac37-016517413e9a.

```INF
[Version]
Signature   = "$WINDOWS NT$"
Provider    = %Provider%
Class       = Firmware
ClassGuid   = {f2e7dd72-6468-4e36-b6f1-6488f42c1b52}
DriverVer   = 01/01/2012,2.0.0.0
CatalogFile = catalog.cat
PnpLockdown = 1

[Manufacturer]
%MfgName% = Firmware,NTarm

[Firmware.NTarm]
%FirmwareDesc% = Firmware_Install,UEFI\RES_{6bd4efb9-23cc-4b4a-ac37-016517413e9a}

[Firmware_Install.NT]
CopyFiles = Firmware_CopyFiles

[Firmware_CopyFiles]
firmware.bin

[Firmware_Install.NT.Hw]
AddReg = Firmware_AddReg

[Firmware_AddReg]
HKR,,FirmwareId,,{6bd4efb9-23cc-4b4a-ac37-016517413e9a}
HKR,,FirmwareVersion,%REG_DWORD%,0x00000002
HKR,,FirmwareFilename,,{6bd4efb9-23cc-4b4a-ac37-016517413e9a}\firmware.bin

[SourceDisksNames]
1 = %DiskName%

[SourceDisksFiles]
firmware.bin = 1

[DestinationDirs]
DefaultDestDir = %DIRID_WINDOWS%,Firmware\{6bd4efb9-23cc-4b4a-ac37-016517413e9a}

[Strings]
; localizable
Provider     = "Contoso Ltd."
MfgName      = "Fabrikam Inc."
FirmwareDesc = "Fabrikam System Firmware 2.0"
DiskName     = "Firmware Update"

; non-localizable
DIRID_WINDOWS = 10
REG_DWORD     = 0x00010001
```

Change the following sections to customize for your setup.

```INF
[Version]
DriverVer --> The date on which this driver package was authored; the Driver version of this driver package. Driver version in this driver package must be greater than the current driver version
CatalogFile --> Name of the catalog file

firmware.bin --> Change all instances of firmware.bin with the name of the firmware image name

[Manufacturer]
%MfgName% = Firmware,NTarm
[Firmware.NTarm] --> Change the architecture. 
For x86, it should be NTx86
For AMD64, it should be NTamd64

[Firmware.NTarm]
%FirmwareDesc% = Firmware_Install,UEFI\RES_{6bd4efb9-23cc-4b4a-ac37-016517413e9a} --> The GUID of the firmware resource

[Firmware_AddReg]
HKR,,FirmwareId,,{6bd4efb9-23cc-4b4a-ac37-016517413e9a} --> The GUID of the firmware resource
HKR,,FirmwareVersion,%REG_DWORD%,0x00000002 --> Version of the firmware for the update
HKR,,FirmwareFilename,,{6bd4efb9-23cc-4b4a-ac37-016517413e9a}\firmware.bin --> The subdirectory named after the GUID of the firmware resource and the firmware image name

[DestinationDirs]
DefaultDestDir = %DIRID_WINDOWS%,Firmware\{6bd4efb9-23cc-4b4a-ac37-016517413e9a} --> The full destination path for the firmware image file based under a subdirectory named after the GUID of the firmware resource within the %SystemRoot%\Firmware directory

[Strings]
; localizable
Modify any strings here [optional]
```

The following table describes the various driver package INF sections and fields with reference to the above sample driver package INF file definition.

<table>
<colgroup>
<col width="33%" />
<col width="33%" />
<col width="33%" />
</colgroup>
<thead>
<tr class="header">
<th>Section/Field</th>
<th>Value</th>
<th>Comment</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><strong>[Version]</strong></td>
<td></td>
<td>Defines driver package versioning information.</td>
</tr>
<tr class="even">
<td>Provider</td>
<td><p>%Provider% = Contoso Inc.</p>
<p>(localized in [Strings] section)</p></td>
<td>Identifies the provider/vendor of the entire firmware resource update driver package.</td>
</tr>
<tr class="odd">
<td>Class/ClassGuid</td>
<td><p>Firmware/</p>
<p>{f2e7dd72-6468-4e36-b6f1-6488f42c1b52}</p></td>
<td>Specifies the date of the driver package. The date and version should both reflect the date and version of the actual firmware resource update as closely as possible in order to ensure that the PnP device installation system can accurately select the best driver package available on the system.</td>
</tr>
<tr class="even">
<td>CatalogFile</td>
<td>catalog.cat</td>
<td>Specifies the associated catalog file that signs the driver package INF file and all associated firmware resource update binaries.</td>
</tr>
<tr class="odd">
<td>PnpLockdown</td>
<td>1</td>
<td>Enables the PnP driver file lockdown mechanism in order to protect installed driver files from being modified externally by unrelated applications. For firmware resource updates, this setting should always be enabled to ensure that firmware resource image files cannot be tampered with outside of the control of the PnP system.</td>
</tr>
<tr class="even">
<td><strong>[Manufacturer]</strong></td>
<td></td>
<td>Lists all distinct driver manufacturers/vendors that define firmware resource updates. Each manufacturer line specifies an [&lt;Models&gt;] section and identifies its supported target platform.</td>
</tr>
<tr class="odd">
<td><p>%MfgName%</p></td>
<td><p>Fabrikam Inc.</p>
<p>(localized in [Strings] section)</p></td>
<td>Identifies the manufacturer/vendor of the firmware resource update. This may be the same as the Provider field.</td>
</tr>
<tr class="even">
<td></td>
<td><p>Firmware,</p>
<p>NTarm</p></td>
<td>Identifies the &lt;Models&gt;] section that defines the firmware resource devices supported by this driver package, including their target driver platforms. In this example, the drivers are only targeted for the ARM-based NT platform and the [&lt;Models&gt;] section is [Firmware.NTarm].</td>
</tr>
<tr class="odd">
<td><strong>[Firmware.NTarm]</strong></td>
<td></td>
<td>[&lt;Models&gt;] section for the ARM-based NT platform that lists all firmware resource devices for which updates are defined. Each hardware model line specifies a [&lt;DDInstall&gt;] section and its associated hardware ID match.</td>
</tr>
<tr class="even">
<td>%FirmwareDesc%</td>
<td><p>Fabrikam System Firmware 2.0</p>
<p>(localized in [Strings] section)</p></td>
<td>Describes the firmware resource update. This is the primary description string used to present the associated firmware resource device instance in Device Manager and other device related UI. For this reason, the description may include the firmware vendor and version.</td>
</tr>
<tr class="odd">
<td></td>
<td><p>Firmware_Install,</p>
<p>UEFI\RES_{RESOURCE_GUID}</p></td>
<td>Identifies the [&lt;DDInstall&gt;] section containing the installation steps for the firmware resource update that targets the device instance identified by the UEFI\RES_{RESOURCE_GUID} hardware ID. Where RESOURCE_GUID is the GUID of the firmware resource that is being updated.</td>
</tr>
<tr class="even">
<td><p><strong>[Firmware_Install.NT]</strong></p>
<p>CopyFiles = Firmware_CopyFiles</p>
<p><strong>[Firmware_CopyFiles]</strong></p>
<p>...</p></td>
<td></td>
<td>[&lt;DDInstall&gt;] section that contains the installation steps for the firmware resource update. For firmware resource updates, this only defines the firmware resource image file to copy into place for a firmware resource update. In this example, the [&lt;DDInstall&gt;] section is [Firmware_Install.NT].</td>
</tr>
<tr class="odd">
<td><em>firmware.bin</em></td>
<td></td>
<td>Specifies the firmware resource update image file to copy. See section [DestinationDirs] below for details about where this file is copied.</td>
</tr>
<tr class="even">
<td><p><strong>[Firmware_Install.NT.Hw]</strong></p>
<p>AddReg = Firmware_AddReg</p>
<p><strong>[Firmware_AddReg]</strong></p>
<p>...</p></td>
<td></td>
<td>[&lt;DDInstall&gt;.Hw] section that contains the hardware-specific installation steps for the firmware resource update. For firmware resource updates, this defines the firmware resource update configuration information in the form of registry values that are set under the device hardware key of the target device instance.</td>
</tr>
<tr class="odd">
<td>FirmwareId</td>
<td>{RESOURCE_GUID}</td>
<td>The firmware GUID of the firmware resource update. Note that this is the same firmware resource GUID that is embedded in the UEFI\RES_{RESOURCE_GUID} hardware ID, however it must be specified here as a standalone value since the PnP system treats all hardware IDs as opaque strings that are strictly used for device/driver matching purposes.</td>
</tr>
<tr class="even">
<td>FirmwareVersion</td>
<td>0x00000002</td>
<td>The firmware version of the firmware resource update, specified as a REG_DWORD value.</td>
</tr>
<tr class="odd">
<td>FirmwareFilename</td>
<td>{RESOURCE_GUID}&lt;em&gt;firmware.bin</em></td>
<td>The firmware filename of the firmware resource update’s Update Capsule image filename. This path is relative to the %SystemRoot%\Firmware directory such that {RESOURCE_GUID} represents a subdirectory used to organize all firmware image files targeted for specific firmware resource.</td>
</tr>
<tr class="even">
<td><strong>[SourceDisksNames]</strong></td>
<td></td>
<td>Lists all distinct driver package source disk locations where associated driver files, such as firmware update resource image files, are contained.</td>
</tr>
<tr class="odd">
<td>1</td>
<td><p>%DiskName% = Firmware Update</p>
<p>(localized in [Strings] section)</p></td>
<td>Specifies an arbitrarily numbered driver package source disk ID and its description name. No optional driver package relative subdirectory is specified so any driver files associated to this disk ID, like the firmware resource update image file, are expected to live directly beside the INF file.</td>
</tr>
<tr class="even">
<td><strong>[SourceDisksFiles]</strong></td>
<td></td>
<td>Lists all driver files referenced by the driver package and links them to a disk ID from the [SourceDisksNames] section.</td>
</tr>
<tr class="odd">
<td><em>firmware.bin</em></td>
<td>1</td>
<td>Establishes the <em>firmware.bin</em> firmware resource update image file as being part of the driver package by linking it with the primary disk ID. No optional file-specific subdirectory is specified so this driver file is expected to live relative to its disk ID’s subdirectory, which in this case is right beside the INF file.</td>
</tr>
<tr class="even">
<td><strong>[DestinationDirs]</strong></td>
<td></td>
<td>Lists the target destination directories of all driver files referenced by the driver package.</td>
</tr>
<tr class="odd">
<td>DefaultDestDir</td>
<td><p>%DIRID_WINDOWS%,Firmware&lt;/p&gt;
<p>{RESOURCE_GUID}</p></td>
<td>Specifies the default destination directory of all driver files copied by this driver package to be %SystemRoot%\Firmware, where DIRID_WINDOWS (10) represents the base %SystemRoot% directory and {RESOURCE_GUID} represents a subdirectory names after the firmware resource GUID.</td>
</tr>
<tr class="even">
<td><strong>[Strings]</strong></td>
<td></td>
<td>Defines key/value mappings for all indirect string tokens (%token%) in the driver package INF file. Use of string tokens enables a driver package INF file to be easily localized by introducing locale-specific [Strings.&lt;LanguageID&gt;] sections. It can also be useful to use string token substitution for defining constant numeric values, such as REG_DWORD.</td>
</tr>
<tr class="odd">
<td>Provider</td>
<td>&quot;Contoso Ltd.&quot;</td>
<td>An example of a string token key/value mapping.</td>
</tr>
</tbody>
</table>



It is important to use a unique name for each firmware resource update image file version in order to avoid any potential collisions with other firmware image files, both your own and those from other firmware vendors. For example, *firmware.bin* from the above should be assigned the following name to satisfy both vendor name and version constraints: *Fabrikam-System-Firmware-2.0.bin*.

In order to ensure that variants of a given firmware resource update image, potentially used for OEM/IHV customization purposes, do not collide when deployed into the same Windows system image, it is recommended that each distinct firmware resource update image is maintained under a subdirectory within the %SystemRoot%\\Firmware directory. This subdirectory should be named after either the target firmware resource GUID. For example, the following firmware resource update image paths satisfy the deployment constraints: %SystemRoot%\\Firmware\\{6bd4efb9-23cc-4b4a-ac37-016517413e9a}\\Fabrikam-System-Firmware-2.0.bin.

## Test signing the firmware driver package


Once the driver package INF file and firmware payload binary are ready, the entire driver package must be signed in order to produce a catalog file. It is crucial that this catalog file vouch for the validity and authenticity of the INF file and firmware payload binary contained within the driver package in order to enable Windows to securely initiate a firmware resource update.

The steps to self-sign the driver package for test purposes are enumerated below. Please note that these steps are for test purposes only. In production, firmware update driver packages must be submitted to the Windows Dev Center Hardware Dashboard for signing. For the steps to sign a firmware driver package for production see [Certifying and signing the update package](certifying-and-signing-the-update-package.md).

1.  Install the latest Windows SDK and Windows Driver Kit. This will install the makecert, pvk2pfx inf2cat and signtool tools under %systemdir%\\Program Files (x86)\\Windows Kits\\&lt;*version*&gt;\\bin\\x86.
2.  Run the following command to create a test certificate.

    ```console
    makecert.exe -r -pe -a sha256 -eku 1.3.6.1.5.5.7.3.3 -n CN=Foo -sv fwu.pvk fwu.cer
    pvk2pfx.exe -pvk fwu.pvk -spc fwu.cer -pi <Password entered during makecert prompt> -spc fwu.cer -pfx fwu.pfx
    ```

    For more information, see [**MakeCert**](https://msdn.microsoft.com/library/windows/hardware/ff548309).

3.  Run the following command to create a catalog file.

    ```console
    Inf2Cat.exe /driver:"." /os:8_x64
    ```

    The */driver* argument points to the location where the INF is located. Change the value of the */os* argument depending on the OS for which the firmware driver package is intended for. For more information, see [**Inf2Cat**](https://msdn.microsoft.com/library/windows/hardware/ff547089).

    For more information about security catalogs and drivers, see [Catalog Files and Digital Signatures](https://msdn.microsoft.com/library/windows/hardware/ff537872) and [Creating a Catalog File for a PnP Driver Package](https://msdn.microsoft.com/library/windows/hardware/ff540161).

4.  Run the following command to sign the catalog file.

    ```console
    signtool sign /fd sha256 /f fwu.pfx /p <Password entered during makecert prompt> delta.cat
    ```

    For more information, see [**SignTool**](https://msdn.microsoft.com/library/windows/hardware/ff551778).

5.  Install the test certificate on the test system:
    1.  Double click on the fwu.cer file and choose the **Install Certificate** option.
    2.  Choose the following options during the certificate installation:
        -   For Store location, choose **Local Machine**.
        -   For Certificate Store, browse and select **Trusted Root Certification Authorities**.

6.  Disable secure boot in the firmware/BIOS options.
7.  Enable test signing in the BCD options so that the OS loader can load the firmware image file (firmware.bin) during boot even if the catalog is not production signed. Run the following command with administrator privileges:

    ```console
    bcdedit /set testsigning on
    ```

After the driver package is signed, it can be installed using one of the following mechanisms:

-   **Device Manager**. For manual testing, Device Manager provides a friendly interface for locating a firmware resource device and updating its driver in order to initiate a firmware resource update.
    1.  Locate the desired firmware resource device under the “Firmware” class while viewing devices by type, or under the “Microsoft UEFI-Compliant System” device while viewing devices by connection.
    2.  Right-click on the firmware resource device and select the “Update Driver Software...” option.
    3.  Use the “Browse my computer for driver software” option to locate and install a newer firmware resource update driver package onto the firmware resource device. This operation will ensure that the specified firmware resource update driver package is in fact newer than any existing firmware resource update driver package that might already be on the firmware resource device before adding it to the Windows Driver Store and initiating an installation.
-   **pnputil**. For automated testing, the pnputil command line utility can be used from an Administrator-elevated command prompt to import a firmware resource update driver package into the Windows Driver Store and initiate a device installation on any/all applicable firmware resource devices that are presently using an older firmware resource version, as established by the DriverVer of their currently installed driver package INF file or a lack of a 3rd party supplied driver package INF file altogether. For example, use the following command line to add and install X:\\firmware.inf:

    ```console
    pnputil -i -a X:\firmware.inf
    ```

    **Note**  The pnputil tool is not supported on Windows 10 Mobile.



If the firmware resource update was successfully installed on a firmware resource device and it supplies a firmware resource update that is a higher version than the current firmware version, then the device will be awaiting a system reboot in order to complete the update operation. A device in this state will indicate its need for the system to be rebooted by maintaining a device problem, which prevents the device from being started and restored to a steady state until the reboot is performed.

## Validating the status of the firmware update


When a firmware driver package is successfully installed, PnP will request a system reboot to apply the updates. Post reboot, the status of the update can be validated. The status of the update is maintained under the following registry key: HKEY\_LOCAL\_MACHINE\\SYSTEM\\CurrentControlSet\\Control\\FirmwareResources\\{RESOURCE\_GUID}.

RESOURCE\_GUID is the GUID of the resource (from ESRT) that was updated.

The “LastAttemptStatus” registry value indicates the status of the firmware update, where a value of 0 indicates success and any non-zero value represents a failure. The value for this registry key are NTSTATUS codes populated by OS Loader based upon the value of the LastAttemptStatus from the ESRT. The following table maps the LastAttemptStatus code to its corresponding NTSTATUS code.

| LastAttemptStatus                        | Code | NTSTATUS                        | Code       |
|------------------------------------------|------|---------------------------------|------------|
| Success                                  | 0    | STATUS\_SUCCESS                 | 0x00000000 |
| Error: Unsuccessful                      | 1    | STATUS\_UNSUCCESSFUL            | 0xC0000001 |
| Error: Insufficient Resources            | 2    | STATUS\_INSUFFICIENT\_RESOURCES | 0xC000009A |
| Error: Incorrect Version                 | 3    | STATUS\_REVISION\_MISMATCH      | 0xC0000059 |
| Error: Invalid Image Format              | 4    | STATUS\_INVALID\_IMAGE\_FORMAT  | 0xC000007B |
| Error: Authentication Error              | 5    | STATUS\_ACCESS\_DENIED          | 0xC0000022 |
| Error: Power Event, AC Not Connected     | 6    | STATUS\_POWER\_STATE\_INVALID   | 0xC00002D3 |
| Error: Power Event, Insufficient Battery | 7    | STATUS\_INSUFFICIENT\_POWER     | 0xC00002DE |



The Hardware ID property of the firmware resource device node should also reflect the change in the firmware version, where XXX is the new firmware version.

-   UEFI\\RES\_{RESOURCE\_GUID}&REV\_XXX

If the firmware update failed, you can retry the failed firmware update:

-   In Device Manager, expand the Firmware node, right-click the firmware resource device, and click **Update Driver Software**.
-   Click **Browse my computer for driver software**, and on the next page click **Let me pick from a list of device drivers on my computer**.
-   Select the same driver that you installed previously, and click OK.

After the next reboot, the OS Loader will call into UpdateCapsule() with the payload of the firmware driver package.

## Related topics

[ESRT table definition](esrt-table-definition.md)  

[Plug and play device](plug-and-play-device.md)  

[Processing updates](processing-updates.md)  

[Device I/O from the UEFI environment](device-i-o-from-the-uefi-environment.md)  

[Seamless crisis prevention and recovery](seamless-crisis-prevention-and-recovery.md)  

[Firmware update status](firmware-update-status.md)  
