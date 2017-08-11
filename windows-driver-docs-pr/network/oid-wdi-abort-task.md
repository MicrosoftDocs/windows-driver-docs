---
title: OID_WDI_ABORT_TASK
author: windows-driver-content
description: OID_WDI_ABORT_TASK is a property that is sent down to cancel a specific pending task.
ms.assetid: 0E454DC9-1CED-497F-90A8-7065883BB945
ms.author: windowsdriverdev 
ms.date: 07/18/2017 
ms.topic: article 
ms.prod: windows-hardware 
ms.technology: windows-devices 
keywords:
 - OID_WDI_ABORT_TASK Network Drivers Starting with Windows Vista
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

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bnetvista\netvista%5D:%20OID_WDI_ABORT_TASK%20%20RELEASE:%20%286/30/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


