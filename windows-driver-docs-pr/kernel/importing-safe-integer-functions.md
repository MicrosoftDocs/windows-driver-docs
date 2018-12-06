---
title: Importing Kernel-Mode Safe Integer Functions
description: The kernel-mode safe integer functions are available as inline code that is contained in ntintsafe.h or in a library that you link your code to.
ms.assetid: C6696C4E-952A-4162-B2BE-F262496FFBD2
ms.localizationpriority: medium
ms.date: 10/17/2018
---

# Importing Kernel-Mode Safe Integer Functions


The kernel-mode safe integer functions are available as inline code that is contained in ntintsafe.h or in a library that you link your code to. This header file is available in the Windows Driver Kit (WDK).

It is important to note that you must use arithmetic operations on unsigned values. To use a signed value, you must use a conversion function to first convert the signed value to an unsigned value safely before using the arithmetic function.

## To use the inline versions of the kernel-mode safe integer functions


Include the header file, as shown.

```ManagedCPlusPlus
#include <ntintsafe.h>
```

 

 




