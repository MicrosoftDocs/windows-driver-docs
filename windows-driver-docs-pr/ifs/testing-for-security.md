---
title: Testing for Security
description: Testing for Security
ms.assetid: d9d98f18-a7fc-479c-8627-0aea53ff0bae
keywords:
- security WDK file systems , testing
- testing security WDK file systems
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Testing for Security


## <span id="ddk_testing_for_security_if"></span><span id="DDK_TESTING_FOR_SECURITY_IF"></span>


Testing for security is not an automated process. Rather, it combines the use of existing tools as well as a thorough threat analysis of the given driver or drivers. Testing a driver thus consists of many separate steps:

-   A thorough threat analysis to actively identify the types of attacks that might be made within the environment where the driver is used. For example, drivers that are present in highly controlled environments may have simpler threat analyses than drivers for mass distribution, which will be subject to arbitrary attacks.

-   Testing with existing tools including the "Designed for Windows" logo tests in the WDK, such as Device Path Exerciser, a device control attack testing utility. The IFS tests in the WDK should also be used to thoroughly test for storage stack issues.

-   Additional tests should be developed as part of normal driver development for specifically testing scenarios identified as part of the threat analysis. These tests would usually be unique to the driver and attempt to probe the particular driver.

Ideally, for testing purposes, the development of validation tests would include input from the original designers of the software, as well as unrelated development resources familiar with the specific type of file system or file system filter driver product being developed, and one or more people familiar with security intrusion analysis and prevention.

 

 




