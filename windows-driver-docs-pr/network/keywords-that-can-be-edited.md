---
title: Keywords That Can Be Edited
description: Keywords That Can Be Edited
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

**\*JumboPacket**
The size, in bytes, of the largest supported Jumbo Packet (an Ethernet frame that is greater than 1514 bytes) that the hardware can support. This is also known as a Jumbo Frame. *\*JumboPacket*'s range of values and maximum value are IHV-defined. For more info, check with your IHV.

**\*ReceiveBuffers**  
The number of receive descriptors used by the miniport adapter. The miniport driver can choose any default value that is appropriate for performance-tuning. Note that if the value is too small, the miniport adapter may run out of receive buffers under heavy load. If the value is too large, system resources are wasted.

**\*TransmitBuffers**  
The size, in bytes, of the transmit buffers that the hardware can support. This size is hardware-dependent and can include data buffers, buffer descriptors, and so on. Hardware vendors can assign any value that is appropriate for their purposes.

**\*NetworkAddress**  
The network address of the device. The format for a MAC address is: XX-XX-XX-XX-XX-XX. The hyphens (-) are optional.

The columns in the table at the end of this topic describe the following attributes for keywords that can be edited:

SubkeyName  
The name of the keyword that you must specify in the INF file and that appears in the registry.

ParamDesc  
The display text that is associated with SubkeyName.

Type  
The type of value that can be edited. The value can be either numeric (**Int**) or text that can be edited (**Edit**).

Default value  
The default value for the integer or text. &lt;IHV defined&gt; indicates that the value is associated with the particular independent hardware vendor (IHV) requirements.

Min  
The minimum value that is allowed for an integer. &lt;IHV defined&gt; indicates that the minimum value is associated with the particular IHV requirements.

Max  
The maximum value that is allowed for an integer. &lt;IHV defined&gt; indicates that the minimum value is associated with the particular IHV requirements.

The following table lists all of the keywords and describes the values that a driver must use for the preceding attributes. For more information about a keyword, search for the keyword in the WDK documentation.

|SubkeyName|ParamDesc|Type|Default value|Min|Max|
|--- |--- |--- |--- |--- |--- |
|**\*JumboPacket**|Jumbo Packet|Int|1514|1514||
|**\*ReceiveBuffers**|Receive Buffers|Int||1||
|**\*TransmitBuffers**|Transmit Buffers|Int||0||
|**\*NetworkAddress**|Network Address|Edit|N/A|N/A|N/A|

 

 

 





