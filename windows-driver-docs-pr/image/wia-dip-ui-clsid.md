---
title: WIA\_DIP\_UI\_CLSID
description: The WIA\_DIP\_UI\_CLSID property contains the vendor-supplied class identifier (CLSID) for any user interface (UI) extension COM object that is installed with a WIA minidriver. The WIA service creates and maintains this property.
ms.assetid: 05b2bda0-d53d-44f9-89c0-e0f6f1fc2b48
keywords: ["WIA_DIP_UI_CLSID Imaging Devices"]
topic_type:
- apiref
api_name:
- WIA_DIP_UI_CLSID
api_location:
- Wiadef.h
api_type:
- HeaderDef
ms.date: 11/28/2017
ms.localizationpriority: medium
---

# WIA\_DIP\_UI\_CLSID


The WIA\_DIP\_UI\_CLSID property contains the vendor-supplied class identifier (CLSID) for any user interface (UI) extension COM object that is installed with a WIA minidriver. The WIA service creates and maintains this property.

## <span id="ddk_wia_dip_ui_clsid_si"></span><span id="DDK_WIA_DIP_UI_CLSID_SI"></span>


Property Type: VT\_BSTR

Valid Values: WIA\_PROP\_NONE

Access Rights: Read-only

Remarks
-------

The UI CLSID value that is contained in the WIA\_DIP\_UI\_CLSID property is obtained from the driver's INF file. If no UI CLSID is specified, the WIA service supplies a default value. This property is used only internally by the WIA service when UI is being displayed.

Requirements
------------

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<tbody>
<tr class="odd">
<td><p>Header</p></td>
<td>Wiadef.h (include Wiadef.h)</td>
</tr>
</tbody>
</table>

 

 





