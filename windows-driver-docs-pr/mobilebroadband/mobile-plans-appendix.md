---
title: Mobile Plans General Appendix
description: This topic describes appendix information for the Mobile Plans program.
keywords:
- Windows Mobile Plans appendix, Mobile Plans appendix mobile operators
ms.date: 07/05/2019
---

# Mobile Plans general appendix

## Web portal flow and reference design

This reference design is a template that you can alter to best represent your brand and products. This reference design shows the recommended UX design with navigation elements, branding locations, and website functionalities.

### MO Direct reference site walkthrough

1. The user clicks on the "Continue" button:

    <img src="images/dynamo_appendix_mo_direct_1_continue.png" alt="MO Direct walkthrough: user clicks on the continue button" title="MO Direct walkthrough: user clicks on the continue button" width="600" />

    - This dialog is prompted by Mobile Plans app.

2. The user enters the MO Direct portal and signs in with their MO account:

    <img src="images/dynamo_appendix_mo_direct_2_sign_in.png" alt="MO Direct walkthrough: user enters MO Direct portal and signs in with their MO account" title="MO Direct walkthrough: user enters MO Direct portal and signs in with their MO account" width="600" />

    - Page layout is consistent throughout all pages. For example, logo and branding elements are in top left, and navigation elements are on the bottom.
    - The sign-in page can link to signing up for a new account.
    - “Forgot password” is optional. Note that the user is in the Walled Garden, and only the Mobile Plans app can access the internet. If you want to support password reset through the MO Direct portal, make sure that users can reset it within two or three steps without launching a browser or email app on the device.

3. The user picks an option:

    <img src="images/dynamo_appendix_mo_direct_3_options.png" alt="MO Direct walkthrough: user picks an option" title="MO Direct walkthrough: user picks an option" width="600" />

    - Present the most important content, available services, at the center of the page.
    - Logo and branding elements are in the top left corner.
    - Navigation buttons are in the bottom right corner.
    - Use large tiles for available options, with a title and short description of the service category.
    - Both the “Next” and “Cancel” buttons are available for users to navigate forward or exit. The MO Direct expected data service categories might include prepaid plans, recurring monthly plans, and attaching a new device to an existing plan.

4. The user submits the order:

    <img src="images/dynamo_appendix_mo_direct_4_submit_order.png" alt="MO Direct walkthrough: user submits an order" title="MO Direct walkthrough: user submits an order" width="600" />

    - Page layout is consistent throughout all pages. For example, logo and branding elements are in top left, and navigation elements are on the bottom.
    - The Terms of Service link must be visible on the web page.
    - The order confirmation page lists key information for users to review before submitting the order, including details on data service, payment method, amount of payment, etc.

5. If the user cancels the MO Direct flow at any time:

    <img src="images/dynamo_appendix_mo_direct_5_cancel.png" alt="MO Direct walkthrough: user cancels MO Direct flow" title="MO Direct walkthrough: user cancels MO Direct flow" width="600" />

    - A confirmation dialog to leave the MO Direct experience is prompted by Mobile Plans app.

6. An order is completed:

    <img src="images/dynamo_appendix_mo_direct_6_order_complete.png" alt="MO Direct walkthrough: order complete" title="MO Direct walkthrough: order complete" width="600" />

    - This shows an example of transaction confirmation, which is part of the mobile operator portal.
    - Once the order is processed successfully and, in this case, after clicking “Continue,” the notification should be posted to the Mobile Plans app with the purchase result, eSIM activation code, and other information required in the API. The user will be automatically redirected to the Mobile Plans app PDP (product details page).
    - If the transaction is for a physical SIM card or the active eSIM profile is in place, you should be activating the plan in the backend.
    - If the transaction requires a new profile to be downloaded, move on to the next step.

7. Downloading an eSIM profile (if applicable):

    <img src="images/dynamo_appendix_mo_direct_7_downloading_esim_profile.png" alt="MO Direct walkthrough: downloading an eSIM profile (if applicable)" title="MO Direct walkthrough: downloading an eSIM profile (if applicable)" width="600" />

    - The eSIM profile is being downloaded.

8. The MO Direct plan is activated:

    <img src="images/dynamo_appendix_mo_direct_8_activated.png" alt="MO Direct walkthrough: MO Direct plan is activated" title="MO Direct walkthrough: MO Direct plan is activated" width="600" />

    - The device is connected.
    - The user has an active MO Direct account.

### Hyperlink experience

If there is a hyperlink pointing to a new page in your MO Direct portal and the user clicks on it, the web view control will render that page in the same window. Users must click on the back button in the Mobile Plans app to return to the previous page.

Alternatively, you might use a hyperlink to launch a dialog within the context of the WebView control.

### Back Button experience

The back button on the menu bar of the Mobile Plans app will navigate users to the previous page just like in a web browser. 

> [!IMPORTANT]
> Build your MO Direct portal as if you are building a shopping cart experience if you would like the user to return to the previous state without losing any data they had entered.

<img src="images/dynamo_appendix_mo_direct_9_back_button.png" alt="MO Direct walkthrough: back button example" title="MO Direct walkthrough: back button example" width="600" />

### Error while loading the MO Direct experience

When there are any unhandled errors or exceptions on the MO Direct portal that cause the Mobile Plans app to fail to load the MO Direct experience, the following error is displayed:

<img src="images/dynamo_appendix_mo_direct_10_error.png" alt="MO Direct walkthrough: error example" title="MO Direct walkthrough: error example" width="600" />

## High level integration schedule

The following table provides a high-level overview of the *Mobile Plans* project integration schedule.

| Phase | Activities | Owner | Time estimate |
| --- | --- | --- | --- |
| Implementation | eSIM profile installable on a Windows device. Test using SMDP+ used for Staging Environment and Production Environment. | MO |  |
|                | Provide the onboarding checklist document, including Staging Environment service configuration | MO |  |
|                | Enable the mobile operator Staging Environment in the *Mobile Plans* Staging Environment | MSFT | Configuration updates occur on the 1st and 3rd Friday of every month |
|                | Submit COSA database update | MO | About 3 months |
|                | MO Direct portal development start |  |
|                | `GetBalance` API development start |  |
| Integration | Enable Walled Garden | MO |  |
|             | Validate COSA update | MO |  |
|             | MO Direct portal development complete | MO |  |
|             | `GetBalance` API development complete | MO |  |
|             | MO development complete - code complete (checkpoint) | MO |  |
|             | Validate `GetBalance` API functionality | MO |  |
|             | End-to-end experience is functional in MO Staging Environment (checkpoint) | MO |  |
|             | Update Service Configuration document to reflect Production Environment settings (if not provided previously) | MO |  |
|             | Provide ICCIDs to be used for `GetBalance` load test | MO |  |
|             | Enable mobile operator Production Environment environment in *Mobile Plans* Staging Environment | MSFT | Configuration updates occur on the 1st and 3rd Friday of every month |
|             | End-to-end experience is functional in MO Production Environment (checkpoint) | MO |  |
| Validaton | Exit criteria test cases complete | MO |  |
|           | Verify test case results | MSFT |  |
|           | Test sign-off (checkpoint) | MSFT |  |
| Rollout | `GetBalance` API load test | MSFT and MO | 1 week |
|         | Monitoring and escalation paths in place | MSFT | 1 week |
|         | Customer support in place | MSFT and MO |  |
|         | Commercial agreement completed | MO |  |
|         | COSA update available in Windows | MSFT |  |
|         | Go/No-Go (final checkpoint) | MSFT and MO |  |
|         | Configure MO Production Environment environment in *Mobile Plans* Production Environment | MSFT |  |
|         | Launch | MSFT and MO | Launch date and time must be agreed upon to ensure that local validation happens |
