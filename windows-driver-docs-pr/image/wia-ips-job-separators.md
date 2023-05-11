---
title: WIA_IPS_JOB_SEPARATORS
description: The WIA_IPS_JOB_SEPARATORS property is used to enable the detection of job separators, and to configure the action that the device executes when it detects a job separator page. The WIA minidriver creates and maintains this property.
keywords: ["WIA_IPS_JOB_SEPARATORS Imaging Devices"]
topic_type:
- apiref
ms.topic: reference
api_name:
- WIA_IPS_JOB_SEPARATORS
api_location:
- Wiadef.h
api_type:
- HeaderDef
ms.date: 05/05/2023
---

# WIA_IPS_JOB_SEPARATORS

The **WIA_IPS_JOB_SEPARATORS** property is used to enable the detection of job separators, and to configure the action that the device executes when it detects a job separator page. The WIA minidriver creates and maintains this property.

Property Type: VT_I4

Valid Values: WIA_PROP_LIST

Access Rights: Read/Write

## Remarks

The following table describes the valid values for the **WIA_IPS_JOB_SEPARATORS** property.

| Value | Definition |
|--|--|
| WIA_SEPARATOR_DISABLED | Job separators detection is disabled. This is the required default value if the property is supported. |
| WIA_SEPARATOR_DETECT_SCAN_CONTINUE | Detect job separator page, scan the separator page, and continue scanning. |
| WIA_SEPARATOR_DETECT_SCAN_STOP | Detect job separator page, scan the separator page, and stop scanning. |
| WIA_SEPARATOR_DETECT_NOSCAN_CONTINUE | Detect job separator page, do not scan (skip) the separator page, and continue scanning. |
| WIA_SEPARATOR_DETECT_NOSCAN_STOP | Detect job separator page, do not scan (skip) the separator page, and stop scanning. |

This property is optional, and is valid only for the Feeder data source item (represented in the [**WIA_IPA_ITEM_CATEGORY**](wia-ipa-item-category.md) property as WIA_CATEGORY_FEEDER).

## Requirements

**Header:** wiadef.h (include Wiadef.h)
