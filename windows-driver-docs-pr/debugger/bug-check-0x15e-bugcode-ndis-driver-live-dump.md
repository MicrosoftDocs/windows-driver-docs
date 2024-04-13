---
title: Bug Check 0x15E BUGCODE_NDIS_DRIVER_LIVE_DUMP
description: The BUGCODE_NDIS_DRIVER_LIVE_DUMP bug code has a value of 0x0000015E. This bug code indicates that NDIS has captured a live kernel dump. NDIS does not generate a bug check in this situation.
keywords: ["Bug Check 0x15E BUGCODE_NDIS_DRIVER_LIVE_DUMP", "BUGCODE_NDIS_DRIVER"]
ms.date: 05/23/2017
topic_type:
- apiref
ms.topic: reference
api_name:
- BUGCODE_NDIS_DRIVER
api_type:
- NA
---

# Bug Check 0x15E: BUGCODE\_NDIS\_DRIVER\_LIVE\_DUMP


The BUGCODE\_NDIS\_DRIVER\_LIVE\_DUMP live dump has a value of 0x0000015E. This bug code indicates that NDIS has captured a live kernel dump. NDIS does not generate a bug check in this situation.

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
<td align="left"><p>NDIS_BUGCHECK_MINIPORT_FATAL_ERROR</p>
<p>A miniport driver has encountered a fatal error and requested re-enumeration.</p></td>
<td align="left"><p>The address of the miniport block. Run <strong><a href="../debuggercmds/-ndiskd-minidriver.md" data-raw-source="[!ndiskd.minidriver](../debuggercmds/-ndiskd-minidriver.md)">!ndiskd.minidriver</a></strong> with this address for more information.</p></td>
<td align="left"><p>The address of the miniport's Physical Device Object (PDO)</p></td>
<td align="left"><p>The fatal error that caused this live dump to be taken. Possible values:</p>
<ol>
<li>70: Caused by user mode</li>
<li>71: Caused by <strong><a href="/windows-hardware/drivers/ddi/ndis/nf-ndis-ndismremoveminiport" data-raw-source="[NdisMRemoveMiniport](/windows-hardware/drivers/ddi/ndis/nf-ndis-ndismremoveminiport)">NdisMRemoveMiniport</a></strong></li>
<li>72: Caused by <strong><a href="/windows-hardware/drivers/ddi/ndis/nf-ndis-ndisiminitializedeviceinstanceex" data-raw-source="[NdisIMInitializeDeviceInstanceEx](/windows-hardware/drivers/ddi/ndis/nf-ndis-ndisiminitializedeviceinstanceex)">NdisIMInitializeDeviceInstanceEx</a></strong> failing</li>
<li>73: Caused by <em><a href="/windows-hardware/drivers/ddi/ndis/nc-ndis-miniport_restart" data-raw-source="[MiniportRestart](/windows-hardware/drivers/ddi/ndis/nc-ndis-miniport_restart)">MiniportRestart</a></em> failing</li>
<li>74: Caused by failing a <a href="/windows-hardware/drivers/network/oid-pnp-set-power" data-raw-source="[OID_PNP_SET_POWER (D0)](../network/oid-pnp-set-power.md)">OID_PNP_SET_POWER (D0)</a> request</li>
<li>75: Caused by failing a <a href="/windows-hardware/drivers/network/oid-pnp-set-power" data-raw-source="[OID_PNP_SET_POWER (Dx)](../network/oid-pnp-set-power.md)">OID_PNP_SET_POWER (Dx)</a> request</li>
</ol></td>
</tr>
<tr class="even">
<td align="left"><p>0x25</p></td>
<td align="left"><p>NDIS_BUGCHECK_WATCHDOG</p>
<p>An attempt to manage the network stack has taken too long. When NDIS calls out into other drivers, NDIS starts a watchdog timer to ensure the call completes promptly. If the call takes too long, NDIS injects a bugcheck.</p>
<p>This can be caused by a simple deadlock. Look with "!stacks 2 ndis" or similar to see if any threads look suspicious. Pay special attention to the PrimaryThread from the NDIS_WATCHDOG_TRIAGE_BLOCK.</p>
<p>This can be caused by lost NBLs, in which case <strong><a href="../debuggercmds/-ndiskd-pendingnbls.md" data-raw-source="[!ndiskd.pendingnbls](../debuggercmds/-ndiskd-pendingnbls.md)">!ndiskd.pendingnbls</a></strong> may help. Check for OIDs that are stuck using <strong><a href="../debuggercmds/-ndiskd-oid.md" data-raw-source="[!ndiskd.oid](../debuggercmds/-ndiskd-oid.md)">!ndiskd.oid</a></strong>.</p></td>
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
<li><strong>TargetObject</strong> is a handle to the protocol, filter module, or miniport adapter that NDIS is waiting on. Run <strong><a href="../debuggercmds/-ndiskd-protocol.md" data-raw-source="[!ndiskd.protocol](../debuggercmds/-ndiskd-protocol.md)">!ndiskd.protocol</a></strong>, <strong><a href="../debuggercmds/-ndiskd-filter.md" data-raw-source="[!ndiskd.filter](../debuggercmds/-ndiskd-filter.md)">!ndiskd.filter</a></strong>, or <strong><a href="../debuggercmds/-ndiskd-netadapter.md" data-raw-source="[!ndiskd.netadapter](../debuggercmds/-ndiskd-netadapter.md)">!ndiskd.netadapter</a></strong> with this handle for more information.</li>
<li><strong>PrimaryThread</strong> is the thread on which NDIS initiated the operation. Usually, this is the first place to look, although the thread may have gone elsewhere if the operation is being handled asynchronously.</li>
</ul></td>
<td align="left"><p>The value of Parameter 4 depends on the value of Parameter 2. Each number in this list corresponds to the same number in Parameter 2.</p>
<ul>
<li>0x01 : 0</li>
<li>0x02 : The NET_PNP_EVENT_CODE of the stuck event. For more information about these codes, see <strong><a href="/windows-hardware/drivers/ddi/netpnp/ns-netpnp-_net_pnp_event" data-raw-source="[NET_PNP_EVENT](/windows-hardware/drivers/ddi/netpnp/ns-netpnp-_net_pnp_event)">NET_PNP_EVENT</a></strong>..</li>
<li>0x03 : The NDIS_STATUS code of the stuck indication. Use <strong><a href="../debuggercmds/-ndiskd-help.md" data-raw-source="[!ndiskd.help](../debuggercmds/-ndiskd-help.md)">!ndiskd.help</a></strong> to decode it.</li>
<li>0x04 : 0</li>
<li>0x11 : 0</li>
<li>0x12 : The NET_PNP_EVENT_CODE of the stuck event. For possible values, see the previous list of values for item 2 in this list.</li>
<li>0x13 : The NDIS_STATUS code of the stuck indication. Use <strong><a href="../debuggercmds/-ndiskd-help.md" data-raw-source="[!ndiskd.help](../debuggercmds/-ndiskd-help.md)">!ndiskd.help</a></strong> to decode it.</li>
<li>0x14 : 0</li>
<li>0x21 : 0</li>
<li>0x22 : 0</li>
<li>0x23 : The OID code of the stuck request. Use <strong><a href="../debuggercmds/-ndiskd-help.md" data-raw-source="[!ndiskd.help](../debuggercmds/-ndiskd-help.md)">!ndiskd.help</a></strong> to decode it.</li>
<li>0x24 : The OID code of the stuck request. Use <strong><a href="../debuggercmds/-ndiskd-help.md" data-raw-source="[!ndiskd.help](../debuggercmds/-ndiskd-help.md)">!ndiskd.help</a></strong> to decode it.</li>
<li>0x25 : 0</li>
<li>0x26 : 0</li>
</ul></td>
</tr>
<tr class="odd">
<td align="left"><p>0x30</p></td>
<td align="left"><p>NDIS_BUGCHECK_STUCK_NBL</p>
<p>A miniport driver has not returned a NBL back to the stack for some time.</p></td>
<td align="left"><p>The address of the miniport block. Run <strong><a href="../debuggercmds/-ndiskd-minidriver.md" data-raw-source="[!ndiskd.minidriver](../debuggercmds/-ndiskd-minidriver.md)">!ndiskd.minidriver</a></strong> with this address for more information.</p></td>
<td align="left"><p>0</p></td>
<td align="left"><p>0</p></td>
</tr>
</tbody>
</table>

 

## Cause

The [**!analyze**](../debuggercmds/-analyze.md) debug extension displays information about the bug check and can be helpful in determining the root cause. Parameter 1 indicates the specific cause of the BUGCODE\_NDIS\_DRIVER\_LIVE\_DUMP bugcheck.

## Remarks

NDIS has detected and recovered from a serious problem in another network driver. Although the system was not halted, this problem may later cause connectivity problems or a fatal bugcheck.

This bug code occurs only in Windows 8.1 and later versions of Windows.

