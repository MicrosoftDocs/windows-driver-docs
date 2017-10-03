---
title: HS_SIM_DATA structure
author: windows-driver-content
description: The HS\_SIM\_DATA structure contains information stored in the SIM card.
ms.assetid: 9e29a85e-e764-4841-b218-c63bba0ca9fa
keywords: 
- HS_SIM_DATA structure Network Drivers Starting with Windows Vista
- PHS_SIM_DATA structure pointer Network Drivers Starting with Windows Vista
ms.author: windowsdriverdev
ms.date: 07/31/2017 
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# HS\_SIM\_DATA structure


The **HS\_SIM\_DATA** structure contains information stored in the SIM card.

Syntax
------

```ManagedCPlusPlus
typedef struct _HS_SIM_DATA {
  WCHAR wszICCID[HS_CONST_MAX_ICCID_LENGTH+1];
  WCHAR wszIMEI[HS_CONST_MAX_IMEI_LENGTH+1];
  WCHAR wszMEID_ME[HS_CONST_MAX_MEID_ME_LENGTH+1];
  WCHAR wszSF_EUIMID[HS_CONST_MAX_SF_EUIMID_LENGTH+1];
} HS_SIM_DATA, *PHS_SIM_DATA;
```

Members
-------

**wszICCID**  
The Integrated Circuit Card Identifier (ICCID) stored in the SIM card.

**wszIMEI**  
The International Mobile Equipment Identity (IMEI) used to identify 3GPP phones.

**wszMEID\_ME**  
The Mobile Equipment Identifier (MEID) defined by 3GPP2.

**wszSF\_EUIMID**  
The Short Form Expanded User Identity Module Identifier (EUIMID) for a R-UIM or CSIM (CDMA SIM application) card.

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
<td>Hotspotoffloadplugin.h (include Hotspotoffloadplugin.h)</td>
</tr>
</tbody>
</table>

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bnetvista\netvista%5D:%20HS_SIM_DATA%20structure%20%20RELEASE:%20%287/31/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


