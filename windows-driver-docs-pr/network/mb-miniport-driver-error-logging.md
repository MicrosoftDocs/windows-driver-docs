---
title: MB Miniport driver Error Logging
description: MB Miniport driver Error Logging
ms.assetid: 57f83d03-29e5-4a20-8c0c-2d00954e7ccb
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# MB Miniport driver Error Logging


MB miniport drivers should perform the following checks in their [*MiniportInitializeEx*](https://msdn.microsoft.com/library/windows/hardware/ff559389) function, such as:

-   The presence of the correct device firmware version required to support the MB driver model.

-   An available COM port to communicate with the device.

-   No resource conflicts.

If a miniport driver fails to obtain resources it requires, it should return NDIS\_STATUS\_RESOURCES from its MiniportInitializeEx function. Miniport drivers should call [**NdisWriteErrorLogEntry**](https://msdn.microsoft.com/library/windows/hardware/ff564663) to log the details of failure to the Windows Event Log.

Miniport drivers should specify the error code in the first element of the last parameter in the call to NdisWriteErrorLogEntry (a variable-sized array of ULONGs) according to the information in the following table.

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<thead>
<tr class="header">
<th align="left">Error code</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td align="left"><p>WWAN_ERROR_UNSUPPORTED_FIRMWARE</p></td>
<td align="left"><p>The device is running an unsupported firmware version.</p></td>
</tr>
<tr class="even">
<td align="left"><p>WWAN_ERROR_COM_PORT_CONFLICT</p></td>
<td align="left"><p>Unable to open COM port for communicating with the device.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>WWAN_ERROR_RESOURCE_CONFLICT_OTHER</p></td>
<td align="left"><p>Any other resource conflict.</p></td>
</tr>
</tbody>
</table>

 

Miniport drivers can put other values in the remainder of the elements of variable-sized array.

 

 





