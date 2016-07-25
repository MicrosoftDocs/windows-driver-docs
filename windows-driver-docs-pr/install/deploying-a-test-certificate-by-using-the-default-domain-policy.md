---
title: Deploying a Test Certificate by Using the Default Domain Policy
description: Deploying a Test Certificate by Using the Default Domain Policy
ms.assetid: eafa4e20-94c5-49d6-a192-2fc7c9f1e64f
keywords: ["MakeCert test certificates WDK", "Trusted Root Certification Authorities certificate store WDK", "Trusted Publishers certificate store WDK", "default domain policies for test certificates"]
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

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bdevinst\devinst%5D:%20Deploying%20a%20Test%20Certificate%20by%20Using%20the%20Default%20Domain%20Policy%20%20RELEASE:%20%287/22/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




