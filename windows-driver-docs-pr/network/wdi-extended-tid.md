---
title: WDI_EXTENDED_TID
description: This topic describes the WDI_EXTENDED_TID data type for WDI miniport drivers.
ms.assetid: C7ECB1BD-CB4A-4FD7-8222-9C9E25C15910
keywords:
- WDI_EXTENDED_TID, WDK WDI_EXTENDED_TID network drivers
ms.date: 11/27/2017
ms.localizationpriority: medium
---

# WDI_EXTENDED_TID

The WDI_EXTENDED_TID data type is a UINT8 value that defines a traffic identifier (TID).

```c++
typedef UINT8 WDI_EXTENDED_TID;
```

## Remarks

Possible values are as follows:

| Value | Description |
| --- | --- |
| 0-15 | 802.11 TIDs |
| 16 (WDI_EXT_TID_NON_QOS) | Non-QoS data |
| 17-24 | Reserved for use with IHV-injected frames. Frames with extended TID in the interval 17-24 are considered higher priority than those with a smaller extended TID in the same interval 17-24. |
| 25-30 | Unused values |
| 31 (WDI_EXT_TID_UNKNOWN) | Unknown/unspecified |

## Requirements

|   |   |
| --- | --- |
| Minimum supported client | Windows 10 |
| Minimum supported server | Windows Server 2016 |
| Header | Dot11wdi.h |

