---
title: What is Driver Security
description: What is Driver Security
ms.assetid: df959e2b-c779-4171-b408-32fbe52ed7af
keywords:
- security WDK file systems , about file system security
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# What is Driver Security


## <span id="ddk_what_is_driver_security_if"></span><span id="DDK_WHAT_IS_DRIVER_SECURITY_IF"></span>


With respect to drivers, anything a user can do that causes a driver to malfunction in such a way that it causes the system to crash or become unusable is a security flaw. When most developers are working on their driver, their focus is on getting the driver to work properly and not whether a malicious intruder will attempt to exploit holes within the system. This is even more the case for file systems and file system filter drivers, which are some of the most complicated types of drivers to write.

However, after a product release, there are users who attempt to probe and identify security weaknesses. Thus, it makes sense for developers to consider these issues during the design and implementation phase in order to minimize the likelihood that such holes exist. The goal is to eliminate as many security holes as possible before they become part of a released product.

Achieving secure drivers requires the cooperation of the designer (consciously thinking of potential threats to the driver), the implementer (defensively coding common operations that can be the source of exploits), and the test team (proactively attempting to find exploits). By properly coordinating all of these activities, the security of the driver will be greatly enhanced.

 

 




