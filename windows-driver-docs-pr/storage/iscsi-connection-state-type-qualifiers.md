---
title: ISCSI\_CONNECTION\_STATE\_TYPE\_QUALIFIERS
description: ISCSI\_CONNECTION\_STATE\_TYPE\_QUALIFIERS
ms.assetid: 53242205-4fd3-471d-abe2-35474491b29d
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

 

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[storage\storage]:%20ISCSI_CONNECTION_STATE_TYPE_QUALIFIERS%20%20RELEASE:%20%281/11/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




