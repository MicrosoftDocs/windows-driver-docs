---
title: Importing Kernel-Mode Safe String Functions
description: Importing Kernel-Mode Safe String Functions
ms.assetid: f1cee7e0-151b-4e03-bf4d-400f328083fa
keywords: ["importing safe string functions", "inline safe string function versions WDK kernel", "library safe string function versions WDK kernel", "byte-counted functions WDK kernel", "character-counted functions WDK kernel", "safe string functions WDK"]
ms.date: 06/16/2017
ms.localizationpriority: medium
---

# Importing Kernel-Mode Safe String Functions





Starting with Windows XP, the kernel-mode safe string library is available as a collection of inline functions that are defined in the Ntstrsafe.h header file.

### <a href="" id="to-use-the-inline-versions-of-the-kernel-mode--safe-string-functions"></a>To use the kernel-mode safe string functions

Include the header file, as shown.

```cpp
#include <ntstrsafe.h>
```

You can make available only the byte-counted or only the character-counted safe string functions.

### To allow only byte-counted functions

Include the following line in your code before including the Ntstrsafe.h header file.

```cpp
#define NTSTRSAFE_NO_CCH_FUNCTIONS
```

### To allow only character-counted functions

Include the following line in your code before including the Ntstrsafe.h header file.

```cpp
#define NTSTRSAFE_NO_CB_FUNCTIONS
```

You can define either NTSTRSAFE\_NO\_CB\_FUNCTIONS or NTSTRSAFE\_NO\_CCH\_FUNCTIONS, but not both.

You can make the [**UNICODE\_STRING**](https://msdn.microsoft.com/library/windows/hardware/ff564879) structure functions unavailable.

### <a href="" id="to-make-unicode-string-structure-functions-unavailable"></a>To make UNICODE\_STRING structure functions unavailable

Include the following line in your code before including the Ntstrsafe.h header file.

```cpp
#define NTSTRSAFE_NO_UNICODE_STRING_FUNCTIONS
```

The maximum number of characters that any ANSI or Unicode string can contain is NTSTRSAFE\_MAX\_CCH. The maximum number of characters that a **UNICODE\_STRING** structure can contain is NTSTRSAFE\_UNICODE\_STRING\_MAX\_CCH. These constants are defined in Ntstrsafe.h.

Your driver can assign smaller values to NTSTRSAFE\_MAX\_CCH and NTSTRSAFE\_UNICODE\_STRING\_MAX\_CCH by including the following lines in your code before including Ntstrsafe.h.

```cpp
#define NTSTRSAFE_MAX_CCH  <new-value>
#define NTSTRSAFE_UNICODE_STRING_MAX_CCH  <new-value>
```

Directives in Ntstrsafe.h verify that your new values are not larger than the default values.

 

 




