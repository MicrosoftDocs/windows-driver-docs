---
title: WDI_PEER_ID
description: This topic describes the WDI_PEER_ID data type for WDI miniport drivers.
keywords:
- WDI_PEER_ID, WDK WDI_PEER_ID network drivers
ms.date: 11/27/2017
---

# WDI_PEER_ID

The WDI_PEER_ID data type is a UINT16 value that defines a peer ID.

```c++
typedef UINT16 WDI_PEER_ID;
```

## Remarks

If you want to specify any peer (wildcard), you can use the WDI_PEER_ANY (0xFFFF) value.

## Requirements

**Minimum supported client**: Windows 10

**Minimum supported server**: Windows Server 2016

**Header**: Dot11wdi.h


