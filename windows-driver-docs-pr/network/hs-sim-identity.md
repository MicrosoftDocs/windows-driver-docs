---
title: HS_SIM_IDENTITY structure
author: windows-driver-content
description: The HS\_SIM\_IDENTITY structure contains SIM identification information required for EAP-SIM or EAP-AKA authentication.
ms.assetid: b45fac33-79de-4006-9dcb-95725be11ec1
keywords: 
- HS_SIM_IDENTITY structure Network Drivers Starting with Windows Vista
- PHS_SIM_IDENTITY structure pointer Network Drivers Starting with Windows Vista
ms.author: windowsdriverdev
ms.date: 07/31/2017 
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# HS\_SIM\_IDENTITY structure


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

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bnetvista\netvista%5D:%20HS_SIM_IDENTITY%20structure%20%20RELEASE:%20%287/31/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


