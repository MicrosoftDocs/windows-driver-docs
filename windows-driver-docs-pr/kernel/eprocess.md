---
title: Windows kernel opaque structures
description: Windows kernel opaque structures
ms.assetid: 4053d82e-78ae-4945-ad5b-44ba41229a5d
ms.localizationpriority: medium
ms.date: 10/17/2018
---

# Windows kernel opaque structures


The following table contains Windows kernel opaque structures:

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<thead>
<tr class="header">
<th>Opaque Structure</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><strong>EPROCESS</strong></td>
<td><p>The <strong>EPROCESS</strong> structure is an opaque structure that serves as the process object for a process.</p>
<p>Some routines, such as <a href="https://docs.microsoft.com/windows-hardware/drivers/ddi/content/ntddk/nf-ntddk-psgetprocesscreatetimequadpart" data-raw-source="[&lt;strong&gt;PsGetProcessCreateTimeQuadPart&lt;/strong&gt;](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/ntddk/nf-ntddk-psgetprocesscreatetimequadpart)"><strong>PsGetProcessCreateTimeQuadPart</strong></a>, use <strong>EPROCESS</strong> to identify the process to operate on. Drivers can use the <a href="https://docs.microsoft.com/windows-hardware/drivers/kernel/mm-bad-pointer#psgetcurrentprocess" data-raw-source="[&lt;strong&gt;PsGetCurrentProcess&lt;/strong&gt;](https://docs.microsoft.com/windows-hardware/drivers/kernel/mm-bad-pointer#psgetcurrentprocess)"><strong>PsGetCurrentProcess</strong></a> routine to obtain a pointer to the process object for the current process and can use the <a href="https://docs.microsoft.com/windows-hardware/drivers/ddi/content/wdm/nf-wdm-obreferenceobjectbyhandle" data-raw-source="[&lt;strong&gt;ObReferenceObjectByHandle&lt;/strong&gt;](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/wdm/nf-wdm-obreferenceobjectbyhandle)"><strong>ObReferenceObjectByHandle</strong></a> routine to obtain a pointer to the process object that is associated with the specified handle. The <a href="https://docs.microsoft.com/windows-hardware/drivers/kernel/mm64bitphysicaladdress" data-raw-source="[&lt;strong&gt;PsInitialSystemProcess&lt;/strong&gt;](https://docs.microsoft.com/windows-hardware/drivers/kernel/mm64bitphysicaladdress)"><strong>PsInitialSystemProcess</strong></a> global variable points to the process object for the system process.</p>
<p>Note that a process object is an Object Manager object. Drivers should use Object Manager routines such as <a href="https://docs.microsoft.com/windows-hardware/drivers/ddi/content/wdm/nf-wdm-obfreferenceobject" data-raw-source="[&lt;strong&gt;ObReferenceObject&lt;/strong&gt;](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/wdm/nf-wdm-obfreferenceobject)"><strong>ObReferenceObject</strong></a> and <a href="https://docs.microsoft.com/windows-hardware/drivers/ddi/content/wdm/nf-wdm-obdereferenceobject" data-raw-source="[&lt;strong&gt;ObDereferenceObject&lt;/strong&gt;](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/wdm/nf-wdm-obdereferenceobject)"><strong>ObDereferenceObject</strong></a> to maintain the object's reference count.</p>
<p>Header: Wdm.h. Include: Wdm.h, Ntddk.h, Ntifs.h.</p></td>
</tr>
<tr class="even">
<td><strong>ETHREAD</strong></td>
<td><p>The <strong>ETHREAD</strong> structure is an opaque structure that serves as the thread object for a thread.</p>
<p>Some routines, such as <a href="https://docs.microsoft.com/windows-hardware/drivers/ddi/content/ntifs/nf-ntifs-psissystemthread" data-raw-source="[&lt;strong&gt;PsIsSystemThread&lt;/strong&gt;](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/ntifs/nf-ntifs-psissystemthread)"><strong>PsIsSystemThread</strong></a>, use <strong>ETHREAD</strong> to identify the thread to operate on. Drivers can use the <a href="https://docs.microsoft.com/windows-hardware/drivers/ddi/content/ntddk/nf-ntddk-psgetcurrentthread" data-raw-source="[&lt;strong&gt;PsGetCurrentThread&lt;/strong&gt;](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/ntddk/nf-ntddk-psgetcurrentthread)"><strong>PsGetCurrentThread</strong></a> routine to obtain a pointer to the thread object for the current thread and can use the <a href="https://docs.microsoft.com/windows-hardware/drivers/ddi/content/wdm/nf-wdm-obreferenceobjectbyhandle" data-raw-source="[&lt;strong&gt;ObReferenceObjectByHandle&lt;/strong&gt;](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/wdm/nf-wdm-obreferenceobjectbyhandle)"><strong>ObReferenceObjectByHandle</strong></a> routine to obtain a pointer to the thread object that is associated with the specified handle.</p>
<p>Note that a thread object is an Object Manager object. Drivers should use Object Manager routines such as <a href="https://docs.microsoft.com/windows-hardware/drivers/ddi/content/wdm/nf-wdm-obfreferenceobject" data-raw-source="[&lt;strong&gt;ObReferenceObject&lt;/strong&gt;](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/wdm/nf-wdm-obfreferenceobject)"><strong>ObReferenceObject</strong></a> and <a href="https://docs.microsoft.com/windows-hardware/drivers/ddi/content/wdm/nf-wdm-obdereferenceobject" data-raw-source="[&lt;strong&gt;ObDereferenceObject&lt;/strong&gt;](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/wdm/nf-wdm-obdereferenceobject)"><strong>ObDereferenceObject</strong></a> to maintain the object's reference count.</p>
<p>Header: Wdm.h. Include: Wdm.h, Ntddk.h, Ntifs.h.</p></td>
</tr>
<tr class="odd">
<td><strong>EX_RUNDOWN_REF</strong></td>
<td><p>The <strong>EX_RUNDOWN_REF</strong> structure is an opaque system structure that contains information about the status of run-down protection for an associated shared object.</p>
<pre class="syntax"><code>typedef struct _EX_RUNDOWN_REF {
  
  ...  // opaque
  
} EX_RUNDOWN_REF, *PEX_RUNDOWN_REF;</code></pre>
<p>The run-down protection routines all take a pointer to an <strong>EX_RUNDOWN_REF</strong> structure as their first parameter. These routines are listed at the bottom of this page.</p>
<p>For more information, see <a href="run-down-protection.md" data-raw-source="[Run-Down Protection](run-down-protection.md)">Run-Down Protection</a>.</p>
<p>Header: Wdm.h. Include Wdm.h.</p></td>
</tr>
<tr class="even">
<td><strong>EX_TIMER</strong></td>
<td><p>The <strong>EX_TIMER</strong> structure is an opaque structure that is used by the operating system to represent an <strong>EX_TIMER</strong> timer object.</p>
<pre class="syntax"><code>typedef struct _EX_TIMER *PEX_TIMER;</code></pre>
<p>All members of this structure are opaque to drivers.</p>
<p>The following <strong>Ex<em>Xxx</em>Timer</strong> routines require a pointer to a system-allocated <strong>EX_TIMER</strong> structure as an input parameter:</p>
<ul>
<li><a href="https://docs.microsoft.com/windows-hardware/drivers/ddi/content/wdm/nf-wdm-exsettimer" data-raw-source="[&lt;strong&gt;ExSetTimer&lt;/strong&gt;](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/wdm/nf-wdm-exsettimer)"><strong>ExSetTimer</strong></a></li>
<li><a href="https://docs.microsoft.com/windows-hardware/drivers/ddi/content/wdm/nf-wdm-excanceltimer" data-raw-source="[&lt;strong&gt;ExCancelTimer&lt;/strong&gt;](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/wdm/nf-wdm-excanceltimer)"><strong>ExCancelTimer</strong></a></li>
<li><a href="https://docs.microsoft.com/windows-hardware/drivers/ddi/content/wdm/nf-wdm-exdeletetimer" data-raw-source="[&lt;strong&gt;ExDeleteTimer&lt;/strong&gt;](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/wdm/nf-wdm-exdeletetimer)"><strong>ExDeleteTimer</strong></a></li>
</ul>
<p><strong>EX_TIMER</strong>-based timer objects are created by the operating system. To get such a timer object, your driver calls the <a href="https://docs.microsoft.com/windows-hardware/drivers/ddi/content/wdm/nf-wdm-exallocatetimer" data-raw-source="[&lt;strong&gt;ExAllocateTimer&lt;/strong&gt;](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/wdm/nf-wdm-exallocatetimer)"><strong>ExAllocateTimer</strong></a> routine. When this object is no longer needed, the driver is responsible for deleting the object by calling <strong>ExDeleteTimer</strong>.</p>
<p>For more information, see <a href="exxxxtimer-routines-and-ex-timer-objects.md" data-raw-source="[Ex&lt;em&gt;Xxx&lt;/em&gt;Timer Routines and EX_TIMER Objects](exxxxtimer-routines-and-ex-timer-objects.md)">Ex<em>Xxx</em>Timer Routines and EX_TIMER Objects</a>.</p>
<p>Header: Wdm.h. Include: Wdm.h, Ntddk.h, Ntifs.h.</p></td>
</tr>
<tr class="odd">
<td><strong>FAST_MUTEX</strong></td>
<td><p>A <strong>FAST_MUTEX</strong> structure is an opaque data structure that represents a fast mutex.</p>
<p>A <strong>FAST_MUTEX</strong> structure is initialized by the <a href="https://docs.microsoft.com/windows-hardware/drivers/ddi/content/wdm/nf-wdm-exinitializefastmutex" data-raw-source="[&lt;strong&gt;ExInitializeFastMutex&lt;/strong&gt;](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/wdm/nf-wdm-exinitializefastmutex)"><strong>ExInitializeFastMutex</strong></a> routine.</p>
<p>For more information about fast mutexes, see <a href="fast-mutexes-and-guarded-mutexes.md" data-raw-source="[Fast Mutexes and Guarded Mutexes](fast-mutexes-and-guarded-mutexes.md)">Fast Mutexes and Guarded Mutexes</a>.</p>
<p>Header: Wdm.h. Include: Wdm.h, Ntddk.h, Ntifs.h.</p></td>
</tr>
<tr class="even">
<td><strong>IO_CSQ</strong></td>
<td><p>The <strong>IO_CSQ</strong> structure is an opaque structure used to specify the driver's cancel-safe IRP queue routines. Do not set the members of this structure directly. Use <a href="https://docs.microsoft.com/windows-hardware/drivers/ddi/content/wdm/nf-wdm-iocsqinitialize" data-raw-source="[&lt;strong&gt;IoCsqInitialize&lt;/strong&gt;](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/wdm/nf-wdm-iocsqinitialize)"><strong>IoCsqInitialize</strong></a> or <a href="https://docs.microsoft.com/windows-hardware/drivers/ddi/content/wdm/nf-wdm-iocsqinitializeex" data-raw-source="[&lt;strong&gt;IoCsqInitializeEx&lt;/strong&gt;](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/wdm/nf-wdm-iocsqinitializeex)"><strong>IoCsqInitializeEx</strong></a> to initialize this structure.</p>
<p>For an overview of how to use cancel-safe IRP queues, see <a href="cancel-safe-irp-queues.md" data-raw-source="[Cancel-Safe IRP Queues](cancel-safe-irp-queues.md)">Cancel-Safe IRP Queues</a>.</p>
<p>Available on Microsoft Windows XP and later versions of the Windows operating system.</p>
<p>Header: Wdm.h. Include: Wdm.h, Ntddk.h, Ntifs.h.</p></td>
</tr>
<tr class="odd">
<td><strong>IO_CSQ_IRP_CONTEXT</strong></td>
<td><p>The <strong>IO_CSQ_IRP_CONTEXT</strong> structure is an opaque data structure used to specify the IRP context for an IRP in the driver's cancel-safe IRP queue. It is used as a key by the <a href="https://docs.microsoft.com/windows-hardware/drivers/ddi/content/wdm/nf-wdm-iocsqinsertirp" data-raw-source="[&lt;strong&gt;IoCsqInsertIrp&lt;/strong&gt;](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/wdm/nf-wdm-iocsqinsertirp)"><strong>IoCsqInsertIrp</strong></a>, <a href="https://docs.microsoft.com/windows-hardware/drivers/ddi/content/wdm/nf-wdm-iocsqinsertirpex" data-raw-source="[&lt;strong&gt;IoCsqInsertIrpEx&lt;/strong&gt;](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/wdm/nf-wdm-iocsqinsertirpex)"><strong>IoCsqInsertIrpEx</strong></a>, and <a href="https://docs.microsoft.com/windows-hardware/drivers/ddi/content/wdm/nf-wdm-iocsqremoveirp" data-raw-source="[&lt;strong&gt;IoCsqRemoveIrp&lt;/strong&gt;](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/wdm/nf-wdm-iocsqremoveirp)"><strong>IoCsqRemoveIrp</strong></a> routines to identify particular IRPs in the queue.</p>
<p>For an overview of how to use cancel-safe IRP queues, see <a href="cancel-safe-irp-queues.md" data-raw-source="[Cancel-Safe IRP Queues](cancel-safe-irp-queues.md)">Cancel-Safe IRP Queues</a>.</p>
<p>Available on Microsoft Windows XP and later versions of the Windows operating system.</p>
<p>Header: Wdm.h. Include: Wdm.h, Ntddk.h, Ntifs.h.</p></td>
</tr>
<tr class="even">
<td><strong>IO_WORKITEM</strong></td>
<td><p>The <strong>IO_WORKITEM</strong> structure is an opaque structure that describes a work item for a system worker thread.</p>
<p>A driver can allocate a work item by calling <a href="https://docs.microsoft.com/windows-hardware/drivers/ddi/content/wdm/nf-wdm-ioallocateworkitem" data-raw-source="[&lt;strong&gt;IoAllocateWorkItem&lt;/strong&gt;](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/wdm/nf-wdm-ioallocateworkitem)"><strong>IoAllocateWorkItem</strong></a>. Alternatively, a driver can allocate its own buffer, and then call <a href="https://docs.microsoft.com/windows-hardware/drivers/ddi/content/wdm/nf-wdm-ioinitializeworkitem" data-raw-source="[&lt;strong&gt;IoInitializeWorkItem&lt;/strong&gt;](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/wdm/nf-wdm-ioinitializeworkitem)"><strong>IoInitializeWorkItem</strong></a> to initialize that buffer as a work item.</p>
<p>Any work item that is allocated by <strong>IoAllocateWorkItem</strong> must be freed by <a href="https://docs.microsoft.com/windows-hardware/drivers/ddi/content/wdm/nf-wdm-iofreeworkitem" data-raw-source="[&lt;strong&gt;IoFreeWorkItem&lt;/strong&gt;](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/wdm/nf-wdm-iofreeworkitem)"><strong>IoFreeWorkItem</strong></a>. Any memory that is initialized by <strong>IoInitializeWorkItem</strong> must be uninitialized by <a href="https://docs.microsoft.com/windows-hardware/drivers/ddi/content/wdm/nf-wdm-iouninitializeworkitem" data-raw-source="[&lt;strong&gt;IoUninitializeWorkItem&lt;/strong&gt;](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/wdm/nf-wdm-iouninitializeworkitem)"><strong>IoUninitializeWorkItem</strong></a> before it can be freed.</p>
<p>For more information about work items, see <a href="system-worker-threads.md" data-raw-source="[System Worker Threads](system-worker-threads.md)">System Worker Threads</a>.</p>
<p>Header: Wdm.h. Include: Wdm.h, Ntddk.h, Ntifs.h.</p></td>
</tr>
<tr class="odd">
<td><strong>KBUGCHECK_CALLBACK_RECORD</strong></td>
<td><p>The <strong>KBUGCHECK_CALLBACK_RECORD</strong> structure is an opaque structure that is used by the <a href="https://docs.microsoft.com/windows-hardware/drivers/ddi/content/wdm/nf-wdm-keregisterbugcheckcallback" data-raw-source="[&lt;strong&gt;KeRegisterBugCheckCallback&lt;/strong&gt;](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/wdm/nf-wdm-keregisterbugcheckcallback)"><strong>KeRegisterBugCheckCallback</strong></a> and <a href="https://docs.microsoft.com/windows-hardware/drivers/ddi/content/wdm/nf-wdm-kederegisterbugcheckcallback" data-raw-source="[&lt;strong&gt;KeDeregisterBugCheckCallback&lt;/strong&gt;](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/wdm/nf-wdm-kederegisterbugcheckcallback)"><strong>KeDeregisterBugCheckCallback</strong></a> routines.</p>
<p>The <strong>KBUGCHECK_CALLBACK_RECORD</strong> structure is used for bookkeeping by the <a href="https://docs.microsoft.com/windows-hardware/drivers/ddi/content/wdm/nf-wdm-keregisterbugcheckreasoncallback" data-raw-source="[&lt;strong&gt;KeRegisterBugCheckReasonCallback&lt;/strong&gt;](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/wdm/nf-wdm-keregisterbugcheckreasoncallback)"><strong>KeRegisterBugCheckReasonCallback</strong></a> and <a href="https://docs.microsoft.com/windows-hardware/drivers/ddi/content/wdm/nf-wdm-kederegisterbugcheckreasoncallback" data-raw-source="[&lt;strong&gt;KeDeregisterBugCheckReasonCallback&lt;/strong&gt;](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/wdm/nf-wdm-kederegisterbugcheckreasoncallback)"><strong>KeDeregisterBugCheckReasonCallback</strong></a> routines.</p>
<p>The structure must be allocated in resident memory, such as nonpaged pool. Use the <a href="https://docs.microsoft.com/windows-hardware/drivers/kernel/mm-bad-pointer" data-raw-source="[&lt;strong&gt;KeInitializeCallbackRecord&lt;/strong&gt;](https://docs.microsoft.com/windows-hardware/drivers/kernel/mm-bad-pointer)"><strong>KeInitializeCallbackRecord</strong></a> routine to initialize the structure before using it.</p>
<p>Header: Ntddk.h. Include: Ntddk.h.</p></td>
</tr>
<tr class="even">
<td><strong>KBUGCHECK_REASON_CALLBACK_RECORD</strong></td>
<td><p>The <strong>KBUGCHECK_REASON_CALLBACK_RECORD</strong> structure is an opaque structure that is used by the <a href="https://docs.microsoft.com/windows-hardware/drivers/ddi/content/wdm/nf-wdm-keregisterbugcheckreasoncallback" data-raw-source="[&lt;strong&gt;KeRegisterBugCheckReasonCallback&lt;/strong&gt;](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/wdm/nf-wdm-keregisterbugcheckreasoncallback)"><strong>KeRegisterBugCheckReasonCallback</strong></a> and <a href="https://docs.microsoft.com/windows-hardware/drivers/ddi/content/wdm/nf-wdm-kederegisterbugcheckreasoncallback" data-raw-source="[&lt;strong&gt;KeDeregisterBugCheckReasonCallback&lt;/strong&gt;](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/wdm/nf-wdm-kederegisterbugcheckreasoncallback)"><strong>KeDeregisterBugCheckReasonCallback</strong></a> routines.</p>
<p>The <strong>KBUGCHECK_REASON_CALLBACK_RECORD</strong> structure is used for bookkeeping by the <a href="https://docs.microsoft.com/windows-hardware/drivers/ddi/content/wdm/nf-wdm-keregisterbugcheckreasoncallback" data-raw-source="[&lt;strong&gt;KeRegisterBugCheckReasonCallback&lt;/strong&gt;](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/wdm/nf-wdm-keregisterbugcheckreasoncallback)"><strong>KeRegisterBugCheckReasonCallback</strong></a> and <a href="https://docs.microsoft.com/windows-hardware/drivers/ddi/content/wdm/nf-wdm-kederegisterbugcheckreasoncallback" data-raw-source="[&lt;strong&gt;KeDeregisterBugCheckReasonCallback&lt;/strong&gt;](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/wdm/nf-wdm-kederegisterbugcheckreasoncallback)"><strong>KeDeregisterBugCheckReasonCallback</strong></a> routines.</p>
<p>The structure must be allocated in resident memory, such as nonpaged pool. Use the <a href="https://docs.microsoft.com/windows-hardware/drivers/kernel/mm-bad-pointer" data-raw-source="[&lt;strong&gt;KeInitializeCallbackRecord&lt;/strong&gt;](https://docs.microsoft.com/windows-hardware/drivers/kernel/mm-bad-pointer)"><strong>KeInitializeCallbackRecord</strong></a> routine to initialize the structure before using it.</p>
<p>Available on Microsoft Windows XP with Service Pack 1 (SP1), Windows Server 2003, and later versions of the Windows operating system.</p>
<p>Header: Ntddk.h. Include: Ntddk.h.</p></td>
</tr>
<tr class="odd">
<td><strong>KDPC</strong></td>
<td><p>The <strong>KDPC</strong> structure is an opaque structure that represents a DPC object. Do not set the members of this structure directly. See <a href="dpc-objects-and-dpcs.md" data-raw-source="[DPC Objects and DPCs](dpc-objects-and-dpcs.md)">DPC Objects and DPCs</a>.</p>
<p>Header: Wdm.h. Include: Wdm.h, Ntddk.h, Ntifs.h.</p></td>
</tr>
<tr class="even">
<td><strong>KFLOATING_SAVE</strong></td>
<td><p>The <strong>KFLOATING_SAVE</strong> structure is an opaque structure that describes the floating-point state that the <a href="https://docs.microsoft.com/windows-hardware/drivers/ddi/content/wdm/nf-wdm-kesavefloatingpointstate" data-raw-source="[&lt;strong&gt;KeSaveFloatingPointState&lt;/strong&gt;](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/wdm/nf-wdm-kesavefloatingpointstate)"><strong>KeSaveFloatingPointState</strong></a> routine saved.</p>
<p>Use <a href="https://docs.microsoft.com/windows-hardware/drivers/ddi/content/wdm/nf-wdm-kerestorefloatingpointstate" data-raw-source="[&lt;strong&gt;KeRestoreFloatingPointState&lt;/strong&gt;](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/wdm/nf-wdm-kerestorefloatingpointstate)"><strong>KeRestoreFloatingPointState</strong></a> to restore the floating-point state.</p>
<p>Header: Wdm.h. Include: Wdm.h, Ntddk.h, Ntifs.h.</p></td>
</tr>
<tr class="odd">
<td><strong>KGUARDED_MUTEX</strong></td>
<td><p>The <strong>KGUARDED_MUTEX</strong> structure is an opaque structure that represents a guarded mutex.</p>
<p>Use <strong>KeInitializeGuardedMutex</strong> to initialize a <strong>KGUARDED_MUTEX</strong> structure as a guarded mutex.</p>
<p>Guarded mutexes must be allocated from non-paged pool.</p>
<p>For more information about guarded mutexes, see <a href="fast-mutexes-and-guarded-mutexes.md" data-raw-source="[Fast Mutexes and Guarded Mutexes](fast-mutexes-and-guarded-mutexes.md)">Fast Mutexes and Guarded Mutexes</a>.</p>
<p>Header: Wdm.h. Include: Wdm.h, Ntddk.h, Ntifs.h.</p></td>
</tr>
<tr class="even">
<td><strong>KINTERRUPT</strong></td>
<td><p>A <strong>KINTERRUPT</strong> structure is an opaque structure that represents an interrupt to the system.</p>
<p><a href="https://docs.microsoft.com/windows-hardware/drivers/ddi/content/wdm/nf-wdm-ioconnectinterruptex" data-raw-source="[&lt;strong&gt;IoConnectInterruptEx&lt;/strong&gt;](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/wdm/nf-wdm-ioconnectinterruptex)"><strong>IoConnectInterruptEx</strong></a> provides a pointer to the <strong>KINTERRUPT</strong> structure for the interrupt when the driver registers an <a href="https://docs.microsoft.com/windows-hardware/drivers/ddi/content/wdm/nc-wdm-kservice_routine" data-raw-source="[&lt;em&gt;InterruptService&lt;/em&gt;](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/wdm/nc-wdm-kservice_routine)"><em>InterruptService</em></a> or <a href="https://docs.microsoft.com/windows-hardware/drivers/ddi/content/wdm/nc-wdm-kmessage_service_routine" data-raw-source="[&lt;em&gt;InterruptMessageService&lt;/em&gt;](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/wdm/nc-wdm-kmessage_service_routine)"><em>InterruptMessageService</em></a> routine. The driver uses this pointer when acquiring or releasing the interrupt spin lock for the interrupt. The driver also uses this pointer when unregistering an <em>InterruptService</em> routine.</p>
<p>Header: Wdm.h. Include: Wdm.h, Ntddk.h, Ntifs.h.</p></td>
</tr>
<tr class="odd">
<td><strong>KLOCK_QUEUE_HANDLE</strong></td>
<td><p>The <strong>KLOCK_QUEUE_HANDLE</strong> structure is an opaque structure that describes a queued spin lock. The driver allocates the <strong>KLOCK_QUEUE_HANDLE</strong> structure, and passes it to <a href="https://docs.microsoft.com/previous-versions/windows/hardware/drivers/ff551899(v=vs.85)" data-raw-source="[&lt;strong&gt;KeAcquireInStackQueuedSpinLock&lt;/strong&gt;](https://docs.microsoft.com/previous-versions/windows/hardware/drivers/ff551899(v=vs.85))"><strong>KeAcquireInStackQueuedSpinLock</strong></a> and <a href="https://docs.microsoft.com/previous-versions/windows/hardware/drivers/ff551908(v=vs.85)" data-raw-source="[&lt;strong&gt;KeAcquireInStackQueuedSpinLockAtDpcLevel&lt;/strong&gt;](https://docs.microsoft.com/previous-versions/windows/hardware/drivers/ff551908(v=vs.85))"><strong>KeAcquireInStackQueuedSpinLockAtDpcLevel</strong></a> to acquire the queued spin lock. Those routines initialize the structure to represent the queued spin lock. The driver passes the structure to <a href="https://docs.microsoft.com/windows-hardware/drivers/ddi/content/wdm/nf-wdm-kereleaseinstackqueuedspinlock" data-raw-source="[&lt;strong&gt;KeReleaseInStackQueuedSpinLock&lt;/strong&gt;](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/wdm/nf-wdm-kereleaseinstackqueuedspinlock)"><strong>KeReleaseInStackQueuedSpinLock</strong></a> and <a href="https://docs.microsoft.com/windows-hardware/drivers/ddi/content/wdm/nf-wdm-kereleaseinstackqueuedspinlockfromdpclevel" data-raw-source="[&lt;strong&gt;KeReleaseInStackQueuedSpinLockFromDpcLevel&lt;/strong&gt;](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/wdm/nf-wdm-kereleaseinstackqueuedspinlockfromdpclevel)"><strong>KeReleaseInStackQueuedSpinLockFromDpcLevel</strong></a> when releasing the spin lock.</p>
<p>For more information, see <a href="queued-spin-locks.md" data-raw-source="[Queued Spin Locks](queued-spin-locks.md)">Queued Spin Locks</a>.</p>
<p>Header: Wdm.h. Include: Wdm.h, Ntddk.h, Ntifs.h.</p></td>
</tr>
<tr class="even">
<td><strong>KTIMER</strong></td>
<td><p>The <strong>KTIMER</strong> structure is an opaque structure that represents a timer object. Do not set the members of this structure directly. For more information, see <a href="timer-objects-and-dpcs.md" data-raw-source="[Timer Objects and DPCs](timer-objects-and-dpcs.md)">Timer Objects and DPCs</a>.</p>
<p>Header: Wdm.h. Include: Wdm.h, Ntddk.h, Ntifs.h.</p></td>
</tr>
<tr class="odd">
<td><strong>LOOKASIDE_LIST_EX</strong></td>
<td><p>The <strong>LOOKASIDE_LIST_EX</strong> structure describes a lookaside list.</p>
<pre class="syntax"><code>typedef struct _LOOKASIDE_LIST_EX {
  ...  // opaque
} LOOKASIDE_LIST_EX, *PLOOKASIDE_LIST_EX;</code></pre>
<p>A lookaside list is a pool of fixed-size buffers that the driver can manage locally to reduce the number of calls to system allocation routines and, thereby, to improve performance. The buffers are of uniform size and are stored as entries in the lookaside list.</p>
<p>Drivers should treat the <strong>LOOKASIDE_LIST_EX</strong> structure as opaque. Drivers that access structure members or that have dependencies on the locations of these members might not remain portable and interoperable with other drivers.</p>
<p>The following See Also section contains a list of the routines that use this structure.</p>
<p>For more information about lookaside lists, see <a href="using-lookaside-lists.md" data-raw-source="[Using Lookaside Lists](using-lookaside-lists.md)">Using Lookaside Lists</a>.</p>
<p>On 64-bit platforms, this structure must be 16-byte aligned.</p>
<p>Supported starting with Windows Vista.</p>
<p>Header: Wdm.h. Include: Wdm.h, Ntddk.h, Ntifs.h.</p></td>
</tr>
<tr class="even">
<td><strong>NPAGED_LOOKASIDE_LIST</strong></td>
<td><p>The <strong>NPAGED_LOOKASIDE_LIST</strong> structure is an opaque structure that describes a lookaside list of fixed-size buffers allocated from nonpaged pool. The system creates new entries and destroys unused entries on the list as necessary. For fixed-size buffers, using a lookaside list is quicker than allocating memory directly.</p>
<p>Use <a href="https://docs.microsoft.com/windows-hardware/drivers/ddi/content/wdm/nf-wdm-exinitializenpagedlookasidelist" data-raw-source="[&lt;strong&gt;ExInitializeNPagedLookasideList&lt;/strong&gt;](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/wdm/nf-wdm-exinitializenpagedlookasidelist)"><strong>ExInitializeNPagedLookasideList</strong></a> to initialize the lookaside list. Use <a href="https://docs.microsoft.com/windows-hardware/drivers/ddi/content/wdm/nf-wdm-exallocatefromnpagedlookasidelist" data-raw-source="[&lt;strong&gt;ExAllocateFromNPagedLookasideList&lt;/strong&gt;](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/wdm/nf-wdm-exallocatefromnpagedlookasidelist)"><strong>ExAllocateFromNPagedLookasideList</strong></a> to allocate a buffer from the list, and <a href="https://docs.microsoft.com/windows-hardware/drivers/ddi/content/wdm/nf-wdm-exfreetonpagedlookasidelist" data-raw-source="[&lt;strong&gt;ExFreeToNPagedLookasideList&lt;/strong&gt;](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/wdm/nf-wdm-exfreetonpagedlookasidelist)"><strong>ExFreeToNPagedLookasideList</strong></a> to return a buffer to the list.</p>
<p>Drivers must always explicitly free any lookaside lists they create before unloading. It is a serious programming error to do otherwise. Use <a href="https://docs.microsoft.com/windows-hardware/drivers/ddi/content/wdm/nf-wdm-exdeletenpagedlookasidelist" data-raw-source="[&lt;strong&gt;ExDeleteNPagedLookasideList&lt;/strong&gt;](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/wdm/nf-wdm-exdeletenpagedlookasidelist)"><strong>ExDeleteNPagedLookasideList</strong></a> to free the list.</p>
<p>Drivers can also use lookaside lists for paged pool. Starting with Windows 2000, a <strong>PAGED_LOOKASIDE_LIST</strong> structure describes a lookaside list that contains paged buffers. Starting with Windows Vista, a <strong>LOOKASIDE_LIST_EX</strong> structure can describe a lookaside list that contains either paged or nonpaged buffers. For more information, see <a href="using-lookaside-lists.md" data-raw-source="[Using Lookaside Lists](using-lookaside-lists.md)">Using Lookaside Lists</a>.</p>
<p>On 64-bit platforms, this structure must be 16-byte aligned.</p>
<p>Supported starting with Windows 2000.</p>
<p>Header: Wdm.h. Include: Wdm.h, Ntddk.h, Ntifs.h.</p></td>
</tr>
<tr class="odd">
<td><strong>OBJECT_TYPE</strong></td>
<td><p><strong>OBJECT_TYPE</strong> is an opaque structure that specifies the object type of a handle. For more information, see <a href="https://docs.microsoft.com/windows-hardware/drivers/ddi/content/wdm/nf-wdm-obreferenceobjectbyhandle" data-raw-source="[&lt;strong&gt;ObReferenceObjectByHandle&lt;/strong&gt;](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/wdm/nf-wdm-obreferenceobjectbyhandle)"><strong>ObReferenceObjectByHandle</strong></a>.</p>
<p>Header: Wdm.h. Include: Wdm.h, Ntddk.h, Ntifs.h.</p></td>
</tr>
<tr class="even">
<td><strong>PAGED_LOOKASIDE_LIST</strong></td>
<td><p>The <strong>PAGED_LOOKASIDE_LIST</strong> structure is an opaque structure that describes a lookaside list of fixed-size buffers allocated from paged pool. The system creates new entries and destroys unused entries on the list as necessary. For fixed-size buffers, using a lookaside list is quicker than allocating memory directly.</p>
<p>Use <a href="https://docs.microsoft.com/windows-hardware/drivers/ddi/content/wdm/nf-wdm-exinitializepagedlookasidelist" data-raw-source="[&lt;strong&gt;ExInitializePagedLookasideList&lt;/strong&gt;](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/wdm/nf-wdm-exinitializepagedlookasidelist)"><strong>ExInitializePagedLookasideList</strong></a> to initialize the lookaside list. Use <a href="https://docs.microsoft.com/windows-hardware/drivers/ddi/content/wdm/nf-wdm-exallocatefrompagedlookasidelist" data-raw-source="[&lt;strong&gt;ExAllocateFromPagedLookasideList&lt;/strong&gt;](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/wdm/nf-wdm-exallocatefrompagedlookasidelist)"><strong>ExAllocateFromPagedLookasideList</strong></a> to allocate a buffer from the list, and <a href="https://docs.microsoft.com/windows-hardware/drivers/ddi/content/wdm/nf-wdm-exfreetopagedlookasidelist" data-raw-source="[&lt;strong&gt;ExFreeToPagedLookasideList&lt;/strong&gt;](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/wdm/nf-wdm-exfreetopagedlookasidelist)"><strong>ExFreeToPagedLookasideList</strong></a> to return a buffer to the list.</p>
<p>Drivers must always explicitly free any lookaside lists they create before unloading. It is a serious programming error to do otherwise. Use <a href="https://docs.microsoft.com/windows-hardware/drivers/ddi/content/wdm/nf-wdm-exdeletepagedlookasidelist" data-raw-source="[&lt;strong&gt;ExDeletePagedLookasideList&lt;/strong&gt;](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/wdm/nf-wdm-exdeletepagedlookasidelist)"><strong>ExDeletePagedLookasideList</strong></a> to free the list.</p>
<p>Drivers can also use lookaside lists for nonpaged pool. Starting with Windows 2000, an <strong>NPAGED_LOOKASIDE_LIST</strong> structure describes a lookaside list that contains nonpaged buffers. Starting with Windows Vista, a <strong>LOOKASIDE_LIST_EX</strong> structure can describe a lookaside list that contains either paged or nonpaged buffers. For more information, see <a href="using-lookaside-lists.md" data-raw-source="[Using Lookaside Lists](using-lookaside-lists.md)">Using Lookaside Lists</a>.</p>
<p>On 64-bit platforms, this structure must be 16-byte aligned.</p>
<p>Supported starting with Windows 2000.</p>
<p>Header: Wdm.h. Include: Wdm.h, Ntddk.h, Ntifs.h.</p></td>
</tr>
<tr class="odd">
<td><strong>RTL_BITMAP</strong></td>
<td><p>The <strong>RTL_BITMAP</strong> structure is an opaque structure that describes a bitmap.</p>
<pre class="syntax"><code>typedef struct _RTL_BITMAP {
  // opaque
} RTL_BITMAP, *PRTL_BITMAP;</code></pre>
<p>Do not directly access the members of this structure. Drivers that have dependencies on member locations or that access member values directly might not remain compatible with future versions of the Windows operating system.</p>
<p>The <strong>RTL_BITMAP</strong> structure serves as a header for a general-purpose, one-dimensional bitmap of arbitrary length. A driver can use such a bitmap as an economical way to keep track of a set of reusable items. For example, a file system can use bitmaps to track which clusters and sectors on a hard disk have already been allocated to hold file data.</p>
<p>For a list of the <strong>Rtl<em>Xxx</em></strong> routines that use <strong>RTL_BITMAP</strong> structures, see the following See Also section. The caller of these <strong>Rtl<em>Xxx</em></strong> routines is responsible for allocating the storage for the <strong>RTL_BITMAP</strong> structure and for the buffer that contains the bitmap. This buffer must begin on a four-byte boundary in memory and must be a multiple of four bytes in length. The bitmap begins at the start of the buffer but can contain any number of bits that will fit in the allocated buffer.</p>
<p>Before supplying an <strong>RTL_BITMAP</strong> structure as a parameter to an <strong>Rtl<em>Xxx</em></strong> routine, call the <a href="https://docs.microsoft.com/windows-hardware/drivers/ddi/content/wdm/nf-wdm-rtlinitializebitmap" data-raw-source="[&lt;strong&gt;RtlInitializeBitMap&lt;/strong&gt;](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/wdm/nf-wdm-rtlinitializebitmap)"><strong>RtlInitializeBitMap</strong></a> routine to initialize the structure. The input parameters to this routine are a pointer to a buffer that contains the bitmap, and the size, in bits, of the bitmap. <strong>RtlInitializeBitMap</strong> does not change the contents of this buffer.</p>
<p>If the caller allocates the storage for the <strong>RTL_BITMAP</strong> structure and bitmap in paged memory, the caller must be running at IRQL &lt;= APC_LEVEL when it passes a pointer to this structure as a parameter to any of the <strong>Rtl<em>Xxx</em></strong> routines that are listed in the See Also section. If the caller allocates the storage from nonpaged memory (or, equivalently, from paged memory that is locked), the caller can be running at any IRQL when it calls the <strong>Rtl<em>Xxx</em></strong> routine.</p>
<p>Supported in Windows 2000 and later versions of Windows.</p>
<p>Header: Wdm.h. Include: Wdm.h, Ntddk.h, Ntifs.h.</p></td>
</tr>
<tr class="even">
<td><strong>RTL_RUN_ONCE</strong></td>
<td><p>The <strong>RTL_RUN_ONCE</strong> structure is an opaque structure that stores the information for a one-time initialization.</p>
<p>Drivers must initialize this structure by calling the <a href="https://docs.microsoft.com/windows-hardware/drivers/ddi/content/ntddk/nf-ntddk-rtlrunonceinitialize" data-raw-source="[&lt;strong&gt;RtlRunOnceInitialize&lt;/strong&gt;](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/ntddk/nf-ntddk-rtlrunonceinitialize)"><strong>RtlRunOnceInitialize</strong></a> routine before passing it to any other <strong>RtlRunOnce<em>Xxx</em></strong> routines.</p>
<p>Available only on Windows Vista and later versions of the Windows operating system.</p>
<p>Header: Ntddk.h. Include: Ntddk.h.</p></td>
</tr>
<tr class="odd">
<td><strong>SECURITY_SUBJECT_CONTEXT</strong></td>
<td><p>The <strong>SECURITY_SUBJECT_CONTEXT</strong> structure is an opaque structure that represents the security context within which a particular operation is taking place.</p>
<p>Header: Wdm.h. Include: Wdm.h, Ntddk.h, Ntifs.h.</p></td>
</tr>
<tr class="even">
<td><strong>SLIST_HEADER</strong></td>
<td><p>An <strong>SLIST_HEADER</strong> structure is an opaque structure that serves as the header for a sequenced singly linked list. For more information, see <a href="singly-and-doubly-linked-lists.md" data-raw-source="[Singly and Doubly Linked Lists](singly-and-doubly-linked-lists.md)">Singly and Doubly Linked Lists</a>.</p>
<p>On 64-bit platforms, <strong>SLIST_HEADER</strong> structures must be 16-byte aligned.</p>
<p>Header: Wdm.h. Include: Wdm.h, Ntddk.h, Ntifs.h.</p></td>
</tr>
<tr class="odd">
<td><strong>XSTATE_SAVE</strong></td>
<td><p>The <strong>XSTATE_SAVE</strong> structure is an opaque structure that describes the extended processor state information that a kernel-mode driver saves and restores.</p>
<pre class="syntax"><code>typedef struct _XSTATE_SAVE {
  ...  // opaque
} XSTATE_SAVE, *PXSTATE_SAVE;</code></pre>
<p>All members are opaque.</p>
<p>This structure is used by the <a href="https://docs.microsoft.com/windows-hardware/drivers/ddi/content/wdm/nf-wdm-kesaveextendedprocessorstate" data-raw-source="[&lt;strong&gt;KeSaveExtendedProcessorState&lt;/strong&gt;](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/wdm/nf-wdm-kesaveextendedprocessorstate)"><strong>KeSaveExtendedProcessorState</strong></a> and <a href="https://docs.microsoft.com/windows-hardware/drivers/ddi/content/wdm/nf-wdm-kerestoreextendedprocessorstate" data-raw-source="[&lt;strong&gt;KeRestoreExtendedProcessorState&lt;/strong&gt;](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/wdm/nf-wdm-kerestoreextendedprocessorstate)"><strong>KeRestoreExtendedProcessorState</strong></a> routines.</p>
<p>Supported in Windows 7 and later versions of the Windows operating system.</p>
<p>Header: Wdm.h. Include: Wdm.h, Ntddk.h, Ntifs.h.</p></td>
</tr>
</tbody>
</table>

 

## Related topics
[**BugCheckDumpIoCallback**](https://msdn.microsoft.com/library/windows/hardware/ff540677)  
[**BugCheckSecondaryDumpDataCallback**](https://msdn.microsoft.com/library/windows/hardware/ff540679)  
[**ExAcquireFastMutex**](https://docs.microsoft.com/previous-versions/windows/hardware/drivers/ff544337(v=vs.85))  
[**ExAcquireFastMutexUnsafe**](https://docs.microsoft.com/previous-versions/windows/hardware/drivers/ff544340(v=vs.85))  
[**ExAllocateFromLookasideListEx**](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/wdm/nf-wdm-exallocatefromlookasidelistex)  
[**ExAllocateFromNPagedLookasideList**](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/wdm/nf-wdm-exallocatefromnpagedlookasidelist)  
[**ExAllocateFromPagedLookasideList**](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/wdm/nf-wdm-exallocatefrompagedlookasidelist)  
[**ExAllocateTimer**](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/wdm/nf-wdm-exallocatetimer)  
[**ExDeletePagedLookasideList**](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/wdm/nf-wdm-exdeletepagedlookasidelist)  
[**ExFreeToPagedLookasideList**](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/wdm/nf-wdm-exfreetopagedlookasidelist)  
[**ExInitializePagedLookasideList**](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/wdm/nf-wdm-exinitializepagedlookasidelist)  
[**ExCancelTimer**](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/wdm/nf-wdm-excanceltimer)  
[**ExDeleteLookasideListEx**](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/wdm/nf-wdm-exdeletelookasidelistex)  
[**ExDeleteNPagedLookasideList**](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/wdm/nf-wdm-exdeletenpagedlookasidelist)  
[**ExDeleteTimer**](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/wdm/nf-wdm-exdeletetimer)  
[**ExFlushLookasideListEx**](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/wdm/nf-wdm-exflushlookasidelistex)  
[**ExFreeToLookasideListEx**](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/wdm/nf-wdm-exfreetolookasidelistex)  
[**ExFreeToNPagedLookasideList**](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/wdm/nf-wdm-exfreetonpagedlookasidelist)  
[**ExInitializeLookasideListEx**](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/wdm/nf-wdm-exinitializelookasidelistex)  
[**ExInitializeNPagedLookasideList**](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/wdm/nf-wdm-exinitializenpagedlookasidelist)  
[**ExInitializeSListHead**](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/wdm/nf-wdm-initializeslisthead)  
[**ExInterlockedFlushSList**](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/wdm/nf-wdm-exinterlockedflushslist)  
[**ExInterlockedPopEntrySList**](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/wdm/nf-wdm-exinterlockedpopentryslist)  
[**ExInterlockedPushEntrySList**](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/wdm/nf-wdm-exinterlockedpushentryslist)  
[**ExQueryDepthSList**](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/wdm/nf-wdm-exquerydepthslist)  
[**ExReleaseFastMutex**](https://docs.microsoft.com/previous-versions/windows/hardware/drivers/ff545549(v=vs.85))  
[**ExReleaseFastMutexUnsafe**](https://docs.microsoft.com/previous-versions/windows/hardware/drivers/ff545567(v=vs.85))  
[**ExSetTimer**](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/wdm/nf-wdm-exsettimer)  
[**ExTryToAcquireFastMutex**](https://docs.microsoft.com/previous-versions/windows/hardware/drivers/ff545647(v=vs.85))  
[*ExTimerCallback*](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/wdm/nc-wdm-ext_callback)  
[**IoAllocateWorkItem**](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/wdm/nf-wdm-ioallocateworkitem)  
[**IoConnectInterruptEx**](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/wdm/nf-wdm-ioconnectinterruptex)  
[**IoCsqInitialize**](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/wdm/nf-wdm-iocsqinitialize)  
[**IoCsqInitializeEx**](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/wdm/nf-wdm-iocsqinitializeex)  
[**IoCsqInsertIrp**](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/wdm/nf-wdm-iocsqinsertirp)  
[**IoCsqInsertIrpEx**](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/wdm/nf-wdm-iocsqinsertirpex)  
[**IoCsqRemoveIrp**](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/wdm/nf-wdm-iocsqremoveirp)  
[**IoDisconnectInterruptEx**](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/wdm/nf-wdm-iodisconnectinterruptex)  
[**IoFreeWorkItem**](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/wdm/nf-wdm-iofreeworkitem)  
[**IoInitializeWorkItem**](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/wdm/nf-wdm-ioinitializeworkitem)  
[**IoRequestDpc**](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/wdm/nf-wdm-iorequestdpc)  
[**IoUninitializeWorkItem**](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/wdm/nf-wdm-iouninitializeworkitem)  
[**KeAcquireGuardedMutex**](https://docs.microsoft.com/previous-versions/windows/hardware/drivers/ff551892(v=vs.85))  
[**KeAcquireGuardedMutexUnsafe**](https://docs.microsoft.com/previous-versions/windows/hardware/drivers/ff551894(v=vs.85))  
[**KeAcquireInStackQueuedSpinLock**](https://docs.microsoft.com/previous-versions/windows/hardware/drivers/ff551899(v=vs.85))  
[**KeAcquireInStackQueuedSpinLockAtDpcLevel**](https://docs.microsoft.com/previous-versions/windows/hardware/drivers/ff551908(v=vs.85))  
[**KeAcquireInterruptSpinLock**](https://docs.microsoft.com/previous-versions/windows/hardware/drivers/ff551914(v=vs.85))  
[**KeCancelTimer**](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/wdm/nf-wdm-kecanceltimer)  
[**KeInitializeCallbackRecord**](https://docs.microsoft.com/windows-hardware/drivers/kernel/mm-bad-pointer)  
[**KeInitializeGuardedMutex**](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/wdm/nf-wdm-keinitializeguardedmutex)  
[**KeInitializeTimer**](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/wdm/nf-wdm-keinitializetimer)  
[**KeInitializeTimerEx**](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/wdm/nf-wdm-keinitializetimerex)  
[**KeReadStateTimer**](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/wdm/nf-wdm-kereadstatetimer)  
[**KeRestoreExtendedProcessorState**](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/wdm/nf-wdm-kerestoreextendedprocessorstate)  
[**KeSaveExtendedProcessorState**](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/wdm/nf-wdm-kesaveextendedprocessorstate)  
[**KeSetTimer**](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/wdm/nf-wdm-kesettimer)  
[**KeSetTimerEx**](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/wdm/nf-wdm-kesettimerex)  
[**KeDeregisterBugCheckCallback**](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/wdm/nf-wdm-kederegisterbugcheckcallback)  
[**KeDeregisterBugCheckReasonCallback**](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/wdm/nf-wdm-kederegisterbugcheckreasoncallback)  
[**KeInsertQueueDpc**](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/wdm/nf-wdm-keinsertqueuedpc)  
[**KeRegisterBugCheckCallback**](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/wdm/nf-wdm-keregisterbugcheckcallback)  
[**KeRegisterBugCheckReasonCallback**](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/wdm/nf-wdm-keregisterbugcheckreasoncallback)  
[**KeReleaseGuardedMutexUnsafe**](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/wdm/nf-wdm-kereleaseguardedmutexunsafe)  
[**KeReleaseInStackQueuedSpinLock**](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/wdm/nf-wdm-kereleaseinstackqueuedspinlock)  
[**KeReleaseInStackQueuedSpinLockFromDpcLevel**](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/wdm/nf-wdm-kereleaseinstackqueuedspinlockfromdpclevel)  
[**KeReleaseInterruptSpinLock**](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/wdm/nf-wdm-kereleaseinterruptspinlock)  
[**KeRestoreFloatingPointState**](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/wdm/nf-wdm-kerestorefloatingpointstate)  
[**KeSaveFloatingPointState**](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/wdm/nf-wdm-kesavefloatingpointstate)  
[**KeSynchronizeExecution**](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/wdm/nf-wdm-kesynchronizeexecution)  
[*LookasideListAllocateEx*](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/wdm/nc-wdm-allocate_function_ex)  
[*LookasideListFreeEx*](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/wdm/nc-wdm-free_function_ex)  
[**ObReferenceObjectByHandle**](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/wdm/nf-wdm-obreferenceobjectbyhandle)  
[**PsGetCurrentProcess**](https://docs.microsoft.com/windows-hardware/drivers/kernel/mm-bad-pointer#psgetcurrentprocess)  
[**PsGetProcessCreateTimeQuadPart**](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/ntddk/nf-ntddk-psgetprocesscreatetimequadpart)  
[**PsInitialSystemProcess**](https://docs.microsoft.com/windows-hardware/drivers/kernel/mm64bitphysicaladdress)  
[**PsIsSystemThread**](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/ntifs/nf-ntifs-psissystemthread)  
[**RtlRunOnceBeginInitialize**](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/ntddk/nf-ntddk-rtlrunoncebegininitialize)  
[**RtlRunOnceComplete**](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/ntddk/nf-ntddk-rtlrunoncecomplete)  
[**RtlRunOnceExecuteOnce**](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/ntddk/nf-ntddk-rtlrunonceexecuteonce)  
[**RtlRunOnceInitialize**](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/ntddk/nf-ntddk-rtlrunonceinitialize)  
[*RunOnceInitialization*](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/ntddk/nc-ntddk-rtl_run_once_init_fn)  
[Run-Down Protection](run-down-protection.md)  
[**SeAccessCheck**](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/wdm/nf-wdm-seaccesscheck)  
[**SeAssignSecurity**](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/wdm/nf-wdm-seassignsecurity)  
[**SeAssignSecurityEx**](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/wdm/nf-wdm-seassignsecurityex)  



