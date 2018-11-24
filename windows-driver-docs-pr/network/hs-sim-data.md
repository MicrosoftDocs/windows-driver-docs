---
title: HS_SIM_DATA structure
description: The HS_SIM_DATA structure contains information stored in the SIM card.
ms.assetid: 9e29a85e-e764-4841-b218-c63bba0ca9fa
keywords: 
- HS_SIM_DATA structure Network Drivers Starting with Windows Vista
- PHS_SIM_DATA structure pointer Network Drivers Starting with Windows Vista
ms.date: 07/31/2017
ms.localizationpriority: medium
---

# HS\_SIM\_DATA structure

[!include[Wi-Fi Hotspot Offloading deprecation](wi-fi-hotspot-offloading-deprecation.md)]


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

 

 




