---
title: WIA_DPS_HORIZONTAL_BED_SIZE
description: The WIA_DPS_HORIZONTAL_BED_SIZE property contains the physical dimensions of a scanner's flatbed, in thousandths of an inch (.001). The WIA minidriver creates and maintains this property.
keywords: ["WIA_DPS_HORIZONTAL_BED_SIZE Imaging Devices"]
topic_type:
- apiref
api_name:
- WIA_DPS_HORIZONTAL_BED_SIZE
api_location:
- Wiadef.h
api_type:
- HeaderDef
ms.date: 09/30/2021
ms.localizationpriority: medium
---

# WIA_DPS_HORIZONTAL_BED_SIZE

The WIA_DPS_HORIZONTAL_BED_SIZE property contains the physical dimensions of a scanner's flatbed, in thousandths of an inch (.001). The WIA minidriver creates and maintains this property.

Property Type: VT_I4

Valid Values: WIA_PROP_NONE

Access Rights: Read-only

## Requirements

**Version:** Beginning with Windows Vista, the WIA_DPS_HORIZONTAL_BED_SIZE property is still available, but it has been replaced by the WIA_IPS_MAX_HORIZONTAL_SIZE property, so you should consider it optional.

**Header:** wiadef.h (include Wiadef.h)

## See also

[**WIA_DPS_VERTICAL_BED_SIZE**](wia-dps-vertical-bed-size.md)

[**WIA_IPS_MAX_HORIZONTAL_SIZE**](wia-ips-max-horizontal-size.md)
