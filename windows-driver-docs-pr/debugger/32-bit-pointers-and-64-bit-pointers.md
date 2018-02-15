---
title: 32-Bit Pointers and 64-Bit Pointers
description: 32-Bit Pointers and 64-Bit Pointers
ms.assetid: 641443b9-465f-4c7e-a13d-47a991304b46
keywords: ["WdbgExts extensions, 32-bit pointers", "WdbgExts extensions, 64-bit pointers"]
ms.author: domars
ms.date: 05/23/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# 32-Bit Pointers and 64-Bit Pointers


## <span id="ddk_32_bit_pointers_and_64_bit_pointers_dbwx"></span><span id="DDK_32_BIT_POINTERS_AND_64_BIT_POINTERS_DBWX"></span>


The WdbgExts.h header file supports both 32-bit and 64-bit pointers. To use 64-bit pointers, simply include the following two lines in your code, in the following order:

```
#define KDEXT_64BIT 
#include wdbgexts.h 
```

It is recommended that you always use 64-bit pointers in your code. This allows your extension to work on any platform, because the debugger will automatically cast 64-bit pointers to 32 bits when the target is 32-bit.

If you intend to use your extension only on 32-bit platforms, you can write a 32-bit extension instead. In that case, you only need to include the following line in your code:

```
#include wdbgexts.h 
```

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[debugger\debugger]:%2032-Bit%20Pointers%20and%2064-Bit%20Pointers%20%20RELEASE:%20%285/15/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




