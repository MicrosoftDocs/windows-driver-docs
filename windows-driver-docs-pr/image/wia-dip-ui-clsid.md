---
title: WIA_DIP_UI_CLSID
description: The WIA_DIP_UI_CLSID property contains the vendor-supplied class identifier (CLSID) for any user interface (UI) extension COM object that is installed with a WIA minidriver. The WIA service creates and maintains this property.
keywords: ["WIA_DIP_UI_CLSID Imaging Devices"]
topic_type:
- apiref
api_name:
- WIA_DIP_UI_CLSID
api_location:
- Wiadef.h
api_type:
- HeaderDef
ms.date: 09/29/2021
---

# WIA_DIP_UI_CLSID

The WIA_DIP_UI_CLSID property contains the vendor-supplied class identifier (CLSID) for any user interface (UI) extension COM object that is installed with a WIA minidriver. The WIA service creates and maintains this property.

Property Type: VT_BSTR

Valid Values: WIA_PROP_NONE

Access Rights: Read-only

## Remarks

The UI CLSID value that is contained in the WIA_DIP_UI_CLSID property is obtained from the driver's INF file. If no UI CLSID is specified, the WIA service supplies a default value. This property is used only internally by the WIA service when UI is being displayed.

## Requirements

**Header:** wiadef.h (include Wiadef.h)
