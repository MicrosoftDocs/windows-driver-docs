---
title: OID\_DOT11\_SUPPORTED\_POWER\_LEVELS
author: windows-driver-content
description: When queried, the OID\_DOT11\_SUPPORTED\_POWER\_LEVELS OID requests that the miniport driver return the following for the current PHY type on the 802.11 station
ms.assetid: c285ff65-f6c0-444d-961d-614c50c86a1c
ms.author: windowsdriverdev
ms.date: 08/08/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
keywords: 
 -OID_DOT11_SUPPORTED_POWER_LEVELS Network Drivers Starting with Windows Vista
---

# OID\_DOT11\_SUPPORTED\_POWER\_LEVELS


**Important**  The [Native 802.11 Wireless LAN](https://msdn.microsoft.com/library/windows/hardware/ff560690) interface is deprecated in Windows 10 and later. Please use the WLAN Device Driver Interface (WDI) instead. For more information about WDI, see [WLAN Universal Windows driver model](https://msdn.microsoft.com/library/windows/hardware/dn897672).

 

When queried, the OID\_DOT11\_SUPPORTED\_POWER\_LEVELS OID requests that the miniport driver return the following for the current PHY type on the 802.11 station:

-   The number of transmit power levels supported by the Physical Media Dependent (PMD) sublayer of the PHY.

-   The transmit power for all the supported levels, in milliwatts (mWs).

The data type for OID\_DOT11\_SUPPORTED\_POWER\_LEVELS is the DOT11\_SUPPORTED\_POWER\_LEVELS structure.

```ManagedCPlusPlus
    typedef struct _DOT11_SUPPORTED_POWER_LEVELS {
         ULONG uNumOfSupportedPowerLevels;
         ULONG uTxPowerLevelValues[8];
    } DOT11_SUPPORTED_POWER_LEVELS, *PDOT11_SUPPORTED_POWER_LEVELS;
  
```

This structure includes the following members:

<a href="" id="unumofsupportedpowerlevels"></a>**uNumOfSupportedPowerLevels**  
Number of supported power levels. **uNumOfSupportedPowerLevels** must have a value from 1 through 8.

<a href="" id="utxpowerlevelvalues"></a>**uTxPowerLevelValues**  
An array of the supported transmit power levels in units of milliwatts (mWs). Each power level must be a value from 0 through 1000.

The miniport driver must use the power level specified in **uTxPowerLevelValues\[0\]** as its default power level. The miniport driver must set the power level of the 802.11 station to this default through its [*MiniportInitializeEx*](https://msdn.microsoft.com/library/windows/hardware/ff559389) function or when reset through a method request of [OID\_DOT11\_RESET\_REQUEST](oid-dot11-reset-request.md).

If the miniport driver is operating in Extensible Station (ExtSTA) mode, the current PHY type is determined through the ExtSTA **msDot11CurrentPhyID** management information base (MIB) object. This MIB object specifies the index of the current PHY type within the 802.11 station's list of supported PHY types. For more information about **msDot11CurrentPhyID**, see [OID\_DOT11\_CURRENT\_PHY\_ID](oid-dot11-current-phy-id.md).

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
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bnetvista\netvista%5D:%20OID_DOT11_SUPPORTED_POWER_LEVELS%20%20RELEASE:%20%288/8/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


