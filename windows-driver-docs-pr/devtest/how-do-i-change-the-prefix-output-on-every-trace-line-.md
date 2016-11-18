---
title: How do I change the prefix output on every trace line
description: How do I change the prefix output on every trace line
ms.assetid: be2b6207-79f5-4d71-a6a2-075f3078a873
---

# How do I change the prefix output on every trace line?


Use the following command to change the prefix output on every trace line:

```
set TRACE_FORMAT_PREFIX=[%9!d!]%8!04X!.%3!04X!::%4!s! [%1!s!] 
tracefmt -f mytracefile 
 
```

For information about the TRACE\_FORMAT\_PREFIX parameters, see the [Trace Message Prefix](trace-message-prefix.md) topic.

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[devtest\devtest]:%20How%20do%20I%20change%20the%20prefix%20output%20on%20every%20trace%20line?%20%20RELEASE:%20%2811/17/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




