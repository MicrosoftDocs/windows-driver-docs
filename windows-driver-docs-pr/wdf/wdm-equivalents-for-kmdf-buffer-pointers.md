---
title: WDM Equivalents for WDF Buffer Pointers
description: WDM Equivalents for WDF Buffer Pointers
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# WDM Equivalents for WDF Buffer Pointers


A Kernel-Mode Driver Framework (KMDF) or User-Mode Driver Framework (UMDF) driver uses the following methods for retrieving I/O buffers for buffered and direct I/O. Unless otherwise specified, the methods apply to both KMDF and UMDF.

-   [**WdfRequestRetrieveOutputBuffer**](/windows-hardware/drivers/ddi/wdfrequest/nf-wdfrequest-wdfrequestretrieveoutputbuffer)
-   [**WdfRequestRetrieveOutputWdmMdl (KMDF only)**](/windows-hardware/drivers/ddi/wdfrequest/nf-wdfrequest-wdfrequestretrieveoutputwdmmdl)
-   [**WdfRequestRetrieveOutputMemory**](/windows-hardware/drivers/ddi/wdfrequest/nf-wdfrequest-wdfrequestretrieveoutputmemory)
-   [**WdfRequestRetrieveInputBuffer**](/windows-hardware/drivers/ddi/wdfrequest/nf-wdfrequest-wdfrequestretrieveinputbuffer)
-   [**WdfRequestRetrieveInputWdmMdl (KMDF only)**](/windows-hardware/drivers/ddi/wdfrequest/nf-wdfrequest-wdfrequestretrieveinputwdmmdl)
-   [**WdfRequestRetrieveInputMemory**](/windows-hardware/drivers/ddi/wdfrequest/nf-wdfrequest-wdfrequestretrieveinputmemory)

The following tables describe what the retrieval methods return for IRP\_MJ\_READ, IRP\_MJ\_WRITE, and IRP\_MJ\_DEVICE\_CONTROL requests for buffered and direct I/O. Requests for neither I/O require special handling because the driver must retrieve the buffers while running in the context of the requesting user-mode process.

## <a href="" id="read"></a>Buffers for IRP\_MJ\_READ Requests


To retrieve a buffer for a read request, a KMDF driver calls one of the **WdfRequestRetrieveOutput**_Xxx_ methods. The buffer that each of these methods returns varies, depending on whether the driver performs buffered or direct I/O. The following table describes the pointer that is returned by each method in WDM terms.

| Function                                                                             | Buffered I/O                                                                                                                                    | Direct I/O                                                                                                                                                                                                |
|--------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**WdfRequestRetrieveOutputBuffer**](/windows-hardware/drivers/ddi/wdfrequest/nf-wdfrequest-wdfrequestretrieveoutputbuffer)             | **Irp-&gt;AssociatedIrp.SystemBuffer**                                                                                                          | [**MmGetSystemAddressForMdlSafe**](../kernel/mm-bad-pointer.md) (**Irp-&gt;MdlAddress**)                                                                                                          |
| [**WdfRequestRetrieveOutputWdmMdl (KMDF only)**](/windows-hardware/drivers/ddi/wdfrequest/nf-wdfrequest-wdfrequestretrieveoutputwdmmdl) | Builds a memory descriptor list (MDL) for **Irp-&gt;AssociatedIrp.SystemBuffer** and returns the MDL.                                           | **Irp-&gt;MdlAddress**                                                                                                                                                                                    |
| [**WdfRequestRetrieveOutputMemory**](/windows-hardware/drivers/ddi/wdfrequest/nf-wdfrequest-wdfrequestretrieveoutputmemory)             | Returns a WDFMEMORY object. Call [**WdfMemoryGetBuffer**](/windows-hardware/drivers/ddi/wdfmemory/nf-wdfmemory-wdfmemorygetbuffer) on this object to get **Irp-&gt;AssociatedIrp.SystemBuffer**. | Returns a WDFMEMORY object. Call [**WdfMemoryGetBuffer**](/windows-hardware/drivers/ddi/wdfmemory/nf-wdfmemory-wdfmemorygetbuffer) on this object to get [**MmGetSystemAddressForMdlSafe**](../kernel/mm-bad-pointer.md) (**Irp-&gt;MdlAddress**). |

 

## <a href="" id="write"></a>Buffers for IRP\_MJ\_WRITE Requests


To retrieve a buffer for a write request, a KMDF driver calls one of the **WdfRequestRetrieveInput**_Xxx_ methods. The buffer that each of these methods returns varies, depending on whether the driver performs buffered or direct I/O. The following table describes the pointer that is returned by each method in WDM terms.

| Function                                                                           | Buffered I/O                                                                                                                                    | Direct I/O                                                                                                                                                                                                |
|------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**WdfRequestRetrieveInputBuffer**](/windows-hardware/drivers/ddi/wdfrequest/nf-wdfrequest-wdfrequestretrieveinputbuffer)             | **Irp-&gt;AssociatedIrp.SystemBuffer**                                                                                                          | [**MmGetSystemAddressForMdlSafe**](../kernel/mm-bad-pointer.md) (**Irp-&gt;MdlAddress**)                                                                                                          |
| [**WdfRequestRetrieveInputWdmMdl (KMDF only)**](/windows-hardware/drivers/ddi/wdfrequest/nf-wdfrequest-wdfrequestretrieveinputwdmmdl) | Builds an MDL for **Irp-&gt;AssociatedIrp.SystemBuffer** and returns the MDL.                                                                   | **Irp-&gt;MdlAddress**                                                                                                                                                                                    |
| [**WdfRequestRetrieveInputMemory**](/windows-hardware/drivers/ddi/wdfrequest/nf-wdfrequest-wdfrequestretrieveinputmemory)             | Returns a WDFMEMORY object. Call [**WdfMemoryGetBuffer**](/windows-hardware/drivers/ddi/wdfmemory/nf-wdfmemory-wdfmemorygetbuffer) on this object to get **Irp-&gt;AssociatedIrp.SystemBuffer**. | Returns a WDFMEMORY object. Call [**WdfMemoryGetBuffer**](/windows-hardware/drivers/ddi/wdfmemory/nf-wdfmemory-wdfmemorygetbuffer) on this object to get [**MmGetSystemAddressForMdlSafe**](../kernel/mm-bad-pointer.md) (**Irp-&gt;MdlAddress**). |

 

## <a href="" id="device-control"></a>Buffers for IRP\_MJ\_DEVICE\_CONTROL Requests


To retrieve a buffer for a device I/O control request, a KMDF driver calls either **WdfRequestRetrieveInputXxx** or **WdfRequestRetrieveOutputXxx** methods. The buffer that each of these methods returns varies, depending on whether the driver performs [buffered or direct I/O](./accessing-data-buffers-in-wdf-drivers.md), as shown in the following table:

| Function                                                                             | Buffered I/O                                                                                                                                    | Direct I/O                                                                                                                                                                                                |
|--------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**WdfRequestRetrieveInputBuffer**](/windows-hardware/drivers/ddi/wdfrequest/nf-wdfrequest-wdfrequestretrieveinputbuffer)               | **Irp-&gt;AssociatedIrp.SystemBuffer**                                                                                                          | [**MmGetSystemAddressForMdlSafe**](../kernel/mm-bad-pointer.md) (**Irp-&gt;MdlAddress**)                                                                                                          |
| [**WdfRequestRetrieveInputWdmMdl (KMDF only)**](/windows-hardware/drivers/ddi/wdfrequest/nf-wdfrequest-wdfrequestretrieveinputwdmmdl)   | Builds an MDL for **Irp-&gt;AssociatedIrp.SystemBuffer** and returns the MDL.                                                                   | Builds an MDL for **Irp-&gt;AssociatedIrp.SystemBuffer** and returns the MDL.                                                                                                                             |
| [**WdfRequestRetrieveInputMemory**](/windows-hardware/drivers/ddi/wdfrequest/nf-wdfrequest-wdfrequestretrieveinputmemory)               | Returns a WDFMEMORY object. Call [**WdfMemoryGetBuffer**](/windows-hardware/drivers/ddi/wdfmemory/nf-wdfmemory-wdfmemorygetbuffer) on this object to get **Irp-&gt;AssociatedIrp.SystemBuffer**. | Returns a WDFMEMORY object. Call [**WdfMemoryGetBuffer**](/windows-hardware/drivers/ddi/wdfmemory/nf-wdfmemory-wdfmemorygetbuffer) on this object to get [**MmGetSystemAddressForMdlSafe**](../kernel/mm-bad-pointer.md) (**Irp-&gt;MdlAddress**). |
| [**WdfRequestRetrieveOutputBuffer**](/windows-hardware/drivers/ddi/wdfrequest/nf-wdfrequest-wdfrequestretrieveoutputbuffer)             | **Irp-&gt;AssociatedIrp.SystemBuffer**                                                                                                          | [**MmGetSystemAddressForMdlSafe**](../kernel/mm-bad-pointer.md) (**Irp-&gt;MdlAddress**)                                                                                                          |
| [**WdfRequestRetrieveOutputWdmMdl (KMDF only)**](/windows-hardware/drivers/ddi/wdfrequest/nf-wdfrequest-wdfrequestretrieveoutputwdmmdl) | Builds a memory descriptor list (MDL) for **Irp-&gt;AssociatedIrp.SystemBuffer** and returns the MDL.                                           | **Irp-&gt;MdlAddress**                                                                                                                                                                                    |
| [**WdfRequestRetrieveOutputMemory**](/windows-hardware/drivers/ddi/wdfrequest/nf-wdfrequest-wdfrequestretrieveoutputmemory)             | Returns a WDFMEMORY object. Call [**WdfMemoryGetBuffer**](/windows-hardware/drivers/ddi/wdfmemory/nf-wdfmemory-wdfmemorygetbuffer) on this object to get **Irp-&gt;AssociatedIrp.SystemBuffer**. | Returns a WDFMEMORY object. Call [**WdfMemoryGetBuffer**](/windows-hardware/drivers/ddi/wdfmemory/nf-wdfmemory-wdfmemorygetbuffer) on this object to get [**MmGetSystemAddressForMdlSafe**](../kernel/mm-bad-pointer.md) (**Irp-&gt;MdlAddress**). |

 

 

