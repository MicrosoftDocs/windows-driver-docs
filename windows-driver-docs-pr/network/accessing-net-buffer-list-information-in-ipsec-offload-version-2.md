---
title: Accessing NET_BUFFER_LIST information in IPsec Offload Version 2
description: Accessing NET_BUFFER_LIST Information in IPsec Offload Version 2
ms.assetid: 0c27b594-2c61-4459-96df-1d7445100bc5
keywords:
- IPsecOV2 WDK TCP/IP transport , NET_BUFFER_LIST information
- NET_BUFFER_LIST
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Accessing NET\_BUFFER\_LIST Information in IPsec Offload Version 2

\[The IPsec Task Offload feature is deprecated and should not be used.\]




NDIS provides out-of-band (OOB) data in the **NetBufferListInfo** member of the [**NET\_BUFFER\_LIST**](https://msdn.microsoft.com/library/windows/hardware/ff568388) structure, which specifies a linked list of [**NET\_BUFFER**](https://msdn.microsoft.com/library/windows/hardware/ff568376) structures. The **NetBufferListInfo** member is an array of values that contain information that is common to all of the NET\_BUFFER structures in the list.

Use the following identifiers with the [**NET\_BUFFER\_LIST\_INFO**](https://msdn.microsoft.com/library/windows/hardware/ff568401) macro to set and get the IPsec offload version 2 (IPsecOV2) OOB data in the **NetBufferListInfo** array:

<a href="" id="ipsecoffloadv2netbufferlistinfo"></a>**IPsecOffloadV2NetBufferListInfo**  
Specifies IPsecOV2 information that is used in offloading IPsec tasks from the TCP/IP protocol to a NIC. When you specify **IPsecOffloadV2NetBufferListInfo**, NET\_BUFFER\_LIST\_INFO returns an [**NDIS\_IPSEC\_OFFLOAD\_V2\_NET\_BUFFER\_LIST\_INFO**](https://msdn.microsoft.com/library/windows/hardware/ff565818) structure.

<a href="" id="ipsecoffloadv2tunnelnetbufferlistinfo"></a>**IPsecOffloadV2TunnelNetBufferListInfo**  
Specifies IPsecOV2 tunnel information that is used in offloading IPsec tasks from the TCP/IP protocol to a NIC. When you specify **IPsecOffloadV2TunnelNetBufferListInfo**, NET\_BUFFER\_LIST\_INFO returns an [**NDIS\_IPSEC\_OFFLOAD\_V2\_TUNNEL\_NET\_BUFFER\_LIST\_INFO**](https://msdn.microsoft.com/library/windows/hardware/ff565843) structure.

<a href="" id="ipsecoffloadv2headernetbufferlistinfo"></a>**IPsecOffloadV2HeaderNetBufferListInfo**  
Specifies the header offsets for IPsec headers in the [**NET\_BUFFER\_LIST**](https://msdn.microsoft.com/library/windows/hardware/ff568388) and the values for the next header and pad length. When you specify **IPsecOffloadV2HeaderNetBufferListInfo**, NET\_BUFFER\_LIST\_INFO returns an [**NDIS\_IPSEC\_OFFLOAD\_V2\_HEADER\_NET\_BUFFER\_LIST\_INFO**](https://msdn.microsoft.com/library/windows/hardware/ff565812) structure.

 

 





