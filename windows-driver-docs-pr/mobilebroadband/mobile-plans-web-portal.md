---
title: Mobile Plans Web Portal
description: This topic describes the implementation step for the Mobile Plans program.
ms.assetid: 283E45EF-D421-429B-A9AF-BED64BB670B0
keywords:
- Windows Mobile Plans Web Portal, Mobile Plans implementation mobile operators
ms.date: 03/15/2019
ms.localizationpriority: medium
---

# Mobile Plans Mobile Operator Web Portal

## Overview

This topic describes the mobile mobile operator web service API/portal that enables mobile operators to provide connectivity solutions directly to Windows users through a curated web experience hosted in the Mobile Plans app. You need to create your web experiences following design policies and implement the web service API to make it reachable. This portal will be used for all scenarios supported in the Mobile Plans solution.

For more info about Web portal flow and reference design, see [Web portal flow and reference design](mobile-plans-appendix.md#web-portal-flow-and-reference-design).

## Web Service API used for eSIM

The Mobile Plans app uses the [WebView](https://docs.microsoft.com/uwp/api/Windows.UI.Xaml.Controls.WebView) control to host the MO Direct experience. The app only trusts content returned by the *Mobile Plans* service.

When starting the WebView, the *eid*, *market*, *location*, *imei*, and *transactionId* parameters are passed to the MO web portal. If there is at least an eSIM profile matching the Mobile Operator, which Mobile Plans is reaching, the *iccids* are passed to the portal as well.

The following example shows these launch parameters for eSIM, embedded in the call to `MyWebView.Navigate()`.

```c#
MyWebView.ScriptNotify += MyWebView_ScriptNotify;

List<Uri> allowedUris = new List<Uri>();

allowedUris.AddRange(AllowedNotifyUris);

MyWebView.AllowedScriptNotifyUris = allowedUris;

MyWebView.Navigate(“https://moportal.com?market=US&location=US&transactionId=%2F7RBTuSJt02OZbX8.4&eid=89033023422130000000000199055797&imei=001102000315468&iccids=8988247000101867183,8988247000103824828”);
```

The Web Service API must disregard any additional parameters it might receive from the Mobile Plans app. This provides flexibility for introducing new features without breaking the *Mobile Plans* experience. Please check the documentation frequently to learn about new features.

The following table describes the launch parameters available for eSIM.

| Parameter name | Description                                                                                                                                                                              | Example                                          |
| -------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------ |
| eid            | The eSIM Identifier. This is sent only if an eSIM is present.                                                                                                                            | `eid= 89033024010400000100000000009136`          |
| iccids         | Optional parameter. Specifies the list of ICCIDs from the available profile on an eSIM only. If there are no ICCID’s matching the MO available on the eSIM, this parameter is not sent. | `iccids=8988247000100003319, 988247000100003555` |
| imei           | The device's IMEI number.                                                                                                                                                                | `imei=001201234567890`                           |
| location       | The user’s current physical location with country-level granularity.                                                                                                                    | `location=us`                                    |
| transactionId  | The Transaction ID used for debugging the session. Providers should log this and send it in the notification payload. Maximum size is 64 characters.                                     | `transactionId=waoigFfX00yGH3Vb.1`               |
| market         | The two-letter ISO code of the region settings in the PC.                                                                                                                                | `market=us`                                      |

The user’s language preference is sent using the Accept-Language header, described in the following table.

| Header name     | Description                                                                                                                                                                                                                                     | Example                  |
| --------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------ |
| Accept-Language | The user’s current language settings. The MO portal should render the contents in the specified language if possible. For more information, see [RFC 7231, section 5.3.5: Accept-Language](https://tools.ietf.org/html/rfc7231#section-5.3.5). | `Accept-Language: en-us` |

## Web Service API used for Physical SIM

The mobile operator portal for physical and eSIM is the same, the difference is which parameters are passed to the portal, the parameters passed are : *market*, *location*, *imei*, *iccid*, and *transactionId*.

```c#
MyWebView.Navigate(“https://moportal.com?iccid=8988247000100003319&imei=001102000311608&market=us&transactionId=waoigFfX00yGH3Vb.1&location=us”);
```

The Web Service API must disregard any additional parameters it might receive from the Mobile Plans app. This provides flexibility for introducing new features without breaking the *Mobile Plans* experience. Please check the documentation frequently to learn about new features.

The following table describes the launch parameters available for Physical SIM.

| Parameter name | Description                                                                                                                                                                              | Example                                          |
| -------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------ |
| iccid          | Required parameter for a physical SIM. Specifies the ICCID on the physical sim.                                                                                                          | `iccid=8988247000100003319`                      |
| imei           | The device's IMEI number.                                                                                                                                                                | `imei=001201234567890`                           |
| location       | The user’s current physical location with country-level granularity.                                                                                                                    | `location=us`                                    |
| transactionId  | The Transaction ID used for debugging the session. Providers should log this and send it in the notification payload. Maximum size is 64 characters.                                     | `transactionId=waoigFfX00yGH3Vb.1`               |
| market         | The two-letter ISO code of the region settings in the PC.                                                                                                                                | `market=us`                                      |

The user’s language preference is sent using the Accept-Language header, described in the following table.

| Header name     | Description                                                                                                                                                                                                                                     | Example                  |
| --------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------ |
| Accept-Language | The user’s current language settings. The MO portal should render the contents in the specified language if possible. For more information, see [RFC 7231, section 5.3.5: Accept-Language](https://tools.ietf.org/html/rfc7231#section-5.3.5). | `Accept-Language: en-us` |

## Web portal design policies

To ensure the best user experience on Windows, you should adhere to the policies in this section when developing the MO Direct experience. These policies are supplementary to the terms and conditions of the *Mobile Plans* Partner Addendum, [Windows App Developer Agreement](https://msdn.microsoft.com/library/windows/apps/hh694058) and [Microsoft Store Policies](https://msdn.microsoft.com/library/windows/apps/dn764944).

### Business functions

| Policy                                                                                                                                                                                                                                                                           | Required or Recommended |
| -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------- |
| The MO Direct experience must meet all applicable legal and regulatory requirements in the countries offered. Any content displayed in the MO Direct portal must comply with all applicable laws.                                                                                | Required                |
| Products offered through the MO Direct experience must be an offer for network connectivity.                                                                                                                                                                                     | Required                |
| Network connectivity products offered through the MO Direct experience must be immediately activated after user completes the purchase flow.                                                                                                                                     | Required                |
| Network connectivity products offered through the MO Direct experience must have clear information on service details. Any specific terms of service must be available for users to review before purchase in the MO Direct experience.                                          | Required                |
| Customer support contact information must be accessible to users in the MO Direct experience.                                                                                                                                                                                    | Required                |
| The privacy policy must be available for users to review in the MO Direct experience.                                                                                                                                                                                            | Required                |
| The account management experience provided by an MO, which can be within the MO Direct experience, a separate and dedicated account management portal, or a dedicated MO app, should enable users to take actions on their current data plans, such as canceling a subscription. | Required                |
| Users will receive an order confirmation after purchasing a data plan from the MO Direct experience successfully.                                                                                                                                                                | Recommended             |

### Security

| Policy                                                                                                                               | Required or Recommended |
| ------------------------------------------------------------------------------------------------------------------------------------ | ----------------------- |
| The MO Direct experience must not deliver or install any 3rd party-owned or branded apps or modules.                                 | Required                |
| Before users exit the MO Direct experience, users must be securely logged out from the MO Direct portal.                             | Required                |
| The MO Direct portal URI and all requests or notifications sent to and from the MO Direct portal must use the secure HTTPS protocol. | Required                |
| All MO portal resources and references must use the secure HTTPS protocol.                                                           | Required                |

### Advertising

| Policy                                                                                                                  | Required or Recommended |
| ----------------------------------------------------------------------------------------------------------------------- | ----------------------- |
| The MO Direct portal must not display any advertisements, sponsored content, videos, large images, animations, or maps. | Required                |

### Capabilities

| Policy                                                                                                                                                                                                                                                                                    | Required or Recommended |
| ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------- |
| The required minimum functionality for the MO Direct experience is to enable a user to purchase a data plan with an account registered with a mobile operator.                                                                                                                            | Required                |
| The MO Direct portal must start up promptly and remain responsive to user input until the user exits the MO Direct experience.                                                                                                                                                            | Required                |
| Once invoked, the MO Direct portal must have and retain user focus until either: <ul><li>The MO Direct flow has completed and the focus has been returned by Mobile Operator back to the Mobile Plans app,</li></ul><p>OR</p><ul><li>The user has cancelled the MO Direct flow.</li></ul> | Required                |
| The MO Direct portal must not display any pop-up windows, open any additional windows, or redirect the user to any other websites or apps, except as required to complete the purchase flow.                                                                                              | Required                |
| The MO Direct portal must handle all legitimate errors and exceptions, such as rejection of payment method, backend failure etc. After the error or exception is handled, the MO Direct portal must remain responsive for users to exit and return to the Microsoft Store.                | Required                |
| If users run into an error that can be fixed with user actions, it is recommended to display mobile operator customer support information with the error message.                                                                                                                         | Recommended             |

### Usability

| Policy                                                                                                                                                                                                                                                                                                                                      | Required or Recommended |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------- |
| The default frame size for the MO Direct portal is 800x600. Adopt responsive web design so that content on the MO Direct portal can be auto-adjusted to fit into the web control frame when users resize the Mobile Plans app.                                                                                                              | Required                |
| Load times and data consumption for loading the MO Direct experience should be optimized.                                                                                                                                                                                                                                                   | Required                |
| The MO Direct experience should be simple and easy navigate with necessary on-screen guidelines.                                                                                                                                                                                                                                            | Required                |
| UI elements on the MO Direct portal should provide a cohesive experience integrated with the Mobile Plans app, not confusing users or reminding the users that this is an embedded web control. For example, there should be no close/max/min button within the MO Direct portal.                                                           | Required                |
| Layout of web pages in the MO Direct portal should be clean and easy to navigate. Users can navigate backward and forward through web pages in the MO Direct portal with UI elements within MO Direct experience. For more info, see [Web portal flow and reference design](mobile-plans-appendix.md#web-portal-flow-and-reference-design). | Required                |
| The MO Direct portal must be functional within the Web Control frame and, once invoked, it must not interfere with users’ interaction with the Mobile Plans app at any time.                                                                                                                                                               | Required                |
| The MO Direct portal must not be cluttered with too many images, banners, lengthy text, external links, etc.                                                                                                                                                                                                                                | Required                |
| An on-screen cancel button within the MO Direct experience should be available for users to exit the flow when applicable.                                                                                                                                                                                                                  | Recommended             |
| Mobile operators can choose the color scheme and fonts that represents the brand the best. Ensure that all visual elements work well together and reinforce the brand.                                                                                                                                                                      | Recommended             |

### Localization

| Policy                                                                                                                                                                          | Required or Recommended |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------- |
| The MO Direct portal should be able to receive and understand users’ locale setting passed by the Mobile Plans service to display content in the proper language.              | Required                |
| Mobile operators may localize the MO Direct portal in the languages they want to support.                                                                                       | Recommended             |
| The experience provided by the MO Direct portal should be reasonably similar in all languages that it supports, although data plan availability can vary from region to region. | Recommended             |

### Accessibility

| Policy                                                                                                                                                                                                                    | Required or Recommended |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------- |
| The MO Direct portal should provide accessibility to disabled users and adhere to the accessibility guidelines applicable in the jurisdictions where the mobile operator implements and enables the MO Direct experience. | Recommended             |
