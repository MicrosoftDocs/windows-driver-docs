---
title: Accessing Read-Only System Memory
description: Accessing Read-Only System Memory
ms.assetid: d2c1f933-3a7e-4e82-b96d-4f019b27abd5
keywords: ["memory management WDK kernel , read-only memory", "read-only memory WDK kernel", "intercepting system calls", "global strings WDK memory"]
ms.date: 06/16/2017
ms.localizationpriority: medium
---

# Accessing Read-Only System Memory





The Windows [memory manager](windows-kernel-mode-memory-manager.md) enforces read-only access of pages that are not marked as writable.

Read-only memory has always been protected in user mode. However, in Windows NT 4.0 and earlier versions, read-only memory was not protected in kernel mode.

If a Windows kernel-mode driver or application tries to write to a read-only memory segment, the system issues a bug check. For more information, see [**Bug Check 0xBE: ATTEMPTED\_WRITE\_TO\_READONLY\_MEMORY**](https://msdn.microsoft.com/library/windows/hardware/ff560161).

### Intercepting System Calls

Some drivers intercept system calls by overwriting the driver's own code and inserting jump instructions or other changes. Because the driver's own code is read-only, this technique will cause a bug check to be issued.

### Global Strings

If a global string is to be modified, it must not be declared as a pointer to a constant value:

```cpp
CHAR *myString = "This string cannot be modified.";
```

In this case, the linker might put the string in a read-only memory segment. Then an attempt to modify the string will result in a bug check.

Instead, the string should be explicitly declared as an array of L-value characters:

```cpp
CHAR myString[] = "This string can be modified.";
```

This declaration makes sure that the string is put in writable memory.

 

 




