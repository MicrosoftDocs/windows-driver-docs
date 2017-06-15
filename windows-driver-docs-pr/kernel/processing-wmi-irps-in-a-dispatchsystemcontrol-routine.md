---
title: Processing WMI IRPs in a DispatchSystemControl Routine
author: windows-driver-content
description: Processing WMI IRPs in a DispatchSystemControl Routine
MS-HAID:
- 'WMI\_b27d7cc8-f2ce-473e-ab59-d7b99d303a97.xml'
- 'kernel.processing\_wmi\_irps\_in\_a\_dispatchsystemcontrol\_routine'
MSHAttr:
- 'PreferredSiteName:MSDN'
- 'PreferredLib:/library/windows/hardware'
ms.assetid: 9f1fc209-ee32-4270-87e5-e360ca5eca17
keywords: ["WMI WDK kernel , requests", "requests WDK WMI", "IRPs WDK WMI", "DispatchSystemControl routine"]
---

# Processing WMI IRPs in a DispatchSystemControl Routine


## <a href="" id="ddk-processing-wmi-irps-in-a-dispatchsystemcontrol-routine-kg"></a>


A driver that handles WMI IRPs in its [*DispatchSystemControl*](https://msdn.microsoft.com/library/windows/hardware/ff543412) routine must handle such an IRP only if the device object pointer at **Parameters.WMI.ProviderId** matches the pointer passed by the driver in its call to [**IoWMIRegistrationControl**](https://msdn.microsoft.com/library/windows/hardware/ff550480). Otherwise, the driver must forward the IRP to the next lower driver.

If the driver handles the request, it must:

Check the GUID at **Parameters.WMI.DataPath** to determine whether it represents a data block supported by the driver and, if not, fail the IRP with STATUS\_WMI\_GUID\_NOT\_FOUND.

A driver should check the input **WNODE\_*XXX*** structure at **Parameters.WMI.Buffer** for the instance name when handling any of the following requests:

[**IRP\_MN\_QUERY\_SINGLE\_INSTANCE**](https://msdn.microsoft.com/library/windows/hardware/ff551718)
[**IRP\_MN\_CHANGE\_SINGLE\_INSTANCE**](https://msdn.microsoft.com/library/windows/hardware/ff550831)
[**IRP\_MN\_CHANGE\_SINGLE\_ITEM**](https://msdn.microsoft.com/library/windows/hardware/ff550836)
[**IRP\_MN\_EXECUTE\_METHOD**](https://msdn.microsoft.com/library/windows/hardware/ff550868)
The driver should check for the instance name as follows:

-   If WNODE\_FLAG\_STATIC\_INSTANCE\_NAMES is set in **WnodeHeader.Flags**, use **InstanceIndex** as an index into the driver's list of static instance names for that block.

-   If WNODE\_FLAG\_STATIC\_INSTANCE\_NAMES is clear in **WnodeHeader.Flags**, use **OffsetInstanceName** as an offset to the instance name string in the input **WNODE\_*XXX*** structure. **OffsetInstanceName** is the offset in bytes from the beginning of the structure to a USHORT that indicates the length of the instance name string in bytes (not characters), including the NUL terminator if present, followed by the string itself in Unicode.

If the driver cannot locate the instance specified by **InstanceIndex** or **OffsetInstanceName**, it must fail the IRP with STATUS\_WMI\_INSTANCE\_NOT\_FOUND.

For an [**IRP\_MN\_EXECUTE\_METHOD**](https://msdn.microsoft.com/library/windows/hardware/ff550868) request, check **MethodID** in the input [**WNODE\_METHOD\_ITEM**](https://msdn.microsoft.com/library/windows/hardware/ff566376) and, if the method is not valid for that data block, fail the IRP with STATUS\_WMI\_ITEMID\_NOT\_FOUND.

If the request generates output, a driver should check the size of the buffer at **Parameters.WMI.BufferSize** when handling any of the following requests:

[**IRP\_MN\_QUERY\_ALL\_DATA**](https://msdn.microsoft.com/library/windows/hardware/ff551650)
[**IRP\_MN\_QUERY\_SINGLE\_INSTANCE**](https://msdn.microsoft.com/library/windows/hardware/ff551718)
[**IRP\_MN\_EXECUTE\_METHOD**](https://msdn.microsoft.com/library/windows/hardware/ff550868)
If the buffer is too small to receive the output, but at least **sizeof**(**WNODE\_TOO\_SMALL**), the driver should succeed the IRP and write a [**WNODE\_TOO\_SMALL**](https://msdn.microsoft.com/library/windows/hardware/ff566379) structure to the buffer at **Parameters.WMI.Buffer**. If the buffer is smaller than **sizeof**(**WNODE\_TOO\_SMALL**), the driver fails the IRP with an NTSTATUS code of STATUS\_BUFFER\_TOO\_SMALL.

If the request generates output and the buffer size is adequate, write the following output to the buffer at **Parameters.WMI.Buffer**:
-   For an **IRP\_MN\_QUERY\_ALL\_DATA** request, the driver writes a [**WNODE\_ALL\_DATA**](https://msdn.microsoft.com/library/windows/hardware/ff566372) structure that contains data for all instances of the specified data block.
-   For an **IRP\_MN\_QUERY\_SINGLE\_INSTANCE** request, the driver writes a [**WNODE\_SINGLE\_INSTANCE**](https://msdn.microsoft.com/library/windows/hardware/ff566377) structure that contains data for the specified instance of a data block.
-   For an **IRP\_MN\_EXECUTE\_METHOD** if the method generates output, the driver writes the method output in driver-determined format following the input [**WNODE\_METHOD\_ITEM**](https://msdn.microsoft.com/library/windows/hardware/ff566376) in the buffer (overwriting input data, if any).

Set **Irp-&gt;IoStatus.Information** to the number of bytes written to the buffer at **Parameters.WMI.Buffer** and **Irp-&gt;IoStatus.Status** to STATUS\_SUCCESS.

Call [**IoCompleteRequest**](https://msdn.microsoft.com/library/windows/hardware/ff548343) to complete the IRP.

For more information, see [WMI WNODE\_*XXX* Structures](wmi-wnode-xxx-structures.md).

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bkernel\kernel%5D:%20Processing%20WMI%20IRPs%20in%20a%20DispatchSystemControl%20Routine%20%20RELEASE:%20%286/14/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


