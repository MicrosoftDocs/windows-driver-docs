---
title: Enterprise CA Test Certificate
description: Enterprise CA Test Certificate
ms.assetid: c2b075c9-cb85-446d-ac07-65aad5507e62
keywords: ["Enterprise CA test certificates WDK"]
---

# Enterprise CA Test Certificate


An *Enterprise CA test certificate* is an Authenticode digital certificate that is deployed by an Enterprise certification authority (Enterprise CA) across an enterprise. As part of a public key infrastructure, a domain administrator can create an Enterprise CA to manage the enterprise-wide Authenticode certification of [driver packages](driver-packages.md) that are under development.

An Enterprise CA is integrated with Active Directory and publishes certificates and certificate revocation lists to Active Directory. The Enterprise CA uses information that is stored in Active Directory, including user accounts and security groups, to approve or deny certificate requests.

An Enterprise CA uses certificate templates. When a certificate is issued, the Enterprise CA uses information in the certificate template to generate a certificate with the appropriate attributes for that certificate type.

If you want to enable automated certificate approval and automatic user certificate enrollment, the Enterprise CA infrastructure must be integrated with Active Directory.

In summary, a domain administrator has to do the following to create an Enterprise CA to manage the enterprise-wide Authenticode certification of [driver packages](driver-packages.md) that are under development:

-   Install an Enterprise CA.

-   Create a test (code-signing) certificate template.

-   Publish the test certificate template in Active Directory.

-   Configure Group Policy to distribute the test certificates that are issued by the Enterprise CA.

Detailed information on how to configure an Enterprise CA is beyond the scope of this documentation. For complete information about how to design a public key infrastructure and installing Enterprise CA, see the [Code-Signing Best Practices](http://go.microsoft.com/fwlink/p/?linkid=68250) website,

the Windows Server 2003 Deployment Kit, the Windows Server 2003 Help and Support Center, and the [Public Key Infrastructures](http://go.microsoft.com/fwlink/p/?linkid=62645) webpage of the [Microsoft TechNet](http://go.microsoft.com/fwlink/p/?linkid=62647) website. The TechNet website includes information about certificates, certificate services, and certificate templates.

Information about configuring an Enterprise CA to test-sign [driver packages](driver-packages.md) is also provided in the readme file *Selfsign\_readme.htm*, which located in the *src\\general\\build\\driversigning* directory of the WDK.

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bdevinst\devinst%5D:%20Enterprise%20CA%20Test%20Certificate%20%20RELEASE:%20%287/22/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




