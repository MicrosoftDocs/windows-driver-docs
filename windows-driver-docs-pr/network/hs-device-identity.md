---
title: HS\_DEVICE\_IDENTITY structure
author: windows-driver-content
description: The HS\_DEVICE\_IDENTITY structure contains information about the device model and manufacturer.
ms.assetid: 4a679fb2-d5b1-4635-9422-a21a316b360c
keywords: 
- HS_DEVICE_IDENTITY structure Network Drivers Starting with Windows Vista
- PHS_DEVICE_IDENTITY structure pointer Network Drivers Starting with Windows Vista
ms.author: windowsdriverdev
ms.date: 07/31/2017 
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
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

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bnetvista\netvista%5D:%20HS_DEVICE_IDENTITY%20structure%20%20RELEASE:%20%287/31/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


