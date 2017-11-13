---
title: Pay-As-You-Go onboarding steps
description: 
author: mattwojo
ms.author: mattwoj
ms.date: 09/01/2017
keywords: 
---

# Network onboarding for Data Marketplace

The Data Marketplace experience is comprised of two user interfaces: the [Windows Connection Manager (a.k.a. the flyout)](#windows-connection-manager) and the [Paid Wi-Fi and Cellular app](#paid-wi-fi-and-cellular-app).

## Windows Connection Manager

Windows Connection Manager (a.k.a. the flyout) refers to the flyout window that launches when you click on the network interface icon, displaying all available network connections. This is the entry point for Data Marketplace purchase flow if available. 

![Windows Connection Manager icon](images/windowsconnectionmanager.png)
![Windows Connection Manager flyout window](images/windowsconnectionmanager2.png)

Tapping on the **Contoso Cellular** connection will expand it with more options. With the **Contoso Cellular** connection expanded, if the provider is Data Marketplace onboarded, a **Connect with a data plan** option will be displayed. Clicking on this option will launch the [Paid Wi-Fi and Cellular app](/paid-wi-fi-and-cellular-app).

![Windows Connection Manager flyout window expanded connection option](images/windowsconnectionmanager3.png)

In order to have this **Connect with a data plan** option available, you must [submit your COSA database](//msdn.microsoft.com/en-us/library/windows/hardware/dn973149.aspx). 

The following table compares the UX based on an operator’s information submitted in COSA database.

| Configuration | UX | Notes |
| ------- | -------- | --------- |
| SIM profile not in COSA range | Customer must manually input the APN for Windows to connect to Operator’s network. | -- |
| SIM profile onboarded in COSA range with ‘Data Marketplace Supported = No’ | Collapsed, Disconnected: ![Collapsed and disconnected window](images/cosa_range1.png) | 1. No remaining balance will be displayed in the flyout for profiles not supporting Data Marketplace. |
| SIM profile onboarded in COSA range with ‘Data Marketplace Supported = No’ | Collapsed, Connected: ![Collapsed and connected window](images/cosa_range2.png) | 2.	No option to launche Paid Wi-Fi & Cellular app from the flyout. |
| SIM profile onboarded in COSA range with ‘Data Marketplace Supported = No’ | Expanded, Connected: ![Expanded and connected window](images/cosa_range3.png) | 3. Customer can launch Paid Wi-Fi & Cellular app from Windows start menu. If the device is eSIM capable (either with embedded or inserted reprogrammable eUICC) and the device is connected to internet, customer can choose from a list of Data Marketplace onboarded providers and purchase from them. |
| SIM profile onboarded in COSA range with ‘Data Marketplace Supported = Yes’ | Collapsed, disconnected, has balance: ![Collapsed, disconnected with balance window](images/cosa_range4.png)| 1. Balance will be retrieved through Get Balance API and displayed in the flyout.|
| SIM profile onboarded in COSA range with ‘Data Marketplace Supported = Yes’ | Collapsed, disconnected, no balance: ![Collapsed, disconnected, no balance window](images/cosa_range5.png) | 2.	When Operator returns no balance, ‘Connect with a data plan’ option is displayed in the flyout. This option launches the Paid Wi-Fi & Cellular app.|
| SIM profile onboarded in COSA range with ‘Data Marketplace Supported = Yes’ | Expanded, connected, has balance: ![Expanded, connected with balance window](images/cosa_range6.png)| |
| SIM profile onboarded in COSA range with ‘Data Marketplace Supported = Yes’ | Expanded, connected, no balance: ![Expanded, connected with no balance window](images/cosa_range7.png)| | 

## Paid Wi-Fi and Cellular app 

The Paid Wi-Fi and Cellular (PWC) app is where customer engages in the purchase flow.


## COSA database submission
This section will discuss the process and implication of having COSA database submitted.

> [!IMPORTANT]
> Starting in Windows 10, version 1703, the APN database is replaced by a new format called COSA. Windows 8, Windows 8.1, and versions of Windows 10 before version 1703 will continue to use the APN database, while Windows 10, version 1703 and later use COSA. For a list of frequently asked questions about COSA, see [COSA FAQ](//docs.microsoft.com/en-us/windows-hardware/drivers/mobilebroadband/cosa---faq).

Get the latest COSA database template from your Data Marketplace partner. 

The following are the required COSA fields for onboarding to Data Marketplace:
- UpdateType
- Country/Region
- Operator
- GSM Provider Name
- MCC
- MNC
- SIM ICCID Range
- Access String
- AlwaysOn
- DataMarketplace Support (must be set to **Yes**)

These additional fields are recommended if you are onboarding to Mobile Operator (MO) Direct:
- Account Experience URL
- (OR) MO App

When you onboard with either an Account Experience URL or an MO App, a customer with an active MO Direct account from your service will see the View my account link in the flyout (see the image below), which launches the MO App or the Account Experience URL in a browser. 

![View my account flyout window](images/view_my_account.png)

![Alt Text](images/imagename.png)

The following fields are highly recommended as they determine the branding assets displayed in the Windows Connection Manager:

- Branding Name
- Branding Icon
- Use Branding On Roaming

![Windows Connection Manager with branding](images/images.png)

In the image above, &quot;Contoso Cellular&quot; is the branding name. Note that there is a single line for the branding name and if the string is too long, it will be truncated. The length of the string depends on the letters you are using (&#39;mmmmm&#39; and &#39;iiiii&#39; are different in length although they are both 5 letters). The maximum count of letters that can fit based on internal tests are listed here.

| Letter | Max Count |
| --- | --- |
| W | 18 |
| M | 19 |
| m | 20 |
| i | 72 |

See [Planning your COSA database](https://msdn.microsoft.com/en-us/library/windows/hardware/dn973149(v=vs.85).aspx) for more information on the required and optional fields in COSA database.

### Submit your COSA database

Once you complete the COSA update spreadsheet and have the icon file, follow the process in [submitting COSA/APN database](https://docs.microsoft.com/en-us/windows-hardware/drivers/mobilebroadband/submitting-the-apn-database-update). Send your case number to your Data Marketplace partner so that we can follow up internally.

You can also contact your Data Marketplace partner for any questions on the submission.

### Testing the COSA database

See the process for Windows 10, version 1703 and later in [test your submission for COSA](https://docs.microsoft.com/en-us/windows-hardware/drivers/mobilebroadband/testing-your-apn-database-submission).

For verifying Data Marketplace purchase option availability in the network flyout, refer to the diagram below:

![Data Marketplace purchase flow availability](images/dm-purchase-flow.png)

## eSIM profile configuration

If you plan to sell data plans to customers with eSIM devices through the Data Marketplace program, you need to build your eSIM infrastructure and prepare eSIM profiles.

### eSIM profile requirements

For data plans sold through Windows Store PAYG or MO Direct, you must prepare eSIM profiles that meet the following requirements:

1. eSIM profile must NOT be PIN locked.
2. eSIM profile must NOT be deleted from your SM-DP+ until you receive the signal which confirms the profile download has been completed successfully.
3. You must NOT set &#39;do not delete&#39; or &#39;do not deactivate&#39; policy on eSIM profiles.
4. Activation code must NOT include any prefix, such as &#39;LPA:&#39;.
5. Activation code can be reused to retry downloading the same profile, when previous attempts to download have failed.

Last but not least, Data Marketplace User Experience expects eSIM profile to be in warm state, meaning that a data plan purchased through Store PAYG or MO Direct can be activated at real-time after downloading the eSIM profile.
