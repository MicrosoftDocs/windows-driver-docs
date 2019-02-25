---
title: WDI_BAND_ID
description: This topic describes the WDI_BAND_ID data type for WDI miniport drivers.
ms.assetid: 28E34D2C-94A5-4035-ACAA-60CECABF3A02
keywords:
- WDI_BAND_ID, WDK WDI_BAND_ID network drivers
ms.date: 11/27/2017
ms.localizationpriority: medium
---

# WDI_BAND_ID

The WDI_BAND_ID data type is a UINT32 value that defines a band ID.

```c++
typedef UINT32 WDI_BAND_ID;
```

## Remarks

Possible band ID values are as follows:

| Value |   | Description |
| --- | --- | --- |
| WDI_BAND_ID_ANY | 0xFFFFFFFF | All bands |
| WDI_BAND_ID_2400 | 1 | 2.4 GHz |
| WDI_BAND_ID_5000 | 2 | 5 GHz |
| WDI_BAND_ID_60000 | 3 | 60 GHz |
| WDI_BAND_ID_900 | 4 | 900 MHz |
| WDI_BAND_ID_CUSTOM_START | 0x80000000 |Specifies the start of the range that is used to define a band ID reported by an IHV. |
| WDI_BAND_ID_CUSTOM_END | 0x81000000 | Specifies the end of the range that is used to define a band ID reported by an IHV. |

## Requirements

|   |   |
| --- | --- |
| Minimum supported client | Windows 10 |
| Minimum supported server | Windows Server 2016 |
| Header | Wditypes.hpp |

