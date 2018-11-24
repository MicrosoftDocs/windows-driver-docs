---
title: Commercial Test Certificate
description: Commercial Test Certificate
ms.assetid: cedceb0c-d39e-45e2-aa42-62cd7b8bed1c
keywords:
- commercial test certificates WDK
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Commercial Test Certificate


A *commercial test certificate* refers to a digital certificate that a publisher obtains from a trusted, third-party, commercial certification authority (CA) that is a member of the Microsoft Root Certificate Program. GTE and VeriSign, Inc. are two examples of such a CA.

A CA that is a member of the Microsoft Root Certificate Program validates the identity and entitlement of an applicant and then issues a certificate that the applicant uses to sign its drivers. The signing process stamps the driver with the publisher's identity and can be used to verify that the driver has not been modified since it was signed.

A commercial test certificate is the same type of certificate as a [commercial release certificate](commercial-release-certificate.md). However, for security reasons, you should not use a digital certificate that is used to test-sign drivers to also sign a release driver. You should obtain separate digital certificates to use for release-signing and for test-signing. For information about how to manage digital certificates, see [Managing the Digital Signature or Code Signing Keys](managing-the-digital-signature-or-code-signing-keys.md).

Follow the instructions that are provided by the CA on how to obtain and install the certificate on a computer where you will sign a driver.

For more information about how to obtain a digital certificate from a CA, see the [Microsoft Root Certificate Program Members](http://go.microsoft.com/fwlink/p/?linkid=16356) website.

 

 





