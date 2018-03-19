---
title: OID_DOT11_WFD_DESIRED_GROUP_ID
author: windows-driver-content
description: When set, the OID_DOT11_WFD_DESIRED_GROUP_ID object identifier (OID) sets WFD group identifier that the miniport should use when starting as the WFD Group Owner (GO).
ms.assetid: BCE476DA-A9CD-4B50-AA89-8B604FDCE1E8
ms.author: windowsdriverdev
ms.date: 08/08/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
keywords: 
 -OID_DOT11_WFD_DESIRED_GROUP_ID Network Drivers Starting with Windows Vista
---

# OID\_DOT11\_WFD\_DESIRED\_GROUP\_ID


**Important**  The [Native 802.11 Wireless LAN](https://msdn.microsoft.com/library/windows/hardware/ff560690) interface is deprecated in Windows 10 and later. Please use the WLAN Device Driver Interface (WDI) instead. For more information about WDI, see [WLAN Universal Windows driver model](https://msdn.microsoft.com/library/windows/hardware/dn897672).

 

When set, the OID\_DOT11\_WFD\_DESIRED\_GROUP\_ID object identifier (OID) sets WFD group identifier that the miniport should use when starting as the WFD Group Owner (GO).

The data type for this OID is the **DOT11\_WFD\_GROUP\_ID** structure.

```ManagedCPlusPlus
    typedef struct _DOT11_WFD_GROUP_ID 
    {
        DOT11_MAC_ADDRESS DeviceAddress;
        DOT11_SSID SSID;    
    } DOT11_WFD_GROUP_ID, * PDOT11_WFD_GROUP_ID;
  
```

This structure includes the following members:

<a href="" id="deviceaddress"></a>**DeviceAddress**  
The address of the device that will become the GO.

<a href="" id="--------ssid"></a> **SSID**  
The SSID for the GO device.

The identifier is used to configure the group when an [OID\_DOT11\_WFD\_START\_GO\_REQUEST](oid-dot11-wfd-start-go-request.md) OID is received.

Requirements
------------

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<tbody>
<tr class="odd">
<td><p>Version</p></td>
<td><p>Supported starting with Windows 8.</p></td>
</tr>
<tr class="even">
<td><p>Header</p></td>
<td>Windot11.h (include Windot11.h)</td>
</tr>
</tbody>
</table>

## See also


[OID\_DOT11\_WFD\_START\_GO\_REQUEST](oid-dot11-wfd-start-go-request.md)

 

 




