---
title: Mobile Plans Web Portal
description: This topic describes the implementation step for the Mobile Plans program.
keywords:
- Windows Mobile Plans Web Portal, Mobile Plans implementation mobile operators
ms.date: 03/25/2019
ms.localizationpriority: medium
---

# Mobile operator web portal

## Overview

This topic describes the web portal that enables mobile operators to provide connectivity solutions directly to Windows users through a curated web experience hosted in the Mobile Plans app. Mobile operators must create their web experiences following these design principles to ensure users have a high quality experience while navigating their portal. The mobile operator web portal is used for all scenarios supported in the Mobile Plans solution and is hence one of the most important components in the program.

For more information about web portal flow and reference design, see [Web portal flow and reference design](mobile-plans-appendix.md#web-portal-flow-and-reference-design).

## Web Portal interface for eSIM-enabled devices

The Mobile Plans app uses the [WebView](/uwp/api/Windows.UI.Xaml.Controls.WebView) control to host and present the mobile operator web portal experience. The portal is invoked by the app calling the mobile operator-hosted service endpoints directly, and returned content is rendered directly within the control

When starting the `WebView`, several parameters are passed to the portal as part of the invocation. If there is at least one eSIM profile associated with the mobile operator, the *iccids* are passed to the portal as well.

The following example shows these launch parameters for eSIM-enabled devices, embedded in the call to `MyWebView.Navigate()`.

```C#
MyWebView.ScriptNotify += MyWebView_ScriptNotify;

List<Uri> allowedUris = new List<Uri>();

allowedUris.AddRange(AllowedNotifyUris);

MyWebView.AllowedScriptNotifyUris = allowedUris;

MyWebView.Navigate(“https://moportal.com?market=US&location=US&transactionId=%2F7RBTuSJt02OZbX8.4&eid=89033023422130000000000199055797&imei=001102000315468&iccids=8988247000101867183,8988247000103824828”);
```

In order to provide backwards compatibility with app updates, the portal must disregard any additional parameters that might also be passed in the requst. This ensures flexibility and ability to introduce new features in the app without disrupting the mobile operator's integration.

The following table describes the launch parameters available for eSIM.

| Parameter name | Description | Example  |
| --- | --- | --- |
| eid            | The eSIM Identifier. This is sent only if an eSIM is present.                                                                                                                            | `eid= 89033024010400000100000000009136`          |
| iccids         | Optional parameter. Specifies the list of ICCIDs from the available profile on an eSIM only. If there are no ICCIDs matching the MO available on the eSIM, this parameter is not sent. | `iccids=8988247000100003319, 988247000100003555` |
| imei           | The device's IMEI number.                                                                                                                                                                | `imei=001201234567890`                           |
| location       | The user’s current physical location with country-level granularity.                                                                                                                    | `location=us`                                    |
| transactionId  | The Transaction ID used for debugging the session. Providers should log this and send it in the notification payload. Maximum size is 64 characters.                                     | `transactionId=waoigFfX00yGH3Vb.1`               |
| market         | The two-letter ISO code of the region settings in the PC.                                                                                                                                | `market=us`                                      |

The user’s language preference is sent using the Accept-Language header, described in the following table.

| Header name     | Description  | Example |
| --- | --- | --- |
| Accept-Language | The user’s current language settings. The MO portal should render the contents in the specified language if possible. For more information, see [RFC 7231, section 5.3.5: Accept-Language](https://tools.ietf.org/html/rfc7231#section-5.3.5). | `Accept-Language: en-us` |

## Web Portal interface for physical SIMs

The interface for invoking the mobile operator portal using legacy physical UICC is the same as for eSIM. However, the parameters passed to the portal are different.

```C#
MyWebView.Navigate(“https://moportal.com?iccid=8988247000100003319&imei=001102000311608&market=us&transactionId=waoigFfX00yGH3Vb.1&location=us”);
```
The following table describes the launch parameters available for a physical SIM.

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

To ensure the best user experience on Windows, mobile operators are encouraged to follow the policies and guidelines in this section when developing their web portal.

### Business functions

| Policy                                                                                                                                                                                                                                                                           | Required or Recommended |
| -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------- |
| The web portal experience must meet all applicable legal and regulatory requirements in the countries offered. Any content displayed in the web portal must comply with all applicable laws. | Required |
| Products offered through the web portal experience must be an offer for network connectivity. | Required |
| Network connectivity products offered through the web portal experience must include clear descriptions of the offering and terms. Any specific terms of service must be available for users to review from within the web portal experience. | Required |
| Customer support contact information must be accessible to users from within the web portal experience. | Required |
| The mobile operator's privacy policy must be available for users to review from within the web portal experience. | Required |
| The account management experience provided by the mobile operator must enable users to take actions on their current data plans, such as canceling a subscription. | Required |
| Users must receive an order confirmation after successfully completing a plan purchase or activation from within the web portal experience. | Recommended |

### Security

| Policy                                                                                                                                                                                                                                                                           | Required or Recommended |
| -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------- |
| The web portal experience must not deliver or install any 3rd party-owned or branded apps or modules. | Required |
| Before users exit the mobile operator’s web portal experience, users must be securely logged out from the web portal.  | Required |
| The portal URI and all requests or notifications sent to and from the web portal must use the secure HTTPS protocol. | Required |
| All web portal resources and references must use the secure HTTPS protocol. | Required |

### Advertising

| Policy                                                                                                                                                                                                                                                                           | Required or Recommended |
| -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------- |
| The web portal must not display, or make available for download, any advertisements, sponsored content, videos, sound files, animations, or otherwise large media files or images. | Required |

### Capabilities

| Policy                                                                                                                                                                                                                                                                           | Required or Recommended |
| -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------- |
| The required minimum functionality for the web portal experience is to enable a user to purchase a data plan using an account registered with the mobile operator. | Required |
| The web portal must start up promptly and remain responsive to user input until the user exits the web portal experience. | Required |
| Once invoked, the web portal must have and retain user focus until either: <ul><li>The activation flow has completed and the focus has been returned by the web portal back to the Mobile Plans app,</li></ul><p>OR</p><ul><li>The user has cancelled the flow and returned to the Mobile Plans app.</li></ul> | Required |
| The web portal must not display any pop-up windows, open any additional windows, or redirect the user to any other websites or apps, except as required to complete the activation flow. | Required |
| The web portal must handle all legitimate errors and exceptions, such as rejection of payment method, backend failure, etc. After the error or exception is handled, the web portal must remain responsive for users to exit and return to the Mobile Plans app. | Required |
| If users run into an error that can be fixed with user actions, it is recommended to display mobile operator customer support information with the error message. | Recommended |

### Usability

| Policy                                                                                                                                                                                                                                                                           | Required or Recommended |
| -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------- |
| The default frame size for the web portal is 800x600. Mobile operators should adopt responsive web design so that content on their web portal can be auto-adjusted to fit into the web control frame when users resize the Mobile Plans app for larger and smaller screens. | Required |
| Load times and data consumption for loading the web portal experience should be optimized. | Required |
| The web portal experience should be simple and easy navigate with necessary on-screen guidelines. | Required |
| User interface elements on the web portal should provide a cohesive experience integrated with the Mobile Plans app, not confusing users or reminding the users that this is an embedded web control. For example, there should be no close/max/min button within the web portal. | Required |
| Layout of pages within the web portal should be clean and easy to navigate. Users can navigate backward and forward through pages in the web portal with UI elements within the portal experience. For more information, see [Web portal flow and reference design](mobile-plans-appendix.md#web-portal-flow-and-reference-design). |Required |
| The web portal must be functional within the WebView Control frame and, once invoked, it must not interfere with users’ interaction with the Mobile Plans app at any time. | Required |
| The web portal must not be cluttered with too many images, banners, lengthy text, external links, etc. | Required |
| An on-screen cancel button within the web experience should be available for users to exit the flow when applicable. | Recommended |
| Mobile operators can choose the color scheme and fonts that best represent their brand. Care should be taken to ensure all visual elements work well together and reinforce the brand. | Recommended |

### Localization

| Policy                                                                                                                                                                                                                                                                           | Required or Recommended |
| -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------- |
| The web portal should be able to receive and understand users’ locale setting passed by the Mobile Plans app to display content in the user's preferred language. | Required |
| Mobile operators may localize their web portal in the languages they wish to support. | Recommended |
| The experience provided by the web portal should be reasonably similar in all languages that it supports, although data plan availability may vary from region to region. | Recommended |

### Accessibility

| Policy                                                                                                                                                                                                                                                                           | Required or Recommended |
| -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------- |
| The web portal should provide accessibility to disabled users and adhere to the accessibility guidelines applicable in the jurisdictions where the mobile operator provides service. | Recommended |
