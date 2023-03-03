---
title: WDI_PORT_ID
description: This topic describes the WDI_PORT_ID data type for WDI miniport drivers.
keywords:
- WDI_PORT_ID, WDK WDI_PORT_ID network drivers
ms.date: 03/02/2023
---

# WDI_PORT_ID

The WDI_PORT_ID data type is a UINT16 value that defines a port ID.

```c++
typedef UINT16 WDI_PORT_ID;
```

## Remarks

If you want to specify any port (wildcard), you can use the WDI_PORT_ANY (0xFFFF) value.

## Requirements

**Minimum supported client**: Windows 10

**Minimum supported server**: Windows Server 2016

**Header**: Dot11wdi.h


