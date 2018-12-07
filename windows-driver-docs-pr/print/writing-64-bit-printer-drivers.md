---
title: Writing 64-Bit Printer Drivers
description: Writing 64-Bit Printer Drivers
ms.assetid: 41f1a521-980e-4ccd-a395-e1d1bf0114d1
keywords:
- printer drivers WDK , 64-bit
- 64-bit WDK printer
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Writing 64-Bit Printer Drivers


If you are writing a 64-bit driver or writing a driver that can be compiled to run on both 32-bit and 64-bit systems, follow the 64-bit porting guidelines in [Driver Programming Techniques](https://msdn.microsoft.com/library/windows/hardware/ff554452). This topic describes some of the limitations and problems that you might encounter in writing a 64-bit printer driver.

For more information about using decorations to identify 64-bit architecture, see the following topics:

-   [Decorations in Printer INF Files](decorations-in-printer-inf-files.md)

-   [How to Use Decorations in INF Files for Printer Drivers](how-to-use-decorations-in-inf-files-for-printer-drivers.md)

### Limitations on Device Context Handles

If a 32-bit application is running on a 64-bit version of the Microsoft Windows operating system, a printer driver plug-in that is running in the context of the Splwow64.exe thunking process should not call the GDI **CreateDC** function; this call will fail.

### Problems with Writing 64-Bit Drivers

In existing 32-bit driver code, be careful about conversions between pointer types and integer types such as DWORD or ULONG. If you have experience writing code for 32-bit machines, you might be used to assuming that a pointer value fits into a DWORD or ULONG. For 64-bit code, this assumption is dangerous. If you cast a pointer to type DWORD or ULONG, a 64-bit pointer might be truncated.

Instead, cast the pointer to type DWORD\_PTR or ULONG\_PTR. An unsigned integer of type DWORD\_PTR or ULONG\_PTR is always large enough to store the entire pointer, regardless of whether the code is compiled for a 32-bit or 64-bit computer.

For example, the pDrvOptItems.UserData pointer field in the [**OEMCUIPPARAM**](https://msdn.microsoft.com/library/windows/hardware/ff557653) structure is of type ULONG\_PTR. The following code example shows what not to do if you copy a 64-bit pointer value to this field.

```cpp
    PUSERDATA pData;
    OEMCUIPPARAM->pDrvOptItems.UserData = (ULONG)pData;  // Wrong
```

The preceding code example casts the *pData* pointer to type ULONG, which can truncate the pointer value if **sizeof**(*pData*) &gt; **sizeof**(ULONG). The correct approach is to cast the pointer to ULONG\_PTR, as shown in the following code example.

```cpp
    PUSERDATA pData;
    OEMCUIPPARAM->pDrvOptItems.UserData = (ULONG_PTR)pData;  // Correct
```

The preceding code example preserves all 64 bits of the pointer value.

Inline 64-bit functions such as **PtrToUlong** and **UlongToPtr** safely convert between pointer and integer types without relying on assumptions about the relative sizes of these types. If one type is shorter than the other, it must be extended when converting to the longer type. If the shorter type is extended by filling with the sign bit or with zeros, each Win64 function can handle these situations. Consider the following code example.

```cpp
    ULONG ulHWPhysAddr[NUM_PHYS_ADDRS];
    ulSlotPhysAddr[0] = ULONG(pulPhysHWBuffer) + HW_BUFFER_SIZE;  // wrong
```

You should replace the preceding code example with the following code example.

```cpp
    ULONG_PTR ulHWPhysAddr[NUM_PHYS_ADDRS];
    ulSlotPhysAddr[0] = PtrToUlong(pulPhysHWBuffer) + HW_BUFFER_SIZE;  // correct
```

The second code example is preferred even though

```cpp
ulSlotPhysAddr
```

might represent the value of a hardware register that is only 32 bits long rather than 64 bits long. For a list of all the new Win64 helper functions for converting between pointer and integer types, see [The New Data Types](https://msdn.microsoft.com/library/windows/hardware/ff564619).
 

 




