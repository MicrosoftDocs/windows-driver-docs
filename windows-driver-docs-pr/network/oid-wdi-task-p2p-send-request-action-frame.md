---
title: OID_WDI_TASK_P2P_SEND_REQUEST_ACTION_FRAME
description: OID_WDI_TASK_P2P_SEND_REQUEST_ACTION_FRAME is issued to the device to send a Wi-Fi Direct Public Action Frame Request.
ms.date: 07/18/2017
keywords:
 - OID_WDI_TASK_P2P_SEND_REQUEST_ACTION_FRAME Network Drivers Starting with Windows Vista
ms.localizationpriority: medium
ms.custom: 19H1
---

# OID\_WDI\_TASK\_P2P\_SEND\_REQUEST\_ACTION\_FRAME


OID\_WDI\_TASK\_P2P\_SEND\_REQUEST\_ACTION\_FRAME is issued to the device to send a Wi-Fi Direct Public Action Frame Request.

| Object | Abort capable                                           | Default priority (host driver policy) | Normal execution time (seconds) |
|--------|---------------------------------------------------------|---------------------------------------|---------------------------------|
| Port   | Yes. The port must be in a clean state after the abort. | 3                                     | 5                               |

 

This command is different than [OID\_WDI\_TASK\_P2P\_SEND\_RESPONSE\_ACTION\_FRAME](oid-wdi-task-p2p-send-response-action-frame.md), which is a significantly more time-sensitive operation.

When the device receives an acknowledgment for a request frame, it shall dwell on the same channel for 100ms and indicate any Wi-Fi Direct Public Action Frames it receives to the host.

While the maximum timeout has not expired, the device shall retry sending the Wi-Fi Direct Public Action frame to the remote device on the remote device’s listen channel.

The task is complete either when the local device receives an acknowledgment from the remote device for the action frame that was sent, the timeout expires, or the host aborts the operation. The device may indicate task completion after the same-channel dwell time has expired.

The host may decide to abort this operation and continue/retry the Wi-Fi Direct action frame exchange, so it is important that the device is able to abort this operation quickly.

## Validation

For miniport drivers that support WDI version 1.1.8 and later, additional validation of the P2P IEs on outgoing P2P Action Frames has been added. This validation addresses a common problem in which the **Configuration Timeout** attribute of the P2P IE has not been converted form units of milliseconds, as provided to the LE in OID_WDI_TASK_P2P_SEND_REQUEST_ACTION_FRAME and [OID_WDI_TASK_P2P_SEND_RESPONSE_ACTION_FRAME](oid-wdi-task-p2p-send-response-action-frame.md), to units of tens of milliseconds, which is the IE format.

The Wi-Fi Direct and Wi-Fi Direct Services HLK tests will fail for drivers supporting WDI version 1.1.8 and later if the **Configuration Timeout** attribute of the P2P IE is not encoded correctly on an outgoing action frame. For WDI versions 1.1.7 and earlier, the tests will print a warning to the test output.

The WDI interface itself is unchanged and continues to use units of milliseconds just as it did in versions 1.1.7 and earlier.

## Task parameters


<table>
<colgroup>
<col width="25%" />
<col width="25%" />
<col width="25%" />
<col width="25%" />
</colgroup>
<thead>
<tr class="header">
<th>TLV</th>
<th>Multiple TLV instances allowed</th>
<th>Optional</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><a href="/windows-hardware/drivers/network/wdi-tlv-p2p-send-action-request-frame-parameters" data-raw-source="[&lt;strong&gt;WDI_TLV_P2P_SEND_ACTION_ REQUEST_FRAME_PARAMETERS&lt;/strong&gt;](./wdi-tlv-p2p-send-action-request-frame-parameters.md)"><strong>WDI_TLV_P2P_SEND_ACTION_ REQUEST_FRAME_PARAMETERS</strong></a></td>
<td></td>
<td></td>
<td>Parameters such as action frame type, device address of target peer adapter, and dialog token.</td>
</tr>
<tr class="even">
<td><a href="/windows-hardware/drivers/network/wdi-tlv-p2p-go-negotiation-request-info" data-raw-source="[&lt;strong&gt;WDI_TLV_P2P_GO_ NEGOTIATION_REQUEST_INFO&lt;/strong&gt;](./wdi-tlv-p2p-go-negotiation-request-info.md)"><strong>WDI_TLV_P2P_GO_ NEGOTIATION_REQUEST_INFO</strong></a></td>
<td></td>
<td>X</td>
<td>GO Negotiation Request Parameters. THe port shall only examine this structure if wfdRequestFrameType is a GO Negotiation request.</td>
</tr>
<tr class="odd">
<td><a href="/windows-hardware/drivers/network/wdi-tlv-p2p-invitation-request-info" data-raw-source="[&lt;strong&gt;WDI_TLV_P2P_INVITATION_REQUEST_INFO&lt;/strong&gt;](./wdi-tlv-p2p-invitation-request-info.md)"><strong>WDI_TLV_P2P_INVITATION_REQUEST_INFO</strong></a></td>
<td></td>
<td>X</td>
<td>Invitation Request Parameters. The port shall only examine this structure if wfdRequestFrameType is an Invitation request.</td>
</tr>
<tr class="even">
<td><a href="/windows-hardware/drivers/network/wdi-tlv-p2p-provision-discovery-request-info" data-raw-source="[&lt;strong&gt;WDI_TLV_P2P_PROVISION_ DISCOVERY_REQUEST_INFO&lt;/strong&gt;](./wdi-tlv-p2p-provision-discovery-request-info.md)"><strong>WDI_TLV_P2P_PROVISION_ DISCOVERY_REQUEST_INFO</strong></a></td>
<td></td>
<td>X</td>
<td>Provision Discovery Request Parameters. The port shall only examine this structure if wfdRequestFrameType is an Provision Discovery request.</td>
</tr>
<tr class="odd">
<td><a href="/windows-hardware/drivers/network/wdi-tlv-bss-entry" data-raw-source="[&lt;strong&gt;WDI_TLV_BSS_ENTRY&lt;/strong&gt;](./wdi-tlv-bss-entry.md)"><strong>WDI_TLV_BSS_ENTRY</strong></a></td>
<td></td>
<td></td>
<td><p>The device discovery entry as returned by the Wi-Fi Direct Discovery task from the port.</p>
<p>This is provided so the port does not need to remember its discovery database in order to send Wi-Fi Direct Action Frame Requests to remote Wi-Fi Direct devices without requiring a discovery.</p></td>
</tr>
<tr class="even">
<td><a href="/windows-hardware/drivers/network/wdi-tlv-vendor-specific-ie" data-raw-source="[&lt;strong&gt;WDI_TLV_VENDOR_SPECIFIC_IE&lt;/strong&gt;](./wdi-tlv-vendor-specific-ie.md)"><strong>WDI_TLV_VENDOR_SPECIFIC_IE</strong></a></td>
<td></td>
<td>X</td>
<td>One or more IEs that must be included in the frame sent by the port.</td>
</tr>
</tbody>
</table>

 

## Task completion indication


[NDIS\_STATUS\_WDI\_INDICATION\_P2P\_SEND\_REQUEST\_ACTION\_FRAME\_COMPLETE](ndis-status-wdi-indication-p2p-send-request-action-frame-complete.md)

## Requirements

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<tbody>
<tr class="odd">
<td><p>Minimum supported client</p></td>
<td><p>Windows 10</p></td>
</tr>
<tr class="even">
<td><p>Minimum supported server</p></td>
<td><p>Windows Server 2016</p></td>
</tr>
<tr class="odd">
<td><p>Header</p></td>
<td>Dot11wdi.h</td>
</tr>
</tbody>
</table>

