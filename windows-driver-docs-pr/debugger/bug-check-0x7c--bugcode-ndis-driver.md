---
title: Bug Check 0x7C BUGCODE_NDIS_DRIVER
description: The BUGCODE_NDIS_DRIVER bug check has a value of 0x0000007C. This bug check indicates that the operating system detected an error in a networking driver.
ms.assetid: 0f2c2e9c-2889-4d99-b653-0ee1d4c2be0e
keywords: ["Bug Check 0x7C BUGCODE_NDIS_DRIVER", "BUGCODE_NDIS_DRIVER"]
ms.author: domars
ms.date: 05/23/2017
topic_type:
- apiref
api_name:
- BUGCODE_NDIS_DRIVER
api_type:
- NA
ms.localizationpriority: medium
---

# Bug Check 0x7C: BUGCODE\_NDIS\_DRIVER


The BUGCODE\_NDIS\_DRIVER bug check has a value of 0x0000007C. This bug check indicates that the operating system detected an error in a networking driver.

**Important** This topic is for programmers. If you are a customer who has received a blue screen error code while using your computer, see [Troubleshoot blue screen errors](https://windows.microsoft.com/windows-10/troubleshoot-blue-screen-errors).

## BUGCODE\_NDIS\_DRIVER Parameters


Parameter 1 indicates the type of violation. The meaning of the other parameters depends on the value of Parameter 1. If a Parameter's value is "0," that means it is not used.

<table>
<colgroup>
<col width="20%" />
<col width="20%" />
<col width="20%" />
<col width="20%" />
<col width="20%" />

</colgroup>
<thead>
<tr class="header">
<th align="left">Parameter 1</th>
<th align="left">Parameter 1 Value and Cause of Error</th>
<th align="left">Parameter 2</th>
<th align="left">Parameter 3</th>
<th align="left">Parameter 4</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td align="left"><p>0x01</p></td>
<td align="left"><p>NDIS_BUGCHECK_ALLOCATE_SHARED_MEM_HIGH_IRQL</p>
<p>A driver called <strong><a href="https://msdn.microsoft.com/library/windows/hardware/ff562782" data-raw-source="[NdisMAllocateSharedMemory](https://msdn.microsoft.com/library/windows/hardware/ff562782)">NdisMAllocateSharedMemory</a></strong> at a raised IRQL.</p></td>
<td align="left"><p>The address of the specific miniport adapter block. Run <strong><a href="-ndiskd-netadapter.md" data-raw-source="[!ndiskd.netadapter](-ndiskd-netadapter.md)">!ndiskd.netadapter</a></strong> with this address for more information.</p></td>
<td align="left"><p>The length of the requested shared memory</p></td>
<td align="left"><p>The current IRQL</p></td>
</tr>
<tr class="even">
<td align="left"><p>0x02</p></td>
<td align="left"><p>NDIS_BUGCHECK_SHARED_MEM_CORRUPTION</p>
<p>During a call to <strong><a href="https://msdn.microsoft.com/library/windows/hardware/ff562782" data-raw-source="[NdisMAllocateSharedMemory](https://msdn.microsoft.com/library/windows/hardware/ff562782)">NdisMAllocateSharedMemory</a></strong>, NDIS detected that a previously-allocated shared memory page had been corrupted.</p></td>
<td align="left"><p>The address of the specific miniport adapter block. Run <strong><a href="-ndiskd-netadapter.md" data-raw-source="[!ndiskd.netadapter](-ndiskd-netadapter.md)">!ndiskd.netadapter</a></strong> with this address for more information.</p></td>
<td align="left"><p>The shared memory page that was corrupted</p></td>
<td align="left"><p>The address of a NDIS_WRAPPER_CONTEXTE that keeps track of shared memory allocations by the driver</p></td>
</tr>
<tr class="odd">
<td align="left"><p>0x03</p></td>
<td align="left"><p>NDIS_BUGCHECK_FREE_INVALID_SHARED_MEM</p>
<p>A miniport driver called <strong><a href="https://msdn.microsoft.com/library/windows/hardware/ff563589" data-raw-source="[NdisMFreeSharedMemory](https://msdn.microsoft.com/library/windows/hardware/ff563589)">NdisMFreeSharedMemory</a></strong> (<strong>Async</strong>) with a shared memory address that had already been freed.</p></td>
<td align="left"><p>The address of the specific miniport adapter block. Run <strong><a href="-ndiskd-netadapter.md" data-raw-source="[!ndiskd.netadapter](-ndiskd-netadapter.md)">!ndiskd.netadapter</a></strong> with this address for more information.</p></td>
<td align="left"><p>The page from which this shared memory was allocated</p></td>
<td align="left"><p>The virtual address of the shared memory</p></td>
</tr>
<tr class="even">
<td align="left"><p>0x04</p></td>
<td align="left"><p>NDIS_BUGCHECK_UNLOAD_DRIVER_INVALID_PARAMETER</p>
<p><strong><a href="https://msdn.microsoft.com/library/windows/hardware/ff540521" data-raw-source="[AddDevice](https://msdn.microsoft.com/library/windows/hardware/ff540521)">AddDevice</a></strong> was called with a driver that is not on the list of drivers that are registered with NDIS.</p>
<p>Enabled only on special instrumented NDIS.</p></td>
<td align="left"><p>The address of the NDIS_M_DRIVER_BLOCK</p></td>
<td align="left"><p>The address of the DRIVER_OBJECT</p></td>
<td align="left"><p>0</p></td>
</tr>
<tr class="odd">
<td align="left"><p>0x05</p></td>
<td align="left"><p>NDIS_BUGCHECK_RECVD_PACKET_IN_USE_BAD_STACK_LOCATION</p>
<p>An Ethernet driver indicated that it received a packet using a packet descriptor that was currently in use by the protocol stack.</p>
<p>Caught by checking stack packet location.</p></td>
<td align="left"><p>The address of the specific miniport adapter block. Run <strong><a href="-ndiskd-netadapter.md" data-raw-source="[!ndiskd.netadapter](-ndiskd-netadapter.md)">!ndiskd.netadapter</a></strong> with this address for more information.</p></td>
<td align="left"><p>The address of the packet descriptor used by the driver. Run <strong><a href="-ndiskd-pkt.md" data-raw-source="[!ndiskd.pkt](-ndiskd-pkt.md)">!ndiskd.pkt</a></strong> with this address for more information.</p></td>
<td align="left"><p>The address of the packet array that contained this packet descriptor</p></td>
</tr>
<tr class="even">
<td align="left"><p>0x06</p></td>
<td align="left"><p>NDIS_BUGCHECK_RECVD_PACKET_IN_USE_BAD_REF_COUNT</p>
<p>An Ethernet driver indicated that it received a packet using a packet descriptor that was currently in use by the protocol stack.</p>
<p>Caught by checking packet reference count.</p></td>
<td align="left"><p>The address of the specific miniport adapter block. Run <strong><a href="-ndiskd-netadapter.md" data-raw-source="[!ndiskd.netadapter](-ndiskd-netadapter.md)">!ndiskd.netadapter</a></strong> with this address for more information.</p></td>
<td align="left"><p>The address of the packet descriptor used by the driver. Run <strong><a href="-ndiskd-pkt.md" data-raw-source="[!ndiskd.pkt](-ndiskd-pkt.md)">!ndiskd.pkt</a></strong> with this address for more information.</p></td>
<td align="left"><p>The address of the packet array that contained this packet descriptor</p></td>
</tr>
<tr class="odd">
<td align="left"><p>0x07</p></td>
<td align="left"><p>An FDDI driver indicated that it received a packet by using a packet descriptor that was currently in use by the protocol stack.</p>
<p>Caught by checking reference count.</p></td>
<td align="left"><p>The address of the specific miniport adapter block. Run <strong><a href="-ndiskd-netadapter.md" data-raw-source="[!ndiskd.netadapter](-ndiskd-netadapter.md)">!ndiskd.netadapter</a></strong> with this address for more information.</p></td>
<td align="left"><p>The address of the packet descriptor used by the driver. Run <strong><a href="-ndiskd-pkt.md" data-raw-source="[!ndiskd.pkt](-ndiskd-pkt.md)">!ndiskd.pkt</a></strong> with this address for more information.</p></td>
<td align="left"><p>The address of the packet array that contained this packet descriptor</p></td>
</tr>
<tr class="even">
<td align="left"><p>0x08</p></td>
<td align="left"><p>NDIS_BUGCHECK_HALT_WITHOUT_INTERRUPT_DEREGISTER</p>
<p>A miniport driver did not deregister its interrupt during the halt process.</p></td>
<td align="left"><p>The address of the specific miniport adapter block. Run <strong><a href="-ndiskd-netadapter.md" data-raw-source="[!ndiskd.netadapter](-ndiskd-netadapter.md)">!ndiskd.netadapter</a></strong> with this address for more information.</p></td>
<td align="left"><p>The address of the NDIS_MINIPORT_INTERRUPT</p></td>
<td align="left"><p>0</p></td>
</tr>
<tr class="odd">
<td align="left"><p>0x09</p></td>
<td align="left"><p>NDIS_BUGCHECK_HALT_WITHOUT_CANCEL_TIMER</p>
<p>A miniport driver stopped without successfully canceling all its timers.</p></td>
<td align="left"><p>The address of the specific miniport adapter block. Run <strong><a href="-ndiskd-netadapter.md" data-raw-source="[!ndiskd.netadapter](-ndiskd-netadapter.md)">!ndiskd.netadapter</a></strong> with this address for more information.</p></td>
<td align="left"><p>The address of the miniport driver&#39;s timer queue (NDIS_MINIPORT_TIMER)</p></td>
<td align="left"><p>0</p></td>
</tr>
<tr class="even">
<td align="left"><p>0x0A</p></td>
<td align="left"><p>NDIS_BUGCHECK_DRIVER_UNLOAD_UNEXPECTED</p>
<p>A miniport driver is getting unloaded prematurely.</p></td>
<td align="left"><p>The address of the NDIS_M_DRIVER_BLOCK</p></td>
<td align="left"><p>The address of the DRIVER_OBJECT</p></td>
<td align="left"><p>The reference count for the miniport driver</p></td>
</tr>
<tr class="odd">
<td align="left"><p>0x0B</p></td>
<td align="left"><p>NDIS_BUGCHECK_INIT_FAILED_WITHOUT_INTERRUPT_DEREGISTER</p>
<p>A miniport driver failed its initialization without deregistering its interrupt.</p></td>
<td align="left"><p>The address of the specific miniport adapter block. Run <strong><a href="-ndiskd-netadapter.md" data-raw-source="[!ndiskd.netadapter](-ndiskd-netadapter.md)">!ndiskd.netadapter</a></strong> with this address for more information.</p></td>
<td align="left"><p>The address of the NDIS_MINIPORT_INTERRUPT</p></td>
<td align="left"><p>0</p></td>
</tr>
<tr class="even">
<td align="left"><p>0x0C</p></td>
<td align="left"><p>NDIS_BUGCHECK_INIT_FAILED_WITHOUT_CANCEL_TIMER</p>
<p>A miniport driver failed its initialization without successfully canceling all its timers.</p></td>
<td align="left"><p>The address of the specific miniport adapter block. Run <strong><a href="-ndiskd-netadapter.md" data-raw-source="[!ndiskd.netadapter](-ndiskd-netadapter.md)">!ndiskd.netadapter</a></strong> with this address for more information.</p></td>
<td align="left"><p>The address of the miniport driver&#39;s timer queue (NDIS_MINIPORT_TIMER)</p></td>
<td align="left"><p>0</p></td>
</tr>
<tr class="odd">
<td align="left"><p>0x0D</p></td>
<td align="left"><p>NDIS_BUGCHECK_HALT_INIT_WITHOUT_INTERRUPT_DEREGISTER</p>
<p>A miniport driver did not deregister its interrupt during the halt process.</p>
<p>The halt was called from the initialize routine after the miniport driver returned success from its initialize handler.</p></td>
<td align="left"><p>The address of the specific miniport adapter block. Run <strong><a href="-ndiskd-netadapter.md" data-raw-source="[!ndiskd.netadapter](-ndiskd-netadapter.md)">!ndiskd.netadapter</a></strong> with this address for more information.</p></td>
<td align="left"><p>The address of the NDIS_MINIPORT_INTERRUPT</p></td>
<td align="left"><p>0</p></td>
</tr>
<tr class="even">
<td align="left"><p>0x0E</p></td>
<td align="left"><p>NDIS_BUGCHECK_HALT_INIT_WITHOUT_CANCEL_TIMER</p>
<p>A miniport driver stopped without successfully canceling all its timers.</p>
<p>The halt was called from the initialize routine after the miniport driver returned success from its initialize handler.</p></td>
<td align="left"><p>The address of the specific miniport adapter block. Run <strong><a href="-ndiskd-netadapter.md" data-raw-source="[!ndiskd.netadapter](-ndiskd-netadapter.md)">!ndiskd.netadapter</a></strong> with this address for more information.</p></td>
<td align="left"><p>The address of the miniport driver&#39;s timer queue (NDIS_MINIPORT_TIMER)</p></td>
<td align="left"><p>0</p></td>
</tr>
<tr class="odd">
<td align="left"><p>0x0F</p></td>
<td align="left"><p>NDIS_BUGCHECK_RESET_COMPLETE_UNEXPECTED</p>
<p>A miniport driver called <strong><a href="https://msdn.microsoft.com/library/windows/hardware/ff563663" data-raw-source="[NdisMResetComplete](https://msdn.microsoft.com/library/windows/hardware/ff563663)">NdisMResetComplete</a></strong> without any pending reset request.</p></td>
<td align="left"><p>The address of the specific miniport adapter block. Run <strong><a href="-ndiskd-netadapter.md" data-raw-source="[!ndiskd.netadapter](-ndiskd-netadapter.md)">!ndiskd.netadapter</a></strong> with this address for more information.</p></td>
<td align="left"><p>The reset status</p></td>
<td align="left"><p>AddressingReset (BOOLEAN)</p></td>
</tr>
<tr class="even">
<td align="left"><p>0x10</p></td>
<td align="left"><p>NDIS_BUGCHECK_PM_INIT_FAILED_NO_INT_DEREGISTER</p>
<p>After resuming from a low-power state, a miniport driver failed its initialization without deregistering its interrupt.</p></td>
<td align="left"><p>The address of the specific miniport adapter block. Run <strong><a href="-ndiskd-netadapter.md" data-raw-source="[!ndiskd.netadapter](-ndiskd-netadapter.md)">!ndiskd.netadapter</a></strong> with this address for more information.</p></td>
<td align="left"><p>The address of the NDIS_MINIPORT_INTERRUPT</p></td>
<td align="left"><p>0</p></td>
</tr>
<tr class="odd">
<td align="left"><p>0x11</p></td>
<td align="left"><p>NDIS_BUGCHECK_PM_INIT_FAILED_NO_CANCEL_TIMER</p>
<p>After resuming from a low-power state, a miniport driver failed its initialization without successfully canceling all its timers.</p></td>
<td align="left"><p>The address of the specific miniport adapter block. Run <strong><a href="-ndiskd-netadapter.md" data-raw-source="[!ndiskd.netadapter](-ndiskd-netadapter.md)">!ndiskd.netadapter</a></strong> with this address for more information.</p></td>
<td align="left"><p>The address of the miniport driver&#39;s timer queue (NDIS_MINIPORT_TIMER)</p></td>
<td align="left"><p>0</p></td>
</tr>
<tr class="even">
<td align="left"><p>0x12</p></td>
<td align="left"><p>NDIS_BUGCHECK_NFILTER_RECVD_PACKET_BAD_REF_COUNT</p>
<p>A miniport driver indicated that it received a packet using a packet descriptor that was currently in use by the protocol stack.</p>
<p>Caught by checking packet reference count.</p></td>
<td align="left"><p>The address of the specific miniport adapter block. Run <strong><a href="-ndiskd-netadapter.md" data-raw-source="[!ndiskd.netadapter](-ndiskd-netadapter.md)">!ndiskd.netadapter</a></strong> with this address for more information.</p></td>
<td align="left"><p>The address of the packet descriptor used by the driver. Run <strong><a href="-ndiskd-pkt.md" data-raw-source="[!ndiskd.pkt](-ndiskd-pkt.md)">!ndiskd.pkt</a></strong> with this address for more information.</p></td>
<td align="left"><p>The address of the packet array that contained this packet descriptor</p></td>
</tr>
<tr class="odd">
<td align="left"><p>0x13</p></td>
<td align="left"><p>NDIS_BUGCHECK_TFILTER_RECVD_PACKET_BAD_REF_COUNT</p>
<p>A Token-Ring miniport driver indicated that it received a packet using a packet descriptor that was currently in use by the protocol stack.</p>
<p>Caught by checking packet reference count.</p></td>
<td align="left"><p>The address of the specific miniport adapter block. Run <strong><a href="-ndiskd-netadapter.md" data-raw-source="[!ndiskd.netadapter](-ndiskd-netadapter.md)">!ndiskd.netadapter</a></strong> with this address for more information.</p></td>
<td align="left"><p>The address of the packet descriptor used by the driver. Run <strong><a href="-ndiskd-pkt.md" data-raw-source="[!ndiskd.pkt](-ndiskd-pkt.md)">!ndiskd.pkt</a></strong> with this address for more information.</p></td>
<td align="left"><p>The address of the packet array that contained this packet descriptor</p></td>
</tr>
<tr class="even">
<td align="left"><p>0x14</p></td>
<td align="left"><p>NDIS_BUGCHECK_WAIT_EVENT_HIGH_IRQL</p>
<p>An NDIS driver called <strong><a href="https://msdn.microsoft.com/library/windows/hardware/ff564651" data-raw-source="[NdisWaitEvent](https://msdn.microsoft.com/library/windows/hardware/ff564651)">NdisWaitEvent</a></strong> at an illegal IRQL</p></td>
<td align="left"><p>The actual IRQL</p></td>
<td align="left"><p>0</p></td>
<td align="left"><p>0</p></td>
</tr>
<tr class="odd">
<td align="left"><p>0x15</p></td>
<td align="left"><p>NDIS_BUGCHECK_INVALID_NDIS5_CALL</p>
<p>A miniport driver called an API that is reserved for older drivers. The driver should only call NDIS 6.x APIs.</p></td>
<td align="left"><p>The address of the specific miniport adapter block. Run <strong><a href="-ndiskd-netadapter.md" data-raw-source="[!ndiskd.netadapter](-ndiskd-netadapter.md)">!ndiskd.netadapter</a></strong> with this address for more information.</p></td>
<td align="left"><p>0</p></td>
<td align="left"><p>0</p></td>
</tr>
<tr class="even">
<td align="left"><p>0x16</p></td>
<td align="left"><p>NDIS_BUGCHECK_INVALID_OPEN_IN_BIND_CONTEXT</p>
<p>A protocol driver improperly opened an adapter during binding.</p></td>
<td align="left"><p>The address of the specific protocol. Run <strong><a href="-ndiskd-protocol.md" data-raw-source="[!ndiskd.protocol](-ndiskd-protocol.md)">!ndiskd.protocol</a></strong> with this address for more information.</p></td>
<td align="left"><p>The address of the context area that is allocated by the protocol driver.</p>
<p>Cast to ndis!NDIS_BIND_CONTEXT.</p></td>
<td align="left"><p>The address of the open handle. Run <strong><a href="-ndiskd-mopen.md" data-raw-source="[!ndiskd.mopen](-ndiskd-mopen.md)">!ndiskd.mopen</a></strong> with this address for more information.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>0x17</p></td>
<td align="left"><p>NDIS_BUGCHECK_IFPROVIDER_DEREGISTER_UNEXPECTED</p>
<p>An Interface Provider called <strong><a href="https://msdn.microsoft.com/library/windows/hardware/ff562703" data-raw-source="[NdisIfDeregisterProvider](https://msdn.microsoft.com/library/windows/hardware/ff562703)">NdisIfDeregisterProvider</a></strong> without first removing all its Interfaces.</p></td>
<td align="left"><p>The address of the interface provider handle. Run <strong><a href="-ndiskd-ifprovider.md" data-raw-source="[!ndiskd.ifprovider](-ndiskd-ifprovider.md)">!ndiskd.ifprovider</a></strong> with this address for more information.</p></td>
<td align="left"><p>0</p></td>
<td align="left"><p>0</p></td>
</tr>
<tr class="even">
<td align="left"><p>0x1B</p></td>
<td align="left"><p>NDIS_BUGCHECK_IF_STACK_TABLE_LOOP</p>
<p>A driver attempted to add an Interface to the ifStackTable, but doing so would cause a cycle. The ifStackTable must not have cycles. Run <strong><a href="-ndiskd-ifstacktable.md" data-raw-source="[!ndiskd.ifstacktable](-ndiskd-ifstacktable.md)">!ndiskd.ifstacktable</a></strong> to see the current table (prior to this call to <strong><a href="https://msdn.microsoft.com/library/windows/hardware/ff562693" data-raw-source="[NdisIfAddIfStackEntry](https://msdn.microsoft.com/library/windows/hardware/ff562693)">NdisIfAddIfStackEntry</a></strong>).</p></td>
<td align="left"><p>The HigherLayerIfIndex being added to the table</p></td>
<td align="left"><p>The LowerLayerIfIndex being added to the table</p></td>
<td align="left"><p>0</p></td>
</tr>
<tr class="odd">
<td align="left"><p>0x1C</p></td>
<td align="left"><p>NDIS_BUGCHECK_MINIPORT_FAILED_OID_WHICH_MUST_SUCCEED</p>
<p>A miniport driver failed an OID request that must not fail. Doing so would leak memory or other resources.</p></td>
<td align="left"><p>The address of the specific miniport adapter block. Run <strong><a href="-ndiskd-netadapter.md" data-raw-source="[!ndiskd.netadapter](-ndiskd-netadapter.md)">!ndiskd.netadapter</a></strong> with this address for more information.</p></td>
<td align="left"><p>The OID that was failed. Use <strong><a href="-ndiskd-help.md" data-raw-source="[!ndiskd.help](-ndiskd-help.md)">!ndiskd.help</a></strong> to find the name of this OID.</p></td>
<td align="left"><p>The failure status code (NDIS_STATUS_XXX) with which the OID request was completed</p></td>
</tr>
<tr class="even">
<td align="left"><p>0x1D</p></td>
<td align="left"><p>NDIS_BUGCHECK_OID_REQUEST_INVALID_BUFFER</p>
<p>A miniport driver or filter driver has completed an OID request illegally. Check that BytesWritten is not greater than the entire length of the buffer.</p></td>
<td align="left"><p>The address of the specific miniport adapter or filter module block. Run <strong><a href="-ndiskd-netadapter.md" data-raw-source="[!ndiskd.netadapter](-ndiskd-netadapter.md)">!ndiskd.netadapter</a></strong> or <strong><a href="-ndiskd-filter.md" data-raw-source="[!ndiskd.filter](-ndiskd-filter.md)">!ndiskd.filter</a></strong> with this address for more information.</p></td>
<td align="left"><p>The address to the <strong><a href="https://msdn.microsoft.com/library/windows/hardware/ff566710" data-raw-source="[NDIS_OID_REQUEST](https://msdn.microsoft.com/library/windows/hardware/ff566710)">NDIS_OID_REQUEST</a></strong> that was completed illegally. Inspect it with <strong><a href="-ndiskd-oid.md" data-raw-source="[!ndiskd.oid](-ndiskd-oid.md)">!ndiskd.oid</a></strong>.</p></td>
<td align="left"><p>0</p></td>
</tr>
<tr class="odd">
<td align="left"><p>0x1E</p></td>
<td align="left"><p>NDIS_BUGCHECK_REFCOUNT_IMBALANCE</p>
<p>NDIS has detected an error in an internal refcount. This can be caused by a refcount underflow (more dereferences than references), or by a tag mismatch.</p></td>
<td align="left"><p>0</p></td>
<td align="left"><p>Internal handle. Use <strong><a href="-ndiskd-ndisref.md" data-raw-source="[!ndiskd.ndisref](-ndiskd-ndisref.md)">!ndiskd.ndisref</a></strong> or cast to ndis!NDIS_REFCOUNT_BLOCK.</p></td>
<td align="left"><p>The current reftag value</p></td>
</tr>
<tr class="even">
<td align="left"><p>0x1F</p></td>
<td align="left"><p>NDIS_BUGCHECK_ILLEGAL_MINIPORT_STATE_TRANSITION</p>
<p>A miniport driver completed a state transition illegally.</p></td>
<td align="left"><p>What failed. Possible values:</p>
<ol>
<li><p>NDIS_BUGCHECK_ILLEGAL_MINIPORT_STATE_TRANSITION_PAUSE_COMPLETE</p>
<p>The miniport called <strong>NdisMPauseComplete</strong> but there was no pending Pause operation.</p></li>
<li><p>NDIS_BUGCHECK_ILLEGAL_MINIPORT_STATE_TRANSITION_RESTART_COMPLETE</p>
<p>The miniport called <strong>NdisMRestartComplete</strong> but there was no pending Restart operation.</p></li>
</ol></td>
<td align="left"><p>The address of the specific miniport adapter block. Run <strong><a href="-ndiskd-netadapter.md" data-raw-source="[!ndiskd.netadapter](-ndiskd-netadapter.md)">!ndiskd.netadapter</a></strong> with this address for more information.</p></td>
<td align="left"><p>0</p></td>
</tr>
<tr class="odd">
<td align="left"><p>0x20</p></td>
<td align="left"><p>NDIS_BUGCHECK_STATUS_INDICATION_INVALID_BUFFER</p>
<p>A miniport driver or filter driver indicated an illegal <strong><a href="https://msdn.microsoft.com/library/windows/hardware/ff567373" data-raw-source="[NDIS_STATUS_INDICATION](https://msdn.microsoft.com/library/windows/hardware/ff567373)">NDIS_STATUS_INDICATION</a></strong>.</p></td>
<td align="left"><p>The type of the status indication. Run <strong><a href="-ndiskd-help.md" data-raw-source="[!ndiskd.help](-ndiskd-help.md)">!ndiskd.help</a></strong> with this code for more information.</p></td>
<td align="left"><p>The handle of the driver instance that indicated this illegal status indication. Run <strong><a href="-ndiskd-netadapter.md" data-raw-source="[!ndiskd.netadapter](-ndiskd-netadapter.md)">!ndiskd.netadapter</a></strong> or <strong><a href="-ndiskd-filter.md" data-raw-source="[!ndiskd.filter](-ndiskd-filter.md)">!ndiskd.filter</a></strong> with this handle for more information.</p></td>
<td align="left"><p>The address of the status indication payload. Its interpretation depends on the type of status indication.</p></td>
</tr>
<tr class="even">
<td align="left"><p>0x21</p></td>
<td align="left"><p>NDIS_BUGCHECK_INVALID_OBJECT_HEADER</p>
<p>A driver created an invalid <strong><a href="https://msdn.microsoft.com/library/windows/hardware/ff566588" data-raw-source="[NDIS_OBJECT_HEADER](https://msdn.microsoft.com/library/windows/hardware/ff566588)">NDIS_OBJECT_HEADER</a></strong>.</p></td>
<td align="left"><p>The handle of the driver that indicated the illegal status indication. Run <strong><a href="-ndiskd-minidriver.md" data-raw-source="[!ndiskd.minidriver](-ndiskd-minidriver.md)">!ndiskd.minidriver</a></strong> or <strong><a href="-ndiskd-filterdriver.md" data-raw-source="[!ndiskd.filterdriver](-ndiskd-filterdriver.md)">!ndiskd.filterdriver</a></strong> with this handle for more information.</p></td>
<td align="left"><p>The object with the malformed header. Its interpretation depends on the API being called. For example, if the driver called <strong>NdisAllocateCloneOidRequest</strong>, then cast the object to ndis!NDIS_OID_REQUEST.</p></td>
<td align="left"><p>0</p></td>
</tr>
<tr class="odd">
<td align="left"><p>0x22</p></td>
<td align="left"><p>NDIS_BUGCHECK_ILLEGAL_NET_PNP_EVENT</p>
<p>A miniport driver or filter driver indicated an illegal <strong><a href="https://msdn.microsoft.com/library/windows/hardware/ff568752" data-raw-source="[NET_PNP_EVENT_NOTIFICATION](https://msdn.microsoft.com/library/windows/hardware/ff568752)">NET_PNP_EVENT_NOTIFICATION</a></strong>.</p></td>
<td align="left"><p>The handle of the driver that indicated the illegal status indication. Run <strong><a href="-ndiskd-minidriver.md" data-raw-source="[!ndiskd.minidriver](-ndiskd-minidriver.md)">!ndiskd.minidriver</a></strong> or <strong><a href="-ndiskd-filterdriver.md" data-raw-source="[!ndiskd.filterdriver](-ndiskd-filterdriver.md)">!ndiskd.filterdriver</a></strong> with this handle for more information.</p></td>
<td align="left"><p>Cast to NET_PNP_EVENT_NOTIFICATION</p></td>
<td align="left"><p>0</p></td>
</tr>
<tr class="even">
<td align="left"><p>0x23</p></td>
<td align="left"><p>NDIS_BUGCHECK_PD_ERROR</p>
<p>An error was detected in the Packet Direct datapath.</p></td>
<td align="left"><p>The subtype of the bugcheck. Possible values:</p>
<ol>
<li><p>NDIS_BUGCHECK_PD_ERROR_EC_THREAD_MISMATCH</p>
<p>An API was called on the wrong thread.</p></li>
<li><p>NDIS_BUGCHECK_PD_ERROR_ILLEGAL_ARM_BY_CLIENT</p>
<p>A PD client attempted to arm the provider while in an illegal state.</p></li>
<li><p>NDIS_BUGCHECK_PD_ERROR_ILLEGAL_ARM_NOTIFICATION</p>
<p>A PD provider illegally triggered a drain notification while it was not armed.</p></li>
<li><p>NDIS_BUGCHECK_PD_ERROR_ILLEGAL_ARM_NOTIFICATION_VIA_ISR</p>
<p>A PD provider illegally triggered an ISR drain notification while it was not armed.</p></li>
<li><p>NDIS_BUGCHECK_PD_ERROR_ILLEGAL_THUNK_BY_LWF</p>
<p>A filter driver attempted to interfere with the Packet Direct datapath.</p></li>
<li><p>NDIS_BUGCHECK_PD_ERROR_ILLEGAL_BM_GROUP_REQUEST</p>
<p>A PD provider illegally attempted to remove itself from a buffer manager group.</p></li>
<li><p>NDIS_BUGCHECK_PD_ERROR_ILLEGAL_PD_BUFFER_SETUP</p>
<p>A PD buffer setup request was malformed.</p></li>
</ol></td>
<td align="left"><p>The value of Parameter 3 depends on the value of Parameter 2. Each number in this list corresponds to the same number in Parameter 2.</p>
<ol>
<li>Cast to NDIS_PD_EC</li>
<li>Cast to NDIS_PD_QUEUE_TRACKER</li>
<li>Cast to NDIS_PD_QUEUE_TRACKER</li>
<li>Cast to NDIS_PD_QUEUE_TRACKER</li>
<li>The handle of the specific filter module. Run <strong><a href="-ndiskd-filter.md" data-raw-source="[!ndiskd.filter](-ndiskd-filter.md)">!ndiskd.filter</a></strong> with this handle for more information.</li>
<li>The buffer manager group, if known</li>
<li>The source PD_MEMORY_HANDLE or PD_BUFFER</li>
</ol></td>
<td align="left"><p>The value of Parameter 4 depends on the value of Parameter 2. Each number in this list corresponds to the same number in Parameter 2.</p>
<ol>
<li>The ETHREAD that was expected</li>
<li>The handle to the PD client</li>
<li>The handle to the PD provider. Run <strong><a href="-ndiskd-netadapter.md" data-raw-source="[!ndiskd.netadapter](-ndiskd-netadapter.md)">!ndiskd.netadapter</a></strong> with this handle for more information.</li>
<li>The handle to the PD provider. Run <strong><a href="-ndiskd-netadapter.md" data-raw-source="[!ndiskd.netadapter](-ndiskd-netadapter.md)">!ndiskd.netadapter</a></strong> with this handle for more information.</li>
<li>The handle to the PD provider. Run <strong><a href="-ndiskd-netadapter.md" data-raw-source="[!ndiskd.netadapter](-ndiskd-netadapter.md)">!ndiskd.netadapter</a></strong> with this handle for more information.</li>
<li><p>If Parameter 3 is 0, this is the provider handle.</p>
<p>If Parameter 3 is non-zero, the PD client has not freed all allocations yet, and this is the PD client handle.</p></li>
<li>The target PD_BUFFER</li>
</ol></td>
</tr>
<tr class="odd">
<td align="left"><p>0x24</p></td>
<td align="left"><p>NDIS_BUGCHECK_UNEXPECTED_FAILURE</p>
<p>An internal operation failed unexpectedly. This is likely to be a bug in NDIS.SYS itself.</p></td>
<td align="left"><p>The operation that failed. Possible values:</p>
<p>0x01 : NDIS_BUGCHECK_UNEXPECTED_FAILURE_KEWAITFORSINGLEOBJECT</p>
<p>A call to KeWaitForSingleObject failed.</p></td>
<td align="left"><p>The failure status code</p></td>
<td align="left"><p>0</p></td>
</tr>
<tr class="even">
<td align="left"><p>0x25</p></td>
<td align="left"><p>NDIS_BUGCHECK_WATCHDOG</p>
<p>An attempt to manage the network stack has taken too long. When NDIS calls out into other drivers, NDIS starts a watchdog timer to ensure the call completes promptly. If the call takes too long, NDIS injects a bugcheck.</p>
<p>This can be caused by a simple deadlock. Look with &quot;!stacks 2 ndis&quot; or similar to see if any threads look suspicious. Pay special attention to the PrimaryThread from the NDIS_WATCHDOG_TRIAGE_BLOCK.</p>
<p>This can be caused by lost NBLs, in which case <strong><a href="-ndiskd-pendingnbls.md" data-raw-source="[!ndiskd.pendingnbls](-ndiskd-pendingnbls.md)">!ndiskd.pendingnbls</a></strong> may help. Check for OIDs that are stuck using <strong><a href="-ndiskd-oid.md" data-raw-source="[!ndiskd.oid](-ndiskd-oid.md)">!ndiskd.oid</a></strong>.</p></td>
<td align="left"><p>The operation that took too long. Possible values:</p>
<ul>
<li><p>0x01 : NDIS_BUGCHECK_WATCHDOG_PROTOCOL_PAUSE</p>
<p>There was a timeout while pausing a protocol driver.</p></li>
<li><p>0x02 : NDIS_BUGCHECK_WATCHDOG_PROTOCOL_NETPNPEVENT</p>
<p>There was a timeout while delivering a NET_PNP_EVENT_NOTIFICATION to a protocol driver.</p></li>
<li><p>0x03 : NDIS_BUGCHECK_WATCHDOG_PROTOCOL_STATUS_INDICATION</p>
<p>There was a timeout while delivering a status indication to a protocol driver.</p></li>
<li><p>0x04 : NDIS_BUGCHECK_WATCHDOG_PROTOCOL_UNBIND</p>
<p>There was a timeout while unbinding a protocol driver.</p></li>
<li><p>0x11 : NDIS_BUGCHECK_WATCHDOG_FILTER_PAUSE</p>
<p>There was a timeout while pausing a filter driver.</p></li>
<li><p>0x12 : NDIS_BUGCHECK_WATCHDOG_FILTER_NETPNPEVENT</p>
<p>There was a timeout while delivering a NET_PNP_EVENT_NOTIFICATION to a filter driver.</p></li>
<li><p>0x13 : NDIS_BUGCHECK_WATCHDOG_FILTER_STATUS_INDICATION</p>
<p>There was a timeout while delivering a status indication to a filter driver.</p></li>
<li><p>0x14 : NDIS_BUGCHECK_WATCHDOG_FILTER_DETACH</p>
<p>There was a timeout while detaching a filter driver.</p></li>
<li><p>0x21 : NDIS_BUGCHECK_WATCHDOG_MINIPORT_PAUSE</p>
<p>There was a timeout while pausing a miniport adapter.</p></li>
<li><p>0x22 : NDIS_BUGCHECK_WATCHDOG_MINIPORT_HALT</p>
<p>There was a timeout while halting a miniport adapter.</p></li>
<li><p>0x23 : NDIS_BUGCHECK_WATCHDOG_MINIPORT_OID</p>
<p>There was a timeout while delivering an OID request to a miniport adapter.</p></li>
<li><p>0x24 : NDIS_BUGCHECK_WATCHDOG_FILTER_OID</p>
<p>There was a timeout while delivering an OID request to a filter driver.</p></li>
<li><p>0x25 : NDIS_BUGCHECK_WATCHDOG_MINIPORT_IDLE</p>
<p>There was a timeout while idling a miniport adapter.</p></li>
<li><p>0x26 : NDIS_BUGCHECK_WATCHDOG_CANCEL_IDLE</p>
<p>There was a timeout while canceling an idle request on a miniport adapter.</p></li>
</ul></td>
<td align="left"><p>Cast to ndis!NDIS_WATCHDOG_TRIAGE_BLOCK. Useful fields:</p>
<ul>
<li><strong>StartTime</strong> shows what time the operation started, in 100ns units, as returned by KeQueryInterruptTime.</li>
<li><strong>TimeoutMilliseconds</strong> shows how long NDIS waited, at a minimum, before triggering this bugcheck.</li>
<li><strong>TargetObject</strong> is a handle to the protocol, filter module, or miniport adapter that NDIS is waiting on. Run <strong><a href="-ndiskd-protocol.md" data-raw-source="[!ndiskd.protocol](-ndiskd-protocol.md)">!ndiskd.protocol</a></strong>, <strong><a href="-ndiskd-filter.md" data-raw-source="[!ndiskd.filter](-ndiskd-filter.md)">!ndiskd.filter</a></strong>, or <strong><a href="-ndiskd-netadapter.md" data-raw-source="[!ndiskd.netadapter](-ndiskd-netadapter.md)">!ndiskd.netadapter</a></strong> with this handle for more information.</li>
<li><strong>PrimaryThread</strong> is the thread on which NDIS initiated the operation. Usually, this is the first place to look, although the thread may have gone elsewhere if the operation is being handled asynchronously.</li>
</ul></td>
<td align="left"><p>The value of Parameter 4 depends on the value of Parameter 2. Each number in this list corresponds to the same hexadecimal value in Parameter 2.</p>
<ul>
<li>0x01 : 0</li>
<li>0x02 : The NET_PNP_EVENT_CODE of the stuck event. For more information about these codes, see <strong><a href="https://msdn.microsoft.com/library/windows/hardware/ff568751" data-raw-source="[NET_PNP_EVENT](https://msdn.microsoft.com/library/windows/hardware/ff568751)">NET_PNP_EVENT</a></strong>..</li>
<li>0x03 : The NDIS_STATUS code of the stuck indication. Use <strong><a href="-ndiskd-help.md" data-raw-source="[!ndiskd.help](-ndiskd-help.md)">!ndiskd.help</a></strong> to decode it.</li>
<li>0x04 : 0</li>
<li>0x11 : 0</li>
<li>0x12 : The NET_PNP_EVENT_CODE of the stuck event. For possible values, see the previous list of values for item 2 in this list.</li>
<li>0x13 : The NDIS_STATUS code of the stuck indication. Use <strong><a href="-ndiskd-help.md" data-raw-source="[!ndiskd.help](-ndiskd-help.md)">!ndiskd.help</a></strong> to decode it.</li>
<li>0x14 : 0</li>
<li>0x21 : 0</li>
<li>0x22 : 0</li>
<li>0x23 : The OID code of the stuck request. Use <strong><a href="-ndiskd-help.md" data-raw-source="[!ndiskd.help](-ndiskd-help.md)">!ndiskd.help</a></strong> to decode it.</li>
<li>0x24 : The OID code of the stuck request. Use <strong><a href="-ndiskd-help.md" data-raw-source="[!ndiskd.help](-ndiskd-help.md)">!ndiskd.help</a></strong> to decode it.</li>
<li>0x25 : 0</li>
<li>0x26 : 0</li>
</ul></td>
</tr>
<tr class="odd">
<td align="left"><p>0x26</p></td>
<td align="left"><p>NDIS_BUGCHECK_INVALID_OID_COMPLETION</p>
<p>A miniport driver attempted to complete an OID request that is not currently pending on that miniport driver. This can be caused by the driver trying to complete the same request more than one time.</p></td>
<td align="left"><p>The miniport driver handle that caused the bugcheck. Run <strong><a href="-ndiskd-minidriver.md" data-raw-source="[!ndiskd.minidriver](-ndiskd-minidriver.md)">!ndiskd.minidriver</a></strong> with this handle for more information.</p></td>
<td align="left"><p>The NDIS OID request the miniport driver was trying to complete. You can try to run <strong><a href="-ndiskd-oid.md" data-raw-source="[!ndiskd.oid](-ndiskd-oid.md)">!ndiskd.oid</a></strong> with this request but the memory might not be valid at this point.</p></td>
<td align="left"><p>0</p></td>
</tr>
<tr class="even">
<td align="left"><p>0x27</p></td>
<td align="left"><p>NDIS_BUGCHECK_LEAKED_NBL</p>
<p>A driver has leaked a <strong><a href="https://msdn.microsoft.com/library/windows/hardware/ff568388" data-raw-source="[NET_BUFFER_LIST](https://msdn.microsoft.com/library/windows/hardware/ff568388)">NET_BUFFER_LIST</a></strong> structure. Check with <strong><a href="-ndiskd-pendingnbls.md" data-raw-source="[!ndiskd.pendingnbls](-ndiskd-pendingnbls.md)">!ndiskd.pendingnbls</a></strong> to see any NBLs that are still pending on this driver.</p></td>
<td align="left"><p>Where the leak was detected. Possible values:</p>
<ul>
<li><p>0x01 : The leak was detected by the NBL tracker. The driver that is currently deregistering or unbinding is the most likely cause. Look at the callstack of the bugchecking thread. Drivers must not unbind or deregister while they still hold active NBLs.</p></li>
</ul></td>
<td align="left"><p>0</p></td>
<td align="left"><p>0</p></td>
</tr>
</tbody>
</table>

 

Cause
-----

Parameter 1 indicates the specific cause of the BUGCODE\_NDIS\_DRIVER bug check.

Remarks
-------

The BUGCODE\_NDIS\_DRIVER bugcheck indendifies problems in network drivers. Often, the problem is caused by a NDIS miniport driver. You can get a complete list of NDIS miniport drivers by using [**!ndiskd.netadapter**](-ndiskd-netadapter.md). You can get a bigger picture overview of the network stack with [**!ndiskd.netreport**](-ndiskd-netreport.md).

This bug check code occurs only on Microsoft Windows Server 2003 and later versions of Windows. In Windows 2000 and Windows XP, the corresponding code is [**bug check 0xD2**](bug-check-0xd2--bugcode-id-driver.md) (BUGCODE\_ID\_DRIVER).

 

 




