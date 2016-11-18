---
title: C28625
description: Warning C28625 Function call used to clear sensitive data will be optimized away.
ms.assetid: 9ae44fbc-9a56-41e4-9972-d76d9b62033c
---

# C28625


warning C28625: Function call used to clear sensitive data will be optimized away

The current function call might be optimized during compilation, which could make sensitive data stay in memory. Use the **SecureZeroMemory** or **RtlSecureZeroMemory** functions instead. A heuristic looks for identifier names that contain items such as "key" or "pass" to trigger this warning.

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[devtest\devtest]:%20C28625%20%20RELEASE:%20%2811/17/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




