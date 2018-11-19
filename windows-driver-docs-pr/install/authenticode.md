---
title: Authenticode Digital Signatures
description: Authenticode Digital Signatures
ms.assetid: b4cddf64-dc1a-47b7-803d-afb1e175c9d5
keywords:
- Authenticode WDK driver signing
- driver signing WDK , Authenticode
- signing drivers WDK , Authenticode
- digital signatures WDK , Authenticode
- signatures WDK , Authenticode
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Authenticode Digital Signatures


Authenticode is a Microsoft code-signing technology that identifies the publisher of Authenticode-signed software. Authenticode also verifies that the software has not been tampered with since it was signed and published.

Authenticode uses cryptographic techniques to verify publisher identity and code integrity. It combines digital signatures with an infrastructure of trusted entities, including certificate authorities (CAs), to assure users that a driver originates from the stated publisher. Authenticode allows users to verify the identity of the software publisher by chaining the certificate in the digital signature up to a trusted root certificate.

Using Authenticode, the software publisher signs the driver or [driver package](driver-packages.md), tagging it with a [digital certificate](digital-certificates.md) that verifies the identity of the publisher and also provides the recipient of the code with the ability to verify the integrity of the code. A certificate is a set of data that identifies the software publisher. It is issued by a CA only after that authority has verified the software publisher's identity. The certificate data includes the publisher's public cryptographic key. The certificate is typically part of a chain of such certificates, ultimately referenced to a well-known CA such as VeriSign.

Authenticode code signing does not alter the executable portions of a driver. Instead, it does the following:

-   With embedded signatures, the signing process embeds a digital signature within a nonexecution portion of the driver file. For more information about this process, see [Embedded Signatures in a Driver File](embedded-signatures-in-a-driver-file.md).

-   With digitally-signed [catalog files](catalog-files.md) (*.cat*), the signing process requires generating a file hash value from the contents of each file within a [driver package](driver-packages.md). This hash value is included in a catalog file. The catalog file is then signed with an embedded signature. In this way, catalog files are a type of detached signature.

**Note**  The [Hardware Certification Kit (HCK)](http://go.microsoft.com/fwlink/p/?linkid=227016) has test categories for a variety of device types. The list of test categories can be found at [Certification Test Reference](https://msdn.microsoft.com/library/windows/hardware/hh998741). If a test category for the device type is included in this list, the software publisher should obtain a [WHQL release signature](whql-release-signature.md) for the [driver package](driver-packages.md) However, if the HCK does not have a test program for the device type, the software publisher can sign the driver package by using the Microsoft Authenticode technology. For more information about this process, see [Signing Drivers for Public Release](signing-drivers-for-public-release.md).

 

 

 





