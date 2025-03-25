---
title: How to Test Preproduction Drivers with Secure Boot Enabled
description: How to test preproduction drivers with Secure Boot enabled
ms.date: 07/10/2024
keywords:
- Secure Boot enabled
- Testing drivers
- Testing pre-production drivers
- Pre-production driver signing and testing
author: mhopkins-msft
ms.author: mhopkins
ms.topic: how-to
---

# How to test preproduction drivers with Secure Boot enabled

On retail and production systems, the Windows kernel only trusts and loads drivers with a production WHQL/WHCP signature. To test preproduction drivers, it's required that driver developers enable [`TESTSIGNING`](./the-testsigning-boot-configuration-option.md) to enable nonproduction drivers to load. `TESTSIGNING` requires disabling Secure Boot, to present a difference in the testing and production environments.

The Windows kernel supports loading preproduction drivers signed with the WHQL/WHCP preproduction signature. The WHQL/WHCP signature is accessible through the Microsoft Hardware Developer Center (HDC).

## Prerequisites

- [Sign your preproduction drivers with Partner Center Hardware dashboard](../dashboard/hardware-submission-create.md)

- Download *EnableUefiSbTest.exe* from the latest version of the Windows Driver Kit (WDK) or from [Download Center](https://aka.ms/PreprodDriverSignatureTool). The default setup location of the *EnableUefiSbTest* tool is **C:\Program Files (x86)\Windows Kits\10\tools\\{arch}\SecureBoot\EnableSB**. `{arch}` can be one of `{amd64, x86, arm, arm64}`. The policies are located under the same SecureBoot directory:**C:\Program Files (x86)\Windows Kits\10\tools\\{arch}\SecureBoot\Policies**.

## Enable support for the preproduction WHQL/WHCP Signature

Once your driver is preproduction signed, you're ready to provision a test computer where you install the driver.

The provisioning tools and payload are provided starting in Windows 11, version 22H2.

Use of the EnableUefiSbTest tool is recommended. Alternatively, you can manually provision the Microsoft Test Root key from the HLK Secure Boot Manual Tests section (`UefiSecureBootManualTests.zip\ManualTests\certs\test\db_MSFTtestSigningRoot.cer`). The Microsoft test key must be included in the Secure Boot database (DB) and the Secure Boot Configuration Policy (SBCP) to enable trust for the preproduction WHQL/WHCP driver signature.

> [!NOTE]
> When provisioning any of the Secure Boot databases, never production sign a payload with the Microsoft test keys inside.

### Provisioning Steps

1. In the system's UEFI menu, disable Secure Boot and clear the Secure Boot keys, if applicable. This allows the provisioning tool to set the test keys to trust the Secure Boot policy file and re-enable Secure Boot.

1. Download the correct Secure Boot policy .p7b file, depending on the system architecture, and the accompanying provisioning tool, *EnableUefiSbTest.exe*, from the WDK. For the location of the provisioning tool, see [Prerequisites](#prerequisites).

1. Run the following command in an elevated instance of PowerShell or Terminal and validate that the PK, KEK, db, dbx, and OemId values are empty ("Not Found"):

    ```PowerShell
    EnableUefiSbTest.exe /dump
    ```

    If Secure Boot is disabled and the keys are successfully cleared, the following output is expected:

    ```PowerShell
    EnableUefiSbTest.exe /dump
    
    Name: PK
    Not Found
    
    Name: KEK
    Not Found
    
    Name: db
    Not Found
    
    Name:dbx
    Not Found
    
    Name: OemId
    Not Found
    ```

1. Provision the Secure Boot test keys into the Secure Boot db and re-enable Secure Boot by running the following command in an elevated instance of PowerShell or Terminal:

    ```PowerShell
    EnableUefiSbTest.exe
    ```

    >[!NOTE]
    > EnableUefiSbTest.exe will not output/return anything after successfully running.

    Optionally, specify the `thirdparty` command to provision the Microsoft UEFI CA certificate alongside the default keys in the Secure Boot DB. This allows trust for Microsoft UEFI CA-signed EFI executables like option ROMs and non-Windows bootloaders.

    ```PowerShell
    EnableUefiSbTest.exe /thirdparty
    ```

1. For devices running Desktop-based Windows, mount the EFI partition of the system and copy over the Secure Boot policy (.p7b) file to **S:/EFI/Microsoft/Boot** by running the following command in an elevated instance of PowerShell or Terminal:

    ```PowerShell
    mountvol s: /s
    copy-item <path_to_p7b> S:/EFI/Microsoft/Boot/SecureBootPolicy.p7b
    ```

    >[!NOTE]
    > Because Windows kernel requires the Secure Boot policy file in the form of `SecureBootPolicy.p7b`, the name and file format must not be modified.

1. For devices not running Desktop-based Windows, copy the corresponding `PreProductionPolicy.pol` to `\EFI\Microsoft\Boot\Policies`. Then delete `FullDebugPolicy.pol` from `\EFI\Microsoft\Boot\Policies`.

1. Reboot the system to allow Windows kernel to refresh the policies. Secure Boot is now re-enabled and provisioned automatically by the provisioning tool. This can be validated by rerunning `EnableUefiSbTest.exe /dump` as admin and validating that only the `dbx` and `OemId` values are empty ("Not Found").

1. The system is ready to validate preproduction WHQL/WHCP signed driver content. Rebooting the system won't affect the state of the device, as long as the Secure Boot keys and Secure Boot policy files aren't modified.

### Deprovisioning Steps

To deprovision the system and opt-out of preproduction signing trust on the system:

1. Delete the Secure Boot policy files from the mounted EFI partition by running the following commands in an elevated instance of PowerShell or Terminal:

    ```PowerShell
    mountvol s: /s
    rm  S:/EFI/Microsoft/Boot/SecureBootPolicy.p7b
    ```

    >[!NOTE]
    > If the validations are being performed on a HoloLens 2, the .pol policy files must also be removed from **S:/EFI/Microsoft/Boot/Policies.**

1. Boot into the system's UEFI menu and reconfigure Secure Boot keys to factory settings.

1. Reboot the system and run `EnableUefiSbTest.exe /dump`, which should return nonempty values for `PK`, `KEK`, `db`, and `dbx` values indicating the keys were returned to factory state.

    >[!NOTE]
    > We recommend clean installing Windows on the system to de-provision a system intended for retail environments.

### FAQs

**Q:** The `EnableUefiSbTest.exe /dump` command is only showing a result for `PK`. Is something wrong?

**A:** This happens if the tool is run as a standard user instead of as admin.

**Q:** The `EnableUefiSbTest.exe /dump` command returns an error that I don't recognize. What do I do?

**A:** An error may be thrown by the tool when Secure Boot hasn't been successfully disabled and/or the Secure Boot keys haven't been cleared. Verify that Secure Boot is disabled.
