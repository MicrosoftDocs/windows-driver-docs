---
title: Waits and APCs
author: windows-driver-content
description: Waits and APCs
MS-HAID:
- 'Synchro\_c88e3997-b7c1-494d-983b-2a69b229a904.xml'
- 'kernel.waits\_and\_apcs'
MSHAttr:
- 'PreferredSiteName:MSDN'
- 'PreferredLib:/library/windows/hardware'
ms.assetid: b967beec-922c-4acf-a578-c476ce024fdb
keywords: ["kernel dispatcher objects WDK , alerts", "dispatcher objects WDK kernel , alerts", "APCs WDK kernel", "alerts WDK kernel", "kernel dispatcher objects WDK , APCs", "dispatcher objects WDK kernel , APCs", "Alertable parameter", "WaitMode parameter", "kernel dispatcher objects WDK , waiting for", "dispatcher objects WDK kernel , waiting for"]
---

# Waits and APCs


## <a href="" id="ddk-do-waiting-threads-receive-alerts-and-apcs-kg"></a>


Threads that wait for a dispatcher object on behalf of a user-mode caller must be prepared for that wait to be interrupted, either by a user APC or by thread termination. When a thread calls [**KeWaitForSingleObject**](https://msdn.microsoft.com/library/windows/hardware/ff553350), [**KeWaitForMultipleObjects**](https://msdn.microsoft.com/library/windows/hardware/ff553324), [**KeWaitForMutexObject**](https://msdn.microsoft.com/library/windows/hardware/ff553344), or [**KeDelayExecutionThread**](https://msdn.microsoft.com/library/windows/hardware/ff551986), the operating system can place the thread in a wait state. Typically, the thread remains in the wait state until the operating system can complete the operation that the caller requests. However, if the caller specifies *WaitMode* = UserMode, the operating system might interrupt the wait. In that case, the routine exits with an NTSTATUS value of STATUS\_USER\_APC.

Any driver that calls one of the preceding four routines with *WaitMode* = UserMode must be prepared to receive a return value of STATUS\_USER\_APC. The driver must complete its current operation with STATUS\_USER\_APC and return control to user mode.

The exact situations in which the operating system interrupts the wait depends on the value of the *Alertable* parameter of the routine. If *Alertable* = **TRUE**, the wait is an alertable wait. Otherwise, the wait is a non-alertable wait. The operating system interrupts alertable waits only to deliver a user APC. The operating system interrupts both kinds of waits to terminate the thread.

The following table explains the relationship between different parameter settings, waits, and user APC delivery.

<table>
<colgroup>
<col width="33%" />
<col width="33%" />
<col width="33%" />
</colgroup>
<thead>
<tr class="header">
<th>Parameters</th>
<th>Wait interrupted?</th>
<th>User APC delivered?</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><em>Alertable</em> = <strong>TRUE</strong>
<em>WaitMode</em> = <strong>UserMode</strong></td>
<td><p>Yes</p></td>
<td><p>Yes</p></td>
</tr>
<tr class="even">
<td><em>Alertable</em> = <strong>TRUE</strong>
<em>WaitMode</em> = <strong>KernelMode</strong></td>
<td><p>Yes</p></td>
<td><p>No</p></td>
</tr>
<tr class="odd">
<td><em>Alertable</em> = <strong>FALSE</strong>
<em>WaitMode</em> = <strong>UserMode</strong></td>
<td><p>Yes, for thread termination. No, for user APCs.</p></td>
<td><p>No</p></td>
</tr>
<tr class="even">
<td><em>Alertable</em> = <strong>FALSE</strong>
<em>WaitMode</em> = <strong>KernelMode</strong></td>
<td><p>No</p></td>
<td><p>No</p></td>
</tr>
</tbody>
</table>

 

You can disable kernel APCs for a thread. If you do disable kernel APCs for a thread, both user APC delivery and thread termination for that thread are also disabled. For more information about how to disable APCs, see [Disabling APCs](disabling-apcs.md).

Alerts, a seldom-used mechanism that are internal to the operating system, can also interrupt alertable wait states. An alert can interrupt a wait when *Alertable* = **TRUE**, regardless of the value of the *WaitMode* parameter. The waiting routine returns a value of STATUS\_ALERTED.

Note that kernel APCs run preemptively, and do not cause **KeWaitFor*Xxx*** or **KeDelayExecutionThread** to return. The system interrupts and resumes the wait internally. Drivers are normally unaffected by this process, but it is possible for the driver to miss a dispatcher object signal for a transient condition, such as a call to [**KePulseEvent**](https://msdn.microsoft.com/library/windows/hardware/ff552979).

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bkernel\kernel%5D:%20Waits%20and%20APCs%20%20RELEASE:%20%286/14/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


