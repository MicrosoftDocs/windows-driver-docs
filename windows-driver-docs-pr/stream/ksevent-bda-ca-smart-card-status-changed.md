---
title: KSEVENT_BDA_CA_SMART_CARD_STATUS_CHANGED
description: Clients use KSEVENT_BDA_CA_SMART_CARD_STATUS_CHANGED to request notification when status on the smart card reader associated with an ECM map node changes.
keywords: ["KSEVENT_BDA_CA_SMART_CARD_STATUS_CHANGED Streaming Media Devices"]
topic_type:
- apiref
api_name:
- KSEVENT_BDA_CA_SMART_CARD_STATUS_CHANGED
api_location:
- Bdamedia.h
api_type:
- HeaderDef
ms.date: 10/11/2021
---

# KSEVENT_BDA_CA_SMART_CARD_STATUS_CHANGED

Clients use **KSEVENT_BDA_CA_SMART_CARD_STATUS_CHANGED** to request notification when status on the smart card reader associated with an ECM map node changes.

## Specifying this event

KSEVENT

## Event data

A KSEVENTDATA structure that describes how to notify about the event.

## Requirements

**Header:** bdamedia.h (include Bdamedia.h)

## See also

[**KSEVENT**](./ksevent-structure.md)

[**KSEVENTDATA**](/windows-hardware/drivers/ddi/ks/ns-ks-kseventdata)

[**KSPROPERTY_BDA_CA_SMART_CARD_STATUS**](ksproperty-bda-ca-smart-card-status.md)
