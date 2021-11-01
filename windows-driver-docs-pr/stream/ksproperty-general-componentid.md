---
title: KSPROPERTY_GENERAL_COMPONENTID
description: The KSPROPERTY_GENERAL_COMPONENTID property is an optional property that allows a client to access general component information stored in the KSCOMPONENTID structure.
keywords: ["KSPROPERTY_GENERAL_COMPONENTID Streaming Media Devices"]
topic_type:
- apiref
api_name:
- KSPROPERTY_GENERAL_COMPONENTID
api_location:
- ks.h
api_type:
- HeaderDef
ms.date: 10/22/2021
ms.localizationpriority: medium
---

# KSPROPERTY_GENERAL_COMPONENTID

The **KSPROPERTY_GENERAL_COMPONENTID** property is an optional property that allows a client to access general component information stored in the [**KSCOMPONENTID**](/windows-hardware/drivers/ddi/ks/ns-ks-kscomponentid) structure.

## Usage Summary Table

| Get | Set | Target | Property Descriptor Type | Property Value Type |
|--|--|--|--|--|
| Yes | No | Filter | [**KSPROPERTY**](/windows-hardware/drivers/stream/ksproperty-structure) | [**KSCOMPONENTID**](/windows-hardware/drivers/ddi/ks/ns-ks-kscomponentid) |

## Remarks

The [**KSCOMPONENTID**](/windows-hardware/drivers/ddi/ks/ns-ks-kscomponentid) structure contains GUID values for **Manufacturer**, **Product**, **Component**, and **Name**. It contains ULONG values for **Version** and **Revision**.

## Requirements

**Header:** ks.h (include Ks.h)

## See also

[**KSPROPERTY**](/windows-hardware/drivers/stream/ksproperty-structure)  

[**KSCOMPONENTID**](/windows-hardware/drivers/ddi/ks/ns-ks-kscomponentid)
