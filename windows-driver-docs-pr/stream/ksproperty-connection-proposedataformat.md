---
title: KSPROPERTY_CONNECTION_PROPOSEDATAFORMAT
description: Clients can use the KSPROPERTY_CONNECTION_PROPOSEDATAFORMAT property to propose a new data format for the connection.
keywords: ["KSPROPERTY_CONNECTION_PROPOSEDATAFORMAT Streaming Media Devices"]
topic_type:
- apiref
ms.topic: reference
api_name:
- KSPROPERTY_CONNECTION_PROPOSEDATAFORMAT
api_location:
- ks.h
api_type:
- HeaderDef
ms.date: 10/18/2021
---

# KSPROPERTY_CONNECTION_PROPOSEDATAFORMAT

Clients can use the **KSPROPERTY_CONNECTION_PROPOSEDATAFORMAT** property to propose a new data format for the connection.

## Usage Summary Table

| Get | Set | Target | Property descriptor type | Property value type |
|--|--|--|--|--|
| No | Yes | Pin | [**KSPROPERTY**](./ksproperty-structure.md) | [**KSDATAFORMAT**](/windows-hardware/drivers/ddi/ks/ns-ks-ksdataformat) |

## Remarks

This property returns a [**KSDATAFORMAT**](/windows-hardware/drivers/ddi/ks/ns-ks-ksdataformat) specifying the proposed data format.

The KS filter returns STATUS_SUCCESS if the pin can be reset to the proposed data format, or an error code otherwise. Note that this property request does not change the data format. Clients use [**KSPROPERTY_CONNECTION_DATAFORMAT**](ksproperty-connection-dataformat.md) to change the format.

## Requirements

**Header:** ks.h (include Ks.h)

## See also

[**KSPROPERTY_CONNECTION_DATAFORMAT**](ksproperty-connection-dataformat.md)

[*AVStrMiniPinSetDataFormat*](/windows-hardware/drivers/ddi/ks/nc-ks-pfnkspinsetdataformat)

[KS Data Formats and Data Ranges](ks-data-formats-and-data-ranges.md)