---
title: Testing Drivers with Secure Boot
description: How to Test Pre-production Drivers with Secure Boot Enabled
keywords:
- Secure Boot enabled
- Testing drivers
- Testing pre-production drivers
- Pre-prodution driver signing and testing
ms.date: 02/22/2022
---

# How to Test Preproduction Drivers with Secure Boot Enabled

On retail and production systems, the Windows kernel will only trust and load drivers with a production WHQL/WHCP signature. To test preproduction drivers, driver developers were required to enable [TESTSIGNING](./the-testsigning-boot-configuration-option.md) to enable non-production drivers to load. TESTSIGNING requires disabling Secure Boot, presenting a difference in the testing and production environments.

The Windows kernel now supports loading preproduction drivers signed with the WHQL/WHCP 'preproduction' certificate accessible through the Microsoft Hardware Developer Center (HDC).

## Signing with the WHQL/WHCP Preproduction Certificate through HDC

## Enabling Support for the Preproduction WHQL/WHCP Signature

The provisioning tools and payload are provided in the retail version of the [Windows Driver Kit (WDK)](../download-the-wdk.md) version 25000.1 and newer or the [WDK Insider Preview](https://www.microsoft.com/software-download/windowsinsiderpreviewWDK) version 22557 and above.

Use of the EnableUefiSbTest tool is optional, and the Microsoft test keys can be manually provisioned. The Microsoft test key must be included in the DB and the SBCP to enable trust for the pre-production driver signer is Microsoft test signed.

> [!NOTE]
> When provisioning any of the Secure Boot databases, never production sign a payload with the Microsoft test keys inside.

### Provisioning Steps

1. In the system’s UEFI menu, disable Secure Boot and clear the Secure Boot keys, if applicable. This will allow the provisioning tool to set the test keys to trust the Secure Boot policy file and re-enable Secure Boot.

2. Download the correct Secure Boot policy .p7b file, depending on the system architecture, as well as the accompanying provisioning tool (EnableUefiSbTest.exe) from the WDK.  

3. Run the following command in an elevated instance of PowerShell or Terminal and validate that the PK, KEK, db, dbx and OemId values are empty (“Not Found”):

```PowerShell
EnableUefiSbTest.exe /dump
```

If Secure Boot is disabled and the keys have been successfully cleared, the following output is expected be by the tool:

```PowerShell
PS C:\> .\EnableUefiSbTest.exe /dump

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

4. Provision the Secure Boot test keys into the Secure Boot db and re-enable Secure Boot by running the following command in an elevated instance of PowerShell or Terminal:

```PowerShell
EnableUefiSbTest.exe
```

**Note: EnableUefiSbTest.exe will not output/return anything after successfully running.**

5. Mount the EFI partition of the system and copy over the Secure Boot policy (.p7b) file to S:/EFI/Microsoft/Boot by running the following command in an elevated instance of PowerShell or Terminal:

```PowerShell
mountvol s: /s
copy-item <path_to_p7b> S:/EFI/Microsoft/Boot/SecureBootPolicy.p7b
```

**Note: The Windows kernel requires the Secure Boot policy file in the form of “SecureBootPolicy.p7b” so the name and file format must not be modified.**

**Note: If the validations are being performed on a WCOS system (e.g. HoloLens OS, SurfaceHub OS, Windows 10x), the corresponding .pol policy files must also be copied over to S:/EFI/Microsoft/Boot/Policies. Additionally, /EFI/Microsoft/Boot/Policies/FullDebugPolicy.pol must be deleted before rebooting.**

6. Reboot the system to allow the Windows kernel to refresh the policies. Secure Boot is now re-enabled and provisioned automatically by the provisioning tool. This can be validated by re-running EnableUefiSbTest.exe /dump as admin and validating that only the dbx and OemId values are empty (“Not Found”).

7. The system is ready to validate preproduction WHQL/WHCP signed driver content. Rebooting the system will not impact the state of the device so long as the Secure Boot keys and Secure Boot policy file(s) are not modified.

### Deprovisioning Steps

To deprovision the system and opt-out of preproduction signing trust on the system, the following steps need to be taken.

1. Delete the Secure Boot policy files from the mounted EFI partition by running the following commands in an elevated instance of PowerShell or Terminal:

```PowerShell
mountvol s: /s
rm  S:/EFI/Microsoft/Boot/SecureBootPolicy.p7b
```

**Note: If the validations are being performed on a WCOS system (e.g. HoloLens OS, Surface Hub OS, Windows 10x), the .pol policy files must also be removed from S:/EFI/Microsoft/Boot/Policies.**

2. Boot into the system’s UEFI menu and reconfigure Secure Boot keys to factory settings.

3. Reboot the system. Running EnableUefiSbTest.exe /dump will now return non-empty values for PK, KEK, db and dbx values indicating the keys were returned to factory state.

**Note: We recommend clean installing Windows on the system to de-provision a system intended for retail environments.**

### FAQs

Q: The EnableUefiSbTest.exe /dump command is only showing a result for PK. Is something wrong?

A: This will happen if the tool is run as a standard user instead of as admin.

Q: The EnableUefiSbTest.exe /dump command returned an error that I do not recognize. What do I do?

A: An error may be thrown by the tool when Secure Boot has not been successfully disabled and/or the Secure
