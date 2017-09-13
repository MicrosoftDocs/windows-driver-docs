---
title: Importing Kernel-Mode Safe String Functions
author: windows-driver-content
description: Importing Kernel-Mode Safe String Functions
ms.assetid: f1cee7e0-151b-4e03-bf4d-400f328083fa
keywords: ["importing safe string functions", "inline safe string function versions WDK kernel", "library safe string function versions WDK kernel", "byte-counted functions WDK kernel", "character-counted functions WDK kernel", "safe string functions WDK"]
ms.author: windowsdriverdev
ms.date: 06/16/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Importing Kernel-Mode Safe String Functions


## <a href="" id="ddk-importing-kernel-mode-safe-string-functions-kg"></a>


Starting with Windows XP, the kernel-mode safe string library is available as a collection of inline functions that are defined in the Ntstrsafe.h header file.

### <a href="" id="to-use-the-inline-versions-of-the-kernel-mode--safe-string-functions"></a>To use the kernel-mode safe string functions

Include the header file, as shown.

```
#include <ntstrsafe.h>
```

You can make available only the byte-counted or only the character-counted safe string functions.

### To allow only byte-counted functions

Include the following line in your code before including the Ntstrsafe.h header file.

```
#define NTSTRSAFE_NO_CCH_FUNCTIONS
```

### To allow only character-counted functions

Include the following line in your code before including the Ntstrsafe.h header file.

```
#define NTSTRSAFE_NO_CB_FUNCTIONS
```

You can define either NTSTRSAFE\_NO\_CB\_FUNCTIONS or NTSTRSAFE\_NO\_CCH\_FUNCTIONS, but not both.

You can make the [**UNICODE\_STRING**](https://msdn.microsoft.com/library/windows/hardware/ff564879) structure functions unavailable.

### <a href="" id="to-make-unicode-string-structure-functions-unavailable"></a>To make UNICODE\_STRING structure functions unavailable

Include the following line in your code before including the Ntstrsafe.h header file.

```
#define NTSTRSAFE_NO_UNICODE_STRING_FUNCTIONS
```

The maximum number of characters that any ANSI or Unicode string can contain is NTSTRSAFE\_MAX\_CCH. The maximum number of characters that a **UNICODE\_STRING** structure can contain is NTSTRSAFE\_UNICODE\_STRING\_MAX\_CCH. These constants are defined in Ntstrsafe.h.

Your driver can assign smaller values to NTSTRSAFE\_MAX\_CCH and NTSTRSAFE\_UNICODE\_STRING\_MAX\_CCH by including the following lines in your code before including Ntstrsafe.h.

```
#define NTSTRSAFE_MAX_CCH  <new-value>
#define NTSTRSAFE_UNICODE_STRING_MAX_CCH  <new-value>
```

Directives in Ntstrsafe.h verify that your new values are not larger than the default values.

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bkernel\kernel%5D:%20Importing%20Kernel-Mode%20Safe%20String%20Functions%20%20RELEASE:%20%286/14/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


