---
title: Writing 64-Bit Audio Drivers
description: Writing 64-Bit Audio Drivers
ms.assetid: 0b4cbb98-506e-443f-bac2-59dbdbcb1798
keywords: ["audio drivers WDK , 64-bit", "64-bit WDK audio"]
---

# Writing 64-Bit Audio Drivers


## <span id="writing_64_bit_audio_drivers"></span><span id="WRITING_64_BIT_AUDIO_DRIVERS"></span>


If you are writing a 64-bit driver or writing a driver that can be compiled to run on both 32- and 64-bit systems, follow the porting guidelines in [Driver Programming Techniques](https://msdn.microsoft.com/library/windows/hardware/ff554452). Some of the pitfalls that you might encounter in writing a 64-bit audio driver are described below.

First and foremost, a potential problem to look for in existing 32-bit driver code is conversion between pointer types and integer types such as DWORD or ULONG. Programmers with experience writing code for 32-bit machines might be used to assuming that a pointer value fits into a DWORD or ULONG. For 64-bit code, this assumption is dangerous. Casting a pointer to type DWORD or ULONG can cause a 64-bit pointer to be truncated. A better approach is to cast the pointer to type DWORD\_PTR or ULONG\_PTR. An unsigned integer of type DWORD\_PTR or ULONG\_PTR is always large enough to store the entire pointer, regardless of whether the code is compiled for a 32- or 64-bit machine.

For example, the [**IRP**](https://msdn.microsoft.com/library/windows/hardware/ff550694) pointer field **IoStatus**.**Information** is of type ULONG\_PTR. The following code shows what not to do when copying a 64-bit pointer value to this field:

```
    PDEVICE_RELATIONS pDeviceRelations;
    Irp->IoStatus.Information = (ULONG)pDeviceRelations;  // wrong
```

This code sample erroneously casts the `pDeviceRelations` pointer to type ULONG, which can truncate the pointer value if `sizeof(pDeviceRelations) > sizeof(ULONG)`. The correct approach is to cast the pointer to ULONG\_PTR, as shown in the following:

```
    PDEVICE_RELATIONS pDeviceRelations;
    Irp->IoStatus.Information = (ULONG_PTR)pDeviceRelations;  // correct
```

This preserves all 64 bits of the pointer value.

A resource list stores the physical address of a resource in a structure of type PHYSICAL\_ADDRESS (see [IResourceList](https://msdn.microsoft.com/library/windows/hardware/ff536976)). To avoid truncating a 64-bit address, you should access the structure's **QuadPart** member rather than its **LowPart** member when copying an address into the structure or reading an address from the structure. For example, the **FindTranslatedPort** macro returns a pointer to a [**CM\_PARTIAL\_RESOURCE\_DESCRIPTOR**](https://msdn.microsoft.com/library/windows/hardware/ff541977) structure that contains the base address of an I/O port. The **u**.**Port**.**Start** member of this structure is a PHYSICAL\_ADDRESS pointer to the base address. The following code shows what not to do:

```
    PUSHORT pBase = (PUSHORT)FindTranslatedPort(0)->u.Port.Start.LowPart;  // wrong
```

Again, this can truncate the pointer. Instead, you should access the **QuadPart** of this member, as shown in the following:

```
    PUSHORT pBase = (PUSHORT)FindTranslatedPort(0)->u.Port.Start.QuadPart;  // correct
```

This copies the entire 64-bit pointer.

Inline Win64 functions such as **PtrToUlong** and **UlongToPtr** safely convert between pointer and integer types without relying on assumptions about the relative sizes of these types. If one type is shorter than the other, it must be extended when converting to the longer type. Whether the shorter type is extended by filling with the sign bit or with zeros is well defined for each Win64 function. This means that any code snippets such as

```
    ULONG ulSlotPhysAddr[NUM_PHYS_ADDRS];
    ulSlotPhysAddr[0] = ULONG(pulPhysDmaBuffer) + DMA_BUFFER_SIZE;  // wrong
```

should be replaced by

```
    ULONG_PTR ulSlotPhysAddr[NUM_PHYS_ADDRS];
    ulSlotPhysAddr[0] = PtrToUlong(pulPhysDmaBuffer) + DMA_BUFFER_SIZE;  // correct
```

This is preferred even though `ulSlotPhysAddr` might represent the value of a hardware register that is only 32 rather than 64 bits long. For a list of all the new Win64 helper functions for converting between pointer and integer types, see [The New Data Types](https://msdn.microsoft.com/library/windows/hardware/ff564619).

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[audio\audio]:%20Writing%2064-Bit%20Audio%20Drivers%20%20RELEASE:%20%287/18/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




