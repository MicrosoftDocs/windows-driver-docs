---
title: DOT11_PMKID_VALUE
author: windows-driver-content
description: Important  The Native 802.11 Wireless LAN interface is deprecated in Windows 10 and later.
ms.assetid: 8b23bb59-251a-4898-b929-b97ff6802744
ms.author: windowsdriverdev
ms.date: 08/08/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
keywords: 
 -DOT11_PMKID_VALUE
---

# DOT11\_PMKID\_VALUE


**Important**  The [Native 802.11 Wireless LAN](https://msdn.microsoft.com/library/windows/hardware/ff560690) interface is deprecated in Windows 10 and later. Please use the WLAN Device Driver Interface (WDI) instead. For more information about WDI, see [WLAN Universal Windows driver model](https://msdn.microsoft.com/library/windows/hardware/dn897672).

 

The **DOT11\_PMKID\_VALUE** array defines a pairwise master key identifier (PMKID).

```ManagedCPlusPlus
typedef UCHAR DOT11_PMKID_VALUE[16];
```

**DOT11\_PMKID\_VALUE**  
The PMKID value. For more information about the format of the PMKID value, refer to Clause 8.5.1.2 of the IEEE 802.11i-2004 standard.

****  

Remarks
-------

An 802.11 station that supports RSNA authentication algorithms uses PMKID values for pre-authentication when it connects to an infrastructure basic service set (BSS) network.

For more information about the PMKID, refer to Clause 8.5.1.2 of the IEEE 802.11i-2004 standard.

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
<td><p>Available in Windows Vista and later versions of the Windows operating systems.</p></td>
</tr>
<tr class="even">
<td><p>Header</p></td>
<td>Windot11.h (include Ndis.h)</td>
</tr>
</tbody>
</table>

## See also


[OID\_DOT11\_PMKID\_LIST](oid-dot11-pmkid-list.md)

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bnetvista\netvista%5D:%20DOT11_PMKID_VALUE%20%20RELEASE:%20%288/8/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


