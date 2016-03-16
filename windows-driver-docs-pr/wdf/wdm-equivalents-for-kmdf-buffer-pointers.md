---
title: WDM Equivalents for WDF Buffer Pointers
description: WDM Equivalents for WDF Buffer Pointers
MSHAttr: PreferredLib /library/windows/hardware
ms.assetid: 7923A3CA-479A-4C7D-B428-F57C9701906E
---

# WDM Equivalents for WDF Buffer Pointers


A Kernel-Mode Driver Framework (KMDF) or User-Mode Driver Framework (UMDF) driver uses the following methods for retrieving I/O buffers for buffered and direct I/O. Unless otherwise specified, the methods apply to both KMDF and UMDF.

-   [**WdfRequestRetrieveOutputBuffer**](https://msdn.microsoft.com/library/windows/hardware/ff550018)
-   [**WdfRequestRetrieveOutputWdmMdl (KMDF only)**](https://msdn.microsoft.com/library/windows/hardware/ff550021)
-   [**WdfRequestRetrieveOutputMemory**](https://msdn.microsoft.com/library/windows/hardware/ff550019)
-   [**WdfRequestRetrieveInputBuffer**](https://msdn.microsoft.com/library/windows/hardware/ff550014)
-   [**WdfRequestRetrieveInputWdmMdl (KMDF only)**](https://msdn.microsoft.com/library/windows/hardware/ff550016)
-   [**WdfRequestRetrieveInputMemory**](https://msdn.microsoft.com/library/windows/hardware/ff550015)

The following tables describe what the retrieval methods return for IRP\_MJ\_READ, IRP\_MJ\_WRITE, and IRP\_MJ\_DEVICE\_CONTROL requests for buffered and direct I/O. Requests for neither I/O require special handling because the driver must retrieve the buffers while running in the context of the requesting user-mode process.

## <a href="" id="read"></a>Buffers for IRP\_MJ\_READ Requests


To retrieve a buffer for a read request, a KMDF driver calls one of the **WdfRequestRetrieveOutput***Xxx* methods. The buffer that each of these methods returns varies, depending on whether the driver performs buffered or direct I/O. The following table describes the pointer that is returned by each method in WDM terms.

| Function                                                                             | Buffered I/O                                                                                                                                    | Direct I/O                                                                                                                                                                                                |
|--------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**WdfRequestRetrieveOutputBuffer**](https://msdn.microsoft.com/library/windows/hardware/ff550018)             | **Irp-&gt;AssociatedIrp.SystemBuffer**                                                                                                          | [**MmGetSystemAddressForMdlSafe**](https://msdn.microsoft.com/library/windows/hardware/ff554559) (**Irp-&gt;MdlAddress**)                                                                                                          |
| [**WdfRequestRetrieveOutputWdmMdl (KMDF only)**](https://msdn.microsoft.com/library/windows/hardware/ff550021) | Builds a memory descriptor list (MDL) for **Irp-&gt;AssociatedIrp.SystemBuffer** and returns the MDL.                                           | **Irp-&gt;MdlAddress**                                                                                                                                                                                    |
| [**WdfRequestRetrieveOutputMemory**](https://msdn.microsoft.com/library/windows/hardware/ff550019)             | Returns a WDFMEMORY object. Call [**WdfMemoryGetBuffer**](https://msdn.microsoft.com/library/windows/hardware/ff548715) on this object to get **Irp-&gt;AssociatedIrp.SystemBuffer**. | Returns a WDFMEMORY object. Call [**WdfMemoryGetBuffer**](https://msdn.microsoft.com/library/windows/hardware/ff548715) on this object to get [**MmGetSystemAddressForMdlSafe**](https://msdn.microsoft.com/library/windows/hardware/ff554559) (**Irp-&gt;MdlAddress**). |

 

## <a href="" id="write"></a>Buffers for IRP\_MJ\_WRITE Requests


To retrieve a buffer for a write request, a KMDF driver calls one of the **WdfRequestRetrieveInput***Xxx* methods. The buffer that each of these methods returns varies, depending on whether the driver performs buffered or direct I/O. The following table describes the pointer that is returned by each method in WDM terms.

| Function                                                                           | Buffered I/O                                                                                                                                    | Direct I/O                                                                                                                                                                                                |
|------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**WdfRequestRetrieveInputBuffer**](https://msdn.microsoft.com/library/windows/hardware/ff550014)             | **Irp-&gt;AssociatedIrp.SystemBuffer**                                                                                                          | [**MmGetSystemAddressForMdlSafe**](https://msdn.microsoft.com/library/windows/hardware/ff554559) (**Irp-&gt;MdlAddress**)                                                                                                          |
| [**WdfRequestRetrieveInputWdmMdl (KMDF only)**](https://msdn.microsoft.com/library/windows/hardware/ff550016) | Builds an MDL for **Irp-&gt;AssociatedIrp.SystemBuffer** and returns the MDL.                                                                   | **Irp-&gt;MdlAddress**                                                                                                                                                                                    |
| [**WdfRequestRetrieveInputMemory**](https://msdn.microsoft.com/library/windows/hardware/ff550015)             | Returns a WDFMEMORY object. Call [**WdfMemoryGetBuffer**](https://msdn.microsoft.com/library/windows/hardware/ff548715) on this object to get **Irp-&gt;AssociatedIrp.SystemBuffer**. | Returns a WDFMEMORY object. Call [**WdfMemoryGetBuffer**](https://msdn.microsoft.com/library/windows/hardware/ff548715) on this object to get [**MmGetSystemAddressForMdlSafe**](https://msdn.microsoft.com/library/windows/hardware/ff554559) (**Irp-&gt;MdlAddress**). |

 

## <a href="" id="device-control"></a>Buffers for IRP\_MJ\_DEVICE\_CONTROL Requests


To retrieve a buffer for a device I/O control request, a KMDF driver calls either **WdfRequestRetrieveInputXxx** or **WdfRequestRetrieveOutputXxx** methods. The buffer that each of these methods returns varies, depending on whether the driver performs [buffered or direct I/O](https://msdn.microsoft.com/library/windows/hardware/ff540701), as shown in the following table:

| Function                                                                             | Buffered I/O                                                                                                                                    | Direct I/O                                                                                                                                                                                                |
|--------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**WdfRequestRetrieveInputBuffer**](https://msdn.microsoft.com/library/windows/hardware/ff550014)               | **Irp-&gt;AssociatedIrp.SystemBuffer**                                                                                                          | [**MmGetSystemAddressForMdlSafe**](https://msdn.microsoft.com/library/windows/hardware/ff554559) (**Irp-&gt;MdlAddress**)                                                                                                          |
| [**WdfRequestRetrieveInputWdmMdl (KMDF only)**](https://msdn.microsoft.com/library/windows/hardware/ff550016)   | Builds an MDL for **Irp-&gt;AssociatedIrp.SystemBuffer** and returns the MDL.                                                                   | Builds an MDL for **Irp-&gt;AssociatedIrp.SystemBuffer** and returns the MDL.                                                                                                                             |
| [**WdfRequestRetrieveInputMemory**](https://msdn.microsoft.com/library/windows/hardware/ff550015)               | Returns a WDFMEMORY object. Call [**WdfMemoryGetBuffer**](https://msdn.microsoft.com/library/windows/hardware/ff548715) on this object to get **Irp-&gt;AssociatedIrp.SystemBuffer**. | Returns a WDFMEMORY object. Call [**WdfMemoryGetBuffer**](https://msdn.microsoft.com/library/windows/hardware/ff548715) on this object to get [**MmGetSystemAddressForMdlSafe**](https://msdn.microsoft.com/library/windows/hardware/ff554559) (**Irp-&gt;MdlAddress**). |
| [**WdfRequestRetrieveOutputBuffer**](https://msdn.microsoft.com/library/windows/hardware/ff550018)             | **Irp-&gt;AssociatedIrp.SystemBuffer**                                                                                                          | [**MmGetSystemAddressForMdlSafe**](https://msdn.microsoft.com/library/windows/hardware/ff554559) (**Irp-&gt;MdlAddress**)                                                                                                          |
| [**WdfRequestRetrieveOutputWdmMdl (KMDF only)**](https://msdn.microsoft.com/library/windows/hardware/ff550021) | Builds a memory descriptor list (MDL) for **Irp-&gt;AssociatedIrp.SystemBuffer** and returns the MDL.                                           | **Irp-&gt;MdlAddress**                                                                                                                                                                                    |
| [**WdfRequestRetrieveOutputMemory**](https://msdn.microsoft.com/library/windows/hardware/ff550019)             | Returns a WDFMEMORY object. Call [**WdfMemoryGetBuffer**](https://msdn.microsoft.com/library/windows/hardware/ff548715) on this object to get **Irp-&gt;AssociatedIrp.SystemBuffer**. | Returns a WDFMEMORY object. Call [**WdfMemoryGetBuffer**](https://msdn.microsoft.com/library/windows/hardware/ff548715) on this object to get [**MmGetSystemAddressForMdlSafe**](https://msdn.microsoft.com/library/windows/hardware/ff554559) (**Irp-&gt;MdlAddress**). |

 

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bwdf\wdf%5D:%20WDM%20Equivalents%20for%20WDF%20Buffer%20Pointers%20%20RELEASE:%20%283/15/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




