---
title: Trusted Root Certification Authorities Certificate Store
description: Trusted Root Certification Authorities Certificate Store
keywords:
- certificate stores WDK
- driver signing WDK , digital signatures
- Trusted Root Certification Authorities certificate store WDK
ms.date: 04/24/2024
ai-usage: ai-assisted
---

# Trusted Root Certification Authorities Certificate Store

Starting with Windows Vista, the Plug and Play (PnP) manager performs driver signature verification during device and driver installation. Verification succeeds when:

-   The signing certificate that was used to create the signature was issued by a certification authority (CA).

-   The corresponding root certificate for the CA is installed in the *Trusted Root Certification Authorities certificate store*. Therefore, the Trusted Root Certification Authorities certificate store contains the root certificates of all CAs that Windows trusts.

To access the Trusted Root Certification Authorities certificate store on a Windows computer, you can use the Microsoft Management Console (MMC) with the Certificates snap-in. Here are the steps to do this on a Windows 10/11 computer:  
   
1. **Open the Run Dialog**: Press `Windows key + R` to open the Run dialog.  
   
2. **Open MMC**: Type `mmc` into the Run dialog and press Enter. This opens the Microsoft Management Console. If prompted by User Account Control (UAC), click Yes to allow the MMC to make changes to your device.  
   
3. **Add the Certificates Snap-in**:  
   - In the MMC window, click on `File` in the menu bar and select `Add/Remove Snap-in`.  
   - In the Add or Remove Snap-ins window, scroll down and select `Certificates`, then click `Add >`.  
   - A pop-up will ask which certificates you want to manage. Select `Computer account`, then click `Next`.  
   - Select `Local computer: (the computer this console is running on)`, then click `Finish`.  
   - You can also choose `My user account` or `Service account` depending on your needs, but for accessing the Trusted Root Certification Authorities, you typically choose `Computer account`.  
   - Click `OK` to close the Add or Remove Snap-ins window.  
   
4. **Access the Trusted Root Certification Authorities**:  
   - In the MMC, under the `Certificates (Local Computer)` tree, expand the `Trusted Root Certification Authorities` folder.  
   - Click on `Certificates` under the `Trusted Root Certification Authorities`. This will display all the certificates that are currently trusted by the computer.  
   
5. **Manage Certificates**:  
   - From here, you can view details of each certificate, import new trusted certificates, or remove existing ones. However, be cautious when adding or removing certificates as it can affect the security and functionality of your system.  
   
6. **Close MMC**:  
   - When you are done, you can simply close the MMC window. If you made changes and it asks if you want to save the console settings, choose `No` unless you plan on reusing this console setup frequently.  
   
Remember, managing certificates and the Trusted Root Certification Authorities store should be done carefully and typically requires administrator privileges. Improper changes can compromise the security of your system.


By default, the Trusted Root Certification Authorities certificate store is configured with a set of public CAs that has met the requirements of the Microsoft Root Certificate Program. Administrators can configure the default set of trusted CAs and install their own private CA for verifying software.

**Note**  A private CA is unlikely to be trusted outside the network environment.

Having a valid digital signature ensures the authenticity and integrity of a [driver package](driver-packages.md). However, it does not mean that the end-user or a system administrator implicitly trusts the software publisher. A user or administrator must decide whether to install or run an application on a case-by-case basis, based on their knowledge of the software publisher and application. By default, a publisher is trusted only if its certificate is installed in the [Trusted Publishers certificate store](trusted-publishers-certificate-store.md).

The name of the Trusted Root Certification Authorities certificate store is *root.* You can manually install the root certificate of a private CA into the Trusted Root Certification Authorities certificate store on a computer by using the [**CertMgr**](../devtest/certmgr.md) tool.

**Note**  The driver signing verification policy that is used by the PnP manager requires that the root certificate of a private CA has been previously installed in the local machine version of the Root Certification Authorities certificate store. For more information, see [Local Machine and Current User Certificate Stores](local-machine-and-current-user-certificate-stores.md).

For more information about driver signing, see [Driver Signing Policy](./kernel-mode-code-signing-policy--windows-vista-and-later-.md).
