---
title: Importing Kernel-Mode Safe Integer Functions
author: windows-driver-content
description: The kernel-mode safe integer functions are available as inline code that is contained in ntintsafe.h or in a library that you link your code to.
ms.assetid: C6696C4E-952A-4162-B2BE-F262496FFBD2
---

# Importing Kernel-Mode Safe Integer Functions


The kernel-mode safe integer functions are available as inline code that is contained in ntintsafe.h or in a library that you link your code to. This header file is available in the Windows Driver Kit (WDK).

It is important to note that you must use arithmetic operations on unsigned values. To use a signed value, you must use a conversion function to first convert the signed value to an unsigned value safely before using the arithmetic function.

## To use the inline versions of the kernel-mode safe integer functions


Include the header file, as shown.

```ManagedCPlusPlus
#include <ntintsafe.h>
```

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bkernel\kernel%5D:%20Importing%20Kernel-Mode%20Safe%20Integer%20Functions%20%20RELEASE:%20%286/14/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


