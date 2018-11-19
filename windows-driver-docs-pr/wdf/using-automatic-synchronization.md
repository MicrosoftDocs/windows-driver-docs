---
title: Using Automatic Synchronization
description: Using Automatic Synchronization
ms.assetid: be7d3c0e-c3cf-4104-ab81-5ecdcb9163c8
keywords:
- synchronization WDK KMDF
- automatic synchronization WDK KMDF
- locking WDK KMDF
- device-level synchronization WDK KMDF
- queue-level synchronization WDK KMDF
- no synchronization WDK KMDF
- synchronization scope WDK KMDF
- execution levels WDK KMDF
- WdfExecutionLevelPassive
- WdfExecutionLevelDispatch
- WdfExecutionLevelInheritFromParent
- WdfSynchronizationScopeDevice
- WdfSynchronizationScopeQueue
- WdfSynchronizationScopeNone
- WdfSynchronizationScopeInheritFromParent
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Using Automatic Synchronization


Almost all of the code in a framework-based driver resides in event callback functions. The framework automatically synchronizes most of a driver's callback functions, as follows:

-   The framework always synchronizes [general device object](https://msdn.microsoft.com/library/windows/hardware/dn265631#device-callbacks), [functional device object (FDO)](https://msdn.microsoft.com/library/windows/hardware/dn265631#fdo-callbacks), and [physical device object (PDO)](https://msdn.microsoft.com/library/windows/hardware/dn265631#pdo-callbacks) event callback functions with each other so that only one of the callback functions (except [*EvtDeviceSurpriseRemoval*](https://msdn.microsoft.com/library/windows/hardware/ff540913), [*EvtDeviceQueryRemove*](https://msdn.microsoft.com/library/windows/hardware/ff540883), and [*EvtDeviceQueryStop*](https://msdn.microsoft.com/library/windows/hardware/ff540885)) can be called at a time for each device. These callback functions support Plug and Play (PnP) and power management events and are called at IRQL = PASSIVE\_LEVEL.

-   Optionally, the framework can synchronize the execution of the callback functions that handle a driver's I/O requests, so that these callback functions run one at a time. Specifically, the framework can synchronize the callback functions for [queue](https://msdn.microsoft.com/library/windows/hardware/dn265647), [interrupt](https://msdn.microsoft.com/library/windows/hardware/dn265640), [deferred procedure call (DPC)](https://msdn.microsoft.com/library/windows/hardware/dn265635), [timer](https://msdn.microsoft.com/library/windows/hardware/dn265670), [work-item](https://msdn.microsoft.com/library/windows/hardware/dn265673), and [file](https://msdn.microsoft.com/library/windows/hardware/dn265638) objects, along with the request object's [*EvtRequestCancel*](https://msdn.microsoft.com/library/windows/hardware/ff541817) callback function. The framework calls most of these callback functions at IRQL = DISPATCH\_LEVEL, but you can force the queue and file object callback functions to run at IRQL = PASSIVE\_LEVEL. (Work-item callback functions always run at PASSIVE\_LEVEL.)

The framework implements this automatic synchronization by using a set of internal synchronization locks. The framework ensures that two or more threads cannot call the same callback function at the same time, because each thread must wait until it can acquire a synchronization lock before calling a callback function. (Optionally, drivers can also acquire these synchronization locks when necessary. For more information, see [Using Framework Locks](using-framework-locks.md).)

Your driver should store object-specific data in [object context space](framework-object-context-space.md). If your driver uses only framework-defined interfaces, only callback functions that receive a handle to the object can access this data. If the framework is synchronizing calls to the driver's callback functions, only one callback function will be called at a time and the object's context space will be accessible to only one callback function at a time.

Unless your driver implements [passive-level interrupt handling](supporting-passive-level-interrupts.md), code that services interrupts and accesses interrupt data must run at the device's IRQL (DIRQL) and requires additional synchronization. For more information, see [Synchronizing Interrupt Code](synchronizing-interrupt-code.md).

If your driver enables automatic synchronization of the callback functions that handle I/O requests, the framework synchronizes these callback functions so that they run one at a time. The following table lists the callback functions that the framework synchronizes.

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<thead>
<tr class="header">
<th align="left">Object type</th>
<th align="left">Synchronized Callback Functions</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td align="left"><p>Queue object</p></td>
<td align="left"><p><a href="request-handlers.md" data-raw-source="[Request handlers](request-handlers.md)">Request handlers</a>, <a href="https://msdn.microsoft.com/library/windows/hardware/ff541771" data-raw-source="[&lt;em&gt;EvtIoQueueState&lt;/em&gt;](https://msdn.microsoft.com/library/windows/hardware/ff541771)"><em>EvtIoQueueState</em></a>, <a href="https://msdn.microsoft.com/library/windows/hardware/ff541779" data-raw-source="[&lt;em&gt;EvtIoResume&lt;/em&gt;](https://msdn.microsoft.com/library/windows/hardware/ff541779)"><em>EvtIoResume</em></a>, <a href="https://msdn.microsoft.com/library/windows/hardware/ff541788" data-raw-source="[&lt;em&gt;EvtIoStop&lt;/em&gt;](https://msdn.microsoft.com/library/windows/hardware/ff541788)"><em>EvtIoStop</em></a></p></td>
</tr>
<tr class="even">
<td align="left"><p>File object</p></td>
<td align="left"><p>All <a href="https://msdn.microsoft.com/library/windows/hardware/dn265638" data-raw-source="[callback functions](https://msdn.microsoft.com/library/windows/hardware/dn265638)">callback functions</a></p></td>
</tr>
<tr class="odd">
<td align="left"><p>Request object</p></td>
<td align="left"><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff541817" data-raw-source="[&lt;em&gt;EvtRequestCancel&lt;/em&gt;](https://msdn.microsoft.com/library/windows/hardware/ff541817)"><em>EvtRequestCancel</em></a></p></td>
</tr>
</tbody>
</table>

 

Optionally, the framework can also synchronize these callback functions with any interrupt, DPC, work-item, and timer object callback functions that your driver provides for the device (excluding the interrupt object's [*EvtInterruptIsr*](https://msdn.microsoft.com/library/windows/hardware/ff541735) callback function). To enable this additional synchronization, the driver must set the **AutomaticSerialization** member of these objects' configuration structures to **TRUE**.

In summary, the framework's automatic synchronization capability provides the following features:

-   The framework always synchronizes each device's PnP and power management callback functions.

-   Optionally, the framework can synchronize an I/O queue's request handlers, and a few additional callback functions (see the previous table).

-   A driver can ask the framework to synchronize callback functions for interrupt, DPC, work-item, and timer objects.

-   Drivers must synchronize code that services interrupts and accesses interrupt data by using the techniques that are described in [Synchronizing Interrupt Code](synchronizing-interrupt-code.md).

-   The framework does not synchronize a driver's other callback functions, such as the driver's [*CompletionRoutine*](https://msdn.microsoft.com/library/windows/hardware/ff540745) callback function, or the callback functions that the I/O target object defines. Instead, the framework provides additional [locks](using-framework-locks.md) that drivers can use to synchronize these callback functions.

### Choosing a Synchronization Scope

You can choose to have the framework synchronize all of the callback functions that are associated with all of a device's I/O queues. Alternatively, you can choose to have the framework separately synchronize the callback functions for each of a device's I/O queues. The synchronization options that are available to your driver are as follows:

-   Device-level synchronization

    The framework synchronizes the callback functions that the previous table contains, for all of the device's I/O queues, so that they run one at a time. The framework achieves this synchronization by acquiring the device's synchronization lock before calling a callback function.

-   Queue-level synchronization

    The framework synchronizes the callback functions that the previous table contains, for each individual I/O queue, so that they run one at a time. The framework achieves this synchronization by acquiring the queue's synchronization lock before calling a callback function.

-   No synchronization

    The framework does not synchronize the execution of the callback functions that the previous table contains and does not acquire a synchronization lock before calling the callback functions. If synchronization is required, the driver must provide it.

To specify whether you want the framework to provide device-level synchronization, queue-level synchronization, or no synchronization for your driver, you can specify a *synchronization scope* for your driver object, device objects, or queue objects. The **SynchronizationScope** member of an object's [**WDF\_OBJECT\_ATTRIBUTES**](https://msdn.microsoft.com/library/windows/hardware/ff552400) structure identifies the object's synchronization scope. The synchronization scope values that your driver can specify are:

<a href="" id="wdfsynchronizationscopedevice"></a>**WdfSynchronizationScopeDevice**  
The framework synchronizes by obtaining a device object's synchronization lock.

<a href="" id="wdfsynchronizationscopequeue"></a>**WdfSynchronizationScopeQueue**  
The framework synchronizes by obtaining a queue object's synchronization lock.

<a href="" id="wdfsynchronizationscopenone"></a>**WdfSynchronizationScopeNone**  
The framework does not synchronize and does not obtain a synchronization lock.

<a href="" id="wdfsynchronizationscopeinheritfromparent"></a>**WdfSynchronizationScopeInheritFromParent**  
The framework obtains the object's **SynchronizationScope** value from the object's parent object.

In general, we do not recommend using device-level synchronization.

For more information about the synchronization scope values, see [**WDF\_SYNCHRONIZATION\_SCOPE**](https://msdn.microsoft.com/library/windows/hardware/ff552518).

The default synchronization scope for driver objects is **WdfSynchronizationScopeNone**. The default synchronization scope for device and queue objects is **WdfSynchronizationScopeInheritFromParent**.

If you want the framework to provide device-level synchronization for all devices, you can use the following steps:

1.  Set **SynchronizationScope** to **WdfSynchronizationScopeDevice** in the [**WDF\_OBJECT\_ATTRIBUTES**](https://msdn.microsoft.com/library/windows/hardware/ff552400) structure of the driver's *driver* object.

2.  Use the default **WdfSynchronizationScopeInheritFromParent** value for each *device* object.

Alternatively, to provide device-level synchronization for individual devices, you can use the following steps:

1.  Use the default **WdfSynchronizationScopeNone** value for the *driver* object.

2.  Set **SynchronizationScope** to **WdfSynchronizationScopeDevice** in the [**WDF\_OBJECT\_ATTRIBUTES**](https://msdn.microsoft.com/library/windows/hardware/ff552400) structure of individual *device* objects.

If you want the framework to provide queue-level synchronization for a device, the following techniques are available:

-   For framework versions 1.9 and later, you should enable queue-level synchronization for individual queues by setting **WdfSynchronizationScopeQueue** in the [**WDF\_OBJECT\_ATTRIBUTES**](https://msdn.microsoft.com/library/windows/hardware/ff552400) structure of the queue object. This is the preferred technique.

-   Alternatively, you can use the following steps in all framework versions:
    1.  Set **SynchronizationScope** to **WdfSynchronizationScopeQueue** in the [**WDF\_OBJECT\_ATTRIBUTES**](https://msdn.microsoft.com/library/windows/hardware/ff552400) structure of the *device* object.
    2.  Use the default **WdfSynchronizationScopeInheritFromParent** value for each device's *queue* objects.

If you do not want the framework to synchronize the callback functions that handle your driver's I/O requests, use the default **SynchronizationScope** value for your driver's driver, device, and queue objects. In this case, the framework does not automatically synchronize the driver's I/O request-related callback functions, and the callback functions can be called at IRQL &lt;= DISPATCH\_LEVEL.

Note that setting a **SynchronizationScope** value synchronizes only the callback functions that the previous table contains. If you want the framework to also synchronize the driver's interrupt, DPC, work-item, and timer object callback functions, the driver must set the **AutomaticSerialization** member of these objects' configuration structures to **TRUE**.

However, you can set **AutomaticSerialization** to **TRUE** only if all of the callback functions that you want to synchronize run at the same IRQL. Choosing an *execution level*, which is described next, might result in incompatible IRQL levels. In such a situation, the driver must use [framework locks](using-framework-locks.md) instead of setting **AutomaticSerialization**. For more information about the configuration structures for interrupt, DPC, work-item, and timer objects, and for more information about restrictions that apply to setting **AutomaticSerialization** in these structures, see [**WDF\_INTERRUPT\_CONFIG**](https://msdn.microsoft.com/library/windows/hardware/ff552347), [**WDF\_DPC\_CONFIG**](https://msdn.microsoft.com/library/windows/hardware/ff551296), [**WDF\_WORKITEM\_CONFIG**](https://msdn.microsoft.com/library/windows/hardware/ff553086), and [**WDF\_TIMER\_CONFIG**](https://msdn.microsoft.com/library/windows/hardware/ff552519).

If you set **AutomaticSerialization** to **TRUE**, you should select queue-level synchronization.

### Choosing an Execution Level

When a driver creates some types of framework objects, it can specify an *execution level* for the object. The execution level specifies the IRQL at which the framework will call the object's event callback functions that handle a driver's I/O requests.

If a driver supplies an execution level, the supplied level affects the callback functions for queue and file objects. Ordinarily, if the driver is using automatic synchronization, the framework calls these callback functions at IRQL = DISPATCH\_LEVEL. By specifying an execution level, the driver can force the framework to call these callback functions at IRQL = PASSIVE\_LEVEL. The framework uses the following rules when setting the IRQL at which queue and file object callback functions are called:

-   If a driver uses automatic synchronization, its queue and file object callback functions are called at IRQL = DISPATCH\_LEVEL unless the driver asks the framework to call its callback functions at IRQL = PASSIVE\_LEVEL.

-   If a driver is not using automatic synchronization and does not specify an execution level, the driver's queue and file object callback functions can be called at IRQL &lt;= DISPATCH\_LEVEL.

Note that if your driver provides file object callback functions, you will most likely want the framework to call these callback functions at IRQL = PASSIVE\_LEVEL because some file data, such as the file name, is pageable.

To supply an execution level, your driver must specify a value for the **ExecutionLevel** member of an object's [**WDF\_OBJECT\_ATTRIBUTES**](https://msdn.microsoft.com/library/windows/hardware/ff552400) structure. The execution level values that your driver can specify are:

<a href="" id="wdfexecutionlevelpassive"></a>**WdfExecutionLevelPassive**  
The framework calls the object's callback functions at IRQL = PASSIVE\_LEVEL.

<a href="" id="wdfexecutionleveldispatch"></a>**WdfExecutionLevelDispatch**  
The framework can call the object's callback functions at IRQL &lt;= DISPATCH\_LEVEL. (If the driver is using automatic synchronization, the framework always calls the callback functions at IRQL = DISPATCH\_LEVEL.)

<a href="" id="wdfexecutionlevelinheritfromparent"></a>**WdfExecutionLevelInheritFromParent**  
The framework obtains the object's **ExecutionLevel** value from the object's parent.

The default execution level for driver objects is **WdfExecutionLevelDispatch**. The default execution level for all other objects is **WdfExecutionLevelInheritFromParent**.

For more information about the execution level values, see [**WDF\_EXECUTION\_LEVEL**](https://msdn.microsoft.com/library/windows/hardware/ff551310).

The following table shows the IRQL level at which the framework can call a driver's callback functions for queue objects and file objects.

<table>
<colgroup>
<col width="33%" />
<col width="33%" />
<col width="33%" />
</colgroup>
<thead>
<tr class="header">
<th align="left">Synchronization Scope</th>
<th align="left">Execution Level</th>
<th align="left">IRQL of Queue and File Callback Functions</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td align="left"><p><strong>WdfSynchronizationScopeDevice</strong></p></td>
<td align="left"><p><strong>WdfExecutionLevelPassive</strong></p></td>
<td align="left"><p>PASSIVE_LEVEL</p></td>
</tr>
<tr class="even">
<td align="left"><p><strong>WdfSynchronizationScopeDevice</strong></p></td>
<td align="left"><p><strong>WdfExecutionLevelDispatch</strong></p></td>
<td align="left"><p>DISPATCH_LEVEL</p></td>
</tr>
<tr class="odd">
<td align="left"><p><strong>WdfSynchronizationScopeQueue</strong></p></td>
<td align="left"><p><strong>WdfExecutionLevelPassive</strong></p></td>
<td align="left"><p>PASSIVE_LEVEL</p></td>
</tr>
<tr class="even">
<td align="left"><p><strong>WdfSynchronizationScopeQueue</strong></p></td>
<td align="left"><p><strong>WdfExecutionLevelDispatch</strong></p></td>
<td align="left"><p>DISPATCH_LEVEL</p></td>
</tr>
<tr class="odd">
<td align="left"><p><strong>WdfSynchronizationScopeNone</strong></p></td>
<td align="left"><p><strong>WdfExecutionLevelPassive</strong></p></td>
<td align="left"><p>PASSIVE_LEVEL</p></td>
</tr>
<tr class="even">
<td align="left"><p><strong>WdfSynchronizationScopeNone</strong></p></td>
<td align="left"><p><strong>WdfExecutionLevelDispatch</strong></p></td>
<td align="left"><p>&lt;= DISPATCH_LEVEL</p></td>
</tr>
</tbody>
</table>

 

You can set the execution level to **WdfExecutionLevelPassive** or **WdfExecutionLevelDispatch** for driver, device, file, queue, timer, and general objects. For other objects, only **WdfExecutionLevelInheritFromParent** is allowed.

You should specify **WdfExecutionLevelPassive** if:

-   Your driver's callback functions must call framework methods or Windows Driver Model (WDM) routines that can be called only at IRQL = PASSIVE\_LEVEL.

-   Your driver's callback functions must access pageable code or data. (For example, file object callback functions typically access pageable data.)

Instead of setting **WdfExecutionLevelPassive**, your driver can set **WdfExecutionLevelDispatch** and provide a callback function that creates [work items](using-framework-work-items.md) if it must handle some operations at IRQL = PASSIVE\_LEVEL.

Before you decide whether your driver should set an object's execution level to **WdfExecutionLevelPassive**, you should determine the IRQL at which your driver and other drivers in the driver stack are called. Consider the following situations:

-   If your driver is at the top of the kernel-mode driver stack, the system typically calls the driver at IRQL = PASSIVE\_LEVEL. The client of such a driver might be a UMDF-based driver or a user-mode application. Specifying **WdfExecutionLevelPassive** does not adversely affect the driver's performance, because the framework does not have to queue your driver's calls to work items that are called at IRQL = PASSIVE\_LEVEL. (In fact, if your driver's client runs in user mode, the driver is always called at IRQL = PASSIVE\_LEVEL even if you do not specify **WdfExecutionLevelPassive**.)

-   If your driver is not at the top of the stack, the system will likely not call your driver at IRQL = PASSIVE\_LEVEL. Therefore, the framework must queue your driver's calls to work items, which are later called at IRQL = PASSIVE\_LEVEL. This process can cause poor driver performance, compared to allowing your driver's callback functions to be called at IRQL &lt;= DISPATCH\_LEVEL.

For DPC objects, and for timer objects that do not represent [passive-level timers](using-timers.md), note that you cannot set the **AutomaticSerialization** member of the configuration structure to **TRUE** if you have set the parent device's execution level to **WdfExecutionLevelPassive**. This is because the framework will acquire the device object's [callback synchronization locks](using-framework-locks.md) at IRQL = PASSIVE\_LEVEL and therefore the locks cannot be used to synchronize the DPC or timer object callback functions, which must execute at IRQL = DISPATCH\_LEVEL. In such a case, your driver should use [framework spin locks](using-framework-locks.md#framework-spin-locks) in any device, DPC, or timer object callback functions that must be synchronized with each other.

Also note that for timer objects that *do* represent passive-level timers, you can set the **AutomaticSerialization** member of the configuration structure to TRUE *only* if the parent device's execution level is set to **WdfExecutionLevelPassive**.

 

 





