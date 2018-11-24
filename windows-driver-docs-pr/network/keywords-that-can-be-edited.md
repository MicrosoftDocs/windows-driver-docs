---
title: Keywords That Can Be Edited
description: Keywords That Can Be Edited
ms.assetid: 88c3a285-941a-4c91-9e61-25c445d07344
keywords:
- installation keywords WDK networking , editing
- editing installation keywords
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Keywords That Can Be Edited





NDIS 6.0 and later versions of NDIS provide standardized keywords that can be edited for miniport drivers of network devices. These standardized keywords are associated with numeric or text values that you can edit in the user interface.

The following example shows an INF file definition for a keyword that can be edited.

```INF
HKR, Ndi\params\<SubkeyName>,ParamDesc, 0, "<ParamDesc>"
HKR, Ndi\params\<SubkeyName>,Type, 0, "int"
HKR, Ndi\params\<SubkeyName>,Default, 0, "<IHV defined>"
HKR, Ndi\params\<SubkeyName>,Optional, 0, "0"
HKR, Ndi\params\<SubkeyName>,Min, 0, "0"
HKR, Ndi\params\<SubkeyName>,Max, 0, "<IHV defined>"
```

The standard keywords that can be edited are:

<a href="" id="---------jumbopacket"></a> \*JumboPacket  
The size, in bytes, of the largest supported Jumbo Packet (an Ethernet frame that is greater than 1514 bytes) that the hardware can support. This is also known as a Jumbo Frame. *\*JumboPacket*'s range of values and maximum value are IHV-defined. Some vendors permit any value between their defined minimum and maximum, while others define an enumeration of supported values. For more info, check with your IHV.

<a href="" id="---------receivebuffers"></a> \*ReceiveBuffers  
The number of receive descriptors used by the miniport adapter. The miniport driver can choose any default value that is appropriate for performance-tuning. Note that if the value is too small, the miniport adapter may run out of receive buffers under heavy load. If the value is too large, system resources are wasted.

<a href="" id="---------transmitbuffers"></a> \*TransmitBuffers  
The size, in bytes, of the transmit buffers that the hardware can support. This size is hardware-dependent and can include data buffers, buffer descriptors, and so on. Hardware vendors can assign any value that is appropriate for their purposes.

<a href="" id="--------networkaddress"></a> NetworkAddress  
The network address of the device. The format for a MAC address is: XX-XX-XX-XX-XX-XX. The hyphens (-) are optional.

The columns in the table at the end of this topic describe the following attributes for keywords that can be edited:

<a href="" id="subkeyname"></a>SubkeyName  
The name of the keyword that you must specify in the INF file and that appears in the registry.

<a href="" id="paramdesc"></a>ParamDesc  
The display text that is associated with SubkeyName.

<a href="" id="type"></a>Type  
The type of value that can be edited. The value can be either numeric (**Int**) or text that can be edited (**Edit**).

<a href="" id="default-value"></a>Default value  
The default value for the integer or text. &lt;IHV defined&gt; indicates that the value is associated with the particular independent hardware vendor (IHV) requirements.

<a href="" id="min"></a>Min  
The minimum value that is allowed for an integer. &lt;IHV defined&gt; indicates that the minimum value is associated with the particular IHV requirements.

<a href="" id="max"></a>Max  
The maximum value that is allowed for an integer. &lt;IHV defined&gt; indicates that the minimum value is associated with the particular IHV requirements.

The following table lists all of the keywords and describes the values that a driver must use for the preceding attributes. For more information about a keyword, search for the keyword in the WDK documentation.

<table style="width:100%;">
<colgroup>
<col width="16%" />
<col width="16%" />
<col width="16%" />
<col width="16%" />
<col width="16%" />
<col width="16%" />
</colgroup>
<thead>
<tr class="header">
<th align="left">SubkeyName</th>
<th align="left">ParamDesc</th>
<th align="left">Type</th>
<th align="left">Default value</th>
<th align="left">Min</th>
<th align="left">Max</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td align="left"><p><em>JumboPacket</p></td>
<td align="left"><p>Jumbo Packet</p></td>
<td align="left"><p>Int</p></td>
<td align="left"><p>1514</p></td>
<td align="left"><p>1514</p></td>
<td align="left"><p>&lt;IHV defined&gt;</p></td>
</tr>
<tr class="even">
<td align="left"><p></em>ReceiveBuffers</p></td>
<td align="left"><p>Receive Buffers</p></td>
<td align="left"><p>Int</p></td>
<td align="left"><p>&lt;IHV defined&gt;</p></td>
<td align="left"><p>1</p></td>
<td align="left"><p>&lt;IHV defined&gt;</p></td>
</tr>
<tr class="odd">
<td align="left"><p>*TransmitBuffers</p></td>
<td align="left"><p>Transmit Buffers</p></td>
<td align="left"><p>Int</p></td>
<td align="left"><p>&lt;IHV defined&gt;</p></td>
<td align="left"><p>0</p></td>
<td align="left"><p>&lt;IHV defined&gt;</p></td>
</tr>
<tr class="even">
<td align="left"><p>NetworkAddress</p></td>
<td align="left"><p>Network Address</p></td>
<td align="left"><p>Edit</p></td>
<td align="left"><p>N/A</p></td>
<td align="left"><p>N/A</p></td>
<td align="left"><p>N/A</p></td>
</tr>
</tbody>
</table>

 

 

 





