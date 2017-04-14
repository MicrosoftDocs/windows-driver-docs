---
title: C28752
description: Warning C28752 Banned usage of kernel32 or advapi32 API.
ms.assetid: F887EB9E-FA5A-4139-AF67-7460BB9254B8
---

# C28752


warning C28752: Banned usage of kernel32 or advapi32 API

This warning indicates that a function is being used that has been deprecated, and has a preferred replacement that is part of Core System.

The Core System binaries provide much of the functionality that kernel32 and advapi32 do, but in many cases a different API call is required. Calling Core System APIs is faster and requires a smaller memory footprint than calling legacy kernel32 or advapi32 APIs.

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[devtest\devtest]:%20C28752%20%20RELEASE:%20%2811/17/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




