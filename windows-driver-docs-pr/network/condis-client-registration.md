---
title: CoNDIS Client Registration
description: CoNDIS Client Registration
keywords:
- client registration WDK CoNDIS
- registering entry points
- entry points WDK networking
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# CoNDIS Client Registration





CoNDIS clients initialize like other protocol drivers and also must register additional CoNDIS entry points. For general information about protocol driver initialization, see [Initializing a Protocol Driver](initializing-a-protocol-driver.md).

To register CoNDIS entry points for *ProtocolXxx* functions, CoNDIS clients call the [**NdisSetOptionalHandlers**](/windows-hardware/drivers/ddi/ndis/nf-ndis-ndissetoptionalhandlers) function from the [*ProtocolSetOptions*](/windows-hardware/drivers/ddi/ndis/nc-ndis-set_options) function. In *ProtocolSetOptions*, all CoNDIS protocol drivers initialize an [**NDIS\_PROTOCOL\_CO\_CHARACTERISTICS**](/windows-hardware/drivers/ddi/ndis/ns-ndis-_ndis_protocol_co_characteristics) structure and pass it at the *OptionalHandlers* parameter of **NdisSetOptionalHandlers**.

To specify entry points for a CoNDIS client, a protocol driver initializes an [**NDIS\_CO\_CLIENT\_OPTIONAL\_HANDLERS**](/windows-hardware/drivers/ddi/ndis/ns-ndis-_ndis_co_client_optional_handlers) structure and passes it at the *OptionalHandlers* parameter of **NdisSetOptionalHandlers**.

For more information about configuring optional protocol driver services, see [Configuring Optional Protocol Driver Services](configuring-optional-protocol-driver-services.md).

 

