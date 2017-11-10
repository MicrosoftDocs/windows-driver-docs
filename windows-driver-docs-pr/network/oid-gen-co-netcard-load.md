---
title: OID_GEN_CO_NETCARD_LOAD
author: windows-driver-content
description: This topic describes the OID_GEN_CO_NETCARD_LOAD object identifier (OID).
ms.assetid: 0fdf9948-6b1a-48c9-87a4-7ecdfd1a8e47
keywords:
- OID_GEN_CO_NETCARD_LOAD
ms.author: windowsdriverdev
ms.date: 11/02/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# OID_GEN_CO_NETCARD_LOAD

> [!NOTE]
> OID_GEN_CO_NETCARD_LOAD is the same as OID_GEN_NETCARD_LOAD.

The OID_GEN_CO_NETCARD_LOAD OID returns the relative load on the transmit system of a connection-oriented miniport driver. The miniport driver derives this number by calculating the difference between the amount of data delivered for transmission from protocols and the amount of data actually sent, as indicated by the packets returned to protocols with [NdisMCoSendComplete](https://msdn.microsoft.com/library/windows/hardware/ff553475). The result is the amount of outstanding transmit data in the miniport driver at any time.

Because this statistic changes at a very high frequency, the miniport driver port should filter it. The simplest filtering method is to maintain a running average of samples of the outstanding transmit data. For example, each time [MiniportCoSendPackets](https://msdn.microsoft.com/library/windows/hardware/ff549426) is called, the miniport driver could add the submitted packet size to a miniport driver-defined variable called *OutstandingBytes*. Each time the miniport driver calls [NdisMCoSendComplete](https://msdn.microsoft.com/library/windows/hardware/ff553475, the miniport driver would then subtract the returned packet size from *OutstandingBytes*. The miniport driver must also maintain a running average, which is the value that the miniport driver should return in response to the OID_GEN_CO_NETCARD_LOAD query. This variable, which could be called *RunningAverage*, must be updated on each *MiniportCoSendPackets*, as follows:

```c++
RunningAverage = [(RunningAverage * C) + (OutstandingBytes * (128 - C))] / 128;
```
In this case, 1 \< *C* \< 128. Larger values of *C* produce smoother filtering.

## Requirements

| | |
| --- | --- |
| Version | Windows Vista and later |
| Header | Ntddndis.h (include Ndis.h) |

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bnetvista\netvista%5D:%20OID_WWAN_DEVICE_CAPS_EX%20%20RELEASE:%20%288/8/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")