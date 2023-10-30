---
title: WIA_IPS_MULTI_FEED_DETECT_METHOD
description: The WIA_IPS_MULTI_FEED_DETECT_METHOD property is used to configure the method used by the device to detect a multiple feed condition.
keywords: ["WIA_IPS_MULTI_FEED_DETECT_METHOD Imaging Devices"]
topic_type:
- apiref
ms.topic: reference
api_name:
- WIA_IPS_MULTI_FEED_DETECT_METHOD
api_location:
- Wiadef.h
api_type:
- HeaderDef
ms.date: 05/17/2019
---

# WIA\_IPS\_MULTI\_FEED\_DETECT\_METHOD

The **WIA\_IPS\_MULTI\_FEED\_DETECT\_METHOD** property is used to configure the method used by the device to detect a multiple feed condition.

This property is initialized and maintained by the WIA mini-driver.

Property Type: VT\_I4

Valid Values: WIA\_PROP\_LIST

Access Rights: Read-Write

## Remarks

The valid values for this property are shown in the following table.

| Value | Description |
| --- | --- |
| WIA_MULTI_FEED_DETECT_ METHOD_LENGTH | The device measures the length of the scanned page with the length of the original page size being scanned. |
| WIA_MULTI_FEED_DETECT_METHOD_OVERLAP | The device detects overlapped scanned pages. |

The mini-driver can support a different set of [**WIA\_IPS\_MULTI\_FEED\_SENSITIVITY**](./wia-ips-multi-feed-sensitivity.md) property values for each **WIA\_IPS\_MULTI\_FEED\_DETECT\_METHOD** property value. When both **WIA\_IPS\_MULTI\_FEED\_DETECT\_METHOD** and the **WIA\_IPS\_MULTI\_FEED\_SENSITIVITY** properties are supported, the WIA application should first set the **WIA\_IPS\_MULTI\_FEED\_DETECT\_METHOD** property to configure the multi-feed detection method, and then set the **WIA\_IPS\_MULTI\_FEED\_SENSITIVITY** property to configure the desired sensitivity for this detection method.

This property is valid only for the Feeder item (WIA\_CATEGORY\_FEEDER) and is optional. There is no required default value when the property is supported.

## Requirements

| &nbsp; | &nbsp; |
| --- |:--- |
| **Header** | Wiadef.h (include Wiadef.h) |
