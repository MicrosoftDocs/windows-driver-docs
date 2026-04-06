---
title: Driver Signing Options
description: This article covers various driver signing offerings available from the Hardware Dev Center blog. The article also recommends best practices.
ms.date: 03/23/2026
ms.topic: best-practice
---

# Driver signing options and best practices

This article covers various driver signing offerings available from the Hardware Dev Center blog. The article also recommends best practices.

## Hardware Lab Kit tested and dashboard signed drivers

 A dashboard signed driver that has passed the Hardware Lab Kit (HLK) tests works on Windows Vista and later, including Windows Server editions. HLK testing is the recommended method for driver signing, because it signs a driver for all OS versions.

HLK tested drivers demonstrate that a manufacturer rigorously tests their hardware to meet all Microsoft requirements regarding reliability, security, power efficiency, serviceability, and performance. Testing includes compliance with industry standards and adherence with Microsoft specifications for technology-specific features. Such testing helps to ensure correct installation, deployment, connectivity, and interoperability.

To learn how to create an HLK tested driver for your dashboard submission, see [Windows HLK Getting Started](/windows-hardware/test/hlk/getstarted/windows-hlk-getting-started).

## Attestation signed drivers for testing scenarios

Windows device installation uses digital signatures to verify the integrity of driver packages and the identity of the software publisher who provides the driver packages.

For testing purposes only, you can submit your drivers for attestation signing, which doesn't require HLK testing.

Attestation signing has the following restrictions and requirements:

- Attestation signed drivers can't be published to Windows Update for retail audiences. To publish a driver to Windows Update for retail audiences, you must submit your driver through the [Windows Hardware Compatibility Program](/windows-hardware/design/compatibility/). Publishing attestation signed drivers to Windows Update for testing purposes is supported by selecting **CoDev** or **Test Registry Key / Surface SSRK** options.

- Attestation signing only works on Windows 10 Desktop and later versions of Windows.

- Attestation signing supports Windows Desktop kernel mode and user mode drivers. For drivers that need to run on previous versions of Windows, you should [submit HLK/HCK test logs for Windows certification](./hardware-submission-create.md).

- Attestation signing doesn't return the proper Portable Executable (PE) level for Early Launch Antimalware (ELAM) or Windows Hello PE binaries. These binaries must be tested and submitted as .hlkx packages to receive the extra signature attributes.

- Attestation signing requires the use of an [extended validation certificate](code-signing-reqs.md#ev-certificate-signed-drivers) to submit the driver to the Partner Center (Hardware Dev Center Dashboard).

- Attestation signing requires that the driver folder names contain no special characters, and no UNC file share paths. Driver folder names must be fewer than 40 characters long.

- When a driver receives attestation signing, it's not Windows Certified. An attestation signature from Microsoft indicates that Windows trusts the driver. But because the driver isn't tested in HLK Studio, there are no assurances about compatibility or functionality.

- DUA (Driver Update Acceptable) doesn't support attestation signed drivers.

- The following PE levels and binaries can be processed through attestation:

  - PeTrust
  - DrmLevel
  - HAL
  - .exe
  - .cab
  - .dll
  - .ocx
  - .msi
  - .xpi
  - .xap

For more information, see [Attestation sign Windows drivers](code-signing-attestation.md).

## Preproduction signed drivers

Preproduction signing is available to partners during early development and validation. Preproduction signed drivers allow partners to test driver binaries on systems where Secure Boot remains enabled.

By default, these drivers aren't trusted on retail systems. Instead, they load only on devices that are explicitly provisioned to trust the preproduction signature. This specification enables higher fidelity testing, including Secure Boot compatibility, while ensuring that you can't broadly deploy unfinished or unvalidated drivers.

### Supported scenarios

You might want to use preproduction signing when partners need to:

- Validate early driver builds that aren't yet ready for WHCP/HLK submission.  

- Perform bring-up and co-development testing with Secure Boot enabled.  

- Test OS security feature interactions, such as Hypervisor-based Code Integrity (HVCI) and kernel/user mode code integrity, in a controlled environment.  

### OS configuration compatibility

When you provision a device with the preproduction signing configuration:

- Driver install and load are supported, with Secure Boot enabled.  

- HVCI, Kernel Mode Code Integrity, and User Mode Code Integrity remain supported, similar to retail and attestation trusted configurations.  

- Drivers don't load on retail systems unless those systems are explicitly provisioned to trust the preproduction signature.  

### Supported driver signature attributes

The following driver signature attributes are supported with preproduction signing: ELAM, HalExt, PETrust, DRM, and Windows Hello.

### Provisioning and submission

To use preproduction signing, partners must provision their test devices to trust the preproduction signature. For detailed provisioning instructions, including required Secure Boot policies and tools, see [How to test preproduction drivers with Secure Boot enabled](../install/preproduction-driver-signing-and-install.md).

Partners can create and manage preproduction submissions by using the Microsoft Hardware Dev Center APIs. For submission steps and package management details, see [Manage preproduction signing submissions](manage-preprod-submissions.md).

## Windows Server signed drivers

Understand the following limitations about Windows Server signed drivers:

- Windows Server 2016 and greater doesn't accept attested device and filter driver signing submissions.

- The dashboard only signs device and filter drivers that successfully pass the HLK tests.

- Windows Server 2016 and greater only loads dashboard signed drivers that successfully pass the HLK tests.

## Windows Defender Application Control

For Windows 10 Enterprise edition, enterprises can implement a policy to modify the driver signing requirements. Windows Defender Application Control (WDAC) provides an enterprise-defined code integrity policy, which can be configured to require at least an attestation signed driver. For more information about WDAC, see [Deploying App Control for Business policies](/windows/security/threat-protection/windows-defender-application-control/windows-defender-application-control-deployment-guide).

## Windows driver signing requirements

The following table summarizes the driver signing requirements for Windows.

| Version                             | Attestation dashboard signed | HLK test passed dashboard signed | Cross-signed using an SHA-1 certificate issued before July 29, 2015       |
|-------------------------------------|------------------------------|----------------------------------|----------------------------------------------------------------------------|
| Windows Vista                       | No                           | Yes                              | Yes                                                                        |
| Windows 7                           | No                           | Yes                              | Yes                                                                        |
| Windows 8 / 8.1                     | No                           | Yes                              | Yes                                                                        |
| Windows 10                          | Yes                          | Yes                              | No (as of Windows 10 1809)                                                 |
| Windows 10 - DG Enabled             | \*Configuration dependent    | \*Configuration dependent        | \*Configuration dependent                                                  |
| Windows Server 2008 R2              | No                           | Yes                              | Yes                                                                        |
| Windows Server 2012 R2              | No                           | Yes                              | Yes                                                                        |
| Windows Server >= 2016              | No                           | Yes                              | Yes                                                                        |
| Windows Server >= 2016 – DG Enabled | \*Configuration dependent    | \*Configuration dependent        | \*Configuration dependent                                                  |
| Windows IoT Enterprise              | Yes                          | Yes                              | Yes                                                                        |
| Windows IoT Enterprise- DG Enabled  | \*Configuration dependent    | \*Configuration dependent        | \*Configuration dependent                                                  |
| Windows IoT Core(1)                 | Yes (not required)           | Yes (not required)               | Yes (Cross signing also works for certificates issued after July 29, 2015) |

\*Configuration dependent – With Windows 10 Enterprise edition, organizations can use WDAC to define custom signing requirements.

(1) Driver signing is required for manufacturers building retail products (that is, for a nondevelopment purpose) with IoT Core. For a list of approved certificate authorities, see [Cross-Certificates for Kernel Mode Code Signing](../install/cross-certificates-for-kernel-mode-code-signing.md). If UEFI Secure Boot is enabled, then you must use signed drivers.
