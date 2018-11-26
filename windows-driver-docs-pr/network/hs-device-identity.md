---
title: HS_DEVICE_IDENTITY structure
description: The HS_DEVICE_IDENTITY structure contains information about the device model and manufacturer.
ms.assetid: 4a679fb2-d5b1-4635-9422-a21a316b360c
keywords: 
- HS_DEVICE_IDENTITY structure Network Drivers Starting with Windows Vista
- PHS_DEVICE_IDENTITY structure pointer Network Drivers Starting with Windows Vista
ms.date: 07/31/2017
ms.localizationpriority: medium
---

# HS\_DEVICE\_IDENTITY structure

[!include[Wi-Fi Hotspot Offloading deprecation](wi-fi-hotspot-offloading-deprecation.md)]


The **HS\_DEVICE\_IDENTITY** structure contains information about the device model and manufacturer.

Syntax
------

```ManagedCPlusPlus
typedef struct _HS_DEVICE_IDENTITY {
  DWORD dwSystemType;
  WCHAR wszPhoneManufacturer[HS_CONST_MAX_DEVICE_INFO_LENGTH+1];
  WCHAR wszPhoneModelName[HS_CONST_MAX_DEVICE_INFO_LENGTH+1];
  WCHAR wszPhoneManufacturerModel[HS_CONST_MAX_DEVICE_INFO_LENGTH+1];
  WCHAR wszDeviceModel[HS_CONST_MAX_DEVICE_INFO_LENGTH+1];
} HS_DEVICE_IDENTITY, *PHS_DEVICE_IDENTITY;
```

Members
-------

**dwSystemType**  
The type of SIM, whether GSM or CDMA.

**wszPhoneManufacturer**  
The phone manufacturer name.

**wszPhoneModelName**  
The phone model name.

**wszPhoneManufacturerModel**  
Another name for the phone manufacturer and model.

**wszDeviceModel**  
The device model name.

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

 

 




