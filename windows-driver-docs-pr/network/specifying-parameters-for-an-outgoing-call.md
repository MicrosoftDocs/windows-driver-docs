---
title: Specifying Parameters for an Outgoing Call
description: Specifying Parameters for an Outgoing Call
keywords:
- CoNDIS WAN drivers WDK networking , outgoing calls
- telephonic services WDK WAN , outgoing calls
- CoNDIS TAPI WDK networking , outgoing calls
- voice streaming WDK networing , outgoing calls
- outgoing calls WDK CoNDIS WAN
- calls WDK CoNDIS WAN
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Specifying Parameters for an Outgoing Call





When making an outgoing call, a call manager or MCM that supports voice streaming must supply the following values in the [**CO\_CALL\_MANAGER\_PARAMETERS**](/previous-versions/windows/hardware/network/ff545381(v=vs.85)) structure:

-   Maximum transmit SDU size (CallMgrParameters-&gt;Transmit.MaxSduSize)

-   Maximum receive SDU size (CallMgrParameters-&gt;Receive.MaxSduSize)

A call manager or MCM that supports an address family other than CO\_ADDRESS\_FAMILY\_TAPI\_PROXY fills in these values when translating TAPI call parameters to NDIS call parameters in response to a query of [OID\_CO\_TAPI\_TRANSLATE\_TAPI\_CALLPARAMS](./oid-co-tapi-translate-tapi-callparams.md).

A call manager or MCM that supports the CO\_ADDRESS\_FAMILY\_TAPI\_PROXY family writes these values to the CO\_CALL\_MANAGER\_PARAMETERS structure in the context of its [**ProtocolCmMakeCall**](/windows-hardware/drivers/ddi/ndis/nc-ndis-protocol_cm_make_call) function. Note that the maximum SDU sizes passed to the *ProtocolCmMakeCall* function are incorrect. The *ProtocolCmMakeCall* function must overwrite the incorrect values with correct values.

 

