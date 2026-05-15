---
title: Trusted Root Certification Authorities Certificate Store
description: Learn about how the Plug and Play manager performs driver signature verification during device and driver installation.
keywords:
- certificate stores WDK
- driver signing WDK , digital signatures
- Trusted Root Certification Authorities certificate store WDK
ms.date: 10/24/2025
ai-usage: ai-assisted
ms.topic: concept-article
#customer intent: As an administrator of a Windows computer who installs drivers, I want to understand how the Plug and Play (PnP) manager performs driver signature verification.
---

# Trusted Root Certification Authorities Certificate Store

The Plug and Play (PnP) manager performs driver signature verification during device and driver installation. Verification succeeds when:

- A certification authority (CA) issued the signing certificate used to create the signature.

- The corresponding root certificate for the CA is installed in the *Trusted Root Certification Authorities certificate store*. The Trusted Root Certification Authorities certificate store contains the root certificates of all CAs that Windows trusts.

To access the Trusted Root Certification Authorities certificate store on a Windows computer, you can use the Microsoft Management Console (MMC) with the Certificates snap-in. Here are the steps for a Windows 10 or later computer:

1. Open the Windows Run dialog: Press **Windows key** + **R** to open the Run dialog.

1. Open the Microsoft Management Console (MMC): Type `mmc` into the Run dialog and press **Enter**. This command opens the Microsoft Management Console. If User Account Control (UAC) prompts you, select **Yes** to allow the MMC to make changes to your device.

1. Add the certificates snap-in:

   1. In the MMC menu bar, select **File** and then select **Add/Remove Snap-in**.
   1. In the **Add or Remove Snap-ins** window, scroll down, and select **Certificates**, then select **Add >**.
   1. A dialog asks which certificates you want to manage. Select **Computer account**, then select **Next**.
   1. Select **Local computer: (the computer this console is running on)**, then select **Finish**.

      You can also choose **My user account** or **Service account** depending on your needs, but for accessing the Trusted Root Certification Authorities, choose **Computer account**.

   1. Select **OK** to close **Add or Remove Snap-ins**.

1. Access the Trusted Root Certification Authorities:

   1. In the MMC, under the **Certificates (Local Computer)** tree, expand the **Trusted Root Certification Authorities** folder.
   1. Select **Certificates** under the **Trusted Root Certification Authorities**. See all the certificates currently trusted by the computer.

1. From here, you can view details of each certificate, import new trusted certificates, or remove existing ones. Be cautious when you add or remove certificates because it can affect the security and functionality of your system.

1. When you're done, you can close the MMC window. If you made changes and it asks if you want to save the console settings, choose **No** unless you plan on reusing this console setup frequently.

> [!CAUTION]
> Managing certificates and the Trusted Root Certification Authorities store typically requires administrator privileges. Be careful when you manage certificates, because improper changes can compromise the security of your system.

By default, the Trusted Root Certification Authorities certificate store is configured with a set of public CAs that meet the requirements of the Microsoft Root Certificate Program. Administrators can configure the default set of trusted CAs and install their own private CA for verifying software.

> [!NOTE]
> A private CA is unlikely to be trusted outside the network environment.

Having a valid digital signature ensures the authenticity and integrity of a [driver package](driver-packages.md). It doesn't mean that the end-user or a system administrator implicitly trusts the software publisher. A user or administrator must decide whether to install or run an application on a case-by-case basis, based on their knowledge of the software publisher and application. By default, a publisher is trusted only if its certificate is installed in the [Trusted Publishers Certificate Store](trusted-publishers-certificate-store.md).

The name of the Trusted Root Certification Authorities certificate store is *root*. You can manually install the root certificate of a private CA into the Trusted Root Certification Authorities certificate store on a computer by using the [CertMgr](../devtest/certmgr.md) tool.

> [!NOTE]
> The driver signing verification policy that is used by the PnP manager requires that the root certificate of a private CA was previously installed in the local machine version of the Root Certification Authorities certificate store. For more information, see [Local machine and current user certificate stores](local-machine-and-current-user-certificate-stores.md).

## Related content

For more information about driver signing, see [Driver Signing Policy](./kernel-mode-code-signing-policy--windows-vista-and-later-.md).
