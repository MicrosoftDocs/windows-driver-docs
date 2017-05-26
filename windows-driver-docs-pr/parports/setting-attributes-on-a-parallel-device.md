---
title: Setting Attributes on a Parallel Device
author: windows-driver-content
description: Setting Attributes on a Parallel Device
ms.assetid: 10df9a1b-99ec-46b1-b515-10fb20fe2aed
keywords:
- parallel devices WDK , attributes
- attributes WDK parallel devices
ms.author: windowsdriverdev
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Setting Attributes on a Parallel Device


## <a href="" id="ddk-setting-attributes-on-a-parallel-device-kg"></a>


A client uses following device control requests to set the indicated operations of a parallel device:

-   [**IOCTL\_PAR\_SET\_INFORMATION**](https://msdn.microsoft.com/library/windows/hardware/ff544103) initializes a parallel device.

-   [**IOCTL\_SERIAL\_SET\_TIMEOUTS**](https://msdn.microsoft.com/library/windows/hardware/ff544126) sets time outs for a parallel device.

-   [**IOCTL\_PAR\_SET\_READ\_ADDRESS**](https://msdn.microsoft.com/library/windows/hardware/ff544107) sets an ECP or EPP read address (channel) for a parallel device.

-   [**IOCTL\_PAR\_SET\_WRITE\_ADDRESS**](https://msdn.microsoft.com/library/windows/hardware/ff544115) sets an ECP or EPP write address (channel) for a parallel device.

 

 


--------------------


