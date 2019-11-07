---
title: Driver Signing Policy
description: Driver Signing Policy
ms.assetid: c3ba672c-5bf2-4885-a85e-fa6d8a47ca54
keywords:
- driver signing WDK , kernel-mode code signing policy
- signing drivers WDK , kernel-mode code signing policy
- digital signatures WDK , kernel-mode code signing policy
- signatures WDK , kernel-mode code signing policy
- kernel-mode code signing policy WDK
- kernel-mode driver signing WDK
- driver package digital signatures WDK
- package digital signatures WDK
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Driver Signing Policy

> [!NOTE]
> Starting with Windows 10, version 1607, Windows will not load any new kernel-mode drivers which are not signed by the Dev Portal.  To get your driver signed, first [Register for the Windows Hardware Dev Center program](https://docs.microsoft.com/windows-hardware/drivers/dashboard/register-for-the-hardware-program). Note that an [EV code signing certificate](https://docs.microsoft.com/windows-hardware/drivers/dashboard/get-a-code-signing-certificate) is required to establish a dashboard account.

There are many different ways to submit drivers to the portal.  For production drivers, you should submit HLK/HCK test logs, as described below.  For testing on Windows 10 client only systems, you can submit your drivers for [attestation signing](../dashboard/attestation-signing-a-kernel-driver-for-public-release.md), which does not require HLK testing.  Or, you can submit your driver for Test signing as described on the [Create a new hardware submission](../dashboard/create-a-new-hardware-submission.md) page.

## Exceptions

Cross-signed drivers are still permitted if any of the following are true:

* The PC was upgraded from an earlier release of Windows to Windows 10, version 1607.
* Secure Boot is off in the BIOS.
* Drivers was signed with an end-entity certificate issued prior to July 29th 2015 that chains to a supported cross-signed CA.

To prevent systems from failing to boot properly, boot drivers will not be blocked, but they will be removed by the Program Compatibility Assistant.

## Signing a driver for client versions of Windows

To sign a driver for Windows 10, follow these steps:

1. For each version of Windows 10 that you want to certify on, download the Windows HLK (Hardware Lab Kit) for that version and run a full cert pass against the client for that version. You'll get one log per version.
2. If you have multiple logs, merge them into a single log using the most recent HLK.
3. Submit your driver and the merged HLK test results to the [Windows Hardware Developer Center Dashboard portal](../dashboard/index.md).

For version-specific details, please review the [WHCP (Windows Hardware Compatibility Program) policy](https://docs.microsoft.com/windows-hardware/design/compatibility/whcp-specifications-policies) for the Windows versions you want to target.

To sign a driver for Windows 7, Windows 8, or Windows 8.1, use the appropriate HCK (Hardware Certification Kit).  For more information, see the [Windows Hardware Certification Kit User's Guide](https://docs.microsoft.com/previous-versions/windows/hardware/hck/jj124227(v=vs.85)).

## Signing a driver for earlier versions of Windows

Before Windows 10, version 1607, the following types of drivers require an Authenticode certificate used together with Microsoft's cross-certificate for cross-signing:

* Kernel-mode device drivers
* User-mode device drivers
* Drivers that stream protected content. This includes audio drivers that use Protected User Mode Audio (PUMA) and Protected Audio Path (PAP), and video device drivers that handle protected video path-output protection management (PVP-OPM) commands. For more information, see [Code-signing for Protected Media Components](https://go.microsoft.com/fwlink/p/?linkid=74262).

## Signing requirements by version

The following table shows signing policies for client operating system versions.

Note that Secure Boot does not apply to Windows Vista and Windows 7.

|Applies to:|Windows Vista, Windows 7; Windows 8+ with Secure Boot off|Windows 8, Windows 8.1, Windows 10, versions 1507, 1511 with Secure Boot on|Windows 10, versions 1607, 1703, 1709 with Secure Boot on|Windows 10, version 1803+ with Secure Boot on|
|--- |--- |--- |--- |--- |
|**Architectures:**|64-bit only, no signature required for 32-bit|64-bit, 32-bit|64-bit, 32-bit|64-bit, 32-bit|
|**Signature required:**|Embedded or catalog file|Embedded or catalog file|Embedded or catalog file|Embedded or catalog file|
|**Signature algorithm:**|SHA2|SHA2|SHA2|SHA2|
|**Certificate:**|Standard roots trusted by Code Integrity|Standard roots trusted by Code Integrity|Microsoft Root Authority 2010, Microsoft Root Certificate Authority, Microsoft Root Authority|Microsoft Root Authority 2010, Microsoft Root Certificate Authority, Microsoft Root Authority|

In addition to driver code signing, you also need to meet the PnP device installation signing requirements for installing a driver.  For more info, see [Plug and Play (PnP) device installation signing requirements](pnp-device-installation-signing-requirements--windows-vista-and-later-.md).

For info about signing an ELAM driver, see [Early launch antimalware](https://docs.microsoft.com/windows/desktop/w8cookbook/secured-boot).

## See Also

* [Installing an Unsigned Driver Package during Development and Test](installing-an-unsigned-driver-during-development-and-test.md)
* [Signing Drivers for Public Release](signing-drivers-for-public-release--windows-vista-and-later-.md)
* [Signing Drivers during Development and Test](signing-drivers-during-development-and-test.md)
* [Digital Signatures](driver-signing.md)
* [Troubleshooting Install and Load Problems with Signed Driver Packages](troubleshooting-install-and-load-problems-with-signed-driver-packages.md)
