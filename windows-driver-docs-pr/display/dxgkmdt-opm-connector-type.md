---
title: DXGKMDT\_OPM\_CONNECTOR\_TYPE enumeration
description: Reserved for system use. Do not use in your driver.
ms.assetid: 57A2F351-99F1-425A-99E3-1167CEFF9FDD
keywords: ["DXGKMDT_OPM_CONNECTOR_TYPE enumeration Display Devices"]
topic_type:
- apiref
api_name:
- DXGKMDT_OPM_CONNECTOR_TYPE
api_location:
- D3dkmdt.h
api_type:
- HeaderDef
ms.author: windowsdriverdev
ms.date: 01/05/2018
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# DXGKMDT\_OPM\_CONNECTOR\_TYPE enumeration


Reserved for system use. Do not use in your driver.

Syntax
------

```ManagedCPlusPlus
typedef enum _DXGKMDT_OPM_CONNECTOR_TYPE {
  DXGKMDT_OPM_CONNECTOR_TYPE_OTHER                     = -1,
  DXGKMDT_OPM_CONNECTOR_TYPE_HD15                      = 0,
  DXGKMDT_OPM_CONNECTOR_TYPE_SVIDEO                    = 1,
  DXGKMDT_OPM_CONNECTOR_TYPE_COMPOSITE_VIDEO           = 2,
  DXGKMDT_OPM_CONNECTOR_TYPE_COMPONENT_VIDEO           = 3,
  DXGKMDT_OPM_CONNECTOR_TYPE_DVI                       = 4,
  DXGKMDT_OPM_CONNECTOR_TYPE_HDMI                      = 5,
  DXGKMDT_OPM_CONNECTOR_TYPE_LVDS                      = 6,
  DXGKMDT_OPM_CONNECTOR_TYPE_D_JPN                     = 8,
  DXGKMDT_OPM_CONNECTOR_TYPE_SDI                       = 9,
  DXGKMDT_OPM_CONNECTOR_TYPE_DISPLAYPORT_EXTERNAL      = 10,
  DXGKMDT_OPM_CONNECTOR_TYPE_DISPLAYPORT_EMBEDDED      = 11,
  DXGKMDT_OPM_CONNECTOR_TYPE_UDI_EXTERNAL              = 12,
  DXGKMDT_OPM_CONNECTOR_TYPE_UDI_EMBEDDED              = 13,
  DXGKMDT_OPM_CONNECTOR_TYPE_RESERVED                  = 14,
  DXGKMDT_OPM_CONNECTOR_TYPE_MIRACAST                  = 15,
  DXGKMDT_OPM_COPP_COMPATIBLE_CONNECTOR_TYPE_INTERNAL  = 0x80000000
} DXGKMDT_OPM_CONNECTOR_TYPE;
```

Constants
---------

<span id="DXGKMDT_OPM_CONNECTOR_TYPE_OTHER"></span><span id="dxgkmdt_opm_connector_type_other"></span>**DXGKMDT\_OPM\_CONNECTOR\_TYPE\_OTHER**

<span id="DXGKMDT_OPM_CONNECTOR_TYPE_HD15"></span><span id="dxgkmdt_opm_connector_type_hd15"></span>**DXGKMDT\_OPM\_CONNECTOR\_TYPE\_HD15**

<span id="DXGKMDT_OPM_CONNECTOR_TYPE_SVIDEO"></span><span id="dxgkmdt_opm_connector_type_svideo"></span>**DXGKMDT\_OPM\_CONNECTOR\_TYPE\_SVIDEO**

<span id="DXGKMDT_OPM_CONNECTOR_TYPE_COMPOSITE_VIDEO"></span><span id="dxgkmdt_opm_connector_type_composite_video"></span>**DXGKMDT\_OPM\_CONNECTOR\_TYPE\_COMPOSITE\_VIDEO**

<span id="DXGKMDT_OPM_CONNECTOR_TYPE_COMPONENT_VIDEO"></span><span id="dxgkmdt_opm_connector_type_component_video"></span>**DXGKMDT\_OPM\_CONNECTOR\_TYPE\_COMPONENT\_VIDEO**

<span id="DXGKMDT_OPM_CONNECTOR_TYPE_DVI"></span><span id="dxgkmdt_opm_connector_type_dvi"></span>**DXGKMDT\_OPM\_CONNECTOR\_TYPE\_DVI**

<span id="DXGKMDT_OPM_CONNECTOR_TYPE_HDMI"></span><span id="dxgkmdt_opm_connector_type_hdmi"></span>**DXGKMDT\_OPM\_CONNECTOR\_TYPE\_HDMI**

<span id="DXGKMDT_OPM_CONNECTOR_TYPE_LVDS"></span><span id="dxgkmdt_opm_connector_type_lvds"></span>**DXGKMDT\_OPM\_CONNECTOR\_TYPE\_LVDS**

<span id="DXGKMDT_OPM_CONNECTOR_TYPE_D_JPN"></span><span id="dxgkmdt_opm_connector_type_d_jpn"></span>**DXGKMDT\_OPM\_CONNECTOR\_TYPE\_D\_JPN**

<span id="DXGKMDT_OPM_CONNECTOR_TYPE_SDI"></span><span id="dxgkmdt_opm_connector_type_sdi"></span>**DXGKMDT\_OPM\_CONNECTOR\_TYPE\_SDI**

<span id="DXGKMDT_OPM_CONNECTOR_TYPE_DISPLAYPORT_EXTERNAL"></span><span id="dxgkmdt_opm_connector_type_displayport_external"></span>**DXGKMDT\_OPM\_CONNECTOR\_TYPE\_DISPLAYPORT\_EXTERNAL**

<span id="DXGKMDT_OPM_CONNECTOR_TYPE_DISPLAYPORT_EMBEDDED"></span><span id="dxgkmdt_opm_connector_type_displayport_embedded"></span>**DXGKMDT\_OPM\_CONNECTOR\_TYPE\_DISPLAYPORT\_EMBEDDED**

<span id="DXGKMDT_OPM_CONNECTOR_TYPE_UDI_EXTERNAL"></span><span id="dxgkmdt_opm_connector_type_udi_external"></span>**DXGKMDT\_OPM\_CONNECTOR\_TYPE\_UDI\_EXTERNAL**

<span id="DXGKMDT_OPM_CONNECTOR_TYPE_UDI_EMBEDDED"></span><span id="dxgkmdt_opm_connector_type_udi_embedded"></span>**DXGKMDT\_OPM\_CONNECTOR\_TYPE\_UDI\_EMBEDDED**

<span id="DXGKMDT_OPM_CONNECTOR_TYPE_RESERVED"></span><span id="dxgkmdt_opm_connector_type_reserved"></span>**DXGKMDT\_OPM\_CONNECTOR\_TYPE\_RESERVED**

<span id="DXGKMDT_OPM_CONNECTOR_TYPE_MIRACAST"></span><span id="dxgkmdt_opm_connector_type_miracast"></span>**DXGKMDT\_OPM\_CONNECTOR\_TYPE\_MIRACAST**

<span id="DXGKMDT_OPM_COPP_COMPATIBLE_CONNECTOR_TYPE_INTERNAL"></span><span id="dxgkmdt_opm_copp_compatible_connector_type_internal"></span>**DXGKMDT\_OPM\_COPP\_COMPATIBLE\_CONNECTOR\_TYPE\_INTERNAL**

Requirements
------------

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<tbody>
<tr class="odd">
<td align="left"><p>Minimum supported client</p></td>
<td align="left"><p>Windows 8.1</p></td>
</tr>
<tr class="even">
<td align="left"><p>Minimum supported server</p></td>
<td align="left"><p>Windows Server 2012 R2</p></td>
</tr>
<tr class="odd">
<td align="left"><p>Header</p></td>
<td align="left">D3dkmdt.h (include D3dkmdt.h)</td>
</tr>
</tbody>
</table>

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[display\display]:%20DXGKMDT_OPM_CONNECTOR_TYPE%20enumeration%20%20RELEASE:%20%281/4/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




