---
title: Authentication and Identification
author: windows-driver-content
description: Authentication and Identification
ms.assetid: fe118cf3-05ce-43b1-b878-4bb99b97dc2e
keywords: ["security WDK file systems , minimizing threats", "authentication WDK file systems", "identification WDK file systems"]
---

# Authentication and Identification


## <span id="ddk_authentication_and_identification_if"></span><span id="DDK_AUTHENTICATION_AND_IDENTIFICATION_IF"></span>


Most drivers are not involved in authentication or identification issues, leaving this task to individual services. One case where a driver might become involved in authentication or identification processing is in access management. In this case, the authentication step is usually handled through calls to the Security Reference Monitor. Authentication and identification information is normally tracked by the operating system by the security token, an internal data structure that encapsulates the security credentials for a given thread or process.

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[ifsk\ifsk]:%20Authentication%20and%20Identification%20%20RELEASE:%20%285/9/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


