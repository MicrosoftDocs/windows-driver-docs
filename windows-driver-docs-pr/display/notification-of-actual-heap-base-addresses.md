---
title: Notification of Actual Heap Base Addresses
description: Notification of Actual Heap Base Addresses
ms.assetid: b2fe29c7-7c97-41c2-a6be-2c0ef25c5b58
keywords:
- heaps WDK DirectDraw
- display memory WDK DirectDraw , heaps
- nonlocal display memory WDK DirectDraw , heaps
- AGP WDK DirectDraw , heaps
- drawing AGP support WDK DirectDraw , heaps
- DirectDraw AGP support WDK Windows 2000 display , heaps
- memory WDK DirectDraw AGP , heaps
- notifications WDK DirectDraw heap addresses
- linear heaps WDK DirectDraw
- physical heaps WDK DirectDraw
ms.author: windows-driver-content
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Notification of Actual Heap Base Addresses


## <span id="ddk_notification_of_actual_heap_base_addresses_gg"></span><span id="DDK_NOTIFICATION_OF_ACTUAL_HEAP_BASE_ADDRESSES_GG"></span>


A driver might need to know the linear and physical address of the base of the heap at DirectDraw initialization time (for example, during mode changes) rather than waiting for a surface creation request and looking at the heaps in the global DirectDraw surface object. To support this, DirectDraw calls the driver-supplied [**DdGetDriverInfo**](https://msdn.microsoft.com/library/windows/hardware/ff549404) callback function with a globally unique identifier (GUID) that identifies the information to be returned by the driver. If the driver recognizes the GUID and has information to return, it copies this information into the supplied data structure and passes it back to DirectDraw.

The driver uses two GUIDs to gather and offer further information regarding Direct Draw heaps:

-   GUID\_GetHeapAlignment

-   GUID\_UpdateNonLocalHeap

GUID\_GetHeapAlignment signals to the driver to gather heap alignment information about any DirectDraw heaps that are passed to it. The heap information is passed to the driver using the [**DD\_GETHEAPALIGNMENTDATA**](https://msdn.microsoft.com/library/windows/hardware/ff551572) structure. GUID\_GetHeapAlignment is defined as:

```
DEFINE_GUID( GUID_GetHeapAlignment,
    0x42e02f16, 0x7b41, 0x11d2, 0x8b, 0xff, 0x0, 0xa0, 0xc9, 0x83, 0xea, 0xf6);
```

GUID\_UpdateNonLocalHeap signals the driver to update its internal state with the heap information with the nonlocal heap structures supplied by DirectDraw. This information is contained in the [**DD\_UPDATENONLOCALHEAPDATA**](https://msdn.microsoft.com/library/windows/hardware/ff551748) structure. GUID\_UpdateNonLocalHeap is defined as:

```
DEFINE_GUID( GUID_UpdateNonLocalHeap,
           0x42e02f17, 0x7b41, 0x11d2, 0x8b, 0xff, 0x0, 0xa0, 0xc9, 0x83, 0xea, 0xf6);
```

If the driver must allocate memory for AGP surfaces by itself, but has exposed heaps to DirectDraw, then [**HeapVidMemAllocAligned**](https://msdn.microsoft.com/library/windows/hardware/ff567267) is exposed as an **Eng** function for this purpose. **HeapVidMemAllocAligned** only deals with heap addresses so it returns an offset. The driver must do whatever memory mapping work it needs to do to turn the information returned from **HeapVidMemAllocAligned** into a virtual address.

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[display\display]:%20Notification%20of%20Actual%20Heap%20Base%20Addresses%20%20RELEASE:%20%282/10/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




