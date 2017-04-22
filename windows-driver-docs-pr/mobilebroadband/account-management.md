---
title: Account management
description: Account management
ms.assetid: 8201a4ac-1344-4a96-b0d5-d4ba8123c4dd
ms.author: windowsdriverdev
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Account management


After users have purchased a subscription, they can perform following tasks:

-   **View current data usage** Users can view their current data usage and understand their billing cycle (or session end date) to make an appropriate decision on their data usage.

-   **Manage account settings** Users can view and securely manage their payment and account details (such as password, email address, and automatic payment information).

-   **Pay a bill** Users can pay their recurring or one-time bill by using your Windows Store app.

Account management functionality presents a subscriber’s relationship with an operator. You can use this to create a branded experience that can distinguish your service from competitors’ services.

Design considerations include the following:

-   **Make data usage a combination of local and back-end information** To reduce the load on the back-end servers as much as possible, Windows provides a local Data Usage API that you can use to combine back-end data usage. You can periodically get the usage information from the back-end and correlate that with local data usage.

-   **Periodically update Windows with data usage** Windows 8 and Windows 8.1 is designed to behave intelligently on metered networks. This can save significant network capacity because Windows and Windows Store apps can use your mobile broadband network for essential traffic. To be more accurate and to include more information for applications (for example, data limits and usage), Windows relies on you to periodically provide correct information. Your app can set this information by using Data Usage APIs.

    ![account overview](images/mb-fig2-accountoverview.png)

## <span id="related_topics"></span>Related topics


[Mobile broadband app scenarios](mobile-broadband-app-scenarios.md)

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bp_mb\p_mb%5D:%20Account%20management%20%20RELEASE:%20%281/18/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")





