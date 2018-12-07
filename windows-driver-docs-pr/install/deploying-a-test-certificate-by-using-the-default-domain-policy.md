---
title: Deploying a Test Certificate by Using the Default Domain Policy
description: Deploying a Test Certificate by Using the Default Domain Policy
ms.assetid: eafa4e20-94c5-49d6-a192-2fc7c9f1e64f
keywords:
- MakeCert test certificates WDK
- Trusted Root Certification Authorities certificate store WDK
- Trusted Publishers certificate store WDK
- default domain policies for test certificates
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Deploying a Test Certificate by Using the Default Domain Policy


A domain administrator who is logged on to a domain on a computer that is running Windows Vista and later versions of Windows can configure the default domain policy to deploy a test certificate to the certificate stores of computers in the domain.

After the default domain policy is configured as described in this topic, the certificate stores of computers in the domain are updated approximately every 90 minutes and every time that a computer is restarted. In addition, each computer can force an update of the default domain policy by using the **gpupdate /force** command.

To configure the default domain policy to deploy a test certificate to the Trusted Root Certification Authorities certificate store, follow these steps:

1.  Click **Start**, point to **Settings**, click **Control Panel**, and then double-click **Administrative Tools**.

2.  Open Domain Security Policy.

3.  In the left pane of the **Console** box, expand **Default Domain Policy**, expand **Computer Configuration**, expand **Windows Settings**, expand **Security Settings**, expand **Public Key Policies**, and select **Trusted Root Certification Authorities**.

4.  On the main menu bar, click **Action**, and then click **Import** to open the Certificate Import Wizard.

5.  On the first page of the Certificate Import Wizard, click **Next**, and then in the **File Name** box of the **File to Import** page, enter the name of the file that contains the certificate to be imported, and then click **Next**. (Or, click **Browse**, browse to the file, and select it).

6.  To finish the Certificate Import Wizard, click **Next** twice and then click **Finish**.

Use the same type of procedure to configure the default domain policy to deploy a test certificate to the Trusted Publishers certificate store as described above for the Trusted Root Certification Authorities certificate store. In step (3) of the procedure in this section, select Trusted Publishers certificate store instead of the Trusted Root Certification Authorities certificate store.

 

 





