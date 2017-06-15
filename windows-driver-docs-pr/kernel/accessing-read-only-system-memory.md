---
title: Accessing Read-Only System Memory
author: windows-driver-content
description: Accessing Read-Only System Memory
MS-HAID:
- 'MemMgmt\_49a24c4c-fb1a-48e3-8f70-094320db30ca.xml'
- 'kernel.accessing\_read\_only\_system\_memory'
MSHAttr:
- 'PreferredSiteName:MSDN'
- 'PreferredLib:/library/windows/hardware'
ms.assetid: d2c1f933-3a7e-4e82-b96d-4f019b27abd5
keywords: ["memory management WDK kernel , read-only memory", "read-only memory WDK kernel", "intercepting system calls", "global strings WDK memory"]
---

# Accessing Read-Only System Memory


## <a href="" id="ddk-accessing-read-only-system-memory-kg"></a>


The Windows [memory manager](windows-kernel-mode-memory-manager.md) enforces read-only access of pages that are not marked as writable.

Read-only memory has always been protected in user mode. However, in Windows NT 4.0 and earlier versions, read-only memory was not protected in kernel mode.

If a Windows kernel-mode driver or application tries to write to a read-only memory segment, the system issues a bug check. For more information, see [**Bug Check 0xBE: ATTEMPTED\_WRITE\_TO\_READONLY\_MEMORY**](https://msdn.microsoft.com/library/windows/hardware/ff560161).

### Intercepting System Calls

Some drivers intercept system calls by overwriting the driver's own code and inserting jump instructions or other changes. Because the driver's own code is read-only, this technique will cause a bug check to be issued.

### Global Strings

If a global string is to be modified, it must not be declared as a pointer to a constant value:

```
CHAR *myString = "This string cannot be modified.";
```

In this case, the linker might put the string in a read-only memory segment. Then an attempt to modify the string will result in a bug check.

Instead, the string should be explicitly declared as an array of L-value characters:

```
CHAR myString[] = "This string can be modified.";
```

This declaration makes sure that the string is put in writable memory.

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bkernel\kernel%5D:%20Accessing%20Read-Only%20System%20Memory%20%20RELEASE:%20%286/14/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


