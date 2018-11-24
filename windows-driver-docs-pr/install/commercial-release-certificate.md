---
title: Commercial Release Certificate
description: Commercial Release Certificate
ms.assetid: bc3966e6-a7e4-4c5c-8dcf-9b95e61ba9b1
keywords:
- commercial release certificates WDK
- catalog files WDK driver signing , commercial release certificates
- public release driver signing WDK , commercial release certificates
- release signing WDK , commercial release certificates
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Commercial Release Certificate


A *commercial release certificate* refers to a digital certificate that a publisher obtains from a trusted, third-party, commercial certification authority (CA) that is a member of the Microsoft Root Certificate Program. GTE and VeriSign, Inc. are two examples of such CAs. A CA that is a member of this program validates the identity and entitlement of an applicant and then issues a certificate that the applicant uses to sign its drivers. The signing process stamps the driver with the publisher's identity and can be used to verify that the driver has not been modified since it was signed.

For security reasons, you should not use a digital certificate that is used to release-sign drivers to test-sign drivers. You should obtain separate digital certificates to use for release-signing and for test-signing. For information about how to manage digital certificates, see [Managing the Digital Signature or Code Signing Keys](managing-the-digital-signature-or-code-signing-keys.md).

Follow the instructions that are provided by the CA about how to obtain and install the release certificate on a computer that you will be using to sign a driver.

For more information about how to obtain a digital certificate from a CA, see the [Microsoft Root Certificate Program Members](http://go.microsoft.com/fwlink/p/?linkid=74266) website.

 

 





