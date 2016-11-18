---
title: Can I tell if my trace provider is enabled for tracing
description: Can I tell if my trace provider is enabled for tracing
ms.assetid: 8cc4e364-a0bc-4ef3-af3c-c08f3183b548
---

# Can I tell if my trace provider is enabled for tracing?


Yes, you can use the WPP\_LEVEL\_ENABLED macro to tell whether your [trace provider](trace-provider.md), such as a kernel-mode driver or user-mode application, is enabled for tracing and which flags are enabled. This is especially useful if your trace provider does extra work to prepare for software tracing.

For example, you can use a condition of the form:

```
If (WPP_LEVEL_ENABLED(flag) {
            // Tracing is enabled
            Prepare to trace
            DoTraceMessage(flag...);
}
```

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[devtest\devtest]:%20Can%20I%20tell%20if%20my%20trace%20provider%20is%20enabled%20for%20tracing?%20%20RELEASE:%20%2811/17/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




