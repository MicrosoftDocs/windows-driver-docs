---
title: DDI usage rule set (KMDF)
description: Use these rules to verify that your driver correctly uses KMDF DDIs correctly.
ms.assetid: 0A3A012C-A1BB-43A5-B38D-4E98928D07E5
---

# DDI usage rule set (KMDF)


Use these rules to verify that your driver correctly uses KMDF DDIs correctly.

## In this section


<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<thead>
<tr class="header">
<th align="left">Topic</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td align="left"><p>[<strong>BufAfterReqCompletedIoctl</strong>](kmdf-bufafterreqcompletedioctl.md)</p></td>
<td align="left"><p>The [<strong>BufAfterReqCompletedIoctl</strong>](kmdf-bufafterreqcompletedioctl.md) rule specifies that within the [<em>EvtIoDeviceControl</em>](https://msdn.microsoft.com/library/windows/hardware/ff541758) callback function, the I/O request buffer retrieved cannot be accessed after the I/O request is completed.</p></td>
</tr>
<tr class="even">
<td align="left"><p>[<strong>BufAfterReqCompletedIntIoctl</strong>](kmdf-bufafterreqcompletedintioctl.md)</p></td>
<td align="left"><p>The [<strong>BufAfterReqCompletedIntIoctl</strong>](kmdf-bufafterreqcompletedintioctl.md) rule specifies that after a request is completed, its buffer cannot be accessed (inside [<em>EvtIoInternalDeviceControl</em>](https://msdn.microsoft.com/library/windows/hardware/ff541768) callback function only). The buffer is retrieved by calling [<strong>WdfRequestRetrieveOutputBuffer</strong>](https://msdn.microsoft.com/library/windows/hardware/ff550018) or [<strong>WdfRequestRetrieveUnsafeUserOutputBuffer</strong>](https://msdn.microsoft.com/library/windows/hardware/ff550024) or [<strong>WdfRequestRetrieveInputBuffer</strong>](https://msdn.microsoft.com/library/windows/hardware/ff550014) or [<strong>WdfRequestRetrieveUnsafeUserInputBuffer</strong>](https://msdn.microsoft.com/library/windows/hardware/ff550022).</p></td>
</tr>
<tr class="odd">
<td align="left"><p>[<strong>BufAfterReqCompletedIntIoctlA</strong>](kmdf-bufafterreqcompletedintioctla.md)</p></td>
<td align="left"><p>The [<strong>BufAfterReqCompletedIntIoctlA</strong>](kmdf-bufafterreqcompletedintioctla.md) rule verifies that after a request is completed, its buffer cannot be accessed (inside [<em>EvtIoInternalDeviceControl</em>](https://msdn.microsoft.com/library/windows/hardware/ff541768) callback only). The buffer was retrieved by calling [<strong>WdfRequestRetrieveInputBuffer</strong>](https://msdn.microsoft.com/library/windows/hardware/ff550014) or [<strong>WdfRequestRetrieveOutputBuffer</strong>](https://msdn.microsoft.com/library/windows/hardware/ff550018) or [<strong>WdfRequestRetrieveUnsafeUserInputBuffer</strong>](https://msdn.microsoft.com/library/windows/hardware/ff550022) or [<strong>WdfRequestRetrieveUnsafeUserOutputBuffer</strong>](https://msdn.microsoft.com/library/windows/hardware/ff550024).</p></td>
</tr>
<tr class="even">
<td align="left"><p>[<strong>BufAfterReqCompletedIoctlA</strong>](kmdf-bufafterreqcompletedioctla.md)</p></td>
<td align="left"><p>The [<strong>BufAfterReqCompletedIoctlA</strong>](kmdf-bufafterreqcompletedioctla.md) rule specifies that within the [<em>EvtIoDeviceControl</em>](https://msdn.microsoft.com/library/windows/hardware/ff541758) callback function, the I/O request buffer retrieved cannot be accessed after the I/O request is completed.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>[<strong>BufAfterReqCompletedRead</strong>](kmdf-bufafterreqcompletedread.md)</p></td>
<td align="left"><p>The [<strong>BufAfterReqCompletedRead</strong>](kmdf-bufafterreqcompletedread.md) rule specifies that within the [<em>EvtIoRead</em>](https://msdn.microsoft.com/library/windows/hardware/ff541776) callback function, the I/O request buffer retrieved cannot be accessed after the I/O request is completed. There are 14 DDIs that serve as possible buffer access methods.</p></td>
</tr>
<tr class="even">
<td align="left"><p>[<strong>BufAfterReqCompletedReadA</strong>](kmdf-bufafterreqcompletedreada.md)</p></td>
<td align="left"><p>The BufAfterReqCompletedReadA rule specifies that within the [<em>EvtIoRead</em>](https://msdn.microsoft.com/library/windows/hardware/ff541776) callback function, the I/O request buffer retrieved cannot be accessed after the I/O request is completed. There are 14 DDIs that serve as possible buffer access methods.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>[<strong>BufAfterReqCompletedWrite</strong>](kmdf-bufafterreqcompletedwrite.md)</p></td>
<td align="left"><p>The BufAfterReqCompletedWrite rule specifies that within the [<em>EvtIoWrite</em>](https://msdn.microsoft.com/library/windows/hardware/ff541813) callback function, the I/O request buffer retrieved cannot be accessed after the I/O request is completed.</p></td>
</tr>
<tr class="even">
<td align="left"><p>[<strong>BufAfterReqCompletedWriteA</strong>](kmdf-bufafterreqcompletedwritea.md)</p></td>
<td align="left"><p>The BufAfterReqCompletedWriteA rule specifies that within the [<em>EvtIoWrite</em>](https://msdn.microsoft.com/library/windows/hardware/ff541813) callback function, the I/O request buffer retrieved cannot be accessed after the I/O request is completed.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>[<strong>ChildDeviceInitApi</strong>](kmdf-childdeviceinitapi.md)</p></td>
<td align="left"><p>The [<strong>ChildDeviceInitApi</strong>](kmdf-childdeviceinitapi.md) rule specifies that for a child device, the framework device object initialization methods must be called before the driver calls the [<strong>WdfDeviceCreate</strong>](https://msdn.microsoft.com/library/windows/hardware/ff545926) method for the child device object.</p></td>
</tr>
<tr class="even">
<td align="left"><p>[<strong>ControlDeviceDeleted</strong>](kmdf-controldevicedeleted.md)</p></td>
<td align="left"><p>The ControDeviceDeleted rule specifies that if a PnP driver creates a control device object, the driver must delete the control device object in one of the cleanup callback functions before the driver unloads.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>[<strong>ControlDeviceInitAPI</strong>](kmdf-controldeviceinitapi.md)</p></td>
<td align="left"><p>The ControlDeviceInitAPI rule specifies that [<strong>WdfControlDeviceInitAllocate</strong>](https://msdn.microsoft.com/library/windows/hardware/ff545841) and all other device object initialization DDIs that set up a [<strong>WDFDEVICE_INIT</strong>](https://msdn.microsoft.com/library/windows/hardware/ff546951) structure for the control device must be called before [<strong>WdfDeviceCreate</strong>](https://msdn.microsoft.com/library/windows/hardware/ff545926) for the control device.</p></td>
</tr>
<tr class="even">
<td align="left"><p>[<strong>CtlDeviceFinishInitDeviceAdd</strong>](kmdf-ctldevicefinishinitdeviceadd.md)</p></td>
<td align="left"><p>The [<strong>CtlDeviceFinishInitDeviceAdd</strong>](kmdf-ctldevicefinishinitdeviceadd.md) rule specifies that if a driver creates control device object in an [<em>EvtDriverDeviceAdd</em>](https://msdn.microsoft.com/library/windows/hardware/ff541693) callback function, it must call [<strong>WdfControlFinishInitializing</strong>](https://msdn.microsoft.com/library/windows/hardware/ff545854) after the device has been created and before it exits from the <strong>EvtDriverDeviceAdd</strong> callback function. This rule does not apply for non-PnP drivers.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>[<strong>CtlDeviceFinishInitDrEntry</strong>](kmdf-ctldevicefinishinitdrentry.md)</p></td>
<td align="left"><p>The CtlDeviceFinishInitDrEntry rule specifies that if a driver creates a control device object in a [<strong>DriverEntry</strong>](https://msdn.microsoft.com/library/windows/hardware/ff540807) callback function, it must call [<strong>WdfControlFinishInitializing</strong>](https://msdn.microsoft.com/library/windows/hardware/ff545854) after the device has been created and before it exits from the [<em>EvtDriverDeviceAdd</em>](https://msdn.microsoft.com/library/windows/hardware/ff541693) callback function. This rule does not apply for non-PnP drivers.</p></td>
</tr>
<tr class="even">
<td align="left"><p>[<strong>DeviceCreateFail</strong>](kmdf-devicecreatefail.md)</p></td>
<td align="left"><p>The [<strong>DeviceCreateFail</strong>](kmdf-devicecreatefail.md) rule specifies that EVT_WDF_DRIVER_DEVICE_ADD returns an error status when the call to [<strong>WdfDeviceCreate</strong>](https://msdn.microsoft.com/library/windows/hardware/ff545926) fails.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>[<strong>DeviceInitAllocate</strong>](kmdf-deviceinitallocate.md)</p></td>
<td align="left"><p>The [<strong>DeviceInitAllocate</strong>](kmdf-deviceinitallocate.md) rule specifies that, for a PDO device or a control device object, the framework device object initialization methods [<strong>WdfPdoInitAllocate</strong>](https://msdn.microsoft.com/library/windows/hardware/ff548786) or [<strong>WdfControlDeviceInitAllocate</strong>](https://msdn.microsoft.com/library/windows/hardware/ff545841) must be called before the driver calls [<strong>WdfDeviceCreate</strong>](https://msdn.microsoft.com/library/windows/hardware/ff545926).</p></td>
</tr>
<tr class="even">
<td align="left"><p>[<strong>DeviceInitAPI</strong>](kmdf-deviceinitapi.md)</p></td>
<td align="left"><p>For an FDO device, the framework device object initialization methods and the framework FDO initialization methods must be called before the driver calls the [<strong>WdfDeviceCreate</strong>](https://msdn.microsoft.com/library/windows/hardware/ff545926) method for the device object.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>[<strong>DoubleDeviceInitFree</strong>](kmdf-doubledeviceinitfree.md)</p></td>
<td align="left"><p>The [<strong>DoubleDeviceInitFree</strong>](kmdf-doubledeviceinitfree.md) rule specifies that drivers should not free device initialization structure twice.</p></td>
</tr>
<tr class="even">
<td align="left"><p>[<strong>DriverCreate</strong>](kmdf-drivercreate.md)</p></td>
<td align="left"><p>The [<strong>DriverCreate</strong>](kmdf-drivercreate.md) rule specifies that a driver that uses Kernel Mode Driver Framework (KMDF) must call the [<strong>WdfDriverCreate</strong>](https://msdn.microsoft.com/library/windows/hardware/ff547175) method to create a framework driver object from within its [<strong>DriverEntry</strong>](https://msdn.microsoft.com/library/windows/hardware/ff540807) routine.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>[<strong>InitFreeDeviceCallback</strong>](kmdf-initfreedevicecallback.md)</p></td>
<td align="left"><p>The InitFreeDeviceCallback rule specifies that a driver must call [<strong>WdfDeviceInitFree</strong>](https://msdn.microsoft.com/library/windows/hardware/ff546050) if the driver encounters an error while it initializes a new framework device object, and if the driver received the [<strong>WDFDEVICE_INIT</strong>](https://msdn.microsoft.com/library/windows/hardware/ff546951) structure from a call to [<strong>WdfControlDeviceInitAllocate</strong>](https://msdn.microsoft.com/library/windows/hardware/ff545841).</p></td>
</tr>
<tr class="even">
<td align="left"><p>[<strong>InitFreeDeviceCreate</strong>](kmdf-initfreedevicecreate.md)</p></td>
<td align="left"><p>The [<strong>InitFreeDeviceCreate</strong>](kmdf-initfreedevicecreate.md) rule specifies that a driver must call [<strong>WdfDeviceInitFree</strong>](https://msdn.microsoft.com/library/windows/hardware/ff546050) instead of [<strong>WdfDeviceCreate</strong>](https://msdn.microsoft.com/library/windows/hardware/ff545926) if an error occurs in one of the device object initialization methods and if the driver received the [<strong>WDFDEVICE_INIT</strong>](https://msdn.microsoft.com/library/windows/hardware/ff546951) structure from a call to [<strong>WdfControlDeviceInitAllocate</strong>](https://msdn.microsoft.com/library/windows/hardware/ff545841).</p></td>
</tr>
<tr class="odd">
<td align="left"><p>[<strong>InitFreeDeviceCreateType2</strong>](kmdf-initfreedevicecreatetype2.md)</p></td>
<td align="left"><p>The InitFreeDeviceCreateType2 rule specifies that a driver must not call [<strong>WdfDeviceCreate</strong>](https://msdn.microsoft.com/library/windows/hardware/ff545926) after it calls [<strong>WdfDeviceInitFree</strong>](https://msdn.microsoft.com/library/windows/hardware/ff546050).</p></td>
</tr>
<tr class="even">
<td align="left"><p>[<strong>InitFreeDeviceCreateType4</strong>](kmdf-initfreedevicecreatetype4.md)</p></td>
<td align="left"><p>The [<strong>InitFreeDeviceCreateType4</strong>](kmdf-initfreedevicecreatetype4.md) rule specifies that a driver must call [<strong>WdfDeviceInitFree</strong>](https://msdn.microsoft.com/library/windows/hardware/ff546050) if the driver encounters an error while it calls [<strong>WdfDeviceCreate</strong>](https://msdn.microsoft.com/library/windows/hardware/ff545926) and if the driver received the [<strong>WDFDEVICE_INIT</strong>](https://msdn.microsoft.com/library/windows/hardware/ff546951) structure from a call to [<strong>WdfControlDeviceInitAllocate</strong>](https://msdn.microsoft.com/library/windows/hardware/ff545841).</p></td>
</tr>
<tr class="odd">
<td align="left"><p>[<strong>InitFreeNull</strong>](kmdf-initfreenull.md)</p></td>
<td align="left"><p>The [<strong>InitFreeNull</strong>](kmdf-initfreenull.md) rule specifies that DDIs receiving PWDFDEVICE_INIT as a parameter cannot be called by using a <strong>NULL</strong> pointer to a [WDFDEVICE_INIT](https://msdn.microsoft.com/library/windows/hardware/ff546951) structure.</p></td>
</tr>
<tr class="even">
<td align="left"><p>[<strong>MdlAfterReqCompletedIntIoctl</strong>](kmdf-mdlafterreqcompletedintioctl.md)</p></td>
<td align="left"><p>The MdlAfterReqCompletedIntIoctl rule specifies that within the [<em>EvtIoInternalDeviceControl</em>](https://msdn.microsoft.com/library/windows/hardware/ff541768) callback function, the memory descriptor list (MDL) cannot be accessed after the I/O request is completed.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>[<strong>MdlAfterReqCompletedIntIoctlA</strong>](kmdf-mdlafterreqcompletedintioctla.md)</p></td>
<td align="left"><p>The [<strong>MdlAfterReqCompletedIntIoctlA</strong>](kmdf-mdlafterreqcompletedintioctla.md) rule specifies that within the [<em>EvtIoInternalDeviceControl</em>](https://msdn.microsoft.com/library/windows/hardware/ff541768) callback function, the memory descriptor list (MDL) cannot be accessed after the I/O request is completed.</p></td>
</tr>
<tr class="even">
<td align="left"><p>[<strong>MdlAfterReqCompletedIoctl</strong>](kmdf-mdlafterreqcompletedioctl.md)</p></td>
<td align="left"><p>The [<strong>MdlAfterReqCompletedIoctl</strong>](kmdf-mdlafterreqcompletedioctl.md) rule specifies that within the [<em>EvtIoDeviceControl</em>](https://msdn.microsoft.com/library/windows/hardware/ff541758) callback function, the memory descriptor list (MDL) cannot be accessed after the I/O request is completed.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>[<strong>MdlAfterReqCompletedIoctlA</strong>](kmdf-mdlafterreqcompletedioctla.md)</p></td>
<td align="left"><p>The [<strong>MdlAfterReqCompletedIoctlA</strong>](kmdf-mdlafterreqcompletedioctla.md) rule specifies that within the [<em>EvtIoDeviceControl</em>](https://msdn.microsoft.com/library/windows/hardware/ff541758) callback function, the memory descriptor list (MDL) cannot be accessed after the I/O request is completed.</p></td>
</tr>
<tr class="even">
<td align="left"><p>[<strong>MdlAfterReqCompletedRead</strong>](kmdf-mdlafterreqcompletedread.md)</p></td>
<td align="left"><p>The [<strong>MdlAfterReqCompletedRead</strong>](kmdf-mdlafterreqcompletedread.md) rule specifies that within the [<em>EvtIoRead</em>](https://msdn.microsoft.com/library/windows/hardware/ff541776) callback function, the memory descriptor list (MDL) object retrieved cannot be accessed after the I/O request is completed.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>[<strong>MdlAfterReqCompletedReadA</strong>](kmdf-mdlafterreqcompletedreada.md)</p></td>
<td align="left"><p>The [<strong>MdlAfterReqCompletedReadA</strong>](kmdf-mdlafterreqcompletedreada.md) rule specifies that within the [<em>EvtIoRead</em>](https://msdn.microsoft.com/library/windows/hardware/ff541776) callback function, the memory descriptor list (MDL) object retrieved cannot be accessed after the I/O request is completed.</p></td>
</tr>
<tr class="even">
<td align="left"><p>[<strong>MdlAfterReqCompletedWrite</strong>](kmdf-mdlafterreqcompletedwrite.md)</p></td>
<td align="left"><p>The [<strong>MdlAfterReqCompletedWrite</strong>](kmdf-mdlafterreqcompletedwrite.md) rule specifies that within the [<em>EvtIoWrite</em>](https://msdn.microsoft.com/library/windows/hardware/ff541813) callback function, the memory descriptor list (MDL) object retrieved cannot be accessed after the I/O request is completed.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>[<strong>MdlAfterReqCompletedWriteA</strong>](kmdf-mdlafterreqcompletedwritea.md)</p></td>
<td align="left"><p>The [<strong>MdlAfterReqCompletedWriteA</strong>](kmdf-mdlafterreqcompletedwritea.md) rule specifies that within the [<em>EvtIoWrite</em>](https://msdn.microsoft.com/library/windows/hardware/ff541813) callback function, the memory descriptor list (MDL) object retrieved cannot be accessed after the I/O request is completed.</p></td>
</tr>
<tr class="even">
<td align="left"><p>[<strong>MemAfterReqCompletedIntIoctl</strong>](kmdf-memafterreqcompletedintioctl.md)</p></td>
<td align="left"><p>The [<strong>MemAfterReqCompletedIntIoctl</strong>](kmdf-memafterreqcompletedintioctl.md) rule specifies that within the [<em>EvtIoInternalDeviceControl</em>](https://msdn.microsoft.com/library/windows/hardware/ff541768) callback function, the framework memory object cannot be accessed after the I/O request is completed.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>[<strong>MemAfterReqCompletedIntIoctlA</strong>](kmdf-memafterreqcompletedintioctla.md)</p></td>
<td align="left"><p>The [<strong>MemAfterReqCompletedIntIoctlA</strong>](kmdf-memafterreqcompletedintioctla.md) rule specifies that within the [<em>EvtIoInternalDeviceControl</em>](https://msdn.microsoft.com/library/windows/hardware/ff541768) callback function, the framework memory object cannot be accessed after the I/O request is completed.</p></td>
</tr>
<tr class="even">
<td align="left"><p>[<strong>MemAfterReqCompletedIoctl</strong>](kmdf-memafterreqcompletedioctl.md)</p></td>
<td align="left"><p>The [<strong>MemAfterReqCompletedIoctl</strong>](kmdf-memafterreqcompletedioctl.md) rule specifies that within the [<em>EvtIoDeviceControl</em>](https://msdn.microsoft.com/library/windows/hardware/ff541758) callback function, the framework memory object cannot be accessed after the I/O request is completed.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>[<strong>MemAfterReqCompletedIoctlA</strong>](kmdf-memafterreqcompletedioctla.md)</p></td>
<td align="left"><p>The [<strong>MemAfterReqCompletedIoctlA</strong>](kmdf-memafterreqcompletedioctla.md) rule specifies that within the [<em>EvtIoDeviceControl</em>](https://msdn.microsoft.com/library/windows/hardware/ff541758) callback function, the framework memory object cannot be accessed after the I/O request is completed.</p></td>
</tr>
<tr class="even">
<td align="left"><p>[<strong>MemAfterReqCompletedRead</strong>](kmdf-memafterreqcompletedread.md)</p></td>
<td align="left"><p>The [<strong>MemAfterReqCompletedRead</strong>](kmdf-memafterreqcompletedread.md) rule specifies that within the [<em>EvtIoRead</em>](https://msdn.microsoft.com/library/windows/hardware/ff541776) callback function, the framework memory object cannot be accessed after the I/O request is completed.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>[<strong>MemAfterReqCompletedReadA</strong>](kmdf-memafterreqcompletedreada.md)</p></td>
<td align="left"><p>The [<strong>MemAfterReqCompletedReadA</strong>](kmdf-memafterreqcompletedreada.md) rule specifies that within the [<em>EvtIoRead</em>](https://msdn.microsoft.com/library/windows/hardware/ff541776) callback function, the framework memory object cannot be accessed after the I/O request is completed.</p></td>
</tr>
<tr class="even">
<td align="left"><p>[<strong>MemAfterReqCompletedWrite</strong>](kmdf-memafterreqcompletedwrite.md)</p></td>
<td align="left"><p>The [<strong>MemAfterReqCompletedWrite</strong>](kmdf-memafterreqcompletedwrite.md) rule specifies that within the [<em>EvtIoWrite</em>](https://msdn.microsoft.com/library/windows/hardware/ff541813) callback function, the framework memory object cannot be accessed after the I/O request is completed.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>[<strong>MemAfterReqCompletedWriteA</strong>](kmdf-memafterreqcompletedwritea.md)</p></td>
<td align="left"><p>The [<strong>MemAfterReqCompletedWriteA</strong>](kmdf-memafterreqcompletedwritea.md) rule specifies that within the [<em>EvtIoWrite</em>](https://msdn.microsoft.com/library/windows/hardware/ff541813) callback function, the framework memory object cannot be accessed after the I/O request is completed.</p></td>
</tr>
<tr class="even">
<td align="left"><p>[<strong>NullCheck</strong>](nullcheck.md)</p></td>
<td align="left"><p>The NullCheck rule verifies that a NULL value inside the driver code is not dereferenced later in the driver. This rule reports a defect if either of these conditions is true:</p>
<ul>
<li>There is an assignment of NULL that is dereferenced later.</li>
<li>There is a global/parameter to a procedure in a driver that may be NULL that is dereferenced later, and there is an explicit check in the driver that suggests that the initial value of the pointer may be NULL.</li>
</ul>
<p>With NullCheck rule violations, the most relevant code statements are highlighted in the trace tree pane. For more information about working with report output, see [Static Driver Verifier Report](https://msdn.microsoft.com/library/windows/hardware/ff552834) and [Understanding the Trace Viewer](https://msdn.microsoft.com/library/windows/hardware/ff554020).</p>
<p></p></td>
</tr>
<tr class="odd">
<td align="left"><p>[<strong>PdoDeviceInitAPI</strong>](kmdf-pdodeviceinitapi.md)</p></td>
<td align="left"><p>The [<strong>PdoDeviceInitAPI</strong>](kmdf-pdodeviceinitapi.md) rule specifies that [<strong>WdfPdoInitAllocate</strong>](https://msdn.microsoft.com/library/windows/hardware/ff548786) and all other device object initialization DDIs that set up a [<strong>WDFDEVICE_INIT</strong>](https://msdn.microsoft.com/library/windows/hardware/ff546951) structure for the physical device object (PDO) must be called before the driver calls [<strong>WdfDeviceCreate</strong>](https://msdn.microsoft.com/library/windows/hardware/ff545926) for the PDO.</p></td>
</tr>
<tr class="even">
<td align="left"><p>[<strong>PdoInitFreeDeviceCallback</strong>](kmdf-pdoinitfreedevicecallback.md)</p></td>
<td align="left"><p>The [<strong>PdoInitFreeDeviceCallback</strong>](kmdf-pdoinitfreedevicecallback.md) rule specifies that the driver must call [<strong>WdfDeviceInitFree</strong>](https://msdn.microsoft.com/library/windows/hardware/ff546050) if an error occurs when the driver calls any framework device object initialization function.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>[<strong>PdoInitFreeDeviceCreate</strong>](kmdf-pdoinitfreedevicecreate.md)</p></td>
<td align="left"><p>The [<strong>PdoInitFreeDeviceCreate</strong>](kmdf-pdoinitfreedevicecreate.md) rule specifies that a driver must call [<strong>WdfDeviceInitFree</strong>](https://msdn.microsoft.com/library/windows/hardware/ff546050) instead of [<strong>WdfDeviceCreate</strong>](https://msdn.microsoft.com/library/windows/hardware/ff545926) if an error occurs in one of the device object initialization functions and if the driver received the WDFDEVICE_INIT structure from a call to [<strong>WdfPdoInitAllocate</strong>](https://msdn.microsoft.com/library/windows/hardware/ff548786).</p></td>
</tr>
<tr class="even">
<td align="left"><p>[<strong>PdoInitFreeDeviceCreateType2</strong>](kmdf-pdoinitfreedevicecreatetype2.md)</p></td>
<td align="left"><p>The PdoInitFreeDeviceCreateType2 rule specifies that a driver must not call [<strong>WdfDeviceCreate</strong>](https://msdn.microsoft.com/library/windows/hardware/ff545926) after it calls [<strong>WdfDeviceInitFree</strong>](https://msdn.microsoft.com/library/windows/hardware/ff546050).</p></td>
</tr>
<tr class="odd">
<td align="left"><p>[<strong>PdoInitFreeDeviceCreateType4</strong>](kmdf-pdoinitfreedevicecreatetype4.md)</p></td>
<td align="left"><p>The PdoInitFreeDeviceCreateType4 rule specifies that the driver must call [<strong>WdfDeviceInitFree</strong>](https://msdn.microsoft.com/library/windows/hardware/ff546050) if an error occurs when the driver calls [<strong>WdfDeviceCreate</strong>](https://msdn.microsoft.com/library/windows/hardware/ff545926).</p></td>
</tr>
<tr class="even">
<td align="left"><p>[<strong>ControlDeviceInitAllocate</strong>](kmdf-controldeviceinitallocate.md)</p></td>
<td align="left"><p>The [<strong>ControlDeviceInitAllocate</strong>](kmdf-controldeviceinitallocate.md) rule specifies that for a control device object, the driver must call the framework device object initialization method [<strong>WdfControlDeviceInitAllocate</strong>](https://msdn.microsoft.com/library/windows/hardware/ff545841) before the driver calls [<strong>WdfDeviceCreate</strong>](https://msdn.microsoft.com/library/windows/hardware/ff545926).</p></td>
</tr>
<tr class="odd">
<td align="left"><p>[<strong>InputBufferAPI</strong>](kmdf-inputbufferapi.md)</p></td>
<td align="left"><p>The [<strong>InputBufferAPI</strong>](kmdf-inputbufferapi.md) rule specifies that the correct DDIs for buffer retrieval are used in the [<em>EvtIoRead</em>](https://msdn.microsoft.com/library/windows/hardware/ff541776)callback function. Within the <em>EvtIoRead</em> callback function, the following DDIs cannot be called for buffer retrieval:</p></td>
</tr>
</tbody>
</table>

 

**To select the DDI usage rule set**

1.  Select your driver project (.vcxProj) in Microsoft Visual Studio. From the **Driver** menu, click **Launch Static Driver Verifier…**.

2.  Click the **Rules** tab. Under **Rule Sets**, select **DDIUsage**.

    To select the default rule set from a Visual Studio developer command prompt window, specify **DDIUsage.sdv** with the **/check** option. For example:

    ```
    msbuild /t:sdv /p:Inputs="/check:DDIUsage.sdv" mydriver.VcxProj /p:Configuration="Win8 Release" /p:Platform=Win32
    ```

    For more information, see [Using Static Driver Verifier to Find Defects in Drivers](https://msdn.microsoft.com/library/windows/hardware/hh454281) and [Static Driver Verifier commands (MSBuild)](https://msdn.microsoft.com/library/windows/hardware/hh466459).

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bdevtest\devtest%5D:%20DDI%20usage%20rule%20set%20%28KMDF%29%20%20RELEASE:%20%281/17/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




