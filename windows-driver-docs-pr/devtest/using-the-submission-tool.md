---
title: Creating a device metadata submission package in Visual Studio
description: Creating a device metadata submission package in Visual Studio
ms.assetid: 17CF8185-C9EE-4B25-BEE7-A1FFB8C92EE0
keywords: ["Creating a device metadata submission package in Visual Studio"]
---

# Creating a device metadata submission package in Visual Studio


To create a device metadata submission package, use the Submission tool in Microsoft Visual Studio.

1.  In Visual Studio, click the **Driver** menu, select **Device Metadata**, and then select **Submission**.
2.  Click **Add Metadata Package**, select the package, and then click **Open**.
3.  Confirm the **Package Name** and **Model Name**, select **Preview** if you want to preview the package, and then click **Next** .
4.  Review the **Model Name**, **Hardware IDs**, and **Experience ID**.
5.  Next to **Experience Name**, type a name for the experience.
    **Note**  This step is required for all package submissions.

     

6.  Next to **Qualification**, select one of the following options from the list:
    -   **This device has an associated logo or unclassified submission**
        -   Enter **Logo Submission IDs**.
    -   **This device uses only inbox drivers and has no associated logo submissions**

7.  If the package has been submitted before, select **Update Experience**.
8.  Click **Next**.
9.  If you haven't signed your package, complete the following steps in the Signature Wizard to sign it:

    1.  Find your certificate file and double-click it to install it.
    2.  Make sure that you install the certificate file in the user store and not in the machine store.
    3.  Click **Launch Signature Wizard**.
    4.  Click **Select store**.
    5.  Select the certificate from the dialog box.
        **Note**   The file name in the Signature Wizard is what you receive after you complete the submission metadata wizard. Therefore, unless you have a specific reason, do not change the file name or path.

         

    6.  Complete the signing process.

10. When you're ready to submit your package, click **Launch Windows Dev Center - Hardware Dashboard**.

For more information about how to submit your package, see [Submit a Device Metadata Package](http://go.microsoft.com/fwlink/p/?linkid=226302).

For more information about the bulkmetadata file, see [Submit a Bulk Metadata Package](http://go.microsoft.com/fwlink/p/?linkid=248427).

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[devtest\dma]:%20Creating%20a%20device%20metadata%20submission%20package%20in%20Visual%20Studio%20%20RELEASE:%20%2811/17/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




