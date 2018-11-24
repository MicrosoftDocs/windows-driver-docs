---
title: Interrupt Sync Objects
description: Interrupt Sync Objects
ms.assetid: c9e228e0-6178-442d-a82a-6b14ed67c9d2
keywords:
- helper objects WDK audio , interrupt sync objects
- interrupt sync objects WDK audio
- IInterruptSync interface
- synchronization WDK audio
- interrupt service routines WDK audio
- ISRs WDK audio
- non-interrupt routines WDK audio
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Interrupt Sync Objects


## <span id="interrupt_sync_objects"></span><span id="INTERRUPT_SYNC_OBJECTS"></span>


The PortCls system driver implements the [IInterruptSync](https://msdn.microsoft.com/library/windows/hardware/ff536590) interface for the benefit of miniport drivers. **IInterruptSync** represents an interrupt sync object that synchronizes the execution of a list of interrupt service routines (ISRs) with non-interrupt routines.

Interrupt sync objects provide two key capabilities:

-   Execution of a list of ISRs in response to an interrupt. The sync object is connected to an interrupt source. Each time the interrupt occurs, the sync object executes the ISRs in a specified order according to the selected mode. (See the following description of the three modes.)

-   Execution of routines that are not ISRs. These non-interrupt routines are not connected to the sync object's interrupt. Instead, a non-interrupt routine runs at a time of the caller's choosing. However, the sync object executes the non-interrupt routine synchronously with the object's list of ISRs. In other words, the non-interrupt routine runs to completion before any of the ISRs in the sync object's list begin executing, and vice versa.

An interrupt sync object is flexible in dealing with multiple ISRs. The ISRs reside in a linked list that the sync object traverses at interrupt time. When a miniport driver registers an ISR with a sync object, it specifies whether the ISR should be added to the beginning or end of this list.

A miniport driver calls the [**PcNewInterruptSync**](https://msdn.microsoft.com/library/windows/hardware/ff537713) function to create an interrupt sync object. During this call, the driver specifies the manner in which the object is to traverse its list of ISRs at interrupt time. The call supports the three options that are specified by the INTERRUPTSYNCMODE enumeration constants in the following table.

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<thead>
<tr class="header">
<th align="left">Constant</th>
<th align="left">Meaning</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td align="left"><p><strong>InterruptSyncModeNormal</strong></p></td>
<td align="left"><p>Call each ISR in the list until one of them returns STATUS_SUCCESS.</p></td>
</tr>
<tr class="even">
<td align="left"><p><strong>InterruptSyncModeAll</strong></p></td>
<td align="left"><p>Call each ISR in the list exactly once, regardless of the return codes of the preceding ISRs.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><strong>InterruptSyncModeRepeat</strong></p></td>
<td align="left"><p>Traverse the entire list of ISRs until a trip through the list occurs in which no ISR in the list returns STATUS_SUCCESS.</p></td>
</tr>
</tbody>
</table>

 

In the **InterruptSyncModeNormal** mode, the sync object calls each ISR in the list until one of them returns STATUS\_SUCCESS. Any ISRs in the list that follow this ISR are not called. This mode emulates the way that the operating system normally handles ISRs. If none of the ISRs return STATUS\_SUCCESS, the behavior is the same as **InterruptSyncModeAll**.

In the **InterruptSyncModeAll** mode, each ISR in the list is called exactly once, regardless of the return codes of the preceding ISRs. This is intended for more primitive hardware where the source of the interrupt is not deterministic, although it might be useful in other situations as well. For example, two interrupt sources might be tightly synchronized on every interrupt, regardless of which of the two sources a particular interrupt comes from.

In the **InterruptSyncModeRepeat** mode, the sync object repeatedly traverses the entire list of ISRs until a trip through the list occurs in which no routine in the list returns STATUS\_SUCCESS. This mode is appropriate for situations in which interrupts from multiple sources might fire on the same interrupt line at the same time, or a second interrupt might fire during ISR processing. Every interrupt source must be able to determine whether it requires processing. The system will stop responding if an ISR that always returns STATUS\_SUCCESS is registered with a sync object in this mode.

In any of these modes, the sync object will acknowledge the interrupt to the operating system if any of the registered ISRs return STATUS\_SUCCESS. In all three modes, if all interrupt sources indicate that they did not successfully handle the interrupt, the sync object will return an unsuccessful result code to the operating system.

The **IInterruptSync** interface supports the following methods:

[**IInterruptSync::CallSynchronizedRoutine**](https://msdn.microsoft.com/library/windows/hardware/ff536592)

[**IInterruptSync::Connect**](https://msdn.microsoft.com/library/windows/hardware/ff536594)

[**IInterruptSync::Disconnect**](https://msdn.microsoft.com/library/windows/hardware/ff536597)

[**IInterruptSync::GetKInterrupt**](https://msdn.microsoft.com/library/windows/hardware/ff536599)

[**IInterruptSync::RegisterServiceRoutine**](https://msdn.microsoft.com/library/windows/hardware/ff536600)

 

 




