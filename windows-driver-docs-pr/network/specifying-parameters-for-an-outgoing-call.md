---
title: Specifying Parameters for an Outgoing Call
description: Specifying Parameters for an Outgoing Call
ms.assetid: 6e11dcd7-33ae-4b9e-8609-1baccec691d5
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





When making an outgoing call, a call manager or MCM that supports voice streaming must supply the following values in the [**CO\_CALL\_MANAGER\_PARAMETERS**](https://msdn.microsoft.com/library/windows/hardware/ff545381) structure:

-   Maximum transmit SDU size (CallMgrParameters-&gt;Transmit.MaxSduSize)

-   Maximum receive SDU size (CallMgrParameters-&gt;Receive.MaxSduSize)

A call manager or MCM that supports an address family other than CO\_ADDRESS\_FAMILY\_TAPI\_PROXY fills in these values when translating TAPI call parameters to NDIS call parameters in response to a query of [OID\_CO\_TAPI\_TRANSLATE\_TAPI\_CALLPARAMS](https://msdn.microsoft.com/library/windows/hardware/ff569100).

A call manager or MCM that supports the CO\_ADDRESS\_FAMILY\_TAPI\_PROXY family writes these values to the CO\_CALL\_MANAGER\_PARAMETERS structure in the context of its [**ProtocolCmMakeCall**](https://msdn.microsoft.com/library/windows/hardware/ff570246) function. Note that the maximum SDU sizes passed to the *ProtocolCmMakeCall* function are incorrect. The *ProtocolCmMakeCall* function must overwrite the incorrect values with correct values.

 

 





