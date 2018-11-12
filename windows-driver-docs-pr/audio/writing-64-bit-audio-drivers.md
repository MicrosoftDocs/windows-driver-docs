---
title: Writing 64-Bit Audio Drivers
description: Writing 64-Bit Audio Drivers
ms.assetid: 0b4cbb98-506e-443f-bac2-59dbdbcb1798
keywords:
- audio drivers WDK , 64-bit
- 64-bit WDK audio
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Writing 64-Bit Audio Drivers


## <span id="writing_64_bit_audio_drivers"></span><span id="WRITING_64_BIT_AUDIO_DRIVERS"></span>


If you are writing a 64-bit driver or writing a driver that can be compiled to run on both 32- and 64-bit systems, follow the porting guidelines in [Driver Programming Techniques](https://msdn.microsoft.com/library/windows/hardware/ff554452). Some of the pitfalls that you might encounter in writing a 64-bit audio driver are described below.

First and foremost, a potential problem to look for in existing 32-bit driver code is conversion between pointer types and integer types such as DWORD or ULONG. Programmers with experience writing code for 32-bit machines might be used to assuming that a pointer value fits into a DWORD or ULONG. For 64-bit code, this assumption is dangerous. Casting a pointer to type DWORD or ULONG can cause a 64-bit pointer to be truncated. A better approach is to cast the pointer to type DWORD\_PTR or ULONG\_PTR. An unsigned integer of type DWORD\_PTR or ULONG\_PTR is always large enough to store the entire pointer, regardless of whether the code is compiled for a 32- or 64-bit machine.

For example, the [**IRP**](https://msdn.microsoft.com/library/windows/hardware/ff550694) pointer field **IoStatus**.**Information** is of type ULONG\_PTR. The following code shows what not to do when copying a 64-bit pointer value to this field:

```cpp
    PDEVICE_RELATIONS pDeviceRelations;
    Irp->IoStatus.Information = (ULONG)pDeviceRelations;  // wrong
```

This code sample erroneously casts the `pDeviceRelations` pointer to type ULONG, which can truncate the pointer value if `sizeof(pDeviceRelations) > sizeof(ULONG)`. The correct approach is to cast the pointer to ULONG\_PTR, as shown in the following:

```cpp
    PDEVICE_RELATIONS pDeviceRelations;
    Irp->IoStatus.Information = (ULONG_PTR)pDeviceRelations;  // correct
```

This preserves all 64 bits of the pointer value.

A resource list stores the physical address of a resource in a structure of type PHYSICAL\_ADDRESS (see [IResourceList](https://msdn.microsoft.com/library/windows/hardware/ff536976)). To avoid truncating a 64-bit address, you should access the structure's **QuadPart** member rather than its **LowPart** member when copying an address into the structure or reading an address from the structure. For example, the **FindTranslatedPort** macro returns a pointer to a [**CM\_PARTIAL\_RESOURCE\_DESCRIPTOR**](https://msdn.microsoft.com/library/windows/hardware/ff541977) structure that contains the base address of an I/O port. The **u**.**Port**.**Start** member of this structure is a PHYSICAL\_ADDRESS pointer to the base address. The following code shows what not to do:

```cpp
    PUSHORT pBase = (PUSHORT)FindTranslatedPort(0)->u.Port.Start.LowPart;  // wrong
```

Again, this can truncate the pointer. Instead, you should access the **QuadPart** of this member, as shown in the following:

```cpp
    PUSHORT pBase = (PUSHORT)FindTranslatedPort(0)->u.Port.Start.QuadPart;  // correct
```

This copies the entire 64-bit pointer.

Inline Win64 functions such as **PtrToUlong** and **UlongToPtr** safely convert between pointer and integer types without relying on assumptions about the relative sizes of these types. If one type is shorter than the other, it must be extended when converting to the longer type. Whether the shorter type is extended by filling with the sign bit or with zeros is well defined for each Win64 function. This means that any code snippets such as

```cpp
    ULONG ulSlotPhysAddr[NUM_PHYS_ADDRS];
    ulSlotPhysAddr[0] = ULONG(pulPhysDmaBuffer) + DMA_BUFFER_SIZE;  // wrong
```

should be replaced by

```cpp
    ULONG_PTR ulSlotPhysAddr[NUM_PHYS_ADDRS];
    ulSlotPhysAddr[0] = PtrToUlong(pulPhysDmaBuffer) + DMA_BUFFER_SIZE;  // correct
```

This is preferred even though `ulSlotPhysAddr` might represent the value of a hardware register that is only 32 rather than 64 bits long. For a list of all the new Win64 helper functions for converting between pointer and integer types, see [The New Data Types](https://msdn.microsoft.com/library/windows/hardware/ff564619).

 

 




