---
title: HS_SIM_IDENTITY structure
description: The HS_SIM_IDENTITY structure contains SIM identification information required for EAP-SIM or EAP-AKA authentication.
ms.assetid: b45fac33-79de-4006-9dcb-95725be11ec1
keywords: 
- HS_SIM_IDENTITY structure Network Drivers Starting with Windows Vista
- PHS_SIM_IDENTITY structure pointer Network Drivers Starting with Windows Vista
ms.date: 07/31/2017
ms.localizationpriority: medium
---

# HS\_SIM\_IDENTITY structure

[!include[Wi-Fi Hotspot Offloading deprecation](wi-fi-hotspot-offloading-deprecation.md)]


The **HS\_SIM\_IDENTITY** structure contains SIM identification information required for EAP-SIM or EAP-AKA authentication.

Syntax
------

```ManagedCPlusPlus
typedef struct _HS_SIM_IDENTITY {
  eHS_SIM_TYPE SimType;
  DWORD        dwMNC;
  DWORD        dwMCC;
  DWORD        dwNID;
  DWORD        dwSID;
  DWORD        dwEapMethods;
} HS_SIM_IDENTITY, *PHS_SIM_IDENTITY;
```

Members
-------

**SimType**  
The type of SIM, whether GSM or CDMA, or none. If the network is GSM, the **dwMNC** and **dwMCC** pair of fields will be defined, whereas for CDMA the **dwSID** and **dwNID** pair of fields must be defined.

**dwMNC**  
Used if the SIM is GSM type.

The mobile network code (MNC) of the GSM network.

**dwMCC**  
Used if the SIM is GSM type.

The mobile country code (MCC) of the GSM network.

**dwNID**  
Used if the SIM is CDMA type.

The Network Identification Number (NID) of the CDMA network.

**dwSID**  
Used if the SIM is CDMA type.

The System Identification Number (SID) of the CDMA network.

**dwEapMethods**  
The EAP authentication method.

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

## See also


[Extensible Authentication Protocol](https://msdn.microsoft.com/library/windows/desktop/aa363502)

 

 




