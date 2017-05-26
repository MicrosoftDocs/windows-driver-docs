---
title: Designing the user experience of a mobile broadband app
description: Designing the user experience of a mobile broadband app
ms.assetid: c84e2814-69ba-4cd0-ba11-1b035ccdfbde
ms.author: windowsdriverdev
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Designing the user experience of a mobile broadband app


This topic provides information about how to design Windows Store mobile broadband apps for Windows 8, Windows 8.1, and Windows 10. It provides user experience design guidelines to design apps for users to manage their mobile broadband account and service. It assumes you familiar with mobile broadband technology, Windows mobile broadband networking, and the Windows Store app platform.

The following sections are available in this topic:

-   [Key scenarios](#keyui)

-   [App organization](#apporg)

-   [Additional resources](#resources)

## <span id="keyui"></span><span id="KEYUI"></span>Key scenarios


The mobile broadband app should include the following key scenarios:

-   **Plan purchase**

    -   Purchase a new subscription to data service.

    -   Refill account balance to a plan.

-   **Account management** Displays account data and current plan information.

-   **View data usage**

    -   Display current data usage and billing cycle information.

    -   Update Windows with the latest data usage.

-   **Notifications** Display data usage and other important account and service messages.

-   **Help and Support** Display troubleshooting and customer support contact information.

## <span id="apporg"></span><span id="APPORG"></span>App organization


The following shows how different pages in the app can be organized:

![overview](images/mb-fig1-overview-windows-store-device-app.png)

-   The app has an account overview landing page that provides a summary of a customer’s account and data usage. It also contains links to other app pages.

-   From the landing page, end users can visit a hub page to view billing, plans, services, or help and support details.

-   Some hub pages lead to task pages and flows, such as a purchase checkout flow.

**Tip**  
For prepaid plans, the account overview could directly link to a **Make a Payment** page for refill scenarios.

 

For more information about how to design these pages, see the following topics:

-   [Design the landing page of a mobile broadband app](design-the-landing-page-of-a-mobile-broadband-app.md)

-   [Design branding in a mobile broadband app](design-branding-in-a-mobile-broadband-app.md)

-   [Design account balance and usage info in a mobile broadband app](design-account-balance-and-usage-info-in-a-mobile-broadband-app.md)

-   [Design messages in a mobile broadband app](design-messages-in-a-mobile-broadband-app.md)

-   [Design billing pages in a mobile broadband app](design-billing-pages-in-a-mobile-broadband-app.md)

-   [Design purchase flows in a mobile broadband app](design-purchase-flows-in-a-mobile-broadband-app.md)

-   [Design help and support pages in a mobile broadband app](design-help-and-support-pages-in-a-mobile-broadband-app.md)

-   [Design services and goods pages in a mobile broadband app](design-services-and-goods-pages-in-a-mobile-broadband-app.md)

-   [Integrate a mobile broadband app with other Windows components](integrate-a-mobile-broadband-app-with-other-windows-components.md)

## <span id="resources"></span><span id="RESOURCES"></span>Additional resources


-   [Index of UX guidelines for Windows Store apps](https://msdn.microsoft.com/library/windows/apps/hh465424)

-   [Overview of mobile broadband](overview-of-mobile-broadband.md)

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bp_mb\p_mb%5D:%20Designing%20the%20user%20experience%20of%20a%20mobile%20broadband%20app%20%20RELEASE:%20%281/18/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




