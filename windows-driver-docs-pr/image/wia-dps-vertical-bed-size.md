---
title: WIA_DPS_VERTICAL_BED_SIZE
description: The WIA_DPS_VERTICAL_BED_SIZE property contains the physical vertical dimensions of a scanner's flatbed, in thousandths of an inch (.001). The WIA minidriver creates and maintains this property.
keywords: ["WIA_DPS_VERTICAL_BED_SIZE Imaging Devices"]
topic_type:
- apiref
api_name:
- WIA_DPS_VERTICAL_BED_SIZE
api_location:
- Wiadef.h
api_type:
- HeaderDef
ms.date: 10/04/2021
---

# WIA_DPS_VERTICAL_BED_SIZE

The WIA_DPS_VERTICAL_BED_SIZE property contains the physical vertical dimensions of a scanner's flatbed, in thousandths of an inch (.001). The WIA minidriver creates and maintains this property.

Property Type: VT_I4

Valid Values: WIA_PROP_NONE

Access Rights: Read-only

## Requirements

**Version:** Beginning with Windows Vista, the WIA_DPS_VERTICAL_BED_SIZE property is still available at the root level of the WIA driver. But this property has been replaced with the WIA_IPS_MAX_VERTICAL_SIZE property, and you should consider it to be optional.

**Header:** wiadef.h (include Wiadef.h)

## See also

[**WIA_DPS_HORIZONTAL_BED_SIZE**](wia-dps-horizontal-bed-size.md)

[**WIA_IPS_MAX_VERTICAL_SIZE**](wia-ips-max-vertical-size.md)
