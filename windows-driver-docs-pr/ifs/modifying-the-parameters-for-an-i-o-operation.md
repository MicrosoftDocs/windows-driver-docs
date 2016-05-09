---
title: Modifying the Parameters for an I/O Operation
description: Modifying the Parameters for an I/O Operation
ms.assetid: 8e25842f-6f10-412f-8cb2-156bea7d7983
keywords: ["preoperation callback routines WDK file system minifilter , modifying parameters", "postoperation callback routines WDK file system minifilter , modifying parameters", "file system minifilter drivers WDK , modifying I/O parameters", "minifilter drivers WDK , modifying I/O parameters"]
---

# Modifying the Parameters for an I/O Operation


## <span id="ddk_modifying_the_parameters_for_an_io_operation_if"></span><span id="DDK_MODIFYING_THE_PARAMETERS_FOR_AN_IO_OPERATION_IF"></span>


A minifilter driver can modify the parameters for an I/O operation. For example, a minifilter driver's [**preoperation callback routine**](https://msdn.microsoft.com/library/windows/hardware/ff551109) can redirect an I/O operation to a different volume by changing the target instance for the operation. The new target instance must be an instance of the same minifilter driver at the same altitude on another volume.

The parameters for an I/O operation are found in the callback data ([**FLT\_CALLBACK\_DATA**](https://msdn.microsoft.com/library/windows/hardware/ff544620)) structure and I/O parameter block ([**FLT\_IO\_PARAMETER\_BLOCK**](https://msdn.microsoft.com/library/windows/hardware/ff544638)) structure for the operation. The minifilter driver's [**preoperation callback routine**](https://msdn.microsoft.com/library/windows/hardware/ff551109) and [**postoperation callback routine**](https://msdn.microsoft.com/library/windows/hardware/ff551107) receive a pointer to the callback data structure for the operation in the *Data* input parameter. The *Iopb* member of the callback data structure is a pointer to an I/O parameter block structure that contains the parameters for the operation.

If a minifilter driver's preoperation callback routine modifies the parameters for an I/O operation, all minifilter drivers below that minifilter driver in the minifilter driver instance stack will receive the modified parameters in their preoperation and postoperation callback routines.

The modified parameters are not received by the current minifilter driver's postoperation callback routine or by any minifilter drivers above that minifilter driver in the minifilter driver instance stack. In all situations, a minifilter driver's preoperation and postoperation callback routines receive the same input parameter values for a given I/O operation.

After modifying the parameters for an I/O operation, the preoperation or postoperation callback routine must indicate that it has done so by calling [**FltSetCallbackDataDirty**](https://msdn.microsoft.com/library/windows/hardware/ff544383), unless it has changed the contents of the callback data structure's **IoStatus** field. Otherwise, the filter manager will ignore any changes to parameter values. **FltSetCallbackDataDirty** sets the FLTFL\_CALLBACK\_DATA\_DIRTY flag in the callback data structure for the I/O operation. Minifilter drivers can test this flag by calling [**FltIsCallbackDataDirty**](https://msdn.microsoft.com/library/windows/hardware/ff543311) or clear it by calling [**FltClearCallbackDataDirty**](https://msdn.microsoft.com/library/windows/hardware/ff541853).

If a minifilter driver's preoperation callback routine modifies the parameters for an I/O operation, all minifilter drivers below that minifilter driver in the minifilter driver instance stack will receive the modified parameters in the *Data* and *FltObjects* input parameters to their preoperation and postoperation callback routines. (Minifilter drivers cannot directly modify the contents of the [**FLT\_RELATED\_OBJECTS**](https://msdn.microsoft.com/library/windows/hardware/ff544816) structure that is pointed to by the *FltObjects* parameter. However, if a minifilter driver modifies the target instance or target file object for an I/O operation, the filter manager modifies the value of the corresponding **Instance** or **FileObject** member of the FLT\_RELATED\_OBJECTS structure that is passed to lower minifilter drivers.)

Although any parameter changes that a minifilter driver's preoperation callback routine makes are not received by the minifilter driver's own postoperation callback routine, a preoperation callback routine is able to pass information about changed parameters to the minifilter driver's own postoperation callback routine. If the preoperation callback routine passes the I/O operation down the stack by returning FLT\_PREOP\_SUCCESS\_WITH\_CALLBACK or FLT\_PREOP\_SYNCHRONIZE, it can store information about changed parameter values into a minifilter driver-defined structure that is pointed to by the *CompletionContext* output parameter. The filter manager passes this structure pointer in the *CompletionContext* input parameter to the postoperation callback routine.

For more information about the parameters for an I/O operation, see [**FLT\_CALLBACK\_DATA**](https://msdn.microsoft.com/library/windows/hardware/ff544620) and [**FLT\_IO\_PARAMETER\_BLOCK**](https://msdn.microsoft.com/library/windows/hardware/ff544638).

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[ifsk\ifsk]:%20Modifying%20the%20Parameters%20for%20an%20I/O%20Operation%20%20RELEASE:%20%285/9/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




