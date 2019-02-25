---
title: WDM Equivalents for WDF Buffer Pointers
description: WDM Equivalents for WDF Buffer Pointers
ms.assetid: 7923A3CA-479A-4C7D-B428-F57C9701906E
ms.date: 04/20/2017
ms.localizationpriority: medium
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

 

 

 





