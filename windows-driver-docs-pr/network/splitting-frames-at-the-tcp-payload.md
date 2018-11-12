---
title: Splitting Frames at the TCP Payload
description: Splitting Frames at the TCP Payload
ms.assetid: 3d7c6f75-4523-4ad3-b15d-53f9d4ee1074
keywords:
- Ethernet frame splitting WDK networking , TCP payload
- TCP payload WDK header-data split
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Splitting Frames at the TCP Payload





NDIS miniport adapters that support header-data split must support splitting frames at the upper-layer-protocol header for TCP frames. However, if the TCP header does not contain any TCP options, the NIC should split the frame at the beginning of the TCP payload.

The NIC might not be able to split a TCP frame if the resulting header buffer has a greater length than the maximum header size. For more information about splitting frames when the maximum header size is exceeded, see [Allocating the Header Buffer](allocating-the-header-buffer.md).

NICs must also support splitting TCP headers with only the timestamp option. That is, the timestamp option is the only TCP option that is mandatory. Otherwise, support for TCP headers with TCP options is optional. If the TCP header of a frame contains an unrecognized TCP option, the NIC must either split the frame at the beginning of TCP header (that is, at the upper-layer-protocol header) or not split the frame.

**Note**  Supporting an IPv4 option, an IPv6 extension header or a TCP option, for the purposes of header-data requirements, implies the ability of the NIC to recognize the element, determine its length, include it in the header MDL and locate its end and the beginning of the next element in the frame.

 

For more information about splitting frames at the beginning of the upper-layer-protocol header, see [Splitting Frames at the Beginning of the Upper-Layer-Protocol Headers](splitting-frames-at-the-beginning-of-the-upper-layer-protocol-headers.md).

If the header-data split provider splits the frame at the TCP payload, the indicated [**NET\_BUFFER\_LIST**](https://msdn.microsoft.com/library/windows/hardware/ff568388) structures must have the NDIS\_NBL\_FLAGS\_IS\_TCP and NDIS\_NBL\_FLAGS\_SPLIT\_AT\_UPPER\_LAYER\_PROTOCOL\_PAYLOAD flags set in the **NblFlags** member. For more information about setting header-data split NET\_BUFFER\_LIST flags, see [Setting NET\_BUFFER\_LIST Information](setting-net-buffer-list-information.md).

 

 





