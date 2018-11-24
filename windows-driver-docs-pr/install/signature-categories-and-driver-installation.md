---
title: Signature Categories and Driver Installation
description: Signature Categories and Driver Installation
ms.assetid: d5b0e3a3-51c3-40d8-a2dc-c9392feff2cb
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Signature Categories and Driver Installation


Before Windows Vista and later versions of Windows installs a driver, the operating system analyzes the driver's signature. If a signature is present, Windows validates all the driver's files against that signature. Based on the results of this analysis, Windows puts the driver in one of the following categories:

<a href="" id="signed-by-a-microsoft-windows-signing-authority--"></a>**Signed by a Microsoft Windows signing authority.**   
These drivers are either inbox, signed by WHQL, or signed by Windows Sustained Engineering.

<a href="" id="signed-by-a-trusted-publisher--"></a>**Signed by a trusted publisher.**   
These drivers were signed by a third-party, and the user has explicitly selected to always trust signed drivers from this publisher.

<a href="" id="signed-by-an-untrusted-publisher--"></a>**Signed by an untrusted publisher.**   
These drivers were signed by a third-party, and the user has explicitly selected to never trust drivers from this publisher.

<a href="" id="signed-by-publisher-of-unknown-trust--"></a>**Signed by publisher of unknown trust.**   
These drivers were signed by a third-party, and the user has not indicated whether to trust this publisher.

<a href="" id="altered--"></a>**Altered.**   
These drivers are signed, but Windows has detected that at least one file in the [driver package](driver-packages.md) was altered since the package was signed.

<a href="" id="unsigned--"></a>**Unsigned.**   
These drivers are either unsigned or have an invalid signature. Valid signatures must be created by using a certificate that was issued by a trusted Certificate Authority (CA).

After the driver is categorized, Windows determines whether it should be installed. The process depends on the type of user. For nonadministrative and standard users, Windows does not prompt the user. It automatically installs drivers signed through either a Windows signing authority or a trusted publisher, and silently refuses to install all others.

Administrative users have more flexibility:

-   If a driver is signed by a Windows signing authority or a trusted publisher, Windows installs the driver without prompting the user.

-   If the driver is signed by an untrusted publisher, Windows does not install the driver. Windows does not prompt the user in this case, but logs an error to *Setupapi.dev.log*.

-   If the driver was signed by a publisher of unknown trust, Windows prompts the user with the following Windows Security dialog box.

    ![screen shot of windows security dialog box for a driver that has an unknown trust](images/install1.png)

    The user must explicitly select whether to install this driver. The user is also able to add the publisher to the list of trusted publishers on the user's system. If the user selects this option, all future drivers from this publisher are treated as trusted when installed on the user's system. If the user does not select this option, the publisher remains in the unknown trust category and administrative users continue to receive this prompt if they attempt to install additional drivers from this publisher.

-   If the driver lacks a valid signature or was altered, Windows prompts administrators with the following Windows Security dialog box. Again, the user must explicitly select whether to install the driver.

    ![screen shot of windows security dialog box for a driver that does not have a valid signature](images/install2.png)

**Note**  On Windows Vista and later versions of Windows, in order for users to play next-generation premium content, such as HD DVD and other formats that are licensed under the *Advanced Access Content System (AACS) Specification*, all kernel-mode components on their system must be signed. That means that, if an administrative user selects to install an unsigned or altered driver, the system is not allowed to play premium content. For more information about how to protect media components in Windows Vista, see [Code Signing for Protected Media Components in Windows Vista](http://go.microsoft.com/fwlink/p/?linkid=74262).

 

 

 





