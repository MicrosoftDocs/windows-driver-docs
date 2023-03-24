---
title: Authoring an update driver package
description: This topic provides information about authoring an update driver package and provides example INF file settings and configurations.
ms.date: 03/22/2023
---

# Authoring an update driver package

It is required that the update payload for each firmware resource described in the ESRT be bundled and distributed in its own driver package so as to allow it to maintain its own versioning scheme without being tied to other firmware resource updates that may not be updated at the same cadence.

The following example provides a sample driver package INF file definition for a firmware resource update that targets the {SYSTEM_FIRMWARE} resource from the ESRT example in Table 2, updating it from version 1 to version 2. For reference purposes, let's assume that the GUID assigned for the SYSTEM_FIRMWARE resource is 6bd4efb9-23cc-4b4a-ac37-016517413e9a.

```inf
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
HKR,,FirmwareFilename,,%13%\firmware.bin
; Prior to Windows 10 1803, the above should instead be:
; HKR,,FirmwareFilename,,{6bd4efb9-23cc-4b4a-ac37-016517413e9a}\firmware.bin

[SourceDisksNames]
1 = %DiskName%

[SourceDisksFiles]
firmware.bin = 1

[DestinationDirs]
DefaultDestDir = 13
; Prior to Windows 10 1803, the above should be:
; DefaultDestDir = %DIRID_WINDOWS%,Firmware\{6bd4efb9-23cc-4b4a-ac37-016517413e9a}

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

```inf
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
HKR,,FirmwareFilename,,%13%\firmware.bin --> firmware.bin should be replaced with the firmware image name
; Prior to Windows 10 1803, the above should instead be:
HKR,,FirmwareFilename,,{6bd4efb9-23cc-4b4a-ac37-016517413e9a}\firmware.bin --> The subdirectory named after the GUID of the firmware resource and the firmware image name

[DestinationDirs]
DefaultDestDir = 13 --> The full destination path as a 'run from Driver Store' binary
; Prior to Windows 10 1803, the above should be:
; DefaultDestDir = %DIRID_WINDOWS%,Firmware\{6bd4efb9-23cc-4b4a-ac37-016517413e9a} --> The full destination path for the firmware image file based under a subdirectory named after the GUID of the firmware resource within the %SystemRoot%\Firmware directory

[Strings]
; localizable
Modify any strings here [optional]
```

The following table describes the various driver package INF sections and fields with reference to the above sample driver package INF file definition.

| Section/Field | Value | Comment |
|--|--|--|
| **[Version]** |  | Defines driver package versioning information. |
| Provider | %Provider% = Contoso Inc.<br><br>(localized in [Strings] section) | Identifies the provider/vendor of the entire firmware resource update driver package. |
| Class/ClassGuid | Firmware/<br><br>{f2e7dd72-6468-4e36-b6f1-6488f42c1b52} | Specifies the date of the driver package. The date and version should both reflect the date and version of the actual firmware resource update as closely as possible in order to ensure that the PnP device installation system can accurately select the best driver package available on the system. |
| CatalogFile | catalog.cat | Specifies the associated catalog file that signs the driver package INF file and all associated firmware resource update binaries. |
| PnpLockdown | 1 | Enables the PnP driver file lockdown mechanism in order to protect installed driver files from being modified externally by unrelated applications. For firmware resource updates, this setting should always be enabled to ensure that firmware resource image files cannot be tampered with outside of the control of the PnP system |
| **[Manufacturer]** |  | Lists all distinct driver manufacturers/vendors that define firmware resource updates. Each manufacturer line specifies an [\<Models\>] section and identifies its supported target platform. |
| %MfgName% | Fabrikam Inc.<br><br>(localized in [Strings] section) | Identifies the manufacturer/vendor of the firmware resource update. This may be the same as the Provider field. |
|  | Firmware,<br><br>NTarm | Identifies the [\<Models\>] section that defines the firmware resource devices supported by this driver package, including their target driver platforms. In this example, the drivers are only targeted for the Arm-based NT platform and the [\<Models\>] section is [Firmware.NTarm]. |
| **[Firmware.NTarm]** |  | [\<Models\>] section for the Arm-based NT platform that lists all firmware resource devices for which updates are defined. Each hardware model line specifies a [\<DDInstall\>] section and its associated hardware ID match. |
| %FirmwareDesc% | Fabrikam System Firmware 2.0<br><br>(localized in [Strings] section) | Describes the firmware resource update. This is the primary description string used to present the associated firmware resource device instance in Device Manager and other device related UI. For this reason, the description may include the firmware vendor and version. |
|  | Firmware_Install,<br><br>UEFI\RES_{RESOURCE_GUID} | Identifies the [\<DDInstall\] section containing the installation steps for the firmware resource update that targets the device instance identified by the UEFI\RES_{RESOURCE_GUID} hardware ID. Where RESOURCE_GUID is the GUID of the firmware resource that is being updated. |
| **[Firmware_Install.NT]**<br><br>CopyFiles = Firmware_CopyFiles<br><br>**[Firmware_CopyFiles]**<br><br>... |  | [\<DDInstall\>] section that contains the installation steps for the firmware resource update. For firmware resource updates, this only defines the firmware resource image file to copy into place for a firmware resource update. In this example, the [\<DDInstall\>] section is [Firmware_Install.NT]. |
| *firmware.bin* |  | Specifies the firmware resource update image file to copy. See section [DestinationDirs] below for details about where this file is copied. |
| **[Firmware_Install.NT.Hw]**<br><br>AddReg = Firmware_AddReg<br><br>**[Firmware_AddReg]**<br><br>... |  | [\<DDInstall\>.Hw] section that contains the hardware-specific installation steps for the firmware resource update. For firmware resource updates, this defines the firmware resource update configuration information in the form of registry values that are set under the device hardware key of the target device instance. |
| FirmwareId | {RESOURCE_GUID} | The firmware GUID of the firmware resource update. Note that this is the same firmware resource GUID that is embedded in the UEFI\RES_{RESOURCE_GUID} hardware ID, however it must be specified here as a standalone value since the PnP system treats all hardware IDs as opaque strings that are strictly used for device/driver matching purposes. |
| FirmwareVersion | 0x00000002 | The firmware version of the firmware resource update, specified as a REG_DWORD value. |
| FirmwareFilename | %13%\\*firmware.bin* | or Windows 10 1803 and later, this should be a 'run from Driver Store' file and supply the full path to the binary such as in the example.  For prior to Windows 10 1803, this should be the relative path and firmware filename of the firmware resource update's Update Capsule image filename under the %SystemRoot%\Firmware directory such that {RESOURCE_GUID} represents a subdirectory used to organize all firmware image files targeted for specific firmware resource. For example, {RESOURCE_GUID}\\*firmware.bin*. |
| **[SourceDisksNames]** |  | Lists all distinct driver package source disk locations where associated driver files, such as firmware update resource image files, are contained. |
| 1 | %DiskName% = Firmware Update<br><br>(localized in [Strings] section) | Specifies an arbitrarily numbered driver package source disk ID and its description name. No optional driver package relative subdirectory is specified so any driver files associated to this disk ID, like the firmware resource update image file, are expected to live directly beside the INF file. |
| **[SourceDisksFiles]** |  | Lists all driver files referenced by the driver package and links them to a disk ID from the [SourceDisksNames] section. |
| *firmware.bin* | 1 | Establishes the *firmware.bin* firmware resource update image file as being part of the driver package by linking it with the primary disk ID. No optional file-specific subdirectory is specified so this driver file is expected to live relative to its disk ID's subdirectory, which in this case is right beside the INF file. |
| **[DestinationDirs]** |  | Lists the target destination directories of all driver files referenced by the driver package. |
| DefaultDestDir | 13 | Specifies the default destination directory of all driver files copied by this driver package.  On Windows 10 1803 and later, this should be DIRID 13 to make the files 'run from Driver Store'.  Prior to Windows 10 1803, this should be %DIRID_WINDOWS%,Firmware\\{RESOURCE_GUID} to specify that the destination of all files is under %SystemRoot%\Firmware, where DIRID_WINDOWS (10) represents the base %SystemRoot% directory and {RESOURCE_GUID} represents a subdirectory named after the firmware resource GUID. |
| **[Strings]** |  | Defines key/value mappings for all indirect string tokens (%token%) in the driver package INF file. Use of string tokens enables a driver package INF file to be easily localized by introducing locale-specific [Strings.\<LanguageID\>] sections. It can also be useful to use string token substitution for defining constant numeric values, such as REG_DWORD. |
| Provider | "Contoso Ltd." | An example of a string token key/value mapping. |

It is important to use a unique name for each firmware resource update image file version in order to avoid any potential collisions with other firmware image files, both your own and those from other firmware vendors. For example, *firmware.bin* from the above should be assigned the following name to satisfy both vendor name and version constraints: *Fabrikam-System-Firmware-2.0.bin*.

In order to ensure that variants of a given firmware resource update image, potentially used for OEM/IHV customization purposes, do not collide when deployed into the same Windows system image, it is recommended that each distinct firmware resource update image is either a ['run from Driver Store'](../develop/run-from-driver-store.md) file (Windows 10 1803 and later) or maintained under a subdirectory within the %SystemRoot%\\Firmware directory. This subdirectory should be named after the target firmware resource GUID. For example, the following firmware resource update image paths satisfy the deployment constraints: %SystemRoot%\\Firmware\\{6bd4efb9-23cc-4b4a-ac37-016517413e9a}\\Fabrikam-System-Firmware-2.0.bin.

## Test signing the firmware driver package

Once the driver package INF file and firmware payload binary are ready, the entire driver package must be signed in order to produce a catalog file. It is crucial that this catalog file vouch for the validity and authenticity of the INF file and firmware payload binary contained within the driver package in order to enable Windows to securely initiate a firmware resource update.

The steps to self-sign the driver package for test purposes are enumerated below. Please note that these steps are for test purposes only. In production, firmware update driver packages must be submitted to the Partner Center for signing. For the steps to sign a firmware driver package for production see [Certifying and signing the update package](certifying-and-signing-the-update-package.md).

1. Install the latest Windows SDK and Windows Driver Kit. This will install the makecert, pvk2pfx inf2cat and signtool tools under %systemdir%\\Program Files (x86)\\Windows Kits\\<*version*>\\bin\\x86.

1. Run the following command to create a test certificate.

    ```console
    makecert.exe -r -pe -a sha256 -eku 1.3.6.1.5.5.7.3.3 -n CN=Foo -sv fwu.pvk fwu.cer
    pvk2pfx.exe -pvk fwu.pvk -spc fwu.cer -pi <Password entered during makecert prompt> -spc fwu.cer -pfx fwu.pfx
    ```

    For more information, see [**MakeCert**](../devtest/makecert.md).

1. Run the following command to create a catalog file.

    ```console
    Inf2Cat.exe /driver:"." /os:8_x64
    ```

    The */driver* argument points to the location where the INF is located. Change the value of the */os* argument depending on the OS for which the firmware driver package is intended for. For more information, see [**Inf2Cat**](../devtest/inf2cat.md).

    For more information about security catalogs and drivers, see [Catalog Files and Digital Signatures](../install/catalog-files.md) and [Creating a Catalog File for a PnP Driver Package](../install/creating-a-catalog-file-for-a-pnp-driver-package.md).

1. Run the following command to sign the catalog file.

    ```console
    signtool sign /fd sha256 /f fwu.pfx /p <Password entered during makecert prompt> delta.cat
    ```

    For more information, see [**SignTool**](../devtest/signtool.md).

1. Install the test certificate on the test system:

    1. Double click on the fwu.cer file and choose the **Install Certificate** option.

    1. Choose the following options during the certificate installation:

        - For Store location, choose **Local Machine**.

        - For Certificate Store, browse and select **Trusted Root Certification Authorities**.

1. Disable secure boot in the firmware/BIOS options.

1. Enable test signing in the BCD options so that the OS loader can load the firmware image file (firmware.bin) during boot even if the catalog is not production signed. Run the following command with administrator privileges:

    ```console
    bcdedit /set testsigning on
    ```

After the driver package is signed, it can be installed using one of the following mechanisms:

- **Device Manager**. For manual testing, Device Manager provides a friendly interface for locating a firmware resource device and updating its driver in order to initiate a firmware resource update.

    1. Locate the desired firmware resource device under the "Firmware" class while viewing devices by type, or under the "Microsoft UEFI-Compliant System" device while viewing devices by connection.

    1. Right-click on the firmware resource device and select the "Update Driver Software..." option.

    1. Use the "Browse my computer for driver software" option to locate and install a newer firmware resource update driver package onto the firmware resource device. This operation will ensure that the specified firmware resource update driver package is in fact newer than any existing firmware resource update driver package that might already be on the firmware resource device before adding it to the Windows Driver Store and initiating an installation.

- **pnputil**. For automated testing, the [PnpUtil](../devtest/pnputil.md) command line utility can be used from an Administrator-elevated command prompt to import a firmware resource update driver package into the Windows Driver Store and initiate a device installation on any/all applicable firmware resource devices that are presently using an older firmware resource version, as established by the DriverVer of their currently installed driver package INF file or a lack of a 3rd party supplied driver package INF file altogether. For example, use the following command line to add and install X:\\firmware.inf:

    ```console
    pnputil -i -a X:\firmware.inf
    ```

If the firmware resource update was successfully installed on a firmware resource device and it supplies a firmware resource update that is a higher version than the current firmware version, then the device will be awaiting a system reboot in order to complete the update operation. A device in this state will indicate its need for the system to be rebooted by maintaining a device problem, which prevents the device from being started and restored to a steady state until the reboot is performed.

## Validating the status of the firmware update

When a firmware driver package is successfully installed, PnP will request a system reboot to apply the updates. Post reboot, the status of the update can be validated. The status of the update is maintained under the following registry key: HKEY_LOCAL_MACHINE\\SYSTEM\\CurrentControlSet\\Control\\FirmwareResources\\{RESOURCE_GUID}.

RESOURCE_GUID is the GUID of the resource (from ESRT) that was updated.

The "LastAttemptStatus" registry value indicates the status of the firmware update, where a value of 0 indicates success and any non-zero value represents a failure. The value for this registry key are NTSTATUS codes populated by OS Loader based upon the value of the LastAttemptStatus from the ESRT. The following table maps the LastAttemptStatus code to its corresponding NTSTATUS code.

| LastAttemptStatus | Code | NTSTATUS | Code |
|--|--|--|--|
| Success | 0 | STATUS_SUCCESS | 0x00000000 |
| Error: Unsuccessful | 1 | STATUS_UNSUCCESSFUL | 0xC0000001 |
| Error: Insufficient Resources | 2 | STATUS_INSUFFICIENT_RESOURCES | 0xC000009A |
| Error: Incorrect Version | 3 | STATUS_REVISION_MISMATCH | 0xC0000059 |
| Error: Invalid Image Format | 4 | STATUS_INVALID_IMAGE_FORMAT | 0xC000007B |
| Error: Authentication Error | 5 | STATUS_ACCESS_DENIED | 0xC0000022 |
| Error: Power Event, AC Not Connected | 6 | STATUS_POWER_STATE_INVALID | 0xC00002D3 |
| Error: Power Event, Insufficient Battery | 7 | STATUS_INSUFFICIENT_POWER | 0xC00002DE |

The Hardware ID property of the firmware resource device node should also reflect the change in the firmware version, where XXX is the new firmware version.

- UEFI\\RES_{RESOURCE_GUID}&REV_XXX

If the firmware update failed, you can retry the failed firmware update:

- In Device Manager, expand the Firmware node, right-click the firmware resource device, and click **Update Driver Software**.

- Click **Browse my computer for driver software**, and on the next page click **Let me pick from a list of device drivers on my computer**.

- Select the same driver that you installed previously, and click OK.

After the next reboot, the OS Loader will call into UpdateCapsule() with the payload of the firmware driver package.

## Related topics

[ESRT table definition](esrt-table-definition.md)  

[Plug and play device](plug-and-play-device.md)  

[Processing updates](processing-updates.md)  

[Device I/O from the UEFI environment](device-i-o-from-the-uefi-environment.md)  

[Seamless crisis prevention and recovery](seamless-crisis-prevention-and-recovery.md)  

[Firmware update status](firmware-update-status.md)
