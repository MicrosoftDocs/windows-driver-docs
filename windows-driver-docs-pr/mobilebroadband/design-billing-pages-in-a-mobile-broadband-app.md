---
title: Design billing pages in a mobile broadband app
description: Design billing pages in a mobile broadband app
MSHAttr:
- 'PreferredSiteName:MSDN'
- 'PreferredLib:/library/windows/hardware'
ms.assetid: 44c5a273-1dd4-4ff5-90aa-9d1f4f855439
---

# Design billing pages in a mobile broadband app


You should provide the user with the ability to view a billing summary, billing history, make payments, or recharge the plan.

![view bill page](images/mb-fig1-viewbillpage.png)

The **Make a payment** form should adhere to form guidelines that are described in [Design purchase flows in a mobile broadband app](design-purchase-flows-in-a-mobile-broadband-app.md). This page can be linked to from the **Billing** page for post-paid plans, and through the **Recharge now** button on the landing page for prepaid plans.

![make payment form](images/mb-fig2-makepaymentform.png)

## <span id="Quick_summary"></span><span id="quick_summary"></span><span id="QUICK_SUMMARY"></span>Quick summary


Appropriate design for the billing page:

-   Follow the form guidelines, including left alignment, white space, proper grid alignment, and touch friendliness.

-   Use a simple layout to improve readability.

-   Use vertical scrolling for long forms because this makes it easier to tab and to use the online keyboard.

-   Make the making payments process a simple experience.

Inappropriate design for the billing page:

-   Don’t try to fill up white space.

-   Don’t use an iframe to host the flows. Instead, build flows directly into the app experience.

-   Don’t make the user wait long times without providing visual feedback.

-   Don’t link to external sites outside of the app.

## <span id="Additional_resources"></span><span id="additional_resources"></span><span id="ADDITIONAL_RESOURCES"></span>Additional resources


-   For more information about views and layouts: see [Choosing a layout](https://msdn.microsoft.com/library/windows/apps/hh465327).

-   For more information about Listviews, see [Quickstart: Adding a ListView](https://msdn.microsoft.com/library/windows/apps/hh465496).

-   For design guidance for error handling, see [Laying out your UI](https://msdn.microsoft.com/library/windows/apps/hh465304).

-   For accessibility guidance, see [Accessibility in Windows Store apps using C++, C#, or Visual Basic](https://msdn.microsoft.com/library/windows/apps/hh452680).

-   For more information about how to use built-in controls, see [Adding controls and content](https://msdn.microsoft.com/library/windows/apps/hh465393).

-   For touch input guidelines, see [Quickstart: Touch input](https://msdn.microsoft.com/library/windows/apps/xaml/hh465387).

## <span id="related_topics"></span>Related topics


[Designing the user experience of a mobile broadband app](designing-the-user-experience-of-a-mobile-broadband-app.md)

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bp_mb\p_mb%5D:%20Design%20billing%20pages%20in%20a%20mobile%20broadband%20app%20%20RELEASE:%20%281/18/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")





