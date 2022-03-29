---
title: KSEVENT_VIDCAP_SEARCH
description: The KSEVENT_VIDCAP_AUTO_UPDATE event is triggered when a search has been completed.
keywords: ["KSEVENT_VIDCAP_SEARCH Streaming Media Devices"]
topic_type:
- apiref
api_name:
- KSEVENT_VIDCAP_SEARCH
api_type:
- NA
ms.date: 10/11/2021
---

# KSEVENT_VIDCAP_SEARCH

The **KSEVENT_VIDCAP_AUTO_UPDATE** event is triggered when a search has been completed.

## Usage Summary Table

| Get | Set | Target | Event descriptor type | Event value type |
|--|--|--|--|--|
| No | Yes | Filter | [**KSEVENT**](./ksevent-structure.md) | [**KSEVENTDATA**](/windows-hardware/drivers/ddi/ks/ns-ks-kseventdata) |

## Remarks

Clients might register for this event when searching for a particular track, for instance, in order to be notified when the search completes.

For more information about DirectShow filters and KsProxy see [Kernel Streaming Proxy](/windows-hardware/drivers/ddi/_stream/index).