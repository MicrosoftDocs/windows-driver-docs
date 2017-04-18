---
title: Creating a service metadata submission package in Visual Studio
description: Creating a service metadata submission package in Visual Studio
ms.assetid: 93C2F66B-EAD3-4C7B-A761-E0AF861101D0
keywords: ["Creating a service metadata submission package in Visual Studio"]
---

# Creating a service metadata submission package in Visual Studio


Use the Submission tool in Microsoft Visual Studio to create a submission package.

### <span id="To_create_a_submission_package"></span><span id="to_create_a_submission_package"></span><span id="TO_CREATE_A_SUBMISSION_PACKAGE"></span>To create a submission package

1.  Click the **Driver** menu, select **Device Metadata**, and then select **Submission**.
2.  Click **Add Metadata Package**, find and select the metadata package, and then click **Open**.
3.  Confirm the **Package Name** and **Model Name**, and then select **Preview** if you want to preview the package.

    **Note**  The **Model Name** field is the **Service Provider** name that is specified as part of the service metadata package.

     

4.  Click **Next**.
5.  Review the **Model Name**, **Hardware IDs**, and **Experience ID**.
6.  Next to **Experience Name**, type a name for the experience.
    **Note**  This step is required for all package submissions.

     

7.  Next to **Qualification**, select **This device has an associated logo or unclassified submission** from the list.
8.  If the package has been submitted before, select **Update Experience**.
9.  Click **Next**.
10. Confirm the mobile broadband provider's information by re-entering the Hardware ID information (for example, IMSI or ICCID). The plain text Hardware ID information is used by the Hardware Dashboard in the Windows Dev Center to verify the hashed Hardware IDs that are specified in the metadata package.
11. If you haven't signed your package, follow these steps to sign it:

    1.  Find your certificate file and double-click it to install it.
    2.  Make sure that you install the certificate file in the user store and not the machine store.
    3.  Click **Launch Signature Wizard**.
    4.  Click **Select store**.
    5.  Select the certificate from the dialog box.
        **Note**  The file name in the Signature Wizard is what you receive after you complete the submission metadata wizard. Therefore, unless you have a specific reason, do not change the file name or path.

         

    6.  Complete the signing process.

12. When you're ready to submit your package, click **Launch Windows Dev Center - Hardware Dashboard**.

For more information about how to submit your package, see [Submit a Device Metadata Package](http://go.microsoft.com/fwlink/p/?linkid=226302).

For more information about the devicemanifest file, see [Submit a Windows Store app for Mobile Broadband](http://go.microsoft.com/fwlink/p/?linkid=248426).

For more information about the bulkmetadata file, see [Submit a Bulk Metadata Package](http://go.microsoft.com/fwlink/p/?linkid=248427).

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[devtest\devtest]:%20Creating%20a%20service%20metadata%20submission%20package%20in%20Visual%20Studio%20%20RELEASE:%20%2811/17/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




