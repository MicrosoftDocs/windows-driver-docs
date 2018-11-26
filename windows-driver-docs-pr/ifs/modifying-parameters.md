---
title: Modifying Parameters
description: Modifying Parameters
ms.assetid: 01accd7f-7aa6-4f83-b8b4-81c04cd48dac
keywords:
- filter manager WDK file system minifilter , modifying parameters
- swap buffers WDK file system minifilter
- buffers WDK file system minifilter
- memory descriptor lists WDK file system minifilter
- MDLs WDK file systems
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Modifying Parameters


A minifilter driver can modify certain parameters associated with an I/O operation, such as the target instance, target file object, and operation-specific parameters including buffer address and memory descriptor list (MDL) address. The minifilter driver usually modifies parameters in its preoperation callback for the I/O request. If the minifilter driver modifies parameters, it must call [**FltSetCallbackDataDirty**](https://msdn.microsoft.com/library/windows/hardware/ff544383) to notify the filter manager that the parameters have changed. It should also record changes in the context passed from its preoperation callback so they are available to its postoperation callback.

A minifilter driver can change the I/O status for an operation when completing the operation in its preoperation callback or failing the operation in its postoperation callback (such as changing a STATUS\_SUCCESS to an error status). It is not necessary to call [**FltSetCallbackDataDirty**](https://msdn.microsoft.com/library/windows/hardware/ff544383) in this case.

For more information about modifying parameters, see [Modifying the Parameters for an I/O Operation](modifying-the-parameters-for-an-i-o-operation.md).

A minifilter driver can "swap buffers" by replacing the buffer field of an I/O request with its own buffer. Such a minifilter driver is responsible for keeping the MDL and buffer fields of the I/O request in sync. The filter manager sets the FLTFL\_CALLBACK\_DATA\_SYSTEM\_BUFFER\_FLAG in the [**FLT\_CALLBACK\_DATA**](https://msdn.microsoft.com/library/windows/hardware/ff544620) structure to indicate whether a buffer is a system buffer; if so, the minifilter driver must allocate the replacement buffer from nonpaged pool and set the MDL field to **NULL**. Otherwise, the buffer can be allocated from either paged or nonpaged pool, and the minifilter driver must always create and set an MDL. (In the case of a fast I/O operation, the new buffer can be allocated from either paged or nonpaged pool and the MDL should be **NULL**.) The minifilter driver must not free the buffer or MDL it is replacing, and it must not free any MDL it has successfully inserted into a callback data structure (the filter manager will free the MDL on behalf of the minifilter driver). After making a change to an MDL or buffer, the minifilter driver must call [**FltSetCallbackDataDirty**](https://msdn.microsoft.com/library/windows/hardware/ff544383).

A minifilter driver must register a postoperation callback for any operation in which it swaps buffers. In this callback routine, the minifilter driver must free any buffers it allocated. The filter manager will free the MDL unless the minifilter driver calls [**FltRetainSwappedBufferMdlAddress**](https://msdn.microsoft.com/library/windows/hardware/ff544352); in this case, the minifilter driver is responsible for freeing the MDL. The minifilter driver can call [**FltGetSwappedBufferMdlAddress**](https://msdn.microsoft.com/library/windows/hardware/ff543161) to get the MDL for the buffer set in its preoperation callback.

If the minifilter driver is unloaded during an operation in which it has swapped buffers, the operation cannot be "drained"; instead, the operation is canceled and the filter manager waits for the operation to complete before unloading the minifilter driver.

See the SwapBuffers sample for an example of a minifilter driver that swaps buffers.

### <span id="Filter_Manager_Routines_for_Modifying_Parameters"></span><span id="filter_manager_routines_for_modifying_parameters"></span><span id="FILTER_MANAGER_ROUTINES_FOR_MODIFYING_PARAMETERS"></span>Filter Manager Routines for Modifying Parameters

The filter manager provides the following support routines for modifying I/O operation parameters in preoperation and postoperation callback routines:

[**FltClearCallbackDataDirty**](https://msdn.microsoft.com/library/windows/hardware/ff541853)

[**FltIsCallbackDataDirty**](https://msdn.microsoft.com/library/windows/hardware/ff543311)

[**FltSetCallbackDataDirty**](https://msdn.microsoft.com/library/windows/hardware/ff544383)

The following routines provide support for swapping buffers:

[**FltGetSwappedBufferMdlAddress**](https://msdn.microsoft.com/library/windows/hardware/ff543161)

[**FltRetainSwappedBufferMdlAddress**](https://msdn.microsoft.com/library/windows/hardware/ff544352)

 

 




