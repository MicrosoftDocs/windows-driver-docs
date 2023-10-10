---
title: Design billing pages in a mobile broadband app
description: Design billing pages in a mobile broadband app
ms.date: 10/05/2023
---

# Design billing pages in a mobile broadband app

You should provide the user with the ability to view a billing summary, billing history, make payments, or recharge the plan.

:::image type="content" source="images/mb-fig1-viewbillpage.png" alt-text="Screenshot of the view bill page in a mobile broadband app.":::

The **Make a payment** form should adhere to form guidelines that are described in [Design purchase flows in a mobile broadband app](design-purchase-flows-in-a-mobile-broadband-app.md). This page can be linked to from the **Billing** page for post-paid plans, and through the **Recharge now** button on the landing page for prepaid plans.

:::image type="content" source="images/mb-fig2-makepaymentform.png" alt-text="Screenshot of the make payment form in a mobile broadband app.":::

## Quick summary

Appropriate design for the billing page:

- Follow the form guidelines, including left alignment, white space, proper grid alignment, and touch friendliness.

- Use a simple layout to improve readability.

- Use vertical scrolling for long forms because this makes it easier to tab and to use the online keyboard.

- Make the making payments process a simple experience.

Inappropriate design for the billing page:

- Don’t try to fill up white space.

- Don’t use an iframe to host the flows. Instead, build flows directly into the app experience.

- Don’t make the user wait long times without providing visual feedback.

- Don’t link to external sites outside of the app.

## Additional resources

- For more information about views and layouts: see [Choosing a layout](/previous-versions/windows/apps/hh465327(v=win.10)).

- For more information about Listviews, see [Quickstart: Adding a ListView](/previous-versions/windows/apps/hh465496(v=win.10)).

- For design guidance for error handling, see [Laying out your UI](/previous-versions/windows/apps/hh465304(v=win.10)).

- For accessibility guidance, see [Accessibility in UWP apps using C++, C#, or Visual Basic](/previous-versions/windows/apps/hh452680(v=win.10)).

- For more information about how to use built-in controls, see [Adding controls and content](/previous-versions/windows/apps/hh465393(v=win.10)).

- For touch input guidelines, see [Quickstart: Touch input](/previous-versions/windows/apps/hh465387(v=win.10)).

## Related topics

[Designing the user experience of a mobile broadband app](designing-the-user-experience-of-a-mobile-broadband-app.md)
