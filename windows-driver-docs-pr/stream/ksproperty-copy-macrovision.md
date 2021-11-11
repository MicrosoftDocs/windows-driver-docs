---
title: KSPROPERTY_COPY_MACROVISION
description: The KSPROPERTY_COPY_MACROVISION property indicates the Macrovision level of the data stream.
keywords: ["KSPROPERTY_COPY_MACROVISION Streaming Media Devices"]
topic_type:
- apiref
api_name:
- KSPROPERTY_COPY_MACROVISION
api_location:
- ksmedia.h
api_type:
- HeaderDef
ms.date: 10/18/2021
ms.localizationpriority: medium
---

# KSPROPERTY_COPY_MACROVISION

The **KSPROPERTY_COPY_MACROVISION** property indicates the Macrovision level of the data stream.

## Usage Summary Table

| Get | Set | Target | Property descriptor type | Property value type |
|--|--|--|--|--|
| No | Yes | Pin | [**KSPROPERTY**](/windows-hardware/drivers/stream/ksproperty-structure) | [**KS_COPY_MACROVISION**](/windows-hardware/drivers/ddi/ksmedia/ns-ksmedia-_ks_copy_macrovision) |

The property value (operation data) is a **KS_COPY_MACROVISION** structure the specifies the Macrovision level of the data stream.

## Remarks

For more information about Macrovision level, see [DVD Copyright Protection](dvd-copyright-protection.md).

## Requirements

**Header:** ksmedia.h (include Ksmedia.h)

## See also

[**KS_COPY_MACROVISION**](/windows-hardware/drivers/ddi/ksmedia/ns-ksmedia-_ks_copy_macrovision)
