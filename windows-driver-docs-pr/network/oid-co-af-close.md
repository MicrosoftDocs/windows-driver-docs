---
title: OID_CO_AF_CLOSE
author: windows-driver-content
description: This topic describes the OID_CO_AF_CLOSE object identifier (OID).
ms.assetid: 451ab9d5-e118-41c9-8d16-02d75a25a1d4
keywords:
- OID_CO_AF_CLOSE
ms.author: windowsdriverdev
ms.date: 11/03/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# OID_CO_AF_CLOSE

The OID_CO_AF_CLOSE OID is sent by a call manager that must unbind itself from an underlying miniport driver. Before unbinding itself from the miniport driver, the call manager sends this OID to each client that has an address family open with the call manager. In response, the client should do the following:

1. If the client has any active multipoint connections, call [NdisClDropParty](https://msdn.microsoft.com/library/windows/hardware/ff561629) as many times as necessary until only a single party remains active on each multipoint VC

2. Call [NdisClCloseCall](https://msdn.microsoft.com/library/windows/hardware/ff561627) as many times as necessary to close all calls still open with the call manager

3. Call [NdisClDeregisterSap](https://msdn.microsoft.com/library/windows/hardware/ff561628) as many times as necessary to deregister all SAPs that the client has registered with the call manager

4. Call [NdisClCloseAddressFamily](https://msdn.microsoft.com/library/windows/hardware/ff561626) to close the address family referenced by NdisAfHandle in the request that contained OID_CO_AF_CLOSE

## Requirements

| | |
| --- | --- |
| Version | Windows Vista and later |
| Header | Ntddndis.h (include Ndis.h) |

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bnetvista\netvista%5D:%20OID_WWAN_DEVICE_CAPS_EX%20%20RELEASE:%20%288/8/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")