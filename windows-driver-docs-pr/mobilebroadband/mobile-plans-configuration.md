---
title: Mobile Plans configuration
description: This topic describes the configuration step for the Mobile Plans program.
ms.assetid: 95122BBB-0466-4130-9209-7EC6545DFD4D
keywords:
- Windows Mobile Plans configuration, Mobile Plans configuration mobile operators
ms.author: windowsdriverdev
ms.date: 09/17/2018
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Mobile Plans configuration

[!include[Mobile Plans Beta Prerelease](../mobile-plans-beta-prerelease.md)]

This topic describes how to build a foundation on Windows connected devices that support *Mobile Plans*. It details how to configure your eSIM profiles to ensure the best consumer experience, as well as how to provide service configuration information that ensures that the *Mobile Plans* experience is properly rendered on Windows devices.

## eSIM profile configuration requirements

You must prepare eSIM profiles that meet the following requirements:

- The eSIM profile must not be PIN locked.
- The eSIM profile must not be deleted from your SM-DP+ server until you receive confirmation that the profile download has been completed successfully. The activation code can be reused to retry downloading the same profile when previous attempts to download have failed. 
- The eSIM profile must not have the “Do not delete” or “Do not deactivate” policies set.
- The activation code must not include any prefixes such as “LPA:”.
- The activation code is available immediately after the MO Direct flow.
- The eSIM profile can be downloaded immediately from the SMDP+ server after MO Direct flow.
- The device can immediately connect to the network for the end user after the eSIM is downloaded and activated.

Finally, the *Mobile Plans* user experience expects the eSIM profile to be in a warm state, meaning that a data plan can be activated in real-time after downloading the eSIM profile.

## Service configuration

After preparing your eSIM profile, the Microsoft configuration service needs to configure the service platform to support you as a mobile operator. To start this process, send an email to [DYNAMOpartnersup@microsoft.com](mailto:swifipartnersup@microsoft.com) with the following information for onboarding: 

1. The brand name you would like to use for your products.
2. The branding logo. Required resolutions are as follows: 150x150, 188x188, 225x225, 600x600, 300x300, and 400x400 pixels. Images should also be full bleed with no transparency.
3. The list of countries where your solution is supported.
4. Your MO Direct portal URI (localization is not supported).
5. A notification URI (described in [Implementation](mobile-plans-implementation.md)).
6. The ICCID range or ranges that you want to want to associate with *Mobile Plans*.
7. MCC/MNC combinations for which you would like phone number lookup to direct to your mobile operator portal.

The following image shows an example for merchandise information and layout of a provider description page (PDP) in the Mobile Plans app. The “A” annotation corresponds to the branding logo you submit, and the “B” annotation corresponds to the brand name.

<img src="images/dynamo_configuration_mo_page.png" alt="Mobile Plans mobile operator page - asset usage example" title="Mobile Plans mobile operator page - asset usage example" width="600" />