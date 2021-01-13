---
title: Commercial Test Certificate
description: Commercial Test Certificate
keywords:
- commercial test certificates WDK
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Commercial Test Certificate

 > [!CAUTION] 
 > Starting in 2021, the majority of cross-certificates will begin to expire. Once these cross-certificates expire, code signing certificates that chain to these cross-certificates will no longer be able to create new kernel mode digital signatures. This will affect all versions of Windows. For more information, see [Deprecation of software publisher certificates and commercial release certificates](deprecation-of-software-publisher-certificates-and-commercial-release-certificates.md).
 
A *commercial test certificate* refers to a digital certificate that a publisher obtains from a trusted, third-party, commercial certification authority (CA) that is a member of the Microsoft Root Certificate Program. GTE and VeriSign, Inc. are two examples of such a CA.

A CA that is a member of the Microsoft Root Certificate Program validates the identity and entitlement of an applicant and then issues a certificate that the applicant uses to sign its drivers. The signing process stamps the driver with the publisher's identity and can be used to verify that the driver has not been modified since it was signed.

A commercial test certificate is the same type of certificate as a [commercial release certificate](commercial-release-certificate.md). However, for security reasons, you should not use a digital certificate that is used to test-sign drivers to also sign a release driver. You should obtain separate digital certificates to use for release-signing and for test-signing. For information about how to manage digital certificates, see [Managing the Digital Signature or Code Signing Keys](managing-the-digital-signature-or-code-signing-keys.md).

Follow the instructions that are provided by the CA on how to obtain and install the certificate on a computer where you will sign a driver.

For more information about how to obtain a digital certificate from a CA, see the [Microsoft Root Certificate Program Members](/previous-versions/ms995347(v=msdn.10)) website.

 

