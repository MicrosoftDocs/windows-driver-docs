---
title: Indicating Receive Network Data to Higher Level Drivers
description: Indicating Receive Network Data to Higher Level Drivers
ms.assetid: 27272427-86bc-4fd3-bd2f-12d94273fcd4
keywords:
- intermediate drivers WDK networking , receive operations
- NDIS intermediate drivers WDK , receive operations
ms.author: windows-driver-content
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Indicating Receive Network Data to Higher Level Drivers


## <a href="" id="ddk-indicating-receive-packets-to-higher-level-drivers-ng"></a>


A connectionless intermediate driver indicates receive network data to the next higher driver by calling the [**NdisMIndicateReceiveNetBufferLists**](https://msdn.microsoft.com/library/windows/hardware/ff563598) function. A connection-oriented intermediate driver indicates receive network data to the next higher driver by calling the [**NdisMCoIndicateReceiveNetBufferLists**](https://msdn.microsoft.com/library/windows/hardware/ff563561) function.

Before indicating the receive network data, the driver processes the data, perhaps converting it to the format expected by a higher-level driver, and if required, copying relevant data into MDLs that are associated with an intermediate-driver-allocated [**NET\_BUFFER**](https://msdn.microsoft.com/library/windows/hardware/ff568376) structure.

 

 





