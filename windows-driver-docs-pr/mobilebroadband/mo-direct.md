---
title: MO Direct
description: Data Marketplace enables your mobile brand and pay-as-you-go connectivity offerings on Windows 10 devices.
author: mattwojo
ms.author: mattwoj
ms.date: 09/01/2017
keywords: 
---

# MO Direct

Mobile Operator Direct (MO Direct) is a program that lets mobile operators sell data plans directly to Windows customers through a web experience embedded in the Paid Wi-Fi &amp; Cellular app. Customers will enjoy a native Windows experience while skipping the hassle of navigating to another website for buying data plans. And they can connect to the Internet using an existing account registered with mobile operators.

To onboard to MO Direct, you need to:

1. Go through the [Network onboarding](network-onboarding.md) steps.
2. Build a self-contained, curated HTML experience that complies to [MO Direct policies](##mo-direct-policies).
3. [Send MO Direct onboarding information](###required-information) to the Data Marketplace team.
4. Integrate with Data Marketplace for [MO Direct APIs](mo-direct-api.md).

## MO Direct policies

These are policies that you should adhere to when developing MO Direct experience. We publish these policies to ensure the best customer experience on Windows. These policies are supplementary to the terms and conditions of Data Marketplace Partner Addendum, Windows [App Developer Agreement](https://msdn.microsoft.com/en-us/library/windows/apps/hh694058.aspx) and [Windows Store Policies](https://msdn.microsoft.com/en-us/library/windows/apps/dn764944.aspx).

### Business functions

| MO Direct experience must meet all applicable legal and regulatory requirements in the countries offered. Any content displayed in the MO Direct portal must comply with all applicable laws. | Required |
| --- | --- |
| Products offered through MO Direct experience must be an offer for network connectivity. | Required |
| Network connectivity products offered through MO Direct experience must be immediately activated after customer completes purchase flow. | Required |
| Network connectivity products offered through MO Direct experience must have clear information on service details. Any specific terms of service must be available for customer to review before purchase in MO Direct experience. | Required |
| When a customer has active Windows Store PAYG balance from a provide for a country, if this customer purchases additional data plans through MO Direct experience from the same provider for the same country, the remaining balance for Windows Store PAYG plan must be merged to the new data plan from MO Direct or be forfeited. This plan changing rule must be presented to the customer visually before customer confirms the purchase in MO Direct experience. At any time, customer must not have a balance from Windows Store PAYG and a balance from MO Direct simultaneously. | Required |
| Customer will get an order confirmation after purchasing a data plan from MO Direct experience successfully. | Required |
| Customer support contact must be accessible to customer in MO Direct experience. | Required |
| Privacy policy must be available for customers to review in MO Direct experience. | Required |
| Account management experience provided by MO, which can be within MO Direct experience, a separate and dedicated account management 
portal, or a dedicated MO App, should enable customers to take actions on their current data plans, such as cancel subscription. | Required |
| For Purchase Intent Connectivity, Mobile Operator can decide the data and time limit. The recommended size allowed is 5MB and time allowed is 1 hour with restricted Internet Access via client policy rules (Walled Garden). | Recommended |

### Security

| MO Direct experience must not deliver or install any third-party owned or branded apps or modules. | Required |
| --- | --- |
| Before customers exit MO Direct experience, customers must be securely logged out from MO Direct portal. | Required |
| MO Direct portal URI and all requests / notifications sent from MO Direct portal must use secure HTTPS protocol. | Required |

### Advertising

| The MO Direct portal must not display any advertisements, sponsored content, videos, large images, animations, or maps. | Required |
| --- | --- |

### Capabilities

| The required minimum functionality for MO Direct experience is to enable a customer to purchase a data plan with an account registered with Mobile Operator. | Required |
| --- | --- |
| When building MO Direct experience, Mobile Operator must adhere to the guidelines and requirements as described in [MO Direct API](mo-direct-api.md) documentation. | Required |
| The MO Direct portal must start up promptly and remain responsive to customer input until customer exits MO Direct experience. | Required |
| Once invoked, the MO Direct portal must have and retain customer focus until either the MO Direct flow has completed, and the focus has been returned by Mobile Operator back to the Paid Wi-Fi &amp; Cellular app OR the customer has cancelled the MO Direct flow. | Required |
| The MO Direct portal must not display any pop-up windows, open any additional windows, or redirect the customer to any other websites or apps, except as required to complete the purchase flow. With Walled Garden firewall rules, only Paid Wi-Fi &amp; Cellular app can access Internet either for zero-rated endpoints or using microbalance. | Required |
| The MO Direct portal must handle all legitimate errors and exceptions, such as rejection on payment method, backend failure etc. After the error or exception is handled, the MO Direct portal must remain responsive for customer to exit and return to the Store. | Required |
| If customer runs into an error that can be fixed with customer actions, it is recommended to display Mobile Operator customer support information with the error message. | Recommended |

### Usability

| The default frame size for the MO Direct portal is 800x600. Adopt responsive web design so that content on the MO Direct portal can be auto-adjusted to fit into the web control frame when customer resize the Paid Wi-Fi &amp; Cellular app. | Required |
| --- | --- |
| Load times and data consumption for loading MO Direct experience should be optimized, so that it does not exhaust Purchase Intent Connectivity data before the customer completes the transaction. | Required |
| MO Direct experience should be simple and easy to go through with necessary on-screen guidelines. | Required |
| UI elements on the MO Direct portal should provide a cohesive experience integrated with the Paid Wi-Fi &amp; Cellular app, not confusing customers or reminding the customers that this is an embedded web control. For example, there should be no close/max/min button within the MO Direct portal. | Required |
| Layout of web pages in the MO Direct portal should be clean and easy to navigate. Customers can navigate backward and forward through web pages in the MO Direct portal with UI elements within MO Direct experience. | Required |
| MO Direct portal must be functional within the Web Control frame and once invoked, it must not interfere customer&#39;s interaction with the Paid Wi-Fi and Cellular app at any time. | Required |
| The MO Direct portal must not be cluttered with too many images, banners, lengthy text, external links and so on. | Required |
| On-screen cancel button within MO Direct experience should be available for customer to exit the flow when it&#39;s applicable. | Recommended |
| Mobile Operator can choose the color scheme and fonts that represents the brand the best. Ensure that all visual elements work well together and reinforce the brand. | Recommended |

### Localization

| The MO Direct portal should be able to receive and understand customer&#39;s locale setting passed by Data Marketplace service to display content in proper language. | Required |
| --- | --- |
| Mobile Operator may localize the MO Direct portal in the languages they want to support. | Recommended |
| The experience provided by the MO Direct portal should be reasonable similar in all languages that it supports, although data plans availability can vary from region to region. | Recommended |

### Accessibility

| The MO Direct portal should provide accessibility to disabled customers, adhere to the accessibility guidelines applicable in the jurisdictions where Mobile Operator implements and enables MO Direct experience. | Recommended |
| --- | --- |

## Build the MO Direct experience

Paid Wi-Fi &amp; Cellular app hosts your MO Direct experience using the Windows **WebView** class. To understand how it works, review the [WebView Class](https://docs.microsoft.com/en-us/uwp/api/Windows.UI.Xaml.Controls.WebView) documentation.

To integrate your MO Direct web experience with Data Marketplace, see [MO Direct API](mo-direct-api.md).

## Direct onboarding process

This section provides a checklist for necessary onboarding steps to launch your MO Direct experience with Data Marketplace.

### Inquiry

- Obtain the latest version of Data Marketplace SDK for Cell Partners, as well as any additional resources for onboarding to MO Direct.
- Resolve open business and technical questions on MO Direct implementation.

### Required information

Please provide the following information:

> [!NOTE]
> Note if you have gone through the [Network onboarding](network-onboarding.md) steps, you don&#39;t need to go through them again. 

- Submit COSA database. Ensure Account Experience URL is included in your COSA database submission, for either a web portal or a dedicated Windows app for customer to manage account.
- If you haven't done so already, go through the [Network onboarding](network-onboarding.md) steps. Additionally, send a list of countries where your MO Direct experience will be available, and the MO Direct portal URL and notification URL in email to [datamartpartnersup@microsoft.com](mailto:swifipartnersup@microsoft.com).

### Design and build the MO Direct portal

- Provide a draft design of your MO Direct portal to review by Microsoft.
- Once you and Microsoft agree on the design, you can move forward with implementation.

### Integration

- Implement MO APIs, including [MO Direct APIs](mo-direct-api.md).
- Test and validate API integration together with Data Marketplace team. You may need to provide a test SIM and a test account for Data Marketplace team to test your MO Direct experience.

### Pre-release review

- Perform a final review and approval with the Data Marketplace team.
- Ensure all shareholders are notified and ready to go live.

### Launch

- Your MO Direct experience goes live!
- Ensure MO Direct experience is maintained as needed to remain in compliance with MO Direct policies.
