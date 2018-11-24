---
title: WDI_PORT_ID
description: This topic describes the WDI_PORT_ID data type for WDI miniport drivers.
ms.assetid: 16385F87-E3BE-4CCC-8E40-C4AAEA399964
keywords:
- WDI_PORT_ID, WDK WDI_PORT_ID network drivers
ms.date: 11/27/2017
ms.localizationpriority: medium
---

# WDI_PORT_ID

The WDI_PORT_ID data type is a UINT16 value that defines a port ID.

```c++
typedef UINT16 WDI_PORT_ID;
```

## Remarks

If you want to specify any port (wildcard), you can use the WDI_PORT_ANY (0xFFFF) value.

## Requirements

|   |   |
| --- | --- |
| Minimum supported client | Windows 10 |
| Minimum supported server | Windows Server 2016 |
| Header | Dot11wdi.h |

