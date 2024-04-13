---
title: WIA_IPS_COLOR_DROP_MULTI
description: The WIA_IPS_COLOR_DROP_MULTI property is used to report when more than one single color can be dropped out at the same time.
keywords: ["WIA_IPS_COLOR_DROP_MULTI Imaging Devices"]
topic_type:
- apiref
ms.topic: reference
api_name:
- WIA_IPS_COLOR_DROP_MULTI
api_location:
- Wiadef.h
api_type:
- HeaderDef
ms.date: 05/17/2019
---

# WIA\_IPS\_COLOR\_DROP\_MULTI

The **WIA\_IPS\_COLOR\_DROP\_MULTI** property is used to report when more than one single color can be dropped out at the same time. For example, if the value of this property is 2, then the application can set the **WIA\_IPS\_COLOR\_DROP\_RED**, **WIA\_IPS\_COLOR\_DROP\_GREEN**, and **WIA\_IPS\_COLOR\_ BLUE** properties to enumerations containing each two values, describing the two colors to be dropped out.

This property is initialized and maintained by the WIA mini-driver.

Property Type: VT\_UI4

Valid Values: WIA\_PROP\_NONE

Access Rights: Read-only

## Remarks

This property is valid for all programmable image data source items, including Flatbed (WIA\_CATEGORY\_FLATBED) and Feeder (WIA\_CATEGORY\_FEEDER) only when the [**WIA\_IPS\_COLOR\_DROP**](./wia-ips-color-drop.md) property is supported.

## Requirements

| &nbsp; | &nbsp; |
| --- |:--- |
| **Header** | Wiadef.h (include Wiadef.h) |
