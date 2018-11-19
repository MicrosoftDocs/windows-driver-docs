---
title: DDI usage rule set (KMDF)
description: Use these rules to verify that your driver correctly uses KMDF DDIs correctly.
ms.assetid: 0A3A012C-A1BB-43A5-B38D-4E98928D07E5
ms.date: 05/21/2018
ms.localizationpriority: medium
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
<td align="left"><p><a href="kmdf-bufafterreqcompletedioctl.md" data-raw-source="[&lt;strong&gt;BufAfterReqCompletedIoctl&lt;/strong&gt;](kmdf-bufafterreqcompletedioctl.md)"><strong>BufAfterReqCompletedIoctl</strong></a></p></td>
<td align="left"><p>The <a href="kmdf-bufafterreqcompletedioctl.md" data-raw-source="[&lt;strong&gt;BufAfterReqCompletedIoctl&lt;/strong&gt;](kmdf-bufafterreqcompletedioctl.md)"><strong>BufAfterReqCompletedIoctl</strong></a> rule specifies that within the <a href="https://msdn.microsoft.com/library/windows/hardware/ff541758" data-raw-source="[&lt;em&gt;EvtIoDeviceControl&lt;/em&gt;](https://msdn.microsoft.com/library/windows/hardware/ff541758)"><em>EvtIoDeviceControl</em></a> callback function, the I/O request buffer retrieved cannot be accessed after the I/O request is completed.</p></td>
</tr>
<tr class="even">
<td align="left"><p><a href="kmdf-bufafterreqcompletedintioctl.md" data-raw-source="[&lt;strong&gt;BufAfterReqCompletedIntIoctl&lt;/strong&gt;](kmdf-bufafterreqcompletedintioctl.md)"><strong>BufAfterReqCompletedIntIoctl</strong></a></p></td>
<td align="left"><p>The <a href="kmdf-bufafterreqcompletedintioctl.md" data-raw-source="[&lt;strong&gt;BufAfterReqCompletedIntIoctl&lt;/strong&gt;](kmdf-bufafterreqcompletedintioctl.md)"><strong>BufAfterReqCompletedIntIoctl</strong></a> rule specifies that after a request is completed, its buffer cannot be accessed (inside <a href="https://msdn.microsoft.com/library/windows/hardware/ff541768" data-raw-source="[&lt;em&gt;EvtIoInternalDeviceControl&lt;/em&gt;](https://msdn.microsoft.com/library/windows/hardware/ff541768)"><em>EvtIoInternalDeviceControl</em></a> callback function only). The buffer is retrieved by calling <a href="https://msdn.microsoft.com/library/windows/hardware/ff550018" data-raw-source="[&lt;strong&gt;WdfRequestRetrieveOutputBuffer&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff550018)"><strong>WdfRequestRetrieveOutputBuffer</strong></a> or <a href="https://msdn.microsoft.com/library/windows/hardware/ff550024" data-raw-source="[&lt;strong&gt;WdfRequestRetrieveUnsafeUserOutputBuffer&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff550024)"><strong>WdfRequestRetrieveUnsafeUserOutputBuffer</strong></a> or <a href="https://msdn.microsoft.com/library/windows/hardware/ff550014" data-raw-source="[&lt;strong&gt;WdfRequestRetrieveInputBuffer&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff550014)"><strong>WdfRequestRetrieveInputBuffer</strong></a> or <a href="https://msdn.microsoft.com/library/windows/hardware/ff550022" data-raw-source="[&lt;strong&gt;WdfRequestRetrieveUnsafeUserInputBuffer&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff550022)"><strong>WdfRequestRetrieveUnsafeUserInputBuffer</strong></a>.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><a href="kmdf-bufafterreqcompletedintioctla.md" data-raw-source="[&lt;strong&gt;BufAfterReqCompletedIntIoctlA&lt;/strong&gt;](kmdf-bufafterreqcompletedintioctla.md)"><strong>BufAfterReqCompletedIntIoctlA</strong></a></p></td>
<td align="left"><p>The <a href="kmdf-bufafterreqcompletedintioctla.md" data-raw-source="[&lt;strong&gt;BufAfterReqCompletedIntIoctlA&lt;/strong&gt;](kmdf-bufafterreqcompletedintioctla.md)"><strong>BufAfterReqCompletedIntIoctlA</strong></a> rule verifies that after a request is completed, its buffer cannot be accessed (inside <a href="https://msdn.microsoft.com/library/windows/hardware/ff541768" data-raw-source="[&lt;em&gt;EvtIoInternalDeviceControl&lt;/em&gt;](https://msdn.microsoft.com/library/windows/hardware/ff541768)"><em>EvtIoInternalDeviceControl</em></a> callback only). The buffer was retrieved by calling <a href="https://msdn.microsoft.com/library/windows/hardware/ff550014" data-raw-source="[&lt;strong&gt;WdfRequestRetrieveInputBuffer&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff550014)"><strong>WdfRequestRetrieveInputBuffer</strong></a> or <a href="https://msdn.microsoft.com/library/windows/hardware/ff550018" data-raw-source="[&lt;strong&gt;WdfRequestRetrieveOutputBuffer&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff550018)"><strong>WdfRequestRetrieveOutputBuffer</strong></a> or <a href="https://msdn.microsoft.com/library/windows/hardware/ff550022" data-raw-source="[&lt;strong&gt;WdfRequestRetrieveUnsafeUserInputBuffer&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff550022)"><strong>WdfRequestRetrieveUnsafeUserInputBuffer</strong></a> or <a href="https://msdn.microsoft.com/library/windows/hardware/ff550024" data-raw-source="[&lt;strong&gt;WdfRequestRetrieveUnsafeUserOutputBuffer&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff550024)"><strong>WdfRequestRetrieveUnsafeUserOutputBuffer</strong></a>.</p></td>
</tr>
<tr class="even">
<td align="left"><p><a href="kmdf-bufafterreqcompletedioctla.md" data-raw-source="[&lt;strong&gt;BufAfterReqCompletedIoctlA&lt;/strong&gt;](kmdf-bufafterreqcompletedioctla.md)"><strong>BufAfterReqCompletedIoctlA</strong></a></p></td>
<td align="left"><p>The <a href="kmdf-bufafterreqcompletedioctla.md" data-raw-source="[&lt;strong&gt;BufAfterReqCompletedIoctlA&lt;/strong&gt;](kmdf-bufafterreqcompletedioctla.md)"><strong>BufAfterReqCompletedIoctlA</strong></a> rule specifies that within the <a href="https://msdn.microsoft.com/library/windows/hardware/ff541758" data-raw-source="[&lt;em&gt;EvtIoDeviceControl&lt;/em&gt;](https://msdn.microsoft.com/library/windows/hardware/ff541758)"><em>EvtIoDeviceControl</em></a> callback function, the I/O request buffer retrieved cannot be accessed after the I/O request is completed.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><a href="kmdf-bufafterreqcompletedread.md" data-raw-source="[&lt;strong&gt;BufAfterReqCompletedRead&lt;/strong&gt;](kmdf-bufafterreqcompletedread.md)"><strong>BufAfterReqCompletedRead</strong></a></p></td>
<td align="left"><p>The <a href="kmdf-bufafterreqcompletedread.md" data-raw-source="[&lt;strong&gt;BufAfterReqCompletedRead&lt;/strong&gt;](kmdf-bufafterreqcompletedread.md)"><strong>BufAfterReqCompletedRead</strong></a> rule specifies that within the <a href="https://msdn.microsoft.com/library/windows/hardware/ff541776" data-raw-source="[&lt;em&gt;EvtIoRead&lt;/em&gt;](https://msdn.microsoft.com/library/windows/hardware/ff541776)"><em>EvtIoRead</em></a> callback function, the I/O request buffer retrieved cannot be accessed after the I/O request is completed. There are 14 DDIs that serve as possible buffer access methods.</p></td>
</tr>
<tr class="even">
<td align="left"><p><a href="kmdf-bufafterreqcompletedreada.md" data-raw-source="[&lt;strong&gt;BufAfterReqCompletedReadA&lt;/strong&gt;](kmdf-bufafterreqcompletedreada.md)"><strong>BufAfterReqCompletedReadA</strong></a></p></td>
<td align="left"><p>The BufAfterReqCompletedReadA rule specifies that within the <a href="https://msdn.microsoft.com/library/windows/hardware/ff541776" data-raw-source="[&lt;em&gt;EvtIoRead&lt;/em&gt;](https://msdn.microsoft.com/library/windows/hardware/ff541776)"><em>EvtIoRead</em></a> callback function, the I/O request buffer retrieved cannot be accessed after the I/O request is completed. There are 14 DDIs that serve as possible buffer access methods.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><a href="kmdf-bufafterreqcompletedwrite.md" data-raw-source="[&lt;strong&gt;BufAfterReqCompletedWrite&lt;/strong&gt;](kmdf-bufafterreqcompletedwrite.md)"><strong>BufAfterReqCompletedWrite</strong></a></p></td>
<td align="left"><p>The BufAfterReqCompletedWrite rule specifies that within the <a href="https://msdn.microsoft.com/library/windows/hardware/ff541813" data-raw-source="[&lt;em&gt;EvtIoWrite&lt;/em&gt;](https://msdn.microsoft.com/library/windows/hardware/ff541813)"><em>EvtIoWrite</em></a> callback function, the I/O request buffer retrieved cannot be accessed after the I/O request is completed.</p></td>
</tr>
<tr class="even">
<td align="left"><p><a href="kmdf-bufafterreqcompletedwritea.md" data-raw-source="[&lt;strong&gt;BufAfterReqCompletedWriteA&lt;/strong&gt;](kmdf-bufafterreqcompletedwritea.md)"><strong>BufAfterReqCompletedWriteA</strong></a></p></td>
<td align="left"><p>The BufAfterReqCompletedWriteA rule specifies that within the <a href="https://msdn.microsoft.com/library/windows/hardware/ff541813" data-raw-source="[&lt;em&gt;EvtIoWrite&lt;/em&gt;](https://msdn.microsoft.com/library/windows/hardware/ff541813)"><em>EvtIoWrite</em></a> callback function, the I/O request buffer retrieved cannot be accessed after the I/O request is completed.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><a href="kmdf-childdeviceinitapi.md" data-raw-source="[&lt;strong&gt;ChildDeviceInitApi&lt;/strong&gt;](kmdf-childdeviceinitapi.md)"><strong>ChildDeviceInitApi</strong></a></p></td>
<td align="left"><p>The <a href="kmdf-childdeviceinitapi.md" data-raw-source="[&lt;strong&gt;ChildDeviceInitApi&lt;/strong&gt;](kmdf-childdeviceinitapi.md)"><strong>ChildDeviceInitApi</strong></a> rule specifies that for a child device, the framework device object initialization methods must be called before the driver calls the <a href="https://msdn.microsoft.com/library/windows/hardware/ff545926" data-raw-source="[&lt;strong&gt;WdfDeviceCreate&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff545926)"><strong>WdfDeviceCreate</strong></a> method for the child device object.</p></td>
</tr>
<tr class="even">
<td align="left"><p><a href="kmdf-controldevicedeleted.md" data-raw-source="[&lt;strong&gt;ControlDeviceDeleted&lt;/strong&gt;](kmdf-controldevicedeleted.md)"><strong>ControlDeviceDeleted</strong></a></p></td>
<td align="left"><p>The ControDeviceDeleted rule specifies that if a PnP driver creates a control device object, the driver must delete the control device object in one of the cleanup callback functions before the driver unloads.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><a href="kmdf-controldeviceinitapi.md" data-raw-source="[&lt;strong&gt;ControlDeviceInitAPI&lt;/strong&gt;](kmdf-controldeviceinitapi.md)"><strong>ControlDeviceInitAPI</strong></a></p></td>
<td align="left"><p>The ControlDeviceInitAPI rule specifies that <a href="https://msdn.microsoft.com/library/windows/hardware/ff545841" data-raw-source="[&lt;strong&gt;WdfControlDeviceInitAllocate&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff545841)"><strong>WdfControlDeviceInitAllocate</strong></a> and all other device object initialization DDIs that set up a <a href="https://msdn.microsoft.com/library/windows/hardware/ff546951" data-raw-source="[&lt;strong&gt;WDFDEVICE_INIT&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff546951)"><strong>WDFDEVICE_INIT</strong></a> structure for the control device must be called before <a href="https://msdn.microsoft.com/library/windows/hardware/ff545926" data-raw-source="[&lt;strong&gt;WdfDeviceCreate&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff545926)"><strong>WdfDeviceCreate</strong></a> for the control device.</p></td>
</tr>
<tr class="even">
<td align="left"><p><a href="kmdf-ctldevicefinishinitdeviceadd.md" data-raw-source="[&lt;strong&gt;CtlDeviceFinishInitDeviceAdd&lt;/strong&gt;](kmdf-ctldevicefinishinitdeviceadd.md)"><strong>CtlDeviceFinishInitDeviceAdd</strong></a></p></td>
<td align="left"><p>The <a href="kmdf-ctldevicefinishinitdeviceadd.md" data-raw-source="[&lt;strong&gt;CtlDeviceFinishInitDeviceAdd&lt;/strong&gt;](kmdf-ctldevicefinishinitdeviceadd.md)"><strong>CtlDeviceFinishInitDeviceAdd</strong></a> rule specifies that if a driver creates control device object in an <a href="https://msdn.microsoft.com/library/windows/hardware/ff541693" data-raw-source="[&lt;em&gt;EvtDriverDeviceAdd&lt;/em&gt;](https://msdn.microsoft.com/library/windows/hardware/ff541693)"><em>EvtDriverDeviceAdd</em></a> callback function, it must call <a href="https://msdn.microsoft.com/library/windows/hardware/ff545854" data-raw-source="[&lt;strong&gt;WdfControlFinishInitializing&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff545854)"><strong>WdfControlFinishInitializing</strong></a> after the device has been created and before it exits from the <strong>EvtDriverDeviceAdd</strong> callback function. This rule does not apply for non-PnP drivers.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><a href="kmdf-ctldevicefinishinitdrentry.md" data-raw-source="[&lt;strong&gt;CtlDeviceFinishInitDrEntry&lt;/strong&gt;](kmdf-ctldevicefinishinitdrentry.md)"><strong>CtlDeviceFinishInitDrEntry</strong></a></p></td>
<td align="left"><p>The CtlDeviceFinishInitDrEntry rule specifies that if a driver creates a control device object in a <a href="https://msdn.microsoft.com/library/windows/hardware/ff540807" data-raw-source="[&lt;strong&gt;DriverEntry&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff540807)"><strong>DriverEntry</strong></a> callback function, it must call <a href="https://msdn.microsoft.com/library/windows/hardware/ff545854" data-raw-source="[&lt;strong&gt;WdfControlFinishInitializing&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff545854)"><strong>WdfControlFinishInitializing</strong></a> after the device has been created and before it exits from the <a href="https://msdn.microsoft.com/library/windows/hardware/ff541693" data-raw-source="[&lt;em&gt;EvtDriverDeviceAdd&lt;/em&gt;](https://msdn.microsoft.com/library/windows/hardware/ff541693)"><em>EvtDriverDeviceAdd</em></a> callback function. This rule does not apply for non-PnP drivers.</p></td>
</tr>
<tr class="even">
<td align="left"><p><a href="kmdf-devicecreatefail.md" data-raw-source="[&lt;strong&gt;DeviceCreateFail&lt;/strong&gt;](kmdf-devicecreatefail.md)"><strong>DeviceCreateFail</strong></a></p></td>
<td align="left"><p>The <a href="kmdf-devicecreatefail.md" data-raw-source="[&lt;strong&gt;DeviceCreateFail&lt;/strong&gt;](kmdf-devicecreatefail.md)"><strong>DeviceCreateFail</strong></a> rule specifies that EVT_WDF_DRIVER_DEVICE_ADD returns an error status when the call to <a href="https://msdn.microsoft.com/library/windows/hardware/ff545926" data-raw-source="[&lt;strong&gt;WdfDeviceCreate&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff545926)"><strong>WdfDeviceCreate</strong></a> fails.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><a href="kmdf-deviceinitallocate.md" data-raw-source="[&lt;strong&gt;DeviceInitAllocate&lt;/strong&gt;](kmdf-deviceinitallocate.md)"><strong>DeviceInitAllocate</strong></a></p></td>
<td align="left"><p>The <a href="kmdf-deviceinitallocate.md" data-raw-source="[&lt;strong&gt;DeviceInitAllocate&lt;/strong&gt;](kmdf-deviceinitallocate.md)"><strong>DeviceInitAllocate</strong></a> rule specifies that, for a PDO device or a control device object, the framework device object initialization methods <a href="https://msdn.microsoft.com/library/windows/hardware/ff548786" data-raw-source="[&lt;strong&gt;WdfPdoInitAllocate&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff548786)"><strong>WdfPdoInitAllocate</strong></a> or <a href="https://msdn.microsoft.com/library/windows/hardware/ff545841" data-raw-source="[&lt;strong&gt;WdfControlDeviceInitAllocate&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff545841)"><strong>WdfControlDeviceInitAllocate</strong></a> must be called before the driver calls <a href="https://msdn.microsoft.com/library/windows/hardware/ff545926" data-raw-source="[&lt;strong&gt;WdfDeviceCreate&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff545926)"><strong>WdfDeviceCreate</strong></a>.</p></td>
</tr>
<tr class="even">
<td align="left"><p><a href="kmdf-deviceinitapi.md" data-raw-source="[&lt;strong&gt;DeviceInitAPI&lt;/strong&gt;](kmdf-deviceinitapi.md)"><strong>DeviceInitAPI</strong></a></p></td>
<td align="left"><p>For an FDO device, the framework device object initialization methods and the framework FDO initialization methods must be called before the driver calls the <a href="https://msdn.microsoft.com/library/windows/hardware/ff545926" data-raw-source="[&lt;strong&gt;WdfDeviceCreate&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff545926)"><strong>WdfDeviceCreate</strong></a> method for the device object.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><a href="kmdf-doubledeviceinitfree.md" data-raw-source="[&lt;strong&gt;DoubleDeviceInitFree&lt;/strong&gt;](kmdf-doubledeviceinitfree.md)"><strong>DoubleDeviceInitFree</strong></a></p></td>
<td align="left"><p>The <a href="kmdf-doubledeviceinitfree.md" data-raw-source="[&lt;strong&gt;DoubleDeviceInitFree&lt;/strong&gt;](kmdf-doubledeviceinitfree.md)"><strong>DoubleDeviceInitFree</strong></a> rule specifies that drivers should not free device initialization structure twice.</p></td>
</tr>
<tr class="even">
<td align="left"><p><a href="kmdf-drivercreate.md" data-raw-source="[&lt;strong&gt;DriverCreate&lt;/strong&gt;](kmdf-drivercreate.md)"><strong>DriverCreate</strong></a></p></td>
<td align="left"><p>The <a href="kmdf-drivercreate.md" data-raw-source="[&lt;strong&gt;DriverCreate&lt;/strong&gt;](kmdf-drivercreate.md)"><strong>DriverCreate</strong></a> rule specifies that a driver that uses Kernel Mode Driver Framework (KMDF) must call the <a href="https://msdn.microsoft.com/library/windows/hardware/ff547175" data-raw-source="[&lt;strong&gt;WdfDriverCreate&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff547175)"><strong>WdfDriverCreate</strong></a> method to create a framework driver object from within its <a href="https://msdn.microsoft.com/library/windows/hardware/ff540807" data-raw-source="[&lt;strong&gt;DriverEntry&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff540807)"><strong>DriverEntry</strong></a> routine.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><a href="kmdf-initfreedevicecallback.md" data-raw-source="[&lt;strong&gt;InitFreeDeviceCallback&lt;/strong&gt;](kmdf-initfreedevicecallback.md)"><strong>InitFreeDeviceCallback</strong></a></p></td>
<td align="left"><p>The InitFreeDeviceCallback rule specifies that a driver must call <a href="https://msdn.microsoft.com/library/windows/hardware/ff546050" data-raw-source="[&lt;strong&gt;WdfDeviceInitFree&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff546050)"><strong>WdfDeviceInitFree</strong></a> if the driver encounters an error while it initializes a new framework device object, and if the driver received the <a href="https://msdn.microsoft.com/library/windows/hardware/ff546951" data-raw-source="[&lt;strong&gt;WDFDEVICE_INIT&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff546951)"><strong>WDFDEVICE_INIT</strong></a> structure from a call to <a href="https://msdn.microsoft.com/library/windows/hardware/ff545841" data-raw-source="[&lt;strong&gt;WdfControlDeviceInitAllocate&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff545841)"><strong>WdfControlDeviceInitAllocate</strong></a>.</p></td>
</tr>
<tr class="even">
<td align="left"><p><a href="kmdf-initfreedevicecreate.md" data-raw-source="[&lt;strong&gt;InitFreeDeviceCreate&lt;/strong&gt;](kmdf-initfreedevicecreate.md)"><strong>InitFreeDeviceCreate</strong></a></p></td>
<td align="left"><p>The <a href="kmdf-initfreedevicecreate.md" data-raw-source="[&lt;strong&gt;InitFreeDeviceCreate&lt;/strong&gt;](kmdf-initfreedevicecreate.md)"><strong>InitFreeDeviceCreate</strong></a> rule specifies that a driver must call <a href="https://msdn.microsoft.com/library/windows/hardware/ff546050" data-raw-source="[&lt;strong&gt;WdfDeviceInitFree&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff546050)"><strong>WdfDeviceInitFree</strong></a> instead of <a href="https://msdn.microsoft.com/library/windows/hardware/ff545926" data-raw-source="[&lt;strong&gt;WdfDeviceCreate&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff545926)"><strong>WdfDeviceCreate</strong></a> if an error occurs in one of the device object initialization methods and if the driver received the <a href="https://msdn.microsoft.com/library/windows/hardware/ff546951" data-raw-source="[&lt;strong&gt;WDFDEVICE_INIT&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff546951)"><strong>WDFDEVICE_INIT</strong></a> structure from a call to <a href="https://msdn.microsoft.com/library/windows/hardware/ff545841" data-raw-source="[&lt;strong&gt;WdfControlDeviceInitAllocate&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff545841)"><strong>WdfControlDeviceInitAllocate</strong></a>.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><a href="kmdf-initfreedevicecreatetype2.md" data-raw-source="[&lt;strong&gt;InitFreeDeviceCreateType2&lt;/strong&gt;](kmdf-initfreedevicecreatetype2.md)"><strong>InitFreeDeviceCreateType2</strong></a></p></td>
<td align="left"><p>The InitFreeDeviceCreateType2 rule specifies that a driver must not call <a href="https://msdn.microsoft.com/library/windows/hardware/ff545926" data-raw-source="[&lt;strong&gt;WdfDeviceCreate&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff545926)"><strong>WdfDeviceCreate</strong></a> after it calls <a href="https://msdn.microsoft.com/library/windows/hardware/ff546050" data-raw-source="[&lt;strong&gt;WdfDeviceInitFree&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff546050)"><strong>WdfDeviceInitFree</strong></a>.</p></td>
</tr>
<tr class="even">
<td align="left"><p><a href="kmdf-initfreedevicecreatetype4.md" data-raw-source="[&lt;strong&gt;InitFreeDeviceCreateType4&lt;/strong&gt;](kmdf-initfreedevicecreatetype4.md)"><strong>InitFreeDeviceCreateType4</strong></a></p></td>
<td align="left"><p>The <a href="kmdf-initfreedevicecreatetype4.md" data-raw-source="[&lt;strong&gt;InitFreeDeviceCreateType4&lt;/strong&gt;](kmdf-initfreedevicecreatetype4.md)"><strong>InitFreeDeviceCreateType4</strong></a> rule specifies that a driver must call <a href="https://msdn.microsoft.com/library/windows/hardware/ff546050" data-raw-source="[&lt;strong&gt;WdfDeviceInitFree&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff546050)"><strong>WdfDeviceInitFree</strong></a> if the driver encounters an error while it calls <a href="https://msdn.microsoft.com/library/windows/hardware/ff545926" data-raw-source="[&lt;strong&gt;WdfDeviceCreate&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff545926)"><strong>WdfDeviceCreate</strong></a> and if the driver received the <a href="https://msdn.microsoft.com/library/windows/hardware/ff546951" data-raw-source="[&lt;strong&gt;WDFDEVICE_INIT&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff546951)"><strong>WDFDEVICE_INIT</strong></a> structure from a call to <a href="https://msdn.microsoft.com/library/windows/hardware/ff545841" data-raw-source="[&lt;strong&gt;WdfControlDeviceInitAllocate&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff545841)"><strong>WdfControlDeviceInitAllocate</strong></a>.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><a href="kmdf-initfreenull.md" data-raw-source="[&lt;strong&gt;InitFreeNull&lt;/strong&gt;](kmdf-initfreenull.md)"><strong>InitFreeNull</strong></a></p></td>
<td align="left"><p>The <a href="kmdf-initfreenull.md" data-raw-source="[&lt;strong&gt;InitFreeNull&lt;/strong&gt;](kmdf-initfreenull.md)"><strong>InitFreeNull</strong></a> rule specifies that DDIs receiving PWDFDEVICE_INIT as a parameter cannot be called by using a <strong>NULL</strong> pointer to a <a href="https://msdn.microsoft.com/library/windows/hardware/ff546951" data-raw-source="[WDFDEVICE_INIT](https://msdn.microsoft.com/library/windows/hardware/ff546951)">WDFDEVICE_INIT</a> structure.</p></td>
</tr>
<tr class="even">
<td align="left"><p><a href="kmdf-mdlafterreqcompletedintioctl.md" data-raw-source="[&lt;strong&gt;MdlAfterReqCompletedIntIoctl&lt;/strong&gt;](kmdf-mdlafterreqcompletedintioctl.md)"><strong>MdlAfterReqCompletedIntIoctl</strong></a></p></td>
<td align="left"><p>The MdlAfterReqCompletedIntIoctl rule specifies that within the <a href="https://msdn.microsoft.com/library/windows/hardware/ff541768" data-raw-source="[&lt;em&gt;EvtIoInternalDeviceControl&lt;/em&gt;](https://msdn.microsoft.com/library/windows/hardware/ff541768)"><em>EvtIoInternalDeviceControl</em></a> callback function, the memory descriptor list (MDL) cannot be accessed after the I/O request is completed.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><a href="kmdf-mdlafterreqcompletedintioctla.md" data-raw-source="[&lt;strong&gt;MdlAfterReqCompletedIntIoctlA&lt;/strong&gt;](kmdf-mdlafterreqcompletedintioctla.md)"><strong>MdlAfterReqCompletedIntIoctlA</strong></a></p></td>
<td align="left"><p>The <a href="kmdf-mdlafterreqcompletedintioctla.md" data-raw-source="[&lt;strong&gt;MdlAfterReqCompletedIntIoctlA&lt;/strong&gt;](kmdf-mdlafterreqcompletedintioctla.md)"><strong>MdlAfterReqCompletedIntIoctlA</strong></a> rule specifies that within the <a href="https://msdn.microsoft.com/library/windows/hardware/ff541768" data-raw-source="[&lt;em&gt;EvtIoInternalDeviceControl&lt;/em&gt;](https://msdn.microsoft.com/library/windows/hardware/ff541768)"><em>EvtIoInternalDeviceControl</em></a> callback function, the memory descriptor list (MDL) cannot be accessed after the I/O request is completed.</p></td>
</tr>
<tr class="even">
<td align="left"><p><a href="kmdf-mdlafterreqcompletedioctl.md" data-raw-source="[&lt;strong&gt;MdlAfterReqCompletedIoctl&lt;/strong&gt;](kmdf-mdlafterreqcompletedioctl.md)"><strong>MdlAfterReqCompletedIoctl</strong></a></p></td>
<td align="left"><p>The <a href="kmdf-mdlafterreqcompletedioctl.md" data-raw-source="[&lt;strong&gt;MdlAfterReqCompletedIoctl&lt;/strong&gt;](kmdf-mdlafterreqcompletedioctl.md)"><strong>MdlAfterReqCompletedIoctl</strong></a> rule specifies that within the <a href="https://msdn.microsoft.com/library/windows/hardware/ff541758" data-raw-source="[&lt;em&gt;EvtIoDeviceControl&lt;/em&gt;](https://msdn.microsoft.com/library/windows/hardware/ff541758)"><em>EvtIoDeviceControl</em></a> callback function, the memory descriptor list (MDL) cannot be accessed after the I/O request is completed.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><a href="kmdf-mdlafterreqcompletedioctla.md" data-raw-source="[&lt;strong&gt;MdlAfterReqCompletedIoctlA&lt;/strong&gt;](kmdf-mdlafterreqcompletedioctla.md)"><strong>MdlAfterReqCompletedIoctlA</strong></a></p></td>
<td align="left"><p>The <a href="kmdf-mdlafterreqcompletedioctla.md" data-raw-source="[&lt;strong&gt;MdlAfterReqCompletedIoctlA&lt;/strong&gt;](kmdf-mdlafterreqcompletedioctla.md)"><strong>MdlAfterReqCompletedIoctlA</strong></a> rule specifies that within the <a href="https://msdn.microsoft.com/library/windows/hardware/ff541758" data-raw-source="[&lt;em&gt;EvtIoDeviceControl&lt;/em&gt;](https://msdn.microsoft.com/library/windows/hardware/ff541758)"><em>EvtIoDeviceControl</em></a> callback function, the memory descriptor list (MDL) cannot be accessed after the I/O request is completed.</p></td>
</tr>
<tr class="even">
<td align="left"><p><a href="kmdf-mdlafterreqcompletedread.md" data-raw-source="[&lt;strong&gt;MdlAfterReqCompletedRead&lt;/strong&gt;](kmdf-mdlafterreqcompletedread.md)"><strong>MdlAfterReqCompletedRead</strong></a></p></td>
<td align="left"><p>The <a href="kmdf-mdlafterreqcompletedread.md" data-raw-source="[&lt;strong&gt;MdlAfterReqCompletedRead&lt;/strong&gt;](kmdf-mdlafterreqcompletedread.md)"><strong>MdlAfterReqCompletedRead</strong></a> rule specifies that within the <a href="https://msdn.microsoft.com/library/windows/hardware/ff541776" data-raw-source="[&lt;em&gt;EvtIoRead&lt;/em&gt;](https://msdn.microsoft.com/library/windows/hardware/ff541776)"><em>EvtIoRead</em></a> callback function, the memory descriptor list (MDL) object retrieved cannot be accessed after the I/O request is completed.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><a href="kmdf-mdlafterreqcompletedreada.md" data-raw-source="[&lt;strong&gt;MdlAfterReqCompletedReadA&lt;/strong&gt;](kmdf-mdlafterreqcompletedreada.md)"><strong>MdlAfterReqCompletedReadA</strong></a></p></td>
<td align="left"><p>The <a href="kmdf-mdlafterreqcompletedreada.md" data-raw-source="[&lt;strong&gt;MdlAfterReqCompletedReadA&lt;/strong&gt;](kmdf-mdlafterreqcompletedreada.md)"><strong>MdlAfterReqCompletedReadA</strong></a> rule specifies that within the <a href="https://msdn.microsoft.com/library/windows/hardware/ff541776" data-raw-source="[&lt;em&gt;EvtIoRead&lt;/em&gt;](https://msdn.microsoft.com/library/windows/hardware/ff541776)"><em>EvtIoRead</em></a> callback function, the memory descriptor list (MDL) object retrieved cannot be accessed after the I/O request is completed.</p></td>
</tr>
<tr class="even">
<td align="left"><p><a href="kmdf-mdlafterreqcompletedwrite.md" data-raw-source="[&lt;strong&gt;MdlAfterReqCompletedWrite&lt;/strong&gt;](kmdf-mdlafterreqcompletedwrite.md)"><strong>MdlAfterReqCompletedWrite</strong></a></p></td>
<td align="left"><p>The <a href="kmdf-mdlafterreqcompletedwrite.md" data-raw-source="[&lt;strong&gt;MdlAfterReqCompletedWrite&lt;/strong&gt;](kmdf-mdlafterreqcompletedwrite.md)"><strong>MdlAfterReqCompletedWrite</strong></a> rule specifies that within the <a href="https://msdn.microsoft.com/library/windows/hardware/ff541813" data-raw-source="[&lt;em&gt;EvtIoWrite&lt;/em&gt;](https://msdn.microsoft.com/library/windows/hardware/ff541813)"><em>EvtIoWrite</em></a> callback function, the memory descriptor list (MDL) object retrieved cannot be accessed after the I/O request is completed.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><a href="kmdf-mdlafterreqcompletedwritea.md" data-raw-source="[&lt;strong&gt;MdlAfterReqCompletedWriteA&lt;/strong&gt;](kmdf-mdlafterreqcompletedwritea.md)"><strong>MdlAfterReqCompletedWriteA</strong></a></p></td>
<td align="left"><p>The <a href="kmdf-mdlafterreqcompletedwritea.md" data-raw-source="[&lt;strong&gt;MdlAfterReqCompletedWriteA&lt;/strong&gt;](kmdf-mdlafterreqcompletedwritea.md)"><strong>MdlAfterReqCompletedWriteA</strong></a> rule specifies that within the <a href="https://msdn.microsoft.com/library/windows/hardware/ff541813" data-raw-source="[&lt;em&gt;EvtIoWrite&lt;/em&gt;](https://msdn.microsoft.com/library/windows/hardware/ff541813)"><em>EvtIoWrite</em></a> callback function, the memory descriptor list (MDL) object retrieved cannot be accessed after the I/O request is completed.</p></td>
</tr>
<tr class="even">
<td align="left"><p><a href="kmdf-memafterreqcompletedintioctl.md" data-raw-source="[&lt;strong&gt;MemAfterReqCompletedIntIoctl&lt;/strong&gt;](kmdf-memafterreqcompletedintioctl.md)"><strong>MemAfterReqCompletedIntIoctl</strong></a></p></td>
<td align="left"><p>The <a href="kmdf-memafterreqcompletedintioctl.md" data-raw-source="[&lt;strong&gt;MemAfterReqCompletedIntIoctl&lt;/strong&gt;](kmdf-memafterreqcompletedintioctl.md)"><strong>MemAfterReqCompletedIntIoctl</strong></a> rule specifies that within the <a href="https://msdn.microsoft.com/library/windows/hardware/ff541768" data-raw-source="[&lt;em&gt;EvtIoInternalDeviceControl&lt;/em&gt;](https://msdn.microsoft.com/library/windows/hardware/ff541768)"><em>EvtIoInternalDeviceControl</em></a> callback function, the framework memory object cannot be accessed after the I/O request is completed.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><a href="kmdf-memafterreqcompletedintioctla.md" data-raw-source="[&lt;strong&gt;MemAfterReqCompletedIntIoctlA&lt;/strong&gt;](kmdf-memafterreqcompletedintioctla.md)"><strong>MemAfterReqCompletedIntIoctlA</strong></a></p></td>
<td align="left"><p>The <a href="kmdf-memafterreqcompletedintioctla.md" data-raw-source="[&lt;strong&gt;MemAfterReqCompletedIntIoctlA&lt;/strong&gt;](kmdf-memafterreqcompletedintioctla.md)"><strong>MemAfterReqCompletedIntIoctlA</strong></a> rule specifies that within the <a href="https://msdn.microsoft.com/library/windows/hardware/ff541768" data-raw-source="[&lt;em&gt;EvtIoInternalDeviceControl&lt;/em&gt;](https://msdn.microsoft.com/library/windows/hardware/ff541768)"><em>EvtIoInternalDeviceControl</em></a> callback function, the framework memory object cannot be accessed after the I/O request is completed.</p></td>
</tr>
<tr class="even">
<td align="left"><p><a href="kmdf-memafterreqcompletedioctl.md" data-raw-source="[&lt;strong&gt;MemAfterReqCompletedIoctl&lt;/strong&gt;](kmdf-memafterreqcompletedioctl.md)"><strong>MemAfterReqCompletedIoctl</strong></a></p></td>
<td align="left"><p>The <a href="kmdf-memafterreqcompletedioctl.md" data-raw-source="[&lt;strong&gt;MemAfterReqCompletedIoctl&lt;/strong&gt;](kmdf-memafterreqcompletedioctl.md)"><strong>MemAfterReqCompletedIoctl</strong></a> rule specifies that within the <a href="https://msdn.microsoft.com/library/windows/hardware/ff541758" data-raw-source="[&lt;em&gt;EvtIoDeviceControl&lt;/em&gt;](https://msdn.microsoft.com/library/windows/hardware/ff541758)"><em>EvtIoDeviceControl</em></a> callback function, the framework memory object cannot be accessed after the I/O request is completed.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><a href="kmdf-memafterreqcompletedioctla.md" data-raw-source="[&lt;strong&gt;MemAfterReqCompletedIoctlA&lt;/strong&gt;](kmdf-memafterreqcompletedioctla.md)"><strong>MemAfterReqCompletedIoctlA</strong></a></p></td>
<td align="left"><p>The <a href="kmdf-memafterreqcompletedioctla.md" data-raw-source="[&lt;strong&gt;MemAfterReqCompletedIoctlA&lt;/strong&gt;](kmdf-memafterreqcompletedioctla.md)"><strong>MemAfterReqCompletedIoctlA</strong></a> rule specifies that within the <a href="https://msdn.microsoft.com/library/windows/hardware/ff541758" data-raw-source="[&lt;em&gt;EvtIoDeviceControl&lt;/em&gt;](https://msdn.microsoft.com/library/windows/hardware/ff541758)"><em>EvtIoDeviceControl</em></a> callback function, the framework memory object cannot be accessed after the I/O request is completed.</p></td>
</tr>
<tr class="even">
<td align="left"><p><a href="kmdf-memafterreqcompletedread.md" data-raw-source="[&lt;strong&gt;MemAfterReqCompletedRead&lt;/strong&gt;](kmdf-memafterreqcompletedread.md)"><strong>MemAfterReqCompletedRead</strong></a></p></td>
<td align="left"><p>The <a href="kmdf-memafterreqcompletedread.md" data-raw-source="[&lt;strong&gt;MemAfterReqCompletedRead&lt;/strong&gt;](kmdf-memafterreqcompletedread.md)"><strong>MemAfterReqCompletedRead</strong></a> rule specifies that within the <a href="https://msdn.microsoft.com/library/windows/hardware/ff541776" data-raw-source="[&lt;em&gt;EvtIoRead&lt;/em&gt;](https://msdn.microsoft.com/library/windows/hardware/ff541776)"><em>EvtIoRead</em></a> callback function, the framework memory object cannot be accessed after the I/O request is completed.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><a href="kmdf-memafterreqcompletedreada.md" data-raw-source="[&lt;strong&gt;MemAfterReqCompletedReadA&lt;/strong&gt;](kmdf-memafterreqcompletedreada.md)"><strong>MemAfterReqCompletedReadA</strong></a></p></td>
<td align="left"><p>The <a href="kmdf-memafterreqcompletedreada.md" data-raw-source="[&lt;strong&gt;MemAfterReqCompletedReadA&lt;/strong&gt;](kmdf-memafterreqcompletedreada.md)"><strong>MemAfterReqCompletedReadA</strong></a> rule specifies that within the <a href="https://msdn.microsoft.com/library/windows/hardware/ff541776" data-raw-source="[&lt;em&gt;EvtIoRead&lt;/em&gt;](https://msdn.microsoft.com/library/windows/hardware/ff541776)"><em>EvtIoRead</em></a> callback function, the framework memory object cannot be accessed after the I/O request is completed.</p></td>
</tr>
<tr class="even">
<td align="left"><p><a href="kmdf-memafterreqcompletedwrite.md" data-raw-source="[&lt;strong&gt;MemAfterReqCompletedWrite&lt;/strong&gt;](kmdf-memafterreqcompletedwrite.md)"><strong>MemAfterReqCompletedWrite</strong></a></p></td>
<td align="left"><p>The <a href="kmdf-memafterreqcompletedwrite.md" data-raw-source="[&lt;strong&gt;MemAfterReqCompletedWrite&lt;/strong&gt;](kmdf-memafterreqcompletedwrite.md)"><strong>MemAfterReqCompletedWrite</strong></a> rule specifies that within the <a href="https://msdn.microsoft.com/library/windows/hardware/ff541813" data-raw-source="[&lt;em&gt;EvtIoWrite&lt;/em&gt;](https://msdn.microsoft.com/library/windows/hardware/ff541813)"><em>EvtIoWrite</em></a> callback function, the framework memory object cannot be accessed after the I/O request is completed.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><a href="kmdf-memafterreqcompletedwritea.md" data-raw-source="[&lt;strong&gt;MemAfterReqCompletedWriteA&lt;/strong&gt;](kmdf-memafterreqcompletedwritea.md)"><strong>MemAfterReqCompletedWriteA</strong></a></p></td>
<td align="left"><p>The <a href="kmdf-memafterreqcompletedwritea.md" data-raw-source="[&lt;strong&gt;MemAfterReqCompletedWriteA&lt;/strong&gt;](kmdf-memafterreqcompletedwritea.md)"><strong>MemAfterReqCompletedWriteA</strong></a> rule specifies that within the <a href="https://msdn.microsoft.com/library/windows/hardware/ff541813" data-raw-source="[&lt;em&gt;EvtIoWrite&lt;/em&gt;](https://msdn.microsoft.com/library/windows/hardware/ff541813)"><em>EvtIoWrite</em></a> callback function, the framework memory object cannot be accessed after the I/O request is completed.</p></td>
</tr>
<tr class="even">
<td align="left"><p><a href="nullcheck.md" data-raw-source="[&lt;strong&gt;NullCheck&lt;/strong&gt;](nullcheck.md)"><strong>NullCheck</strong></a></p></td>
<td align="left"><p>The NullCheck rule verifies that a NULL value inside the driver code is not dereferenced later in the driver. This rule reports a defect if either of these conditions is true:</p>
<ul>
<li>There is an assignment of NULL that is dereferenced later.</li>
<li>There is a global/parameter to a procedure in a driver that may be NULL that is dereferenced later, and there is an explicit check in the driver that suggests that the initial value of the pointer may be NULL.</li>
</ul>
<p>With NullCheck rule violations, the most relevant code statements are highlighted in the trace tree pane. For more information about working with report output, see <a href="https://msdn.microsoft.com/library/windows/hardware/ff552834" data-raw-source="[Static Driver Verifier Report](https://msdn.microsoft.com/library/windows/hardware/ff552834)">Static Driver Verifier Report</a> and <a href="https://msdn.microsoft.com/library/windows/hardware/ff554020" data-raw-source="[Understanding the Trace Viewer](https://msdn.microsoft.com/library/windows/hardware/ff554020)">Understanding the Trace Viewer</a>.</p>
<p></p></td>
</tr>
<tr class="odd">
<td align="left"><p><a href="kmdf-pdodeviceinitapi.md" data-raw-source="[&lt;strong&gt;PdoDeviceInitAPI&lt;/strong&gt;](kmdf-pdodeviceinitapi.md)"><strong>PdoDeviceInitAPI</strong></a></p></td>
<td align="left"><p>The <a href="kmdf-pdodeviceinitapi.md" data-raw-source="[&lt;strong&gt;PdoDeviceInitAPI&lt;/strong&gt;](kmdf-pdodeviceinitapi.md)"><strong>PdoDeviceInitAPI</strong></a> rule specifies that <a href="https://msdn.microsoft.com/library/windows/hardware/ff548786" data-raw-source="[&lt;strong&gt;WdfPdoInitAllocate&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff548786)"><strong>WdfPdoInitAllocate</strong></a> and all other device object initialization DDIs that set up a <a href="https://msdn.microsoft.com/library/windows/hardware/ff546951" data-raw-source="[&lt;strong&gt;WDFDEVICE_INIT&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff546951)"><strong>WDFDEVICE_INIT</strong></a> structure for the physical device object (PDO) must be called before the driver calls <a href="https://msdn.microsoft.com/library/windows/hardware/ff545926" data-raw-source="[&lt;strong&gt;WdfDeviceCreate&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff545926)"><strong>WdfDeviceCreate</strong></a> for the PDO.</p></td>
</tr>
<tr class="even">
<td align="left"><p><a href="kmdf-pdoinitfreedevicecallback.md" data-raw-source="[&lt;strong&gt;PdoInitFreeDeviceCallback&lt;/strong&gt;](kmdf-pdoinitfreedevicecallback.md)"><strong>PdoInitFreeDeviceCallback</strong></a></p></td>
<td align="left"><p>The <a href="kmdf-pdoinitfreedevicecallback.md" data-raw-source="[&lt;strong&gt;PdoInitFreeDeviceCallback&lt;/strong&gt;](kmdf-pdoinitfreedevicecallback.md)"><strong>PdoInitFreeDeviceCallback</strong></a> rule specifies that the driver must call <a href="https://msdn.microsoft.com/library/windows/hardware/ff546050" data-raw-source="[&lt;strong&gt;WdfDeviceInitFree&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff546050)"><strong>WdfDeviceInitFree</strong></a> if an error occurs when the driver calls any framework device object initialization function.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><a href="kmdf-pdoinitfreedevicecreate.md" data-raw-source="[&lt;strong&gt;PdoInitFreeDeviceCreate&lt;/strong&gt;](kmdf-pdoinitfreedevicecreate.md)"><strong>PdoInitFreeDeviceCreate</strong></a></p></td>
<td align="left"><p>The <a href="kmdf-pdoinitfreedevicecreate.md" data-raw-source="[&lt;strong&gt;PdoInitFreeDeviceCreate&lt;/strong&gt;](kmdf-pdoinitfreedevicecreate.md)"><strong>PdoInitFreeDeviceCreate</strong></a> rule specifies that a driver must call <a href="https://msdn.microsoft.com/library/windows/hardware/ff546050" data-raw-source="[&lt;strong&gt;WdfDeviceInitFree&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff546050)"><strong>WdfDeviceInitFree</strong></a> instead of <a href="https://msdn.microsoft.com/library/windows/hardware/ff545926" data-raw-source="[&lt;strong&gt;WdfDeviceCreate&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff545926)"><strong>WdfDeviceCreate</strong></a> if an error occurs in one of the device object initialization functions and if the driver received the WDFDEVICE_INIT structure from a call to <a href="https://msdn.microsoft.com/library/windows/hardware/ff548786" data-raw-source="[&lt;strong&gt;WdfPdoInitAllocate&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff548786)"><strong>WdfPdoInitAllocate</strong></a>.</p></td>
</tr>
<tr class="even">
<td align="left"><p><a href="kmdf-pdoinitfreedevicecreatetype2.md" data-raw-source="[&lt;strong&gt;PdoInitFreeDeviceCreateType2&lt;/strong&gt;](kmdf-pdoinitfreedevicecreatetype2.md)"><strong>PdoInitFreeDeviceCreateType2</strong></a></p></td>
<td align="left"><p>The PdoInitFreeDeviceCreateType2 rule specifies that a driver must not call <a href="https://msdn.microsoft.com/library/windows/hardware/ff545926" data-raw-source="[&lt;strong&gt;WdfDeviceCreate&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff545926)"><strong>WdfDeviceCreate</strong></a> after it calls <a href="https://msdn.microsoft.com/library/windows/hardware/ff546050" data-raw-source="[&lt;strong&gt;WdfDeviceInitFree&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff546050)"><strong>WdfDeviceInitFree</strong></a>.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><a href="kmdf-pdoinitfreedevicecreatetype4.md" data-raw-source="[&lt;strong&gt;PdoInitFreeDeviceCreateType4&lt;/strong&gt;](kmdf-pdoinitfreedevicecreatetype4.md)"><strong>PdoInitFreeDeviceCreateType4</strong></a></p></td>
<td align="left"><p>The PdoInitFreeDeviceCreateType4 rule specifies that the driver must call <a href="https://msdn.microsoft.com/library/windows/hardware/ff546050" data-raw-source="[&lt;strong&gt;WdfDeviceInitFree&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff546050)"><strong>WdfDeviceInitFree</strong></a> if an error occurs when the driver calls <a href="https://msdn.microsoft.com/library/windows/hardware/ff545926" data-raw-source="[&lt;strong&gt;WdfDeviceCreate&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff545926)"><strong>WdfDeviceCreate</strong></a>.</p></td>
</tr>
<tr class="even">
<td align="left"><p><a href="kmdf-controldeviceinitallocate.md" data-raw-source="[&lt;strong&gt;ControlDeviceInitAllocate&lt;/strong&gt;](kmdf-controldeviceinitallocate.md)"><strong>ControlDeviceInitAllocate</strong></a></p></td>
<td align="left"><p>The <a href="kmdf-controldeviceinitallocate.md" data-raw-source="[&lt;strong&gt;ControlDeviceInitAllocate&lt;/strong&gt;](kmdf-controldeviceinitallocate.md)"><strong>ControlDeviceInitAllocate</strong></a> rule specifies that for a control device object, the driver must call the framework device object initialization method <a href="https://msdn.microsoft.com/library/windows/hardware/ff545841" data-raw-source="[&lt;strong&gt;WdfControlDeviceInitAllocate&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff545841)"><strong>WdfControlDeviceInitAllocate</strong></a> before the driver calls <a href="https://msdn.microsoft.com/library/windows/hardware/ff545926" data-raw-source="[&lt;strong&gt;WdfDeviceCreate&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff545926)"><strong>WdfDeviceCreate</strong></a>.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><a href="kmdf-inputbufferapi.md" data-raw-source="[&lt;strong&gt;InputBufferAPI&lt;/strong&gt;](kmdf-inputbufferapi.md)"><strong>InputBufferAPI</strong></a></p></td>
<td align="left"><p>The <a href="kmdf-inputbufferapi.md" data-raw-source="[&lt;strong&gt;InputBufferAPI&lt;/strong&gt;](kmdf-inputbufferapi.md)"><strong>InputBufferAPI</strong></a> rule specifies that the correct DDIs for buffer retrieval are used in the <a href="https://msdn.microsoft.com/library/windows/hardware/ff541776" data-raw-source="[&lt;em&gt;EvtIoRead&lt;/em&gt;](https://msdn.microsoft.com/library/windows/hardware/ff541776)"><em>EvtIoRead</em></a>callback function. Within the <em>EvtIoRead</em> callback function, the following DDIs cannot be called for buffer retrieval:</p></td>
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

 

 





