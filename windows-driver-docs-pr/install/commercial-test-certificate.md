---
title: Commercial Test Certificate
description: Commercial Test Certificate
ms.assetid: cedceb0c-d39e-45e2-aa42-62cd7b8bed1c
keywords: ["commercial test certificates WDK"]
---

# Commercial Test Certificate


A *commercial test certificate* refers to a digital certificate that a publisher obtains from a trusted, third-party, commercial certification authority (CA) that is a member of the Microsoft Root Certificate Program. GTE and VeriSign, Inc. are two examples of such a CA.

A CA that is a member of the Microsoft Root Certificate Program validates the identity and entitlement of an applicant and then issues a certificate that the applicant uses to sign its drivers. The signing process stamps the driver with the publisher's identity and can be used to verify that the driver has not been modified since it was signed.

A commercial test certificate is the same type of certificate as a [commercial release certificate](commercial-release-certificate.md). However, for security reasons, you should not use a digital certificate that is used to test-sign drivers to also sign a release driver. You should obtain separate digital certificates to use for release-signing and for test-signing. For information about how to manage digital certificates, see [Managing the Digital Signature or Code Signing Keys](managing-the-digital-signature-or-code-signing-keys.md).

Follow the instructions that are provided by the CA on how to obtain and install the certificate on a computer where you will sign a driver.

For more information about how to obtain a digital certificate from a CA, see the [Microsoft Root Certificate Program Members](http://go.microsoft.com/fwlink/p/?linkid=16356) website.

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bdevinst\devinst%5D:%20Commercial%20Test%20Certificate%20%20RELEASE:%20%287/22/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




