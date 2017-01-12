---
title: Certify a New App
description: Certify a New App
MS-HAID:
- 'p\_dashboard.certify\_a\_new\_app'
- 'hw\_dashboard.certify\_a\_new\_app'
MSHAttr:
- 'PreferredSiteName:MSDN'
- 'PreferredLib:/library/windows/hardware'
ms.assetid: 2a11dfe3-e197-4455-ad79-2c9ef5897c46
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

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bhw_dashboard\hw_dashboard%5D:%20Certify%20a%20New%20App%20%20RELEASE:%20%281/3/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")





