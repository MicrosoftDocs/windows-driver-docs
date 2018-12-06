---
title: Creating a service metadata submission package in Visual Studio
description: Creating a service metadata submission package in Visual Studio
ms.assetid: 93C2F66B-EAD3-4C7B-A761-E0AF861101D0
keywords:
- Creating a service metadata submission package in Visual Studio
ms.date: 04/20/2017
ms.localizationpriority: medium
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

For more information about the devicemanifest file, see [Submit a UWP app for Mobile Broadband](http://go.microsoft.com/fwlink/p/?linkid=248426).

For more information about the bulkmetadata file, see [Submit a Bulk Metadata Package](http://go.microsoft.com/fwlink/p/?linkid=248427).

 

 





