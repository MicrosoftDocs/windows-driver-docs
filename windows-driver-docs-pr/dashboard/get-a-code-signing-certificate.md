---
title: Get a code signing certificate
description: Get a code signing certificate
ms.topic: article
ms.date: 02/10/2022
---

# Get a code signing certificate

Before you can establish a Partner Center account, you need to get a code signing certificate to secure your digital information. This certificate is the accepted standard for establishing your company's ownership of the code you submit. It allows you to digitally sign PE binaries, such as .exe, .cab, .dll, .ocx, .msi, .xpi and .xap files.

## Step 1: Obtain an EV certificate

- Microsoft requires an extended validation (EV) code signing certificate from partners enrolled and authorized for kernel mode code signing as part of the Microsoft Trusted Root Certificate Program. If you already have an approved EV certificate from one of these authorities, you can use it to establish a Partner Center account. If you don't have a certificate, you'll need to buy a new one.

## Step 2: Buy a new code signing certificate

If you don't have an approved EV code signing certificate, you can buy one from one of the certificate authorities shown below.

### Extended validation code signing certificates

The following certificate authorities are listed in alphabetical order.

- [Certum EV code signing certificate](https://shop.certum.eu/data-safety/code-signing-certificates/certum-ev-code-sigining.html)
- [DigiCert EV code signing certificate](https://www.digicert.com/order/order-1.php)
- [Entrust EV code signing certificate](https://www.entrustdatacard.com/products/digital-signing-certificates/code-signing-certificates)
- [GlobalSign EV code signing certificate](https://go.microsoft.com/fwlink/p/?LinkId=620888)
- [IdenTrust EV code signing certificate](https://www.identrust.com/certificates/trustid-ev-code-signing)
- [Sectigo (formerly Comodo) EV code signing certificate](https://go.microsoft.com/fwlink/?linkid=863208)
- [SSL.com EV code signing certificate](https://www.ssl.com/certificates/ev-code-signing/)

## Step 3: Retrieve code signing certificates

Once the certificate authority has verified your contact information and your certificate purchase is approved, follow their directions to retrieve the certificate.

> [!NOTE]
> You must use the same computer and browser to buy and retrieve your certificate.

## Step 4: Add the certificates to your account on Partner Center

For step-by-step instructions, see [Add or Update a code signing certificate](update-a-code-signing-certificate.md).

## Next steps

- If you're setting up a new Partner Center account, follow the steps in [Register for the Hardware Program](register-for-the-hardware-program.md).
- If you've already set up a Partner Center account and need to renew a certificate, follow the steps in [Add or Update a code signing certificate](update-a-code-signing-certificate.md).

## FAQ

This section provides answers to frequently asked questions about code signing for Windows 10. Additional code signing information is available on the Windows Hardware Certification blog.

- [Driver Signing Changes in Windows 10](https://techcommunity.microsoft.com/t5/Windows-Hardware-Certification/Driver-Signing-changes-in-Windows-10/ba-p/364859)
- [Driver Signing changes in Windows 10, version 1607](https://techcommunity.microsoft.com/t5/Windows-Hardware-Certification/Driver-Signing-changes-in-Windows-10-version-1607/ba-p/364894)
- [Update on Sysdev EV Certificate requirement](https://techcommunity.microsoft.com/t5/Windows-Hardware-Certification/Update-on-Sysdev-EV-Certificate-requirement/ba-p/364879)

### HLK tested and dashboard signed drivers

- A dashboard signed driver that has passed the HLK tests will work on Windows Vista through Windows 10, including Windows Server editions. This is the recommended method for driver signing, because it allows a single process for all OS versions. In addition, HLK tested drivers demonstrate that a manufacturer has rigorously tested their hardware to meet all of Microsoft's requirements with regards to reliability, security, power efficiency, serviceability, and performance, so as to provide a great Windows experience. This includes compliance with industry standards and adherence with Microsoft specifications for technology-specific features, helping to ensure correct installation, deployment, connectivity and interoperability. For more information about the HLK, see [Windows Hardware Compatibility Program](/windows-hardware/design/compatibility/index).

### Windows 10 attestation signing

- A dashboard signed driver using attestation signing will only work on Windows 10 and later.
- An attestation signed driver will only work for Windows 10. The driver will not work for other versions of Windows, such as Windows 7, Windows 8.1, or Windows Server 2016 and greater.
- Attestation signing supports Windows 10 kernel mode and user mode drivers.

### Windows Defender Application Control

- Enterprises may implement a policy to modify the driver signing requirements using Windows 10 Enterprise edition. Windows Defender Application Control (WDAC) provides an enterprise-defined code integrity policy, which may be configured to require at least an attestation-signed driver. For more information about WDAC, see [Planning and getting started on the Windows Defender Application Control deployment process](/windows/security/threat-protection/windows-defender-application-control/windows-defender-application-control-deployment-guide).

### Windows Server

- Windows Server 2016 and greater will not accept attested device and filter driver signing submissions.
- The dashboard will only sign device and filter drivers that have successfully passed the HLK tests.
- Windows Server 2016 and greater will only load dashboard signed drivers that have successfully passed the HLK tests.

### EV certificates

- As of October 31, 2015, your Hardware Dev Center dashboard account must have at least one EV certificate associated with it to submit binaries for attestation signing or to submit binaries for HLK certification.
- The submitted binaries themselves must be signed.
- EV certificates must be SHA-256.

### OS support summary

This table summarizes the driver signing requirements for Windows.

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

(1) Driver signing is required for manufacturers building retail products (i.e. for a non-development purpose) with IoT Core. For a list of approved Certificate Authorities (CAs), see [Cross-Certificates for Kernel Mode Code Signing](../install/cross-certificates-for-kernel-mode-code-signing.md). Note that if UEFI Secure Boot is enabled, then drivers must be signed.
