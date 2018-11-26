---
title: WDI_FRAME_ID
description: This topic describes the WDI_FRAME_ID data type for WDI miniport drivers.
ms.assetid: 7D886BA2-EDD2-4770-948C-9C891D07EF58
keywords:
- WDI_FRAME_ID, WDK WDI_FRAME_ID network drivers
ms.date: 11/27/2017
ms.localizationpriority: medium
---

# WDI_FRAME_ID

The WDI_FRAME_ID data type is a UINT16 value that defines a frame ID. This is only an identifier. It does not convey information about the ordering of frames.

```c++
typedef UINT16 WDI_FRAME_ID;
```

## Requirements

|   |   |
| --- | --- |
| Minimum supported client | Windows 10 |
| Minimum supported server | Windows Server 2016 |
| Header | Dot11wdi.h |

