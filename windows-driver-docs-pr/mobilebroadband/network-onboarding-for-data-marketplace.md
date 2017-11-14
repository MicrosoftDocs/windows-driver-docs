---
title: Network onboarding for Data Marketplace
author: windows-driver-content
description: This topic describes network onboarding for Data Marketplace.
ms.assetid: BF16A8DF-78B8-43B0-ABEF-380CAAE28DAC
keywords:
- Data Marketplace mobile operators, Data Marketplace mobile broadband WDK
ms.author: windowsdriverdev
ms.date: 11/13/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Network onboarding for Data Marketplace

The Data Marketplace experience is comprised of two user interfaces: the [Windows Connection Manager (a.k.a. the flyout)](#windows-connection-manager) and the [Paid Wi-Fi and Cellular app](#paid-wi-fi-and-cellular-app).

## Windows Connection Manager

Windows Connection Manager (a.k.a. the flyout) refers to the flyout window that launches when you click on the network interface icon, displaying all available network connections. This is the entry point for Data Marketplace purchase flow if available. 

<p><img src="images/windowsconnectionmanager2.png" alt="Windows Connection Manager flyout window" title="Windows Connection Manager flyout window" style="width: 250px;"/></p>
<p><img src="images/windowsconnectionmanager.png" alt="Windows Connection Manager icon" title="Windows Connection Manager icon"/></p>

Tapping on the **Contoso Cellular** connection will expand it with more options. With the **Contoso Cellular** connection expanded, if the provider is Data Marketplace onboarded, a **Connect with a data plan** option will be displayed. Clicking on this option will launch the [Paid Wi-Fi and Cellular app](/paid-wi-fi-and-cellular-app).

<p><img src="images/windowsconnectionmanager3.png" alt="Windows Connection Manager flyout window expanded connection option" title="Windows Connection Manager flyout window expanded connection option" style="width: 250px;"/></p>

In order to have this **Connect with a data plan** option available, you must [submit your COSA database](planning-your-desktop-cosa-apn-database-submission.md). 

The following table compares the UX based on an operator’s information submitted in COSA database.

| Configuration | UX | Notes |
| ------- | -------- | --------- |
| SIM profile not in COSA range | Customer must manually input the APN for Windows to connect to Operator’s network. | -- |
| SIM profile onboarded in COSA range with ‘Data Marketplace Supported = No’ | Collapsed, Disconnected: <p><img src="images/cosa_range1.png" alt="Collapsed and disconnected window" title="Collapsed and disconnected window" style="width: 250px;"/></p> | 1. No remaining balance will be displayed in the flyout for profiles not supporting Data Marketplace. |
| SIM profile onboarded in COSA range with ‘Data Marketplace Supported = No’ | Collapsed, Connected: <p><img src="images/cosa_range2.png" alt="Collapsed and connected window" title="Collapsed and connected window" style="width: 250px;"/></p> | 2.	No option to launche Paid Wi-Fi & Cellular app from the flyout. |
| SIM profile onboarded in COSA range with ‘Data Marketplace Supported = No’ | Expanded, Connected: <p><img src="images/cosa_range3.png" alt="Expanded and connected window" title="Expanded and connected window" style="width: 250px;"/></p> | 3. Customer can launch Paid Wi-Fi & Cellular app from Windows start menu. If the device is eSIM capable (either with embedded or inserted reprogrammable eUICC) and the device is connected to internet, customer can choose from a list of Data Marketplace onboarded providers and purchase from them. |
| SIM profile onboarded in COSA range with ‘Data Marketplace Supported = Yes’ | Collapsed, disconnected, has balance: <p><img src="images/cosa_range4.png" alt="Collapsed, disconnected with balance window" title="Collapsed, disconnected with balance window" style="width: 250px;"/></p> | 1. Balance will be retrieved through Get Balance API and displayed in the flyout.|
| SIM profile onboarded in COSA range with ‘Data Marketplace Supported = Yes’ | Collapsed, disconnected, no balance: <p><img src="images/cosa_range5.png" alt="Collapsed, disconnected, no balance window" title="Collapsed, disconnected, no balance window" style="width: 250px;"/></p> | 2.	When Operator returns no balance, ‘Connect with a data plan’ option is displayed in the flyout. This option launches the Paid Wi-Fi & Cellular app.|
| SIM profile onboarded in COSA range with ‘Data Marketplace Supported = Yes’ | Expanded, connected, has balance: <p><img src="images/cosa_range6.png" alt="Expanded, connected with balance window" title="Expanded, connected with balance window" style="width: 250px;"/></p> | |
| SIM profile onboarded in COSA range with ‘Data Marketplace Supported = Yes’ | Expanded, connected, no balance: <p><img src="images/cosa_range7.png" alt="Expanded, connected with no balance window" title="Expanded, connected with no balance window" style="width: 250px;"/></p> | | 

## Paid Wi-Fi and Cellular app 

The Paid Wi-Fi and Cellular (PWC) app is where customer engages in the purchase flow.


## COSA database submission
This section will discuss the process and implication of having COSA database submitted.

> [!IMPORTANT]
> Starting in Windows 10, version 1703, the APN database is replaced by a new format called COSA. Windows 8, Windows 8.1, and versions of Windows 10 before version 1703 will continue to use the APN database, while Windows 10, version 1703 and later use COSA. For a list of frequently asked questions about COSA, see [COSA overview](cosa-overview.md).

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

<p><img src="images/view_my_account.png" alt="View my account flyout window" title="View my account flyout window" style="width: 250px;"/></p>

![Alt text](BUGBUG NEED IMAGE)

The following fields are highly recommended as they determine the branding assets displayed in the Windows Connection Manager:

- Branding Name
- Branding Icon
- Use Branding On Roaming

![Windows Connection Manager with branding](BUGBUG NEED IMAGE)

Note that there is a single line for the branding name and if the string is too long, it will be truncated. The length of the string depends on the letters you are using (&#39;mmmmm&#39; and &#39;iiiii&#39; are different in length although they are both 5 letters). The maximum count of letters that can fit based on internal tests are listed in the following table.

| Letter | Max Count |
| --- | --- |
| W | 18 |
| M | 19 |
| m | 20 |
| i | 72 |

See [Desktop COSA/APN database settings](desktop-cosa-apn-database-settings.md) for more information on the required and optional fields in COSA database.

### Submit your COSA database

Once you complete the COSA update spreadsheet and have the icon file, follow the process in [Submitting the desktop COSA/APN database update](submitting-the-desktop-cosa-apn-database-update.md). Send your case number to your Data Marketplace partner so that we can follow up internally.

You can also contact your Data Marketplace partner for any questions on the submission.

### Testing the COSA database

See the process for Windows 10, version 1703 and later in [Testing your desktop COSA/APN database submission](testing-your-desktop-cosa-apn-database-submission.md).

For verifying Data Marketplace purchase option availability in the network flyout, refer to the following diagram:

<p><img src="images/dm-purchase-flow.png" alt="Data Marketplace purchase flow availability" title="Data Marketplace purchase flow availability" style="width: 800px;"/></p>

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

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bp_mb\p_mb%5D:%20Planning%20your%20APN%20database%20submission%20%20RELEASE:%20%281/18/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")
