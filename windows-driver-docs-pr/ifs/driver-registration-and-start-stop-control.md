---
title: Driver Registration and Start/Stop Control
description: Driver Registration and Start/Stop Control
ms.assetid: 66f44703-1277-49fe-a481-c8712172db0f
keywords:
- RDBSS WDK file systems , start/stop control
- Redirected Drive Buffering Subsystem WDK file systems , start/stop control
- start/stop controls WDK RDBSS
- RDBSS WDK file systems , driver registration
- Redirected Drive Buffering Subsystem WDK file systems , driver registration
- driver registrations WDK RDBSS
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Driver Registration and Start/Stop Control


## <span id="ddk_driver_registration_and_start_stop_control_if"></span><span id="DDK_DRIVER_REGISTRATION_AND_START_STOP_CONTROL_IF"></span>


When the operating system is started, Windows loads RDBSS and any network mini-redirector drivers based on settings in the registry. For a monolithic network mini-redirector driver, which is linked statically with rdbsslib.lib, the driver must call the [**RxDriverEntry**](https://msdn.microsoft.com/library/windows/hardware/ff554404) routine from its [**DriverEntry**](https://msdn.microsoft.com/library/windows/hardware/ff544113) routine to initialize the copy of the RDBSSLIB library linked with the network driver. In this case, the **RxDriverEntry** routine must be called before any other RDBSS routines are called and used. For a non-monolithic network mini-redirector driver (the Microsoft SMB redirector), the rdbss.sys device driver is initialized in its own **DriverEntry** routine when loaded.

A network mini-redirector registers with RDBSS when the driver is loaded by the kernel and unregisters with RDBSS when the driver is unloaded. A network mini-redirector informs RDBSS that it has been loaded by calling [**RxRegisterMinirdr**](https://msdn.microsoft.com/library/windows/hardware/ff554693), the registration routine exported from RDBSS. As part of this registration process, the network mini-redirector passes a parameter to **RxRegisterMinirdr** that is a pointer to a large structure, MINIRDR\_DISPATCH. This structure contains configuration information for the network mini-redirector and a dispatch table of pointers to callback routines implemented by the network mini-redirector kernel driver. RDBSS makes calls to the network mini-redirector driver through this list of callback routines.

The [**RxRegisterMinirdr**](https://msdn.microsoft.com/library/windows/hardware/ff554693) routine sets all of the driver dispatch routines of the network mini-redirector driver to point to the top-level RDBSS dispatch routine, [**RxFsdDispatch**](https://msdn.microsoft.com/library/windows/hardware/ff554468). A network mini-redirector can override this behavior by saving its own entry points and rewriting the driver dispatch with its own entry points after the call to **RxRegisterMinirdr** returns or by setting a special parameter when calling **RxRegisterMinirdr**.

The network mini-redirector driver does not actually start operation until it receives a call to its [**MRxStart**](https://msdn.microsoft.com/library/windows/hardware/ff550829) routine, one of the callback routines passed in the MINIRDR\_DISPATCH structure. The **MrxStart** callback routine must be implemented by the network mini-redirector driver if it wishes to receive callback routines for operations unless the network mini-redirector preserves its own driver dispatch entry points. Otherwise, RDBSS will only allow the following I/O request packets through to the driver until **MrxStart** returns successfully:

-   IRP requests for device creates and device operations where the FileObject-&gt;FileName.Length on the IRPSP is zero and the FileObject-&gt;RelatedFileObject is **NULL**.

For any other IRP request, the RDBSS dispatch routine [**RxFsdDispatch**](https://msdn.microsoft.com/library/windows/hardware/ff554468) will return a status of STATUS\_REDIRECTOR\_NOT\_STARTED.

The RDBSS dispatch routine will also fail any requests for the following I/O request packets:

-   IRP\_MJ\_CREATE\_MAILSLOT

-   IRP\_MJ\_CREATE\_NAMED\_PIPE

The [**MrxStart**](https://msdn.microsoft.com/library/windows/hardware/ff550829) callback routine implemented by the network mini-redirector is called by RDBSS when the [**RxStartMinirdr**](https://msdn.microsoft.com/library/windows/hardware/ff554736) routine is called. The RDBSS **RxStartMinirdr** routine is usually called as a result of a file system control code (FSCTL) or I/O control code (IOCTL) request from a user-mode application or service to start the network mini-redirector. The call to **RxStartMinirdr** cannot be made from the [**DriverEntry**](https://msdn.microsoft.com/library/windows/hardware/ff544113) routine of the network mini-redirector after a successful call to [**RxRegisterMinirdr**](https://msdn.microsoft.com/library/windows/hardware/ff554693)since some of the start processing requires that the driver initialization be completed. Once the **RxStartMinirdr** call is received, RDBSS completes the start process by calling the **MrxStart** routine of the network mini-redirector. If the call to **MrxStart** returns success, RDBSS sets the internal state of the mini-redirector in RDBSS to RDBSS\_STARTED.

RDBSS exports a routine, [**RxSetDomainForMailslotBroadcast**](https://msdn.microsoft.com/library/windows/hardware/ff554718), to set the domain for mailslot broadcasts. This routine is used during registration if the network mini-redirector supports mailslots.

A convenience routine, [**\_\_RxFillAndInstallFastIoDispatch**](https://msdn.microsoft.com/library/windows/hardware/ff557374), exported by RDBSS can be used to copy all of the IRP\_MJ\_XXX driver routine pointers for handling I/O request processing to the comparable fast I/O dispatch vectors, but this routine only works for non-monolithic drivers.

RDBSS also exports routines to notify RDBSS that the network mini-redirector is starting or stopping. These calls are used if a network mini-redirector includes a user-mode administration service or utility application that starts and stops the redirector. This user-mode service or application can send custom FSCTL or IOCTL requests to the network mini-redirector driver to indicate that it should start or stop. The redirector can call the RDBSS [**RxStartMinirdr**](https://msdn.microsoft.com/library/windows/hardware/ff554736) or [**RxStopMinirdr**](https://msdn.microsoft.com/library/windows/hardware/ff554743) routines to notify RDBSS to start or stop this network mini-redirector.

The following table lists the RDBSS driver registration and start/stop control routines.

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
<td align="left"><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff554404" data-raw-source="[&lt;strong&gt;RxDriverEntry&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff554404)"><strong>RxDriverEntry</strong></a></p></td>
<td align="left"><p>This routine is called by a monolithic network mini-redirector driver from its <a href="https://msdn.microsoft.com/library/windows/hardware/ff544113" data-raw-source="[&lt;strong&gt;DriverEntry&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff544113)"><strong>DriverEntry</strong></a> routine to initialize RDBSS.</p>
<p>For non-monolithic drivers, this initialization routine is equivalent to the <a href="https://msdn.microsoft.com/library/windows/hardware/ff544113" data-raw-source="[&lt;strong&gt;DriverEntry&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff544113)"><strong>DriverEntry</strong></a> routine of the rbss.sys device driver.</p></td>
</tr>
<tr class="even">
<td align="left"><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff554693" data-raw-source="[&lt;strong&gt;RxRegisterMinirdr&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff554693)"><strong>RxRegisterMinirdr</strong></a></p></td>
<td align="left"><p>This routine is called by a network mini-redirector driver to register the driver with RDBSS, which adds the registration information to an internal registration table. RDBSS also builds a device object for the network mini-redirector.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff554718" data-raw-source="[&lt;strong&gt;RxSetDomainForMailslotBroadcast&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff554718)"><strong>RxSetDomainForMailslotBroadcast</strong></a></p></td>
<td align="left"><p>This routine is called by a network mini-redirector driver to set the domain used for mailslot broadcasts, if mailslots are supported by the driver.</p></td>
</tr>
<tr class="even">
<td align="left"><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff554736" data-raw-source="[&lt;strong&gt;RxStartMinirdr&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff554736)"><strong>RxStartMinirdr</strong></a></p></td>
<td align="left"><p>This routine starts up a network mini-redirector that called to register itself. RDBSS will also register the network mini-redirector driver as a UNC provider with the MUP if the driver indicates support for UNC names.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff554743" data-raw-source="[&lt;strong&gt;RxStopMinirdr&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff554743)"><strong>RxStopMinirdr</strong></a></p></td>
<td align="left"><p>This routine stops a network mini-redirector driver. A driver that is stopped will no longer receive new commands except IOCTL or FSCTL requests.</p></td>
</tr>
<tr class="even">
<td align="left"><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff554662" data-raw-source="[&lt;strong&gt;RxpUnregisterMinirdr&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff554662)"><strong>RxpUnregisterMinirdr</strong></a></p></td>
<td align="left"><p>This routine is called by a network mini-redirector driver to de-register the driver with RDBSS and remove the registration information from the internal RDBSS registration table.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff554744" data-raw-source="[&lt;strong&gt;RxUnregisterMinirdr&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff554744)"><strong>RxUnregisterMinirdr</strong></a></p></td>
<td align="left"><p>This routine is an inline function defined in rxstruc.h that is called by a network mini-redirector driver to de-register the driver with RDBSS and remove the registration information from the internal RDBSS registration table. The <a href="https://msdn.microsoft.com/library/windows/hardware/ff554744" data-raw-source="[&lt;strong&gt;RxUnregisterMinirdr&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff554744)"><strong>RxUnregisterMinirdr</strong></a> inline function internally calls <a href="https://msdn.microsoft.com/library/windows/hardware/ff554662" data-raw-source="[&lt;strong&gt;RxpUnregisterMinirdr&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff554662)"><strong>RxpUnregisterMinirdr</strong></a>.</p></td>
</tr>
<tr class="even">
<td align="left"><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff557374" data-raw-source="[&lt;strong&gt;__RxFillAndInstallFastIoDispatch&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff557374)"><strong>__RxFillAndInstallFastIoDispatch</strong></a></p></td>
<td align="left"><p>This routine fills out a fast I/O dispatch vector to be identical with the normal dispatch I/O vector and installs it into the driver object associated with the device object passed.</p></td>
</tr>
</tbody>
</table>

 

The following macro is defined in the mrx.h header file that calls one of these routines. This macro is normally used instead of calling the [**\_\_RxFillAndInstallFastIoDispatch**](https://msdn.microsoft.com/library/windows/hardware/ff557374) routine directly.

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<thead>
<tr class="header">
<th align="left">Macro</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td align="left"><p><strong>RxFillAndInstallFastIoDispatch</strong>(<em>__devobj</em>, <em>__fastiodisp</em>)</p></td>
<td align="left"><p>This macro calls <a href="https://msdn.microsoft.com/library/windows/hardware/ff557374" data-raw-source="[&lt;strong&gt;__RxFillAndInstallFastIoDispatch&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff557374)"><strong>__RxFillAndInstallFastIoDispatch</strong></a>to fill out a fast I/O dispatch vector to be identical with the normal dispatch I/O vector and installs it into the driver object associated with the device object passed.</p></td>
</tr>
</tbody>
</table>

 

 

 




