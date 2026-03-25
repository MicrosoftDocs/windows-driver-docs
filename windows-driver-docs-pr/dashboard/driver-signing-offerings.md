---
title: Driver signing offerings
description: Driver signing offerings in Hardware Dev Center
ms.date: 03/23/2026
ms.topic: best-practice
---

# Driver signing offerings

## Hardware Lab Kit (HLK) tested and dashboard signed drivers

 A dashboard signed driver that has passed the HLK tests works on Windows Vista and later, including Windows Server editions. HLK testing is the recommended method for driver signing, because it signs a driver for all OS versions. HLK tested drivers demonstrate that a manufacturer rigorously tests their hardware to meet all of Microsoft's requirements regarding reliability, security, power efficiency, serviceability, and performance, to provide a great Windows experience. Testing includes compliance with industry standards and adherence with Microsoft specifications for technology-specific features, helping to ensure correct installation, deployment, connectivity, and interoperability. To learn how to create an HLK tested driver for your dashboard submission see [Windows HLK Getting Started](/windows-hardware/test/hlk/getstarted/windows-hlk-getting-started).

## Attestation signed drivers for testing scenarios

Windows device installation uses digital signatures to verify the integrity of driver packages and the identity of the software publisher who provides the driver packages.

For testing purposes only, you can submit your drivers for attestation signing, which doesn't require HLK testing.

Attestation signing has the following restrictions and requirements:

- Attestation signed drivers can't be published to Windows Update for retail audiences. To publish a driver to Windows Update for retail audiences, you must submit your driver through the [Windows Hardware Compatibility Program (WHCP)](/windows-hardware/design/compatibility/). Publishing attestation signed drivers to Windows Update for testing purposes is supported by selecting *CoDev* or *Test Registry Key / Surface SSRK* options.

- Attestation signing only works on Windows 10 Desktop and later versions of Windows.

- Attestation signing supports Windows Desktop kernel mode and user mode drivers. For drivers that need to run on previous versions of Windows, you should [submit HLK/HCK test logs for Windows certification](./hardware-submission-create.md).

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

## Preproduction (Preprod) signed drivers
Preproduction signing is an additional signing option available to partners during early development and validation. Preprod signed drivers allow partners to test in development driver binaries on systems where Secure Boot remains enabled.

Preprod signed drivers are **not trusted by default** on retail systems. Instead, they load only on devices that have been explicitly provisioned to trust the preproduction signature. This enables higher fidelity testing, including Secure Boot compatibility, while ensuring that unfinished or unvalidated drivers cannot be deployed broadly. 

### Supported scenarios
Preproduction signing can be used when partners need to:
- Validate early driver builds that are not yet ready for WHCP/HLK submission.  
- Perform bring up and co development testing with Secure Boot enabled.  
- Test OS security feature interactions such as Hypervisor based Code Integrity (HVCI) and kernel/user mode code integrity in a controlled environment.  

### OS configuration compatibility
When a device is provisioned with the preproduction signing configuration:
- **Driver install and load** is supported with Secure Boot enabled.  
- **HVCI**, **Kernel Mode Code Integrity**, and **User Mode Code Integrity** remain supported, similar to retail and attestation trusted configurations.  
- Drivers will not load on retail systems unless those systems have been explicitly provisioned to trust the preproduction signature.  

### Supported driver signature attributes
- ELAM
- HalExt
- PETrust
- DRM
- WindowsHello

### Provisioning and submission
To use preproduction signing, partners must provision their test devices to trust the preproduction signature. For detailed provisioning instructions, including required Secure Boot policies and tools, see [How to test preproduction drivers with Secure Boot enabled](../install/preproduction-driver-signing-and-install.md)

Partners can create and manage preproduction submissions using the Microsoft Hardware Dev Center APIs. For submission steps and package management details, see [Manage Preproduction signing submissions](manage-preprod-submissions.md)

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
