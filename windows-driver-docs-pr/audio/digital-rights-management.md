---
title: Digital Rights Management
description: Digital Rights Management
ms.assetid: 7ce19196-5180-421f-b6be-ac4a235a8c16
keywords: ["WDM audio drivers WDK , Digital Rights Management", "audio drivers WDK , Digital Rights Management", "Digital Rights Management WDK audio", "DRM WDK audio", "security WDK audio", "proprietary data security WDK audio", "usage rules WDK audio", "playback rules WDK audio", "encryption WDK audio", "cryptography WDK audio", "WDM audio drivers WDK , security", "audio drivers WDK , security", "protected content WDK audio", "digital content security WDK audio", "scrambled content WDK audio", "unauthorized copying WDK audio", "copy protection WDK audio"]
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

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[audio\audio]:%20Digital%20Rights%20Management%20%20RELEASE:%20%287/18/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




