---
title: Certify a New App
description: Certify a New App
ms.assetid: 2a11dfe3-e197-4455-ad79-2c9ef5897c46
ms.author: windowsdriverdev
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Certify a New App


Follow these steps to certify a new Windows or Windows Server app.

**To certify a new Windows app**

1.  Use the [Windows App Certification Kit](http://go.microsoft.com/fwlink/p/?LinkId=219252) to certify an app for Windows 7 or Windows 8.

2.  In the Windows Dev Center, click **Dashboard**, and then sign in with your Microsoft account.

3.  Click **App certification**.

4.  On the App Certification page, in the **Create certification** tile, click **Certify a client app**.

5.  Browse to the Windows ACK test results.

    **Note**  
    You can make sure that the report is finalized before uploading by using the following command**: appcert.exe finalizereport -reportfilepath** &lt;*name*&gt;

     

6.  Complete the **Product info** form. You can add a description, image, and page URL if you want users to learn more about the app. You can also select one or more supported languages. Then click **Next**.

7.  Add any additional information, such as category, URLs for different versions, and comments, and then click **Next**.

8.  If the app is antimalware, choose the **Security** category and the **PC Protection** subcategory.

    **Note**  
    **Windows 8** antimalware apps require you to choose which standards committee your company belongs to, as well as which testing institutions verified the app. The app also undergoes manual verification by Microsoft.

     

9.  Review the information for errors, and then click **Submit**.

10. Review the next steps, and then click **Finish** to submit the package for certification.

To see the status of a submission, click **Manage client certification**, and then search for the submission ID.

**To certify a new Windows Server app**

1.  Use the Product Identification Tool to certify a **Windows Server** app.

2.  In the Windows Dev Center, click **Dashboard**, and then sign in with your Microsoft account .

3.  Click **App certification**.

4.  On the **App certification** page, in the **Create certification** tile, click **Certify a server app**.

5.  Browse to the **ProductInformation.xml** file generated from the Product Identification Tool.

6.  Complete the product information form. You can enter a name and version number for the primary product, as well as a date after which Microsoft can display the app in the Windows Server Catalog or on the Windows Marketplace. Then click **Next**.

7.  Add any additional names that are currently used to market the app, and then click **Next**.

    **Note**  
    You can add more names later.

     

8.  Select one or more programs that the app works with, and then click **Next**.

9.  Select a category for the app, and then click **Next**.

10. Click **Finish**, and then download the files we created for the app. Files are sent to a testing authority before apps can be certified. The name of the testing authority is added to the information form after you submit it.

To see the status of a submission, click **Manage server certifications** and search for the submission ID.

## <span id="related_topics"></span>Related topics


[Manage App Certifications](https://msdn.microsoft.com/library/windows/hardware/br230791.aspx)

 

 






