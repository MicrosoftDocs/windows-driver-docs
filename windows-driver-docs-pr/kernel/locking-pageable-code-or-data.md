---
title: Locking Pageable Code or Data
description: Locking Pageable Code or Data
ms.assetid: b99b6af3-b4b1-4fd6-ac73-27c1068183a4
keywords: ["pageable drivers WDK kernel , locking code or data", "locking WDK pageable drivers", "restoring pageable status", "resident code WDK pageable drivers", "isolating pageable code", "PAGE keyword WDK"]
ms.date: 06/16/2017
ms.localizationpriority: medium
---

# Locking Pageable Code or Data





Certain kernel-mode drivers, such as the serial and parallel drivers, do not have to be memory-resident unless the devices they manage are open. However, as long as there is an active connection or port, some part of the driver code that manages that port must be resident to service the device. When the port or connection is not being used, the driver code is not required. In contrast, a driver for a disk that contains system code, application code, or the system paging file must always be memory-resident because the driver constantly transfers data between its device and the system.

A driver for a sporadically used device (such as a modem) can free system space when the device it manages is not active. If you place in a single section the code that must be resident to service an active device, and if your driver locks the code in memory while the device is being used, this section can be designated as pageable. When the driver's device is opened, the operating system brings the pageable section into memory and the driver locks it there until no longer needed.

The system CD audio driver code uses this technique. Code for the driver is grouped into pageable sections according to the manufacturer of CD device. Certain brands might never be present on a given system. Also, even if a CD-ROM exists on a system, it might be accessed infrequently, so grouping code into pageable sections by CD type makes sure that code for devices that do not exist on a particular computer will never be loaded. However, when the device is accessed, the system loads the code for the appropriate CD device. Then the driver calls the [**MmLockPagableCodeSection**](https://msdn.microsoft.com/library/windows/hardware/ff554601) routine, as described below, to lock its code into memory while its device is being used.

To isolate the pageable code into a named section, mark it with the following compiler directive:

**\#pragma alloc\_text(PAGE*Xxx**<em>, *RoutineName</em>**)**

The name of a pageable code section must start with the four letters "PAGE" and can be followed by up to four characters (represented here as ***Xxx***) to uniquely identify the section. The first four letters of the section name (that is, "PAGE") must be capitalized. The *RoutineName* identifies an entry point to be included in the pageable section.

The shortest valid name for a pageable code section in a driver file is simply PAGE. For example, the pragma directive in the following code example identifies `RdrCreateConnection` as an entry point in a pageable code section named PAGE.

```cpp
#ifdef  ALLOC_PRAGMA 
#pragma alloc_text(PAGE, RdrCreateConnection) 
#endif 
```

To make pageable driver code resident and locked in memory, a driver calls [**MmLockPagableCodeSection**](https://msdn.microsoft.com/library/windows/hardware/ff554601), passing an address (typically the entry point of a driver routine) that is in the pageable code section. **MmLockPagableCodeSection** locks in the whole contents of the section that contains the routine referenced in the call. In other words, this call makes every routine associated with the same PAGE*Xxx* identifier resident and locked in memory.

**MmLockPagableCodeSection** returns a handle to be used when unlocking the section (by calling the [**MmUnlockPagableImageSection**](https://msdn.microsoft.com/library/windows/hardware/ff556377) routine) or when the driver must lock the section from additional locations in its code.

A driver can also treat seldom-used data as pageable so that it, too, can be paged out until the device it supports is active. For example, the system mixer driver uses pageable data. The mixer device has no asynchronous I/O associated with it, so this driver can make its data pageable.

The name of a pageable data section must start with the four letters "PAGE" and can be followed by up to four characters to uniquely identify the section. The first four letters of the section name (that is, "PAGE") must be capitalized.

Avoid assigning identical names to code and data sections. To make source code more readable, driver developers typically assign the name PAGE to the pageable code section because this name is short and it might appear in numerous alloc\_text pragma directives. Longer names are then assigned to any pageable data sections (for example, PAGEDATA for data\_seg, PAGEBSS for bss\_seg, and so on) that the driver might require.

For example, the first two pragma directives in the following code example define two pageable data sections, PAGEDATA and PAGEBSS. PAGEDATA is declared using the data\_seg pragma directive and contains initialized data. PAGEBSS is declared using the bss\_seg pragma directive and contains uninitialized data.

```cpp
#pragma data_seg("PAGEDATA")
#pragma bss_seg("PAGEBSS")

INT Variable1 = 1;
INT Variable2;

CHAR Array1[64*1024] = { 0 };
CHAR Array2[64*1024];

#pragma data_seg()
#pragma bss_seg()
```

In this code example, `Variable1` and `Array1` are explicitly initialized and are therefore placed in the PAGEDATA section. `Variable2` and `Array2` are implicitly zero-initialized and are placed in the PAGEBSS section.

Implicitly initializing global variables to zero reduces the size of the on-disk executable file and is preferred over explicit initialization to zero. Explicit zero-initialization should be avoided except in cases where it is required in order to place a variable in a specific data section.

To make a data section memory-resident and lock it in memory, a driver calls [**MmLockPagableDataSection**](https://msdn.microsoft.com/library/windows/hardware/ff554607), passing a data item that appears in the pageable data section. **MmLockPagableDataSection** returns a handle to be used in subsequent locking or unlocking requests.

To restore a locked section's pageable status, call [**MmUnlockPagableImageSection**](https://msdn.microsoft.com/library/windows/hardware/ff556377), passing the handle value returned by [**MmLockPagableCodeSection**](https://msdn.microsoft.com/library/windows/hardware/ff554601) or [**MmLockPagableDataSection**](https://msdn.microsoft.com/library/windows/hardware/ff554607), as appropriate. A driver's [*Unload*](https://msdn.microsoft.com/library/windows/hardware/ff564886) routine must call **MmUnlockPagableImageSection** to release each handle it has obtained for lockable code and data sections.

Locking a section is an expensive operation because the memory manager must search its loaded module list before locking the pages into memory. If a driver locks a section from many locations in its code, it should use the more efficient [**MmLockPagableSectionByHandle**](https://msdn.microsoft.com/library/windows/hardware/ff554610) after its initial call to **MmLockPagable*Xxx*Section**.

The handle passed to **MmLockPagableSectionByHandle** is the handle returned by the earlier call to **MmLockPagableCodeSection** or **MmLockPagableDataSection**.

The memory manager maintains a count for each section handle and increments this count every time that a driver calls **MmLockPagable*Xxx*** for that section. A call to **MmUnlockPagableImageSection** decrements the count. While the counter for any section handle is nonzero, that section remains locked in memory.

The handle to a section is valid as long as its driver is loaded. Therefore, a driver should call **MmLockPagable*Xxx*Section** only one time. If the driver requires additional locking calls, it should use **MmLockPagableSectionByHandle**.

If a driver calls any **MmLockPagable*Xxx*** routine for a section that is already locked, the memory manager increments the reference count for the section. If the section is paged out when the lock routine is called, the memory manager pages in the section and sets its reference count to one.

Using this technique minimizes the driver's effect on system resources. When the driver runs, it can lock into memory the code and data that must be resident. When there are no outstanding I/O requests for its device, (that is, when the device is closed or if the device was never opened), the driver can unlock the same code or data, making it available to be paged out.

However, after a driver has connected interrupts, any driver code that can be called during interrupt processing always must be memory resident. While some device drivers can be made pageable or locked into memory on demand, some core set of such a driver's code and data must be permanently resident in system space.

Consider the following implementation guidelines for locking a code or data section.

- The primary use of the **Mm(Un)Lock*Xxx*** routines is to enable normally nonpaged code or data to be made pageable and brought in as nonpaged code or data. Drivers such as the serial driver and the parallel driver are good examples: if there are no open handles to a device such a driver manages, parts of code are not needed and can remain paged out. The redirector and server are also good examples of drivers that can use this technique. When there are no active connections, both of these components can be paged out.

- The whole pageable section is locked into memory.

- One section for code and one for data per driver is efficient. Many named, pageable sections are generally inefficient.

- Keep purely pageable sections and paged but locked-on-demand sections separate.

- Remember that **MmLockPagableCodeSection** and **MmLockPagableDataSection** should not be frequently called. These routines can cause heavy I/O activity when the memory manager loads the section. If a driver must lock a section from several locations in its code, it should use **MmLockPagableSectionByHandle**.

 

 




