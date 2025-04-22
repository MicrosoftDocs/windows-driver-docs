---
title: Enterprise CA Test Certificate
description: Enterprise CA Test Certificate
keywords:
- Enterprise CA test certificates WDK
ms.date: 04/22/2025
---

# Enterprise CA Test Certificate

An *Enterprise CA test certificate* is an Authenticode digital certificate that an Enterprise certification authority (Enterprise CA) deploys across an enterprise. As part of a public key infrastructure, a domain administrator can create an Enterprise CA to manage the enterprise-wide Authenticode certification of [driver packages](driver-packages.md) that are under development.

An Enterprise CA is integrated with Active Directory and publishes certificates and certificate revocation lists to Active Directory. The Enterprise CA uses information stored in Active Directory, to approve or deny certificate requests. The information in Active Directory includes user accounts and security groups.

An Enterprise CA uses certificate templates. When a certificate is issued, the Enterprise CA uses information in the certificate template to generate a certificate with the appropriate attributes for that certificate type.

If you want to enable automated certificate approval and automatic user certificate enrollment, the Enterprise CA infrastructure must be integrated with Active Directory.

In summary, a domain administrator has to do the following to create an Enterprise CA to manage the enterprise-wide Authenticode certification of [driver packages](driver-packages.md) that are under development:

- Install an Enterprise CA.

- Create a test (code-signing) certificate template.

- Publish the test certificate template in Active Directory.

- Configure Group Policy to distribute the test certificates that the Enterprise CA issues.

Detailed information on how to configure an Enterprise CA is beyond the scope of this article. For complete information about designing a public key infrastructure and installing Enterprise CA, see [Code-Signing Best Practices](/windows-hardware/test/hlk/), the [Windows Server deployment, configuration, and administration](/training/paths/windows-server-deployment-configuration-administration/), [Public Key Infrastructures](/previous-versions/windows/it-pro/windows-server-2003/cc757327(v=ws.10)), and the [Window Server Tech Community](https://techcommunity.microsoft.com/category/Windows-Server). The Tech Community includes discussions about certificates, certificate services, and certificate templates.

Information about configuring an Enterprise CA to test-sign [driver packages](driver-packages.md) is also provided in the readme file *Selfsign_readme.htm*, which located in the *src\\general\\build\\driversigning* directory of the Windows Driver Kit (WDK).
