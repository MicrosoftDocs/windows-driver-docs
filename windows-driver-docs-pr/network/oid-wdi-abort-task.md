---
title: OID_WDI_ABORT_TASK
description: OID_WDI_ABORT_TASK is a property that is sent down to cancel a specific pending task.
ms.assetid: 0E454DC9-1CED-497F-90A8-7065883BB945
ms.date: 07/18/2017
keywords:
 - OID_WDI_ABORT_TASK Network Drivers Starting with Windows Vista
ms.localizationpriority: medium
---

# OID\_WDI\_ABORT\_TASK


OID\_WDI\_ABORT\_TASK is a property that is sent down to cancel a specific pending task.

| Scope | Set serialized with task | Normal execution time (seconds) |
|-------|--------------------------|---------------------------------|
| Port  | No                       | 1                               |

 

This command follows property semantics. It should be treated as a signal, should be handled as quickly as possible, and should be completed independently of task completion. The IHV component must then attempt to complete the pending task as soon as possible.

## Command parameters


| TLV                                                                    | Multiple TLV instances allowed | Optional | Description                                          |
|------------------------------------------------------------------------|--------------------------------|----------|------------------------------------------------------|
| [**WDI\_TLV\_CANCEL\_PARAMETERS**](https://msdn.microsoft.com/library/windows/hardware/dn926163) |                                |          | Information for the command that is being cancelled. |

 

## Command result


Contains a status of NDIS\_STATUS\_SUCCESS. There is no additional payload.
## Examples


Original input task command:

Field
Subfield
Type
Value
NDIS\_OID\_REQUEST
Oid
NDIS\_OID
OID(WDI\_TASK\_SCAN)
InputBufferLength
UINT32
0x210 (example)
InformationBuffer
PVOID
Pointer to memory block containing WDI\_MESSAGE\_HEADER + TLV payload
WDI\_MESSAGE\_HEADER
PortId
UINT16
0x0001 (example)
Reserved
UINT16
N/A
WiFiStatus
NDIS\_STATUS
N/A
TransactionId
UINT32
0x1111 (example)
IhvSpecificId
UINT32
N/A
TLV Payload
TLV Payload
Various
Payload data
 

Abort task input command (with message header):

Field
Subfield
Type
Value
NDIS\_OID\_REQUEST
Oid
NDIS\_OID
OID(WDI\_ABORT\_TASK)
InputBufferLength
UINT32
sizeof(WDI\_MESSAGE\_HEADER) + sizeof(WDI\_TLV\_CANCEL\_PARAMETERS)
InformationBuffer
PVOID
Pointer to memory block containing WDI\_MESSAGE\_HEADER + TLV payload
WDI\_MESSAGE\_HEADER
PortId
UINT16
0x0001 (example)
Reserved
UINT16
N/A
WiFiStatus
NDIS\_STATUS
N/A
TransactionId
UINT32
0x2222 (example)
IhvSpecificId
UINT32
0
WDI\_TLV\_CANCEL\_PARAMETERS
OriginalTaskOid
NDIS\_OID
OID(WDI\_TASK\_SCAN)
OriginalPortId
UINT16
0x0001 (example)
OriginalTransactionId
UINT32
0x1111 (example)
 

Abort task command result:

Field
Subfield
Type
Value
NDIS\_OID\_REQUEST
Oid
NDIS\_OID
OID(WDI\_TASK\_SCAN)
OutputBufferLength
UINT32
sizeof(WDI\_MESSAGE\_HEADER)
InformationBuffer
PVOID
Pointer to memory block containing WDI\_MESSAGE\_HEADER
WDI\_MESSAGE\_HEADER
PortId
UINT16
0x0001 (example)
Reserved
UINT16
N/A
WiFiStatus
NDIS\_STATUS
NDIS\_STATUS\_SUCCESS
TransactionId
UINT32
0x2222 (example)
IhvSpecificId
UINT32
N/A
 

Requirements
------------

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

 

 




