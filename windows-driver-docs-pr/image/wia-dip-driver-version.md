---
title: WIA_DIP_DRIVER_VERSION
description: The WIA_DIP_DRIVER_VERSION property contains the current DLL version of a WIA minidriver. The WIA service creates and maintains this property.
keywords: ["WIA_DIP_DRIVER_VERSION Imaging Devices"]
topic_type:
- apiref
ms.topic: reference
api_name:
- WIA_DIP_DRIVER_VERSION
api_location:
- Wiadef.h
api_type:
- HeaderDef
ms.date: 09/29/2021
---

# WIA_DIP_DRIVER_VERSION

The WIA_DIP_DRIVER_VERSION property contains the current DLL version of a WIA minidriver. The WIA service creates and maintains this property.

Property Type: VT_BSTR

Valid Values: WIA_PROP_NONE

Access Rights: Read-only

## Remarks

If the WIA minidriver does not supply a version resource, the WIA service supplies the value "0.0.0.0" as a default. An application reads WIA_DIP_DRIVER_VERSION to determine the version of the WIA minidriver DLL.

**Note**   Beginning with Windows Vista, the wildcard IP address 0.0.0.0 is not available.
Also beginning with Windows Vista, if the **IPAutoconfigurationEnabled** registry key is set to a value of 0, automatic IP address assignment is disabled, and no IP address is assigned. In this case, the **ipconfig** command line tool will not display an IP address. If the key is set to a nonzero value, an IP address is automatically assigned. This key can be located at the following paths in the registry:

`HKEY_LOCAL_MACHINE\SYSTEM\Current Control Set\Services\Tcpip\Parameters\IPAutoconfigurationEnabled`

`HKEY_LOCAL_MACHINE\SYSTEM\Current Control Set\Services\Tcpip\Parameters\Interfaces\*GUID*\IPAutoconfigurationEnabled`

## Requirements

**Header:** wiadef.h (include Wiadef.h)
