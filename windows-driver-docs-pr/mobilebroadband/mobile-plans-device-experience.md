---
title: Mobile Plans Device Experience
description: This topic describes the Windows device experience after Mobile Plans activates.
ms.assetid: E97AD441-86F7-439C-9800-7DD93AAC0545
keywords:
- Windows Mobile Plans device experience, Mobile Plans mobile operators
ms.date: 03/15/2019
ms.localizationpriority: medium
---

# Mobile Plans Windows device experience

This topic describes, which are the capabilities that Mobile Plans program offers to ensure that mobile operator customers have experiences according to the mobile operator offerings.

## Basic Windows experiences

This section describes which are the options to configure what the *View my account* link in the Windows Connection Manager, also known as also known as the network flyout.

The *View my account* link could be configured to:

- Launch a web browser and open a defined web page
- Launch the Mobile Plans app and open the Mobile Plans Web Portal

 Once an option has been choose, please request a COSA database update to implement the righ behavior, please see [Planning your desktop COSA/APN database submission](planning-your-desktop-cosa-apn-database-submission.md).

The following settings apply for the above options:

- *AccountExperienceURL* parameter defines the web page.
- *AppID* parameter defined which app launched, to use Mobile Plans app configure _Microsoft.OneConnect_8wekyb3d8bbwe!App_

The following image shows an example of the network flyout:

<img src="images/mobile_plans_network_flyout_basic.png" alt="Windows Connection Manager showing basic MO" title="Windows Connection Manager showing basic MO" width="250" />
