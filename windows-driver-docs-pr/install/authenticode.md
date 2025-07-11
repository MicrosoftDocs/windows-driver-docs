---
title: Authenticode Digital Signatures
description: Explore digital signatures with Authenticode, identify the publisher of Authenticode-signed software, and confirm published software has no changes after signing.
keywords:
- Authenticode WDK driver signing
- driver signing WDK , Authenticode
- signing drivers WDK , Authenticode
- digital signatures WDK , Authenticode
- signatures WDK , Authenticode
ms.date: 07/11/2025
---

# Authenticode digital signatures

Authenticode is a Microsoft code-signing technology that identifies the publisher of Authenticode-signed software. Authenticode also verifies the software has no changes since it was signed and published.

Authenticode uses cryptographic techniques to verify publisher identity and code integrity. It combines digital signatures with an infrastructure of trusted entities, including certificate authorities (CAs), to assure users that a driver originates from the stated publisher. Authenticode allows users to verify the identity of the software publisher by chaining the certificate in the digital signature up to a trusted root certificate.

The software publisher uses Authenticode to sign the driver or [driver package](driver-packages.md) by tagging it with a [digital certificate](digital-certificates.md). The certificate verifies the identity of the publisher and enables recipients of the code to verify the integrity of the code. A certificate is a set of data that identifies the software publisher. A CA issues the certificate only after that authority verifies the software publisher's identity. The certificate data includes the publisher's public cryptographic key. The certificate is typically part of a chain of such certificates, ultimately referenced to a well-known CA such as VeriSign.

Authenticode code signing doesn't alter the executable portions of a driver. Instead, it completes the following actions:

- **Embedded signatures**: The signing process embeds a digital signature within a nonexecution portion of the driver file. For more information, see [Embedded signatures in a driver file](embedded-signatures-in-a-driver-file.md).

- **Digitally signed [catalog files](catalog-files.md)**: The signing process requires generating a file hash value from the contents of each catalog file (_.cat_) within a [driver package](driver-packages.md). This hash value is included in a catalog file. The catalog file is then signed with an embedded signature. In this way, catalog files are a type of detached signature.

> [!NOTE]
> The [Hardware Certification Kit (HCK)](/previous-versions/windows/hardware/hck/jj124227(v=vs.85)) includes test categories for various of device types. You can review the list of test categories for Windows Hardware Lab Kit (HLK) in the [HLK API reference](/windows-hardware/test/hlk/api/hlk-api-reference). If a test category for the device type is included in this list, the software publisher should obtain a [Windows Hardware Quality Labs (WHQL) release signature](whql-release-signature.md) for the [driver package](driver-packages.md). However, if the HCK doesn't have a test program for the device type, the software publisher can sign the driver package by using the Microsoft Authenticode technology. For more information, see [Signing drivers for public release](signing-drivers-for-public-release--windows-vista-and-later-.md).