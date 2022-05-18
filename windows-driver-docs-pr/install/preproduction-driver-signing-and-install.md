---
title: How to test drivers with Secure Boot enabled
description: How to test pre-production drivers with Secure Boot enabled
keywords:
- Secure Boot enabled
- Testing drivers
- Testing pre-production drivers
- Pre-production driver signing and testing
ms.date: 03/15/2022
---

# How to test pre-production drivers with Secure Boot enabled

On retail and production systems, the Windows kernel only trusts and loads drivers with a production WHQL/WHCP signature. To test pre-production drivers, it has been required that driver developers enable [TESTSIGNING](./the-testsigning-boot-configuration-option.md) to enable non-production drivers to load. TESTSIGNING required disabling Secure Boot, presenting a difference in the testing and production environments.

Now, the Windows kernel supports loading pre-production drivers signed with the WHQL/WHCP pre-production certificate. The WHQL/WHCP signature accessible through the Microsoft Hardware Developer Center (HDC).

## Prerequisites
- [Sign your pre-production drivers with Partner Center Hardware dashboard](../dashboard/create-a-new-hardware-submission.md)

The first step is to submit your driver to HDC to request pre-production signing.

## Enable support for the pre-production WHQL/WHCP Signature

Once you have a driver that has been pre-production signed, you're ready to provision your test computer so that the driver will run on it.

The provisioning tools and payload are provided in [Windows Insider Preview WDK](https://www.microsoft.com/software-download/windowsinsiderpreviewWDK) version 22557 and above.

Use of the EnableUefiSbTest tool is optional, and the Microsoft test keys can be manually provisioned. The Microsoft test key must be included in the Secure Boot database (DB) and the Secure Boot Configuration Policy (SBCP) to enable trust for the pre-production WHQL/WHCP driver signature.

> [!NOTE]
> When provisioning any of the Secure Boot databases, never production sign a payload with the Microsoft test keys inside.

### Provisioning Steps

1. In the system’s UEFI menu, disable Secure Boot and clear the Secure Boot keys, if applicable. This will allow the provisioning tool to set the test keys to trust the Secure Boot policy file and re-enable Secure Boot.

1. Download the correct Secure Boot policy .p7b file, depending on the system architecture, as well as the accompanying provisioning tool (EnableUefiSbTest.exe) from the WDK.  

1. Run the following command in an elevated instance of PowerShell or Terminal and validate that the PK, KEK, db, dbx and OemId values are empty (“Not Found”):

```PowerShell
EnableUefiSbTest.exe /dump
```

If Secure Boot is disabled and the keys have been successfully cleared, the following output is expected:

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

1. Provision the Secure Boot test keys into the Secure Boot db and re-enable Secure Boot by running the following command in an elevated instance of PowerShell or Terminal:

```PowerShell
EnableUefiSbTest.exe
```

**Note: EnableUefiSbTest.exe will not output/return anything after successfully running.**

1. For devices running Desktop-based Windows, mount the EFI partition of the system and copy over the Secure Boot policy (.p7b) file to S:/EFI/Microsoft/Boot by running the following command in an elevated instance of PowerShell or Terminal:

```PowerShell
mountvol s: /s
copy-item <path_to_p7b> S:/EFI/Microsoft/Boot/SecureBootPolicy.p7b
```

**Note: The Windows kernel requires the Secure Boot policy file in the form of `SecureBootPolicy.p7b` so the name and file format must not be modified.**

1. For devices not running Desktop-based Windows, copy the corresponding `PreProductionPolicy.pol` to `\EFI\Microsoft\Boot\Policies`. Then delete `FullDebugPolicy.pol` from `\EFI\Microsoft\Boot\Policies`.

1. Reboot the system to allow the Windows kernel to refresh the policies. Secure Boot is now re-enabled and provisioned automatically by the provisioning tool. This can be validated by re-running EnableUefiSbTest.exe /dump as admin and validating that only the dbx and OemId values are empty (“Not Found”).

1. The system is ready to validate preproduction WHQL/WHCP signed driver content. Rebooting the system will not impact the state of the device so long as the Secure Boot keys and Secure Boot policy file(s) are not modified.

### Deprovisioning Steps

To deprovision the system and opt-out of preproduction signing trust on the system, the following steps need to be taken.

1. Delete the Secure Boot policy files from the mounted EFI partition by running the following commands in an elevated instance of PowerShell or Terminal:

```PowerShell
mountvol s: /s
rm  S:/EFI/Microsoft/Boot/SecureBootPolicy.p7b
```

**Note: If the validations are being performed on a HoloLens 2, the .pol policy files must also be removed from S:/EFI/Microsoft/Boot/Policies.**

2. Boot into the system’s UEFI menu and reconfigure Secure Boot keys to factory settings.

3. Reboot the system. Running EnableUefiSbTest.exe /dump will now return non-empty values for PK, KEK, db and dbx values indicating the keys were returned to factory state.

**Note: We recommend clean installing Windows on the system to de-provision a system intended for retail environments.**

### FAQs

Q: The EnableUefiSbTest.exe /dump command is only showing a result for PK. Is something wrong?

A: This will happen if the tool is run as a standard user instead of as admin.

Q: The EnableUefiSbTest.exe /dump command returned an error that I do not recognize. What do I do?

A: An error may be thrown by the tool when Secure Boot has not been successfully disabled and/or the Secure
