---
title: Windows Display Driver Model (WDDM) 64-Bit Issues
description: Windows Display Driver Model (WDDM) 64-Bit Issues
ms.assetid: ab391fca-bc98-4e98-9531-7a1d24ee173d
keywords:
- 64-bit WDK display
- display driver model WDK Windows Vista , 64-bit
- Windows Vista display driver model WDK , 64-bit
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Windows Display Driver Model (WDDM) 64-Bit Issues


To allow 32-bit applications to run on a 64-bit operating system, a 32-bit user-mode display driver must be provided in addition to the 64-bit user-mode display driver that 64-bit applications require. However, only the 64-bit version of a display miniport driver is required on a 64-bit operating system. Windows on Windows (WOW64) enables 32-bit applications to run on a 64-bit operating system. For more information, see [Supporting 32-Bit I/O in Your 64-Bit Driver](https://msdn.microsoft.com/library/windows/hardware/ff563897).

To install a 32-bit user-mode display driver on a 64-bit operating system, the following entry must be set in an add-registry section of the INF file for the graphics device's display miniport driver. This must happen so that the 32-bit user-mode display driver's DLL name is added to the registry during driver installation:

```inf
 [Xxx_SoftwareDeviceSettings]
...
 HKR,, UserModeDriverNameWow, %REG_MULTI_SZ%, Xxx.dll
...
```

The INF file must contain information to direct the operating system to copy the 32-bit user-mode display driver into the system's %systemroot%\\SysWOW64 directory. For more information, see [**INF CopyFiles Directive**](https://msdn.microsoft.com/library/windows/hardware/ff546346) and [**INF DestinationDirs Section**](https://msdn.microsoft.com/library/windows/hardware/ff547383).

Because WOW64 cannot process opaque or untyped data structures such as the [**D3DDDICB\_ALLOCATE**](https://msdn.microsoft.com/library/windows/hardware/ff544137) structure passed via the [**pfnAllocateCb**](https://msdn.microsoft.com/library/windows/hardware/ff568893) function, it cannot perform an automatic conversion from 32 bit to 64 bit. Therefore, for WOW64 to work correctly, you must consider the following items when writing a 32-bit user-mode display driver to run on a 64-bit operating system:

-   Avoid pointers or data types that are sensitive to multiple operating systems, such as, SIZE\_T or HANDLE. Along with making the size of the entire structure variable, these variable-width data types make the alignment and position of individual members different. If variable width members are unavoidable, you can add another member to indicate that the data structure originates from a 32-bit user-mode display driver. The 64-bit display miniport driver can then properly perform the conversion.

-   Even if variable width members are not present, you might need to consider architecture-specific alignment requirements. For instance, on x64, a UINT64 (or QWORD) should be 8-byte aligned. Because a 32-bit user-mode display driver compiled by a standard 32-bit compiler might not align these native 64-bit types correctly, the 64-bit display miniport driver might not be able to accurately access data from the 32-bit user-mode display driver. However, you can force alignment by using the appropriate **pragma** compiler directives. Although using **pragma** compiler directives might cause a slight waste of space on 32-bit operating systems, this lets you use identical 32-bit user-mode display drivers on 32-bit and 64-bit operating systems. If you cannot force alignment by using the appropriate **pragma** compiler directives, the 32-bit user-mode display driver that runs using WOW64 on a 64-bit operating system must be different from the 32-bit user-mode display driver running on a 32-bit operating system.

 

 





