---
title: Enterprise CA Test Certificate
description: Enterprise CA Test Certificate
ms.assetid: c2b075c9-cb85-446d-ac07-65aad5507e62
keywords:
- Enterprise CA test certificates WDK
ms.date: 04/20/2017
ms.localizationpriority: medium
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

Information about configuring an Enterprise CA to test-sign [driver packages](driver-packages.md) is also provided in the readme file *Selfsign_readme.htm*, which located in the *src\\general\\build\\driversigning* directory of the WDK.

 

 





