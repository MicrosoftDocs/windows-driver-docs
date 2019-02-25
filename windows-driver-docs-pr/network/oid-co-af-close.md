---
title: OID_CO_AF_CLOSE
description: This topic describes the OID_CO_AF_CLOSE object identifier (OID).
ms.assetid: 451ab9d5-e118-41c9-8d16-02d75a25a1d4
keywords:
- OID_CO_AF_CLOSE
ms.date: 11/03/2017
ms.localizationpriority: medium
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

