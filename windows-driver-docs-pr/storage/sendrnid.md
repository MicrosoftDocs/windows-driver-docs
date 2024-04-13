---
title: SendRNID Function
description: The SendRNID WMI method sends a request node identification data (RNID) command to the indicated port.
keywords: ["SendRNID function Storage Devices"]
topic_type:
- apiref
ms.topic: reference
api_name:
- SendRNID
api_location:
- Hbaapi.lib
- Hbaapi.dll
api_type:
- LibDef
ms.date: 10/17/2018
---

# SendRNID function


The **SendRNID** WMI method sends a request node identification data (RNID) command to the indicated port.

## Syntax

```ManagedCPlusPlus
void SendRNID(
   [in, HBAType("HBA_WWN")] uint8                                                          wwn[8],
   [in, HBAType("HBA_WWNTYPE"), Values{"NODE_WWN", "PORT_WWN"}, ValueMap{"0", "1"}] uint32 wwntype,
   [out, HBA_STATUS_QUALIFIERS] HBA_STATUS                                                 HBAStatus,
   [out] uint32                                                                            ResponseBufferCount,
   [out, WmiSizeIs("ResponseBufferCount")] uint8                                           ResponseBuffer[]
);
```

## Parameters

*wwn*   
A worldwide name for the port to which the RNID command is sent. This information is delivered to the miniport driver in the **wwn** member of a [**SendRNID\_IN**](/windows-hardware/drivers/ddi/hbapiwmi/ns-hbapiwmi-_sendrnid_in) structure.

*wwntype*   
Deprecated. Do not use.

*HBAStatus*   
On return, contains the status of the operation. For a list of allowed values and their descriptions, see [HBA\_STATUS](hba-status.md). The miniport driver returns this information in the **HBAStatus** member of a [**SendRNID\_OUT**](/windows-hardware/drivers/ddi/hbapiwmi/ns-hbapiwmi-_sendrnid_out) structure.

*ResponseBufferCount*   
The size in bytes of the results of the RNID command. The miniport driver returns this information in the **ResponseBufferCount** member of a [**SendRNID\_OUT**](/windows-hardware/drivers/ddi/hbapiwmi/ns-hbapiwmi-_sendrnid_out) structure.

*ResponseBuffer*   
The results of the RNID command. The miniport driver returns this information in the **ResponseBuffer** member of a [**SendRNID\_OUT**](/windows-hardware/drivers/ddi/hbapiwmi/ns-hbapiwmi-_sendrnid_out) structure.

## Return value

Not applicable to WMI methods.

## Remarks

This WMI method belongs to the [MSFC\_HBAAdapterMethods WMI Class](msfc-hbaadaptermethods-wmi-class.md).

## Requirements

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<tbody>
<tr class="odd">
<td align="left"><p>Target platform</p></td>
<td align="left">Desktop</td>
</tr>
<tr class="even">
<td align="left"><p>Header</p></td>
<td align="left">Hbapiwmi.h (include Hbapiwmi.h, Hbaapi.h, or Hbaapi.h)</td>
</tr>
<tr class="odd">
<td align="left"><p>Library</p></td>
<td align="left">Hbaapi.lib</td>
</tr>
</tbody>
</table>

## <span id="see_also"></span>See also


[HBA\_STATUS](hba-status.md)

[**SendRNID\_IN**](/windows-hardware/drivers/ddi/hbapiwmi/ns-hbapiwmi-_sendrnid_in)

[**SendRNID\_OUT**](/windows-hardware/drivers/ddi/hbapiwmi/ns-hbapiwmi-_sendrnid_out)

 

