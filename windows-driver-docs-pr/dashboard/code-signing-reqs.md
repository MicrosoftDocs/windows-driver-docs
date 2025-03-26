---
title: Driver code signing requirements
description: Driver code signing requirements
ms.date: 07/15/2024
---

# Driver code signing requirements

Your drivers must be signed with a certificate before you submit them to the hardware dashboard. Your organization can associate any number of certificates with its dashboard account, and each one of your submissions must be signed with any one of those certificates. There's no restriction on the number of certificates (both extended validation (EV) and Standard) associated with your organization.

This article provides general information on the types of code signing available for your drivers, and the associated requirements for those drivers.

For more extensive information on driver signing requirements see the following pages:

- [Driver Signing Changes in Windows 10](https://techcommunity.microsoft.com/t5/Windows-Hardware-Certification/Driver-Signing-changes-in-Windows-10/ba-p/364859)
- [Driver Signing changes in Windows 10, version 1607](https://techcommunity.microsoft.com/t5/Windows-Hardware-Certification/Driver-Signing-changes-in-Windows-10-version-1607/ba-p/364894)
- [Update on Sysdev EV Certificate requirement](https://techcommunity.microsoft.com/t5/Windows-Hardware-Certification/Update-on-Sysdev-EV-Certificate-requirement/ba-p/364879)

## Where to get code signing certificates

Code signing certificates can be purchased from one of the following certificate authorities:

- [DigiCert code signing certificate](https://order.digicert.com/step1/code_signing)
- [Sectigo code signing certificate](https://www.sectigo.com/ssl-certificates-tls/code-signing)
- [GlobalSign code signing certificate](https://go.microsoft.com/fwlink/p/?LinkId=620888)
- [SSL.com code signing certificate](https://www.ssl.com/certificates/ev-code-signing/)

## EV certificate signed drivers

Your Hardware Dev Center dashboard account must have at least one EV certificate associated with it to submit binaries for attestation signing or to submit binaries for HLK certification.

The following rules apply:

- Your registered EV certificate must be valid at the time of submission.
- While Microsoft strongly recommends that you sign individual submissions with an EV certificate, you can alternatively sign submissions with an Authenticode signing certificate that is also registered to your Partner Center account.
- All certificates must be SHA2 and signed with the `/fd sha256` SignTool command line switch.

If you already have an approved EV certificate from a certificate authority, you can use it to establish a Partner Center account. If you don't have an EV certificate, choose [one the certificate authorities](#where-to-get-code-signing-certificates) and follow their directions for purchase.

Once the certificate authority verifies your contact information and your certificate purchase is approved, follow their directions to retrieve the certificate.

## HLK tested and dashboard signed drivers

 A dashboard signed driver that has passed the HLK tests works on Windows Vista and later, including Windows Server editions. HLK testing is the recommended method for driver signing, because it signs a driver for all OS versions. HLK tested drivers demonstrate that a manufacturer rigorously tests their hardware to meet all of Microsoft's requirements regarding reliability, security, power efficiency, serviceability, and performance, to provide a great Windows experience. Testing includes compliance with industry standards and adherence with Microsoft specifications for technology-specific features, helping to ensure correct installation, deployment, connectivity, and interoperability. To learn how to create an HLK tested driver for your dashboard submission see [Windows HLK Getting Started](/windows-hardware/test/hlk/getstarted/windows-hlk-getting-started).

## Windows 10 attestation signed drivers for testing scenarios

Windows device installation uses digital signatures to verify the integrity of driver packages and the identity of the software publisher who provides the driver packages.

For testing purposes only, you can submit your drivers for attestation signing, which doesn't require HLK testing.

Attestation signing has the following restrictions and requirements:

- Attestation signed drivers can't be published to Windows Update for retail audiences. To publish a driver to Windows Update for retail audiences, you must submit your driver through the [Windows Hardware Compatibility Program (WHCP)](/windows-hardware/design/compatibility/). Publishing attestation signed drivers to Windows Update for testing purposes is supported by selecting *CoDev* or *Test Registry Key / Surface SSRK* options.

- Attestation signing only works on Windows 10 Desktop and later versions of Windows.

- Attestation signing supports Windows 10 Desktop kernel mode and user mode drivers. Although user mode drivers don't need to be signed by Microsoft for Windows 10, the same attestation process can be used for both user and kernel mode drivers. For drivers that need to run on previous versions of Windows, you should [submit HLK/HCK test logs for Windows certification](./hardware-submission-create.md).

- Attestation signing doesn't return the proper PE Level for **ELAM** or **Windows Hello** PE binaries. These binaries must be tested and submitted as .hlkx packages to receive the extra signature attributes.

- Attestation signing requires the use of an [extended validation (EV) Certificate](code-signing-reqs.md#ev-certificate-signed-drivers) to submit the driver to the Partner Center (Hardware Dev Center Dashboard).

- Attestation signing requires driver folder names to contain no special characters, no UNC file share paths, and to be fewer than 40 characters long.

- When a driver receives attestation signing, it's not Windows Certified. An attestation signature from Microsoft indicates that the driver is trusted by Windows. But because the driver hasn't been tested in HLK Studio, there are no assurances made around compatibility, functionality, and so on. A driver that receives attestation signing can't be published to retail audiences through Windows Update. If you wish to publish your driver to retail audiences, you must submit your driver through the [Windows Hardware Compatibility Program (WHCP)](/windows-hardware/design/compatibility/).

- DUA (Driver Update Acceptable) doesn't support drivers signed using attestation.

- The following PE levels and binaries can be processed through Attestation:

  - **PeTrust**
  - **DrmLevel**
  - **HAL**
  - .exe
  - .cab
  - .dll
  - .ocx
  - .msi
  - .xpi
  - .xap

For information on how to create an attestation signed driver for Windows 10+ drivers, see [Attestation sign Windows 10+ drivers](code-signing-attestation.md).

## Windows Server signed drivers

- Windows Server 2016 and greater doesn't accept attested device and filter driver signing submissions.
- The dashboard only signs device and filter drivers that successfully pass the HLK tests.
- Windows Server 2016 and greater only loads dashboard signed drivers that successfully pass the HLK tests.

## Windows Defender Application Control

Enterprises can implement a policy to modify the driver signing requirements using Windows 10 Enterprise edition. Windows Defender Application Control (WDAC) provides an enterprise-defined code integrity policy, which can be configured to require at least an attestation-signed driver. For more information about WDAC, see [Planning and getting started on the Windows Defender Application Control deployment process](/windows/security/threat-protection/windows-defender-application-control/windows-defender-application-control-deployment-guide).

## Windows driver signing requirements

The following table summarizes the driver signing requirements for Windows:

| Version | *Attestation Dashboard Signed* | *HLK Test Passed Dashboard Signed* | *Cross-signed using a SHA-1 certificate issued prior to July 29, 2015* |
|--|--|--|--|
| Windows Vista | No | Yes | Yes |
| Windows 7 | No | Yes | Yes |
| Windows 8 / 8.1 | No | Yes | Yes |
| Windows 10 | Yes | Yes | No (as of Windows 10 1809) |
| Windows 10 - DG Enabled | \*Configuration Dependent | \*Configuration Dependent | \*Configuration Dependent |
| Windows Server 2008 R2 | No | Yes | Yes |
| Windows Server 2012 R2 | No | Yes | Yes |
| Windows Server >= 2016 | No | Yes | Yes |
| Windows Server >= 2016 – DG Enabled | \*Configuration Dependent | \*Configuration Dependent | \*Configuration Dependent |
| Windows IoT Enterprise | Yes | Yes | Yes |
| Windows IoT Enterprise- DG Enabled | \*Configuration Dependent | \*Configuration Dependent | \*Configuration Dependent |
| Windows IoT Core(1) | Yes (Not Required) | Yes (Not Required) | Yes (Cross signing will also work for certificates issued after July 29, 2015) |

\*Configuration dependent – With Windows 10 Enterprise edition, organizations can use Windows Defender Application Control (WDAC) to define custom signing requirements. For more information about WDAC, see [Planning and getting started on the Windows Defender Application Control deployment process](/windows/security/threat-protection/windows-defender-application-control/windows-defender-application-control-deployment-guide).

(1) Driver signing is required for manufacturers building retail products (that is, for a nondevelopment purpose) with IoT Core. For a list of approved Certificate Authorities (CAs), see [Cross-Certificates for Kernel Mode Code Signing](../install/cross-certificates-for-kernel-mode-code-signing.md). If UEFI Secure Boot is enabled, then drivers must be signed.
