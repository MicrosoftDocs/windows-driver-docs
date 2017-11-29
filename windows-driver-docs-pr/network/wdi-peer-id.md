---
title: WDI_PEER_ID
author: windows-driver-content
description: This topic describes the WDI_PEER_ID data type for WDI miniport drivers.
ms.assetid: 2D8700BC-7FED-4343-AC3F-8C43B0BE40FF
keywords:
- WDI_PEER_ID, WDK WDI_PEER_ID network drivers
ms.author: windowsdriverdev
ms.date: 11/27/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# WDI_PEER_ID

The WDI_PEER_ID data type is a UINT16 value that defines a peer ID.

```c++
typedef UINT16 WDI_PEER_ID;
```

## Remarks

If you want to specify any peer (wildcard), you can use the WDI_PEER_ANY (0xFFFF) value.

## Requirements

|   |   |
| --- | --- |
| Minimum supported client | Windows 10 |
| Minimum supported server | Windows Server 2016 |
| Header | Dot11wdi.h |

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bp_mb\p_mb%5D:%20Planning%20your%20APN%20database%20submission%20%20RELEASE:%20%281/18/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")