---
title: What is Driver Security
description: What is Driver Security
ms.assetid: df959e2b-c779-4171-b408-32fbe52ed7af
keywords: ["security WDK file systems , about file system security"]
---

# What is Driver Security


## <span id="ddk_what_is_driver_security_if"></span><span id="DDK_WHAT_IS_DRIVER_SECURITY_IF"></span>


With respect to drivers, anything a user can do that causes a driver to malfunction in such a way that it causes the system to crash or become unusable is a security flaw. When most developers are working on their driver, their focus is on getting the driver to work properly and not whether a malicious intruder will attempt to exploit holes within the system. This is even more the case for file systems and file system filter drivers, which are some of the most complicated types of drivers to write.

However, after a product release, there are users who attempt to probe and identify security weaknesses. Thus, it makes sense for developers to consider these issues during the design and implementation phase in order to minimize the likelihood that such holes exist. The goal is to eliminate as many security holes as possible before they become part of a released product.

Achieving secure drivers requires the cooperation of the designer (consciously thinking of potential threats to the driver), the implementer (defensively coding common operations that can be the source of exploits), and the test team (proactively attempting to find exploits). By properly coordinating all of these activities, the security of the driver will be dramatically enhanced.

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[ifsk\ifsk]:%20What%20is%20Driver%20Security%20%20RELEASE:%20%285/9/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




