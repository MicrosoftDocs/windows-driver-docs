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

 

 





