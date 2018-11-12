---
title: Digital Rights Management
description: Digital Rights Management
ms.assetid: 7ce19196-5180-421f-b6be-ac4a235a8c16
keywords:
- WDM audio drivers WDK , Digital Rights Management
- audio drivers WDK , Digital Rights Management
- Digital Rights Management WDK audio
- DRM WDK audio
- security WDK audio
- proprietary data security WDK audio
- usage rules WDK audio
- playback rules WDK audio
- encryption WDK audio
- cryptography WDK audio
- WDM audio drivers WDK , security
- audio drivers WDK , security
- protected content WDK audio
- digital content security WDK audio
- scrambled content WDK audio
- unauthorized copying WDK audio
- copy protection WDK audio
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Digital Rights Management


## <span id="digital_rights_management"></span><span id="DIGITAL_RIGHTS_MANAGEMENT"></span>


Digital Rights Management (DRM) provides content providers with the means to protect their proprietary music or other data from unauthorized copying and other illegal uses. DRM technology protects digital content by encrypting it and attaching to it usage rules that determine the conditions under which a user can play back the content. Usage rules typically prevent copying or limit the number of times that the content plays. The operating system works together with drivers to enforce these rules.

DRM is designed to be transparent to users unless they attempt to violate the usage rules that they agreed to when they purchased the digital content.

Any digital-audio content that is protected by DRM can be played only by trusted audio drivers. These are drivers that have passed hardware compatibility testing by Microsoft to verify that they are DRM-compliant and contain no loopholes through which the DRM security measures can be circumvented.

In addition, protected content cannot be played when a debugger is attached to the driver.

For Microsoft Windows Me drivers, WHQL (Microsoft Windows Hardware Quality Lab) testing for DRM compliance is optional. However, for drivers in Windows XP and later, DRM compliance is required. For details, see the **DRM Requirements** topic in the following list.

This section presents the following topics:

[DRM Overview](drm-overview.md)

[Content IDs and Content Rights](content-ids-and-content-rights.md)

[Forwarding DRM Content IDs](forwarding-drm-content-ids.md)

[DRM Requirements](drm-requirements.md)

[Developing and Debugging DRM Drivers](developing-and-debugging-drm-drivers.md)

[DRM Functions and Interfaces](drm-functions-and-interfaces.md)

 

 




