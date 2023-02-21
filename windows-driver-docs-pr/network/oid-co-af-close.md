---
title: OID_CO_AF_CLOSE
ms.topic: reference
description: This topic describes the OID_CO_AF_CLOSE object identifier (OID).
keywords:
- OID_CO_AF_CLOSE
ms.date: 11/03/2017
---

# OID_CO_AF_CLOSE

The OID_CO_AF_CLOSE OID is sent by a call manager that must unbind itself from an underlying miniport driver. Before unbinding itself from the miniport driver, the call manager sends this OID to each client that has an address family open with the call manager. In response, the client should do the following:

1. If the client has any active multipoint connections, call [NdisClDropParty](/windows-hardware/drivers/ddi/ndis/nf-ndis-ndiscldropparty) as many times as necessary until only a single party remains active on each multipoint VC

2. Call [NdisClCloseCall](/windows-hardware/drivers/ddi/ndis/nf-ndis-ndisclclosecall) as many times as necessary to close all calls still open with the call manager

3. Call [NdisClDeregisterSap](/windows-hardware/drivers/ddi/ndis/nf-ndis-ndisclderegistersap) as many times as necessary to deregister all SAPs that the client has registered with the call manager

4. Call [NdisClCloseAddressFamily](/windows-hardware/drivers/ddi/ndis/nf-ndis-ndisclcloseaddressfamily) to close the address family referenced by NdisAfHandle in the request that contained OID_CO_AF_CLOSE

## Requirements

**Version**: Windows Vista and later
**Header**: Ntddndis.h (include Ndis.h)
