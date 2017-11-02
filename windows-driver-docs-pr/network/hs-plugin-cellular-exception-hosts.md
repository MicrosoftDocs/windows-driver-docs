---
title: HS_PLUGIN_CELLULAR_EXCEPTION_HOSTS structure
author: windows-driver-content
description: The HS_PLUGIN_CELLULAR_EXCEPTION_HOSTS structure contains the list of hosts that the plugin requires to be connected over a cellular bearer only during the authentication process.
ms.assetid: cc7ad05b-d03b-463a-9d22-1982aee882e8
keywords: 
- HS_PLUGIN_CELLULAR_EXCEPTION_HOSTS structure Network Drivers Starting with Windows Vista
- PHS_PLUGIN_CELLULAR_EXCEPTION_HOSTS structure pointer Network Drivers Starting with Windows Vista
ms.author: windowsdriverdev
ms.date: 07/31/2017 
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# HS\_PLUGIN\_CELLULAR\_EXCEPTION\_HOSTS structure

[!include[Wi-Fi Hotspot Offloading deprecation](wi-fi-hotspot-offloading-deprecation.md)]


The **HS\_PLUGIN\_CELLULAR\_EXCEPTION\_HOSTS** structure contains the list of hosts that the plugin requires to be connected over a cellular bearer only during the authentication process. This is an optional capability that can be requested by the plugin. For more information, see [**HS\_PLUGIN\_QUERY\_CELLULAR\_EXCEPTION\_HOSTS**](hs-plugin-query-cellular-exception-hosts.md).

Syntax
------

```ManagedCPlusPlus
typedef struct _HS_PLUGIN_CELLULAR_EXCEPTION_HOSTS {
  DWORD               dwCount;
  HS_PLUGIN_HOST_NAME pExceptions[*];
  HS_PLUGIN_HOST_NAME pExceptions[1];
} HS_PLUGIN_CELLULAR_EXCEPTION_HOSTS, *PHS_PLUGIN_CELLULAR_EXCEPTION_HOSTS;
```

Members
-------

**dwCount**  
The number of host names in the list pointed to by **pExceptions**.

**pExceptions**  
Used if MIDL is utilized. Unique, size is (dwCount).

Pointer to the list of host names.

**pExceptions**  
Used if MIDL is not utilized.

Pointer to the list of host names.

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


[**HS\_PLUGIN\_QUERY\_CELLULAR\_EXCEPTION\_HOSTS**](hs-plugin-query-cellular-exception-hosts.md)

[Microsoft Interface Definition Language](https://msdn.microsoft.com//library/windows/desktop/aa367091)

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bnetvista\netvista%5D:%20HS_PLUGIN_CELLULAR_EXCEPTION_HOSTS%20structure%20%20RELEASE:%20%287/31/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


