---
title: ISCSI\_CONNECTION\_STATE\_TYPE\_QUALIFIERS
description: ISCSI\_CONNECTION\_STATE\_TYPE\_QUALIFIERS
ms.assetid: 53242205-4fd3-471d-abe2-35474491b29d
ms.localizationpriority: medium
ms.date: 10/17/2018
---

# ISCSI\_CONNECTION\_STATE\_TYPE\_QUALIFIERS


## <span id="ddk_iscsi_connection_state_type_qualifiers_kr"></span><span id="DDK_ISCSI_CONNECTION_STATE_TYPE_QUALIFIERS_KR"></span>


The ISCSI\_CONNECTION\_STATE\_TYPE\_QUALIFIERS WMI property qualifier corresponds to a group of values that represent the connection state.

The following table describes the ISCSI\_CONNECTION\_STATE\_TYPE\_QUALIFIERS values.

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<thead>
<tr class="header">
<th align="left">Connection state value</th>
<th align="left">Meaning</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td align="left"><p>0</p></td>
<td align="left"><p>The connection is in the logon request phase. The connection has been established, but the target still has not sent a valid logon response with the final bit set.</p></td>
</tr>
<tr class="even">
<td align="left"><p>1</p></td>
<td align="left"><p>The target has sent a valid logon response with the final bit set, the connection is in the full feature phase, and the initiator can send SCSI commands and data to targets.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>2</p></td>
<td align="left"><p>The initiator has sent a valid logoff command, but the connection has not yet been closed.</p></td>
</tr>
</tbody>
</table>

 

 

 





