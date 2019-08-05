---
title: WDM Equivalents for WDF Buffer Pointers
description: WDM Equivalents for WDF Buffer Pointers
ms.assetid: 7923A3CA-479A-4C7D-B428-F57C9701906E
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# WDM Equivalents for WDF Buffer PointersF


A Kernel-Mode Driver Framework (KMDF) or User-Mode Driver Framework (UMDF) driver uses the following methods for retrieving I/O buffers for buffered and direct I/O. Unless otherwise specified, the methods apply to both KMDF and UMDF.

-   [**WdfRequestRetrieveOutputBuffer**](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/wdfrequest/nf-wdfrequest-wdfrequestretrieveoutputbuffer)
-   [**WdfRequestRetrieveOutputWdmMdl (KMDF only)**](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/wdfrequest/nf-wdfrequest-wdfrequestretrieveoutputwdmmdl)
-   [**WdfRequestRetrieveOutputMemory**](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/wdfrequest/nf-wdfrequest-wdfrequestretrieveoutputmemory)
-   [**WdfRequestRetrieveInputBuffer**](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/wdfrequest/nf-wdfrequest-wdfrequestretrieveinputbuffer)
-   [**WdfRequestRetrieveInputWdmMdl (KMDF only)**](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/wdfrequest/nf-wdfrequest-wdfrequestretrieveinputwdmmdl)
-   [**WdfRequestRetrieveInputMemory**](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/wdfrequest/nf-wdfrequest-wdfrequestretrieveinputmemory)

The following tables describe what the retrieval methods return for IRP\_MJ\_READ, IRP\_MJ\_WRITE, and IRP\_MJ\_DEVICE\_CONTROL requests for buffered and direct I/O. Requests for neither I/O require special handling because the driver must retrieve the buffers while running in the context of the requesting user-mode process.

## <a href="" id="read"></a>Buffers for IRP\_MJ\_READ Requests


To retrieve a buffer for a read request, a KMDF driver calls one of the **WdfRequestRetrieveOutput**_Xxx_ methods. The buffer that each of these methods returns varies, depending on whether the driver performs buffered or direct I/O. The following table describes the pointer that is returned by each method in WDM terms.

| Function                                                                             | Buffered I/O                                                                                                                                    | Direct I/O                                                                                                                                                                                                |
|--------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**WdfRequestRetrieveOutputBuffer**](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/wdfrequest/nf-wdfrequest-wdfrequestretrieveoutputbuffer)             | **Irp-&gt;AssociatedIrp.SystemBuffer**                                                                                                          | [**MmGetSystemAddressForMdlSafe**](https://docs.microsoft.com/windows-hardware/drivers/kernel/mm-bad-pointer) (**Irp-&gt;MdlAddress**)                                                                                                          |
| [**WdfRequestRetrieveOutputWdmMdl (KMDF only)**](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/wdfrequest/nf-wdfrequest-wdfrequestretrieveoutputwdmmdl) | Builds a memory descriptor list (MDL) for **Irp-&gt;AssociatedIrp.SystemBuffer** and returns the MDL.                                           | **Irp-&gt;MdlAddress**                                                                                                                                                                                    |
| [**WdfRequestRetrieveOutputMemory**](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/wdfrequest/nf-wdfrequest-wdfrequestretrieveoutputmemory)             | Returns a WDFMEMORY object. Call [**WdfMemoryGetBuffer**](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/wdfmemory/nf-wdfmemory-wdfmemorygetbuffer) on this object to get **Irp-&gt;AssociatedIrp.SystemBuffer**. | Returns a WDFMEMORY object. Call [**WdfMemoryGetBuffer**](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/wdfmemory/nf-wdfmemory-wdfmemorygetbuffer) on this object to get [**MmGetSystemAddressForMdlSafe**](https://docs.microsoft.com/windows-hardware/drivers/kernel/mm-bad-pointer) (**Irp-&gt;MdlAddress**). |

 

## <a href="" id="write"></a>Buffers for IRP\_MJ\_WRITE Requests


To retrieve a buffer for a write request, a KMDF driver calls one of the **WdfRequestRetrieveInput**_Xxx_ methods. The buffer that each of these methods returns varies, depending on whether the driver performs buffered or direct I/O. The following table describes the pointer that is returned by each method in WDM terms.

| Function                                                                           | Buffered I/O                                                                                                                                    | Direct I/O                                                                                                                                                                                                |
|------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**WdfRequestRetrieveInputBuffer**](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/wdfrequest/nf-wdfrequest-wdfrequestretrieveinputbuffer)             | **Irp-&gt;AssociatedIrp.SystemBuffer**                                                                                                          | [**MmGetSystemAddressForMdlSafe**](https://docs.microsoft.com/windows-hardware/drivers/kernel/mm-bad-pointer) (**Irp-&gt;MdlAddress**)                                                                                                          |
| [**WdfRequestRetrieveInputWdmMdl (KMDF only)**](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/wdfrequest/nf-wdfrequest-wdfrequestretrieveinputwdmmdl) | Builds an MDL for **Irp-&gt;AssociatedIrp.SystemBuffer** and returns the MDL.                                                                   | **Irp-&gt;MdlAddress**                                                                                                                                                                                    |
| [**WdfRequestRetrieveInputMemory**](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/wdfrequest/nf-wdfrequest-wdfrequestretrieveinputmemory)             | Returns a WDFMEMORY object. Call [**WdfMemoryGetBuffer**](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/wdfmemory/nf-wdfmemory-wdfmemorygetbuffer) on this object to get **Irp-&gt;AssociatedIrp.SystemBuffer**. | Returns a WDFMEMORY object. Call [**WdfMemoryGetBuffer**](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/wdfmemory/nf-wdfmemory-wdfmemorygetbuffer) on this object to get [**MmGetSystemAddressForMdlSafe**](https://docs.microsoft.com/windows-hardware/drivers/kernel/mm-bad-pointer) (**Irp-&gt;MdlAddress**). |

 

## <a href="" id="device-control"></a>Buffers for IRP\_MJ\_DEVICE\_CONTROL Requests


To retrieve a buffer for a device I/O control request, a KMDF driver calls either **WdfRequestRetrieveInputXxx** or **WdfRequestRetrieveOutputXxx** methods. The buffer that each of these methods returns varies, depending on whether the driver performs [buffered or direct I/O](https://docs.microsoft.com/windows-hardware/drivers/wdf/accessing-data-buffers-in-wdf-drivers), as shown in the following table:

| Function                                                                             | Buffered I/O                                                                                                                                    | Direct I/O                                                                                                                                                                                                |
|--------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**WdfRequestRetrieveInputBuffer**](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/wdfrequest/nf-wdfrequest-wdfrequestretrieveinputbuffer)               | **Irp-&gt;AssociatedIrp.SystemBuffer**                                                                                                          | [**MmGetSystemAddressForMdlSafe**](https://docs.microsoft.com/windows-hardware/drivers/kernel/mm-bad-pointer) (**Irp-&gt;MdlAddress**)                                                                                                          |
| [**WdfRequestRetrieveInputWdmMdl (KMDF only)**](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/wdfrequest/nf-wdfrequest-wdfrequestretrieveinputwdmmdl)   | Builds an MDL for **Irp-&gt;AssociatedIrp.SystemBuffer** and returns the MDL.                                                                   | Builds an MDL for **Irp-&gt;AssociatedIrp.SystemBuffer** and returns the MDL.                                                                                                                             |
| [**WdfRequestRetrieveInputMemory**](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/wdfrequest/nf-wdfrequest-wdfrequestretrieveinputmemory)               | Returns a WDFMEMORY object. Call [**WdfMemoryGetBuffer**](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/wdfmemory/nf-wdfmemory-wdfmemorygetbuffer) on this object to get **Irp-&gt;AssociatedIrp.SystemBuffer**. | Returns a WDFMEMORY object. Call [**WdfMemoryGetBuffer**](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/wdfmemory/nf-wdfmemory-wdfmemorygetbuffer) on this object to get [**MmGetSystemAddressForMdlSafe**](https://docs.microsoft.com/windows-hardware/drivers/kernel/mm-bad-pointer) (**Irp-&gt;MdlAddress**). |
| [**WdfRequestRetrieveOutputBuffer**](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/wdfrequest/nf-wdfrequest-wdfrequestretrieveoutputbuffer)             | **Irp-&gt;AssociatedIrp.SystemBuffer**                                                                                                          | [**MmGetSystemAddressForMdlSafe**](https://docs.microsoft.com/windows-hardware/drivers/kernel/mm-bad-pointer) (**Irp-&gt;MdlAddress**)                                                                                                          |
| [**WdfRequestRetrieveOutputWdmMdl (KMDF only)**](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/wdfrequest/nf-wdfrequest-wdfrequestretrieveoutputwdmmdl) | Builds a memory descriptor list (MDL) for **Irp-&gt;AssociatedIrp.SystemBuffer** and returns the MDL.                                           | **Irp-&gt;MdlAddress**                                                                                                                                                                                    |
| [**WdfRequestRetrieveOutputMemory**](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/wdfrequest/nf-wdfrequest-wdfrequestretrieveoutputmemory)             | Returns a WDFMEMORY object. Call [**WdfMemoryGetBuffer**](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/wdfmemory/nf-wdfmemory-wdfmemorygetbuffer) on this object to get **Irp-&gt;AssociatedIrp.SystemBuffer**. | Returns a WDFMEMORY object. Call [**WdfMemoryGetBuffer**](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/wdfmemory/nf-wdfmemory-wdfmemorygetbuffer) on this object to get [**MmGetSystemAddressForMdlSafe**](https://docs.microsoft.com/windows-hardware/drivers/kernel/mm-bad-pointer) (**Irp-&gt;MdlAddress**). |

 

 

 





