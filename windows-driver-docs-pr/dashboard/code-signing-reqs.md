---
title: Driver code signing requirements
description: Driver code signing requirements
ms.topic: article
ms.date: 04/19/2022
---

# Driver code signing requirements
 
This article provides general information on the types of code signing available for your drivers, as well as the associated requirements for those drivers.

For more extensive information on driver signing requirements see the following pages:

- [Driver Signing Changes in Windows 10](https://techcommunity.microsoft.com/t5/Windows-Hardware-Certification/Driver-Signing-changes-in-Windows-10/ba-p/364859)
- [Driver Signing changes in Windows 10, version 1607](https://techcommunity.microsoft.com/t5/Windows-Hardware-Certification/Driver-Signing-changes-in-Windows-10-version-1607/ba-p/364894)
- [Update on Sysdev EV Certificate requirement](https://techcommunity.microsoft.com/t5/Windows-Hardware-Certification/Update-on-Sysdev-EV-Certificate-requirement/ba-p/364879)

## Where to get code signing certificates

Code signing certificates can be purchased from one of the following certificate authorities:

- [DigiCert code signing certificate](https://www.digicert.com/order/order-1.php)
- [Entrust code signing certificate](https://www.entrustdatacard.com/products/digital-signing-certificates/code-signing-certificates)
- [GlobalSign code signing certificate](https://go.microsoft.com/fwlink/p/?LinkId=620888)
- [SSL.com code signing certificate](https://www.ssl.com/certificates/ev-code-signing/)

## EV certificate signed drivers

Your Hardware Dev Center dashboard account must have at least one extended validation (EV) certificate associated with it to submit binaries for attestation signing or to submit binaries for HLK certification.

The following rules apply:

* Your registered EV certificate must be valid at the time of submission.
* While Microsoft strongly recommends that you sign individual submissions with an EV certificate, you can alternatively sign submissions with an Authenticode signing certificate that is also registered to your Partner Center account.
* All certificates must be SHA2 and signed with the `/fd sha256` SignTool command line switch.

If you already have an approved EV certificate from a certificate authorities, you can use it to establish a Partner Center account. If you don't have an EV certificate, chose [one the certificate authorities](#where-to-get-code-signing-certificates) and follow their directions for purchase.

Once the certificate authority has verified your contact information and your certificate purchase is approved, follow their directions to retrieve the certificate.

## HLK tested and dashboard signed drivers

 A dashboard signed driver that has passed the HLK tests will work on Windows Vista through Windows 10, including Windows Server editions. This is the recommended method for driver signing, because it allows a single process for all OS versions. In addition, HLK tested drivers demonstrate that a manufacturer has rigorously tested their hardware to meet all of Microsoft's requirements with regards to reliability, security, power efficiency, serviceability, and performance, so as to provide a great Windows experience. This includes compliance with industry standards and adherence with Microsoft specifications for technology-specific features, helping to ensure correct installation, deployment, connectivity and interoperability. For more information about the HLK, see [Windows Hardware Compatibility Program](/windows-hardware/design/compatibility/index).

## Windows 10 attestation signed drivers

Windows device installation uses digital signatures to verify the integrity of driver packages and to verify the identity of the software publisher who provided the driver packages. For Windows 10 Desktop and later systems, you can submit your drivers for attestation signing, which doesn't require HLK testing. However, attestation signing will only work on Windows 10 Desktop and later versions of Windows. An attestation signed driver won't work for other versions of Windows, such as Windows Server 2016, Windows 8, or Windows 7. Attestation signing supports Windows 10 Desktop kernel mode and user mode drivers. Although user mode drivers don't need to be signed by Microsoft for Windows 10, the same attestation process can be used for both user and kernel mode drivers. For drivers that need to run on previous versions of Windows, you should [submit HLK/HCK test logs for Windows certification](./hardware-certification-submissions.md).

Attestation signing has the following properties.

- Attestation signing supports Windows 10 kernel mode and user mode drivers. Although user mode drivers do not need to be signed by Microsoft for Windows 10, the same attestation process can be used for both user and kernel mode drivers.

- Attestation signing won't return the proper PE Level for **ELAM** or **Windows Hello** PE binaries.  These must be tested and submitted as .hlkx packages to receive the additional signature attributes.

- Attestation signing requires the use of an [extended validation (EV) Certificate](code-signing-reqs.md#ev-certificate-signed-drivers) to submit the driver to the Partner Center (Hardware Dev Center Dashboard).

- An attestation signed driver works on Windows 10. It doesn't work on earlier versions of Windows, such as Windows 8.1 and Windows 7, and isn't supported for Windows Server 2016 and later.

- Attestation signing requires driver folder names to contain no special characters, no UNC file share paths, and to be less than 40 characters long.

- When a driver receives attestation signing, it's not [Windows Certified](hardware-certification-submissions.md). An attestation signature from Microsoft indicates that the driver can be trusted by Windows, but because the driver has not been tested in HLK Studio, there are no assurances made around compatibility, functionality, and so on.

- DUA (Driver Update Acceptable) doesn't support drivers signed using attestation.

- To get your driver Windows Certified, you'll need to submit an .hlkx package generated by HLK Studio to the Partner Center.

- To get your driver attestation signed, you need to create and submit a CAB file.

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

## Windows Server signed drivers

- Windows Server 2016 and greater will not accept attested device and filter driver signing submissions.
- The dashboard will only sign device and filter drivers that have successfully passed the HLK tests.
- Windows Server 2016 and greater will only load dashboard signed drivers that have successfully passed the HLK tests.

## Windows Defender Application Control

Enterprises may implement a policy to modify the driver signing requirements using Windows 10 Enterprise edition. Windows Defender Application Control (WDAC) provides an enterprise-defined code integrity policy, which may be configured to require at least an attestation-signed driver. For more information about WDAC, see [Planning and getting started on the Windows Defender Application Control deployment process](/windows/security/threat-protection/windows-defender-application-control/windows-defender-application-control-deployment-guide).

## Windows driver signing requirements

The table below summarizes the driver signing requirements for Windows:

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

(1) Driver signing is required for manufacturers building retail products (i.e. for a non-development purpose) with IoT Core. For a list of approved Certificate Authorities (CAs), see [Cross-Certificates for Kernel Mode Code Signing](../install/cross-certificates-for-kernel-mode-code-signing.md). If UEFI Secure Boot is enabled, then drivers must be signed.
