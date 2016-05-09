---
title: Driver Start, Stop, and Device Control
description: Driver Start, Stop, and Device Control
ms.assetid: d3608a5f-3bf4-43b1-8c32-55a6fcd4fbe8
keywords: ["mini-redirectors WDK , starting", "mini-redirectors WDK , stopping", "mini-redirectors WDK , device controls"]
---

# Driver Start, Stop, and Device Control


Driver registration is handled in the **DriverEntry** routine of a network mini-redirector driver. When a network mini-redirector first starts (in its **DriverEntry** routine), the driver must call the RDBSS [**RxRegisterMinirdr**](https://msdn.microsoft.com/library/windows/hardware/ff554693) routine to register the network mini-redirector with RDBSS. The network mini-redirector passes in a MINIRDR\_DISPATCH structure which includes configuration data and a table of routine pointers (a dispatch table) to the routines that the network mini-redirector driver implements.

The [**MRxStart**](https://msdn.microsoft.com/library/windows/hardware/ff550829) and [**MRxStop**](https://msdn.microsoft.com/library/windows/hardware/ff550833) routines must be implemented by the network mini-redirector driver to allow the driver to be started and stopped.

The sequence to start or stop the network mini-redirector is complex. This sequence is normally initiated by a user-mode application or service supplied with network mini-redirector driver to control the driver for administration and management purposes. The network mini-redirector can use a service that is configured to start automatically when the operating system starts. This service can request that the network mini-redirector be started whenever the operating system starts.

[**MRxStart**](https://msdn.microsoft.com/library/windows/hardware/ff550829) is called by RDBSS when the [**RxStartMinirdr**](https://msdn.microsoft.com/library/windows/hardware/ff554736) routine is called. The **RxStartMinirdr** routine is usually called as a result of an FSCTL or IOCTL request from a user-mode application or service to start the network mini-redirector. The call to **RxStartMinirdr** cannot be made from the **DriverEntry** routine of the network mini-redirector after a successful call to [**RxRegisterMinirdr**](https://msdn.microsoft.com/library/windows/hardware/ff554693)because some of the start processing requires that the driver initialization be completed. Once the **RxStartMinirdr** call is received, RDBSS completes the start process by calling the **MRxStart** routine of the network mini-redirector. If the call to **MRxStart** returns success, RDBSS sets the internal state of the mini-redirector in RDBSS to RDBSS\_STARTED.

[**MRxStop**](https://msdn.microsoft.com/library/windows/hardware/ff550833) is called by RDBSS when the [**RxStopMinirdr**](https://msdn.microsoft.com/library/windows/hardware/ff554743) routine is called. The RDBSS **RxStopMinirdr** routine is usually called as a result of an FSCTL or IOCTL request from a user-mode application or service to stop the network mini-redirector. This call can also be made from the network mini-redirector or, as part of shutdown process, by the operating system. Once the **RxStopMinirdr** call is received, RDBSS completes the process by calling the **MRxStop** routine of the network mini-redirector.

The [**MRxDevFcbXXXControlFile**](https://msdn.microsoft.com/library/windows/hardware/ff549876) routine is used to receive requests from a user-mode application or service to control the network mini-redirector by making IOCTL or FSCTL calls on a device FCB.

In addition, there are two low I/O routines that handle IOCTL and FSCTL operations on the driver object: [**MRxLowIOSubmit\[LOWIO\_OP\_FSCTL\]**](https://msdn.microsoft.com/library/windows/hardware/ff550709) and [**MRxLowIOSubmit\[LOWIO\_OP\_IOCTL\]**](https://msdn.microsoft.com/library/windows/hardware/ff550715).

A network mini-redirector can also use these low I/O routines to provide control and management of the network mini-redirector from a user-mode application or service.

The following table lists the routines that can be implemented by a network mini-redirector for start, stop, and device control operations.

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<thead>
<tr class="header">
<th align="left">Routine</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td align="left">[<strong>MRxDevFcbXXXControlFile</strong>](https://msdn.microsoft.com/library/windows/hardware/ff549876)</td>
<td align="left"><p>RDBSS calls this routine to pass a device FCB control request to the network mini-redirector. RDBSS issues this call in response to receiving an IRP_MJ_DEVICE_CONTROL, IRP_MJ_FILE_SYSTEM_CONTROL, or IRP_MJ_INTERNAL_DEVICE_CONTROL on a device FCB.</p></td>
</tr>
<tr class="even">
<td align="left">[<strong>MRxStart</strong>](https://msdn.microsoft.com/library/windows/hardware/ff550829)</td>
<td align="left"><p>RDBSS calls this routine to start the network mini-redirector.</p></td>
</tr>
<tr class="odd">
<td align="left">[<strong>MRxStop</strong>](https://msdn.microsoft.com/library/windows/hardware/ff550833)</td>
<td align="left"><p>RDBSS calls this routine to stop the network mini-redirector.</p></td>
</tr>
</tbody>
</table>

 

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[ifsk\ifsk]:%20Driver%20Start,%20Stop,%20and%20Device%20Control%20%20RELEASE:%20%285/9/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




