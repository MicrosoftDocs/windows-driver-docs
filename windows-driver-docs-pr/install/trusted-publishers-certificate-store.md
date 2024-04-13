---
title: Trusted Publishers Certificate Store
description: Trusted Publishers Certificate Store
keywords:
- driver signing WDK , Trusted Publishers certificate store
- Trusted Publishers certificate store WDK
- certificate stores WDK
ms.date: 03/18/2022
---

# Trusted Publishers Certificate Store

The *Trusted Publishers certificate store* contains information about the Authenticode (signing) certificates of trusted publishers that are installed on a computer. In order to test and debug your [driver packages](driver-packages.md) within your organization, your company should install the Authenticode certificates that are used to sign driver packages in the Trusted Publishers certificate store. Install the Authenticode certificates on each computer in the workgroup or organizational unit that runs signed code. The name of the Trusted Publishers certificate store is *trustedpublisher.*

If a publisher's Authenticode certificate is in the Trusted Publishers certificate store, Windows installs a [driver package](driver-packages.md) that was digitally signed by the certificate without prompting the user (*silent install*). By installing the Authenticode certificates in the Trusted Publishers certificate store, you can automate the installation of your driver package on various systems that are used for internal testing and debugging.

> [!IMPORTANT]
> This practice of automating the installation of driver packages is only suggested for your internal systems. This practice should never be followed for any driver package that is distributed outside your organization.

The Trusted Publishers certificate store differs from the [Trusted Root Certification Authorities certificate store](trusted-root-certification-authorities-certificate-store.md) in that only *end-entity* certificates can be trusted. For example, if an Authenticode certificate from a CA was used to [test-sign](introduction-to-test-signing.md) a driver package, adding that certificate to the Trusted Publishers certificate store does not configure all certificates that this CA issued as trusted. Each certificate must be added separately to the Trusted Publishers certificate store.

Use a Group Policy to distribute certificates to an organizational unit on a network. In this situation, the administrator adds a Certificate Rule to a Group Policy to establish trust in a publisher.

You can manually install the Authenticode certificates into the Trusted Publishers certificate store on a computer by using the [**CertMgr**](../devtest/certmgr.md) tool.

> [!NOTE]
> The driver signing verification policy used by Plug and Play requires that the Authenticode certificate of a CA has been previously installed in the local machine version of the Trusted Publishers certificate store. For more information, see [Local Machine and Current User Certificate Stores](local-machine-and-current-user-certificate-stores.md).

For more information about how to deploy Authenticode certificates in an enterprise using Group Policy, see the readme file *Selfsign_readme.htm*, which is located in the *bin\selfsign* directory of the WDK.
