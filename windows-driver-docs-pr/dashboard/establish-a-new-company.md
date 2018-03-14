---
title: Establish a new company
description: Establish a new company
ms.assetid: 98cdd891-3bb8-4aa1-8418-35c2670ba087
ms.author: windowsdriverdev
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Establish a new company

> [!IMPORTANT]
> This content only applies to administration tasks for the Sysdev dashboard, which is being replaced by the Windows Hardware Dev Center Dashboard. See [Windows Hardware Dev Center Dashboard](https://msdn.microsoft.com/en-us/windows/hardware/drivers/dashboard/index) for current support and transition timelines.  

Before you can establish a new company on the Hardware Dev Center dashboard, you need to get an approved standard code signing or extended validation (EV) code signing certificate from one of the approved certificate authorities. To learn more, see [Get a code signing certificate](https://msdn.microsoft.com/library/windows/hardware/hh801887.aspx).

Once you have the code signing certificate, follow the steps to establish a new company.

**Establish a new company**

1.  Download the certificate you received from the certificate authority.

2.  From the Hardware Dev Center dashboard, sign in with the Microsoft account you want to use for submissions.

3.  On the **Create a company account** page, in the **Create a Company Account** section, click **Next**.

4.  In the **How to obtain a code signed Winqual.exe file** section, make sure you’ve followed the steps to digitally code sign the [Winqual.exe file](http://go.microsoft.com/fwlink/?LinkId=393250) using the [SignTool](http://go.microsoft.com/fwlink/p/?LinkId=238330), and then click **Next**.

5.  In the **Provide code signed Winqual.exe file** section, browse to the Winqual.exe file, and then click **Next**.

6.  In the **Contact Address** section, enter the address for your company, as well as email address and phone number, and then click **Next**.

    **Note**  
    The email address you enter must be the work email address for an Administrator of the company account you just created.

     

    When the organization has been established, you can set permissions for yourself and sign the legal agreements.

    **Note**  
    If you are establishing a Company for the Windows Reference Design feature you will see an additional **Account Info** page where you can add your preferred OEM ID, preferred email language and choose to open an App Store account if applicable.

     

## <span id="related_topics"></span>Related topics


[Manage Legal Agreements](https://msdn.microsoft.com/library/windows/hardware/br230801.aspx)

[Create and Manage Your Profile](https://msdn.microsoft.com/library/windows/hardware/br230768.aspx)

[For Administrators](https://msdn.microsoft.com/library/windows/hardware/br230765.aspx)

[Manage users and permissions](https://msdn.microsoft.com/library/windows/hardware/br230781.aspx)

 

 

