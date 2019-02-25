---
title: Splitting Frames at the UDP Payload
description: Splitting Frames at the UDP Payload
ms.assetid: 10116077-89d2-4d07-9807-46b6281e9851
keywords:
- Ethernet frame splitting WDK networking , UDP payload
- UDP payload WDK header-data split
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Splitting Frames at the UDP Payload





NDIS miniport adapters that support header-data split must support splitting frames at the upper-layer-protocol header for UDP frames. However, the NIC must first try to split the frame at the beginning of UDP payload.

The NIC might not be able to split a UDP frame if the resulting header buffer has a greater length than the maximum header size. For more information about splitting frames when the maximum header size is exceeded, see [Allocating the Header Buffer](allocating-the-header-buffer.md).

If the NIC cannot split the frame at the UDP payload, the NIC should split the frame at the beginning of the upper-layer-protocol header or should not split the frame. For more information about splitting frames at the beginning of the upper-layer-protocol header, see [Splitting Frames at the Beginning of the Upper-Layer-Protocol Headers](splitting-frames-at-the-beginning-of-the-upper-layer-protocol-headers.md).

If the header-data split provider splits the frame at the UDP payload, the indicated [**NET\_BUFFER\_LIST**](https://msdn.microsoft.com/library/windows/hardware/ff568388) structures must have the NDIS\_NBL\_FLAGS\_IS\_UDP and NDIS\_NBL\_FLAGS\_SPLIT\_AT\_UPPER\_LAYER\_PROTOCOL\_PAYLOAD flags set in the **NblFlags** member. For more information about setting header-data split NET\_BUFFER\_LIST flags, see [Setting NET\_BUFFER\_LIST Information](setting-net-buffer-list-information.md).

 

 





