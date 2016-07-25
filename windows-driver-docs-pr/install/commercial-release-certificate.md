---
title: Commercial Release Certificate
description: Commercial Release Certificate
ms.assetid: bc3966e6-a7e4-4c5c-8dcf-9b95e61ba9b1
keywords: ["commercial release certificates WDK", "catalog files WDK driver signing , commercial release certificates", "public release driver signing WDK , commercial release certificates", "release signing WDK , commercial release certificates"]
---

# Commercial Release Certificate


A *commercial release certificate* refers to a digital certificate that a publisher obtains from a trusted, third-party, commercial certification authority (CA) that is a member of the Microsoft Root Certificate Program. GTE and VeriSign, Inc. are two examples of such CAs. A CA that is a member of this program validates the identity and entitlement of an applicant and then issues a certificate that the applicant uses to sign its drivers. The signing process stamps the driver with the publisher's identity and can be used to verify that the driver has not been modified since it was signed.

For security reasons, you should not use a digital certificate that is used to release-sign drivers to test-sign drivers. You should obtain separate digital certificates to use for release-signing and for test-signing. For information about how to manage digital certificates, see [Managing the Digital Signature or Code Signing Keys](managing-the-digital-signature-or-code-signing-keys.md).

Follow the instructions that are provided by the CA about how to obtain and install the release certificate on a computer that you will be using to sign a driver.

For more information about how to obtain a digital certificate from a CA, see the [Microsoft Root Certificate Program Members](http://go.microsoft.com/fwlink/p/?linkid=74266) website.

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bdevinst\devinst%5D:%20Commercial%20Release%20Certificate%20%20RELEASE:%20%287/22/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




