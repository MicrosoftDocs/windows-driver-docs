---
title: KSPROPERTY_CONNECTION_DATAFORMAT
description: Clients use the KSPROPERTY_CONNECTION_DATAFORMAT property to set the current data format.
keywords: ["KSPROPERTY_CONNECTION_DATAFORMAT Streaming Media Devices"]
topic_type:
- apiref
api_name:
- KSPROPERTY_CONNECTION_DATAFORMAT
api_location:
- ks.h
api_type:
- HeaderDef
ms.date: 10/18/2021
---

# KSPROPERTY_CONNECTION_DATAFORMAT

Clients use the **KSPROPERTY_CONNECTION_DATAFORMAT** property to set the current data format.

## Usage Summary Table

| Get | Set | Target | Property descriptor type | Property value type |
|--|--|--|--|--|
| No | Yes | Pin | [**KSPROPERTY**](./ksproperty-structure.md) | [**KSDATAFORMAT**](/windows-hardware/drivers/ddi/ks/ns-ks-ksdataformat) |

## Remarks

This property takes a [**KSDATAFORMAT**](/windows-hardware/drivers/ddi/ks/ns-ks-ksdataformat) structure specifying the requested data format.

KS filters only need to support this property if they allow clients to reset the current property, or if connections can be made with the data format incompletely specified.

For more information about the **KSPROPERTY_CONNECTION_DATAFORMAT** property, see [KS Data Formats and Data Ranges](ks-data-formats-and-data-ranges.md) and [Data Range Intersections in AVStream](data-range-intersections-in-avstream.md).

## Requirements

**Header:** ks.h (include Ks.h)

## See also

[**KSSTREAM_HEADER**](/windows-hardware/drivers/ddi/ks/ns-ks-ksstream_header)

[**KSPROPERTY_CONNECTION_PROPOSEDATAFORMAT**](ksproperty-connection-proposedataformat.md)

[**KSPROPERTY_PIN_PROPOSEDATAFORMAT**](ksproperty-pin-proposedataformat.md)