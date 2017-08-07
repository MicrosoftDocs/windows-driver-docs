---
title: OID\_DOT11\_AUTO\_CONFIG\_ENABLED
author: windows-driver-content
description: OID\_DOT11\_AUTO\_CONFIG\_ENABLED
ms.assetid: aefa79fb-e156-4b67-9008-ef88f4f32302
ms.author: windowsdriverdev
ms.date: 08/08/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
keywords:
 - OID_DOT11_AUTO_CONFIG_ENABLED Network Drivers Starting with Windows Vista
---

# OID\_DOT11\_AUTO\_CONFIG\_ENABLED


**Important**  The [Native 802.11 Wireless LAN](https://msdn.microsoft.com/library/windows/hardware/ff560690) interface is deprecated in Windows 10 and later. Please use the WLAN Device Driver Interface (WDI) instead. For more information about WDI, see [WLAN Universal Windows driver model](https://msdn.microsoft.com/library/windows/hardware/dn897672).

 

When set, the OID\_DOT11\_AUTO\_CONFIG\_ENABLED object identifier (OID) requests that the miniport driver set the value of the Extensible Station (ExtSTA) **msDot11AutoConfigEnabled** management information base (MIB) object to the specified value.

When queried, this OID requests that the miniport driver return the value of the **msDot11AutoConfigEnabled** MIB object.

The **msDot11AutoConfigEnabled** MIB object specifies the current settings for the following automatic configuration modes:

<a href="" id="automatic-media-access-control--mac--configuration-"></a>Automatic media access control (MAC) configuration.  
When automatic MAC configuration is enabled, the 802.11 station manages the configuration of the MAC and can fail set requests that would change MAC related parameters.

For more information about this mode, see [Automatic MAC Configuration](https://msdn.microsoft.com/library/windows/hardware/ff543813).

<a href="" id="automatic-phy-configuration-"></a>Automatic PHY configuration.  
When automatic PHY configuration is enabled, the 802.11 station manages the configuration of the PHY and can fail set requests that would change PHY related parameters.

For more information about this mode, see [Automatic PHY Configuration](https://msdn.microsoft.com/library/windows/hardware/ff543816).

The data type for OID\_DOT11\_AUTO\_CONFIG\_ENABLED is a ULONG value, with the automatic configuration settings defined through the following bitmask:

<a href="" id="dot11-phy-auto-config-enabled-flag"></a>DOT11\_PHY\_AUTO\_CONFIG\_ENABLED\_FLAG  
If this bit is set, the miniport driver has enabled automatic PHY configuration.

<a href="" id="dot11-mac-auto-config-enabled-flag"></a>DOT11\_MAC\_AUTO\_CONFIG\_ENABLED\_FLAG  
If this bit is set, the miniport driver has enabled automatic MAC configuration.

The default for the **msDot11AutoConfigEnabled** MIB object has the following flags set:

-   DOT11\_PHY\_AUTO\_CONFIG\_ENABLED\_FLAG

-   DOT11\_MAC\_AUTO\_CONFIG\_ENABLED\_FLAG

The miniport driver must set this MIB object to its default if any of the following occurs:

-   The miniport driver's [*MiniportInitializeEx*](miniportinitializeex.md) function is called.

-   A method request of [OID\_DOT11\_RESET\_REQUEST](oid-dot11-reset-request.md) is made to reset the media access control (MAC) layer of the 802.11 station and the **bSetDefaultMIB** member of the DOT11\_RESET\_REQUEST structure is **TRUE**.

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


[Native 802.11 Wireless LAN OIDs](https://msdn.microsoft.com/library/windows/hardware/ff560691)

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bnetvista\netvista%5D:%20OID_DOT11_AUTO_CONFIG_ENABLED%20%20RELEASE:%20%288/3/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


