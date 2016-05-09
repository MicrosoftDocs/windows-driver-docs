---
title: Testing for Security
description: Testing for Security
ms.assetid: d9d98f18-a7fc-479c-8627-0aea53ff0bae
keywords: ["security WDK file systems , testing", "testing security WDK file systems"]
---

# Testing for Security


## <span id="ddk_testing_for_security_if"></span><span id="DDK_TESTING_FOR_SECURITY_IF"></span>


Testing for security is not an automated process. Rather, it combines the use of existing tools as well as a thorough threat analysis of the given driver or drivers. Testing a driver thus consists of many separate steps:

-   A thorough threat analysis to actively identify the types of attacks that might be made within the environment where the driver is used. For example, drivers that are present in highly controlled environments may have simpler threat analyses than drivers for mass distribution, which will be subject to arbitrary attacks.

-   Testing with existing tools including the "Designed for Windows" logo tests in the WDK, such as Device Path Exerciser, a device control attack testing utility. The IFS tests in the WDK should also be used to thoroughly test for storage stack issues.

-   Additional tests should be developed as part of normal driver development for specifically testing scenarios identified as part of the threat analysis. These tests would usually be unique to the driver and attempt to probe the particular driver.

Ideally, for testing purposes, the development of validation tests would include input from the original designers of the software, as well as unrelated development resources familiar with the specific type of file system or file system filter driver product being developed, and one or more people familiar with security intrusion analysis and prevention.

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[ifsk\ifsk]:%20Testing%20for%20Security%20%20RELEASE:%20%285/9/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




