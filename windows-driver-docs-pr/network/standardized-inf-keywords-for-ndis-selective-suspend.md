---
title: Standardized INF Keywords for NDIS Selective Suspend
description: Standardized INF Keywords for NDIS Selective Suspend
ms.assetid: A45EE23D-1C60-4DA4-82A5-89DB5CE48E21
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Standardized INF Keywords for NDIS Selective Suspend


The following standardized INF keywords are defined to enable, disable, and configure parameters for NDIS selective suspend on a miniport driver:

[**\*SelectiveSuspend** INF Keyword](#selectivesuspend-keyword)

[**\*SSIdleTimeout** INF Keyword](#ssidletimeout-keyword)

[**\*SSIdleTimeoutScreenOff** INF Keyword](#ssidletimeoutscreenoff-keyword)


For more information about standardized INF keywords, see [Standardized INF Keywords for Network Devices](standardized-inf-keywords-for-network-devices.md).

## \*SelectiveSuspend INF Keyword


The INF file for the miniport driver that supports NDIS selective suspend must specify the **\*SelectiveSuspend** standardized INF keyword. After the driver is installed, administrators can update the **\*SelectiveSuspend** keyword value in the **Advanced** property page for the network adapter. For more information about advanced properties, see [Specifying Configuration Parameters for the Advanced Properties Page](specifying-configuration-parameters-for-the-advanced-properties-page.md).

**Note**   The miniport driver is automatically restarted after a change is made in the **Advanced** property page for the adapter.

 

The **\*SelectiveSuspend** INF keyword is an enumeration keyword. The following table describes the possible INF entries for the **\*SelectiveSuspend** INF keyword. The columns in this table describe the following attributes for an enumeration keyword:

<a href="" id="subkeyname"></a>SubkeyName  
The name of the keyword that you must specify in the INF file. This name also appears in the registry under the **NDI\\params\\** key for the network adapter.

<a href="" id="paramdesc"></a>ParamDesc  
The display text that is associated with SubkeyName.

**Note**  The independent hardware vendor (IHV) can define any descriptive text for the SubkeyName.

 

<a href="" id="value"></a>Value  
The enumeration integer value that is associated with each SubkeyName in the list.

<a href="" id="enumdesc"></a>EnumDesc  
The display text that is associated with each value that appears in the **Advanced** property page.

<table>
<colgroup>
<col width="25%" />
<col width="25%" />
<col width="25%" />
<col width="25%" />
</colgroup>
<thead>
<tr class="header">
<th align="left">SubkeyName</th>
<th align="left">ParamDesc</th>
<th align="left">Value</th>
<th align="left">EnumDesc</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td align="left"><p><strong>*SelectiveSuspend</strong></p></td>
<td align="left"><p>Selective suspend</p></td>
<td align="left"><p>0</p></td>
<td align="left"><p>Disabled</p></td>
</tr>
<tr class="even">
<td align="left"></td>
<td align="left"></td>
<td align="left"><p>1 (Default)</p></td>
<td align="left"><p>Enabled</p></td>
</tr>
</tbody>
</table>

 

The miniport driver must check the **\*SelectiveSuspend** keyword value in the registry before it advertises its support for NDIS selective suspend. If the **\*SelectiveSuspend** keyword has a value of zero, the miniport must not advertise support for any selective suspend capabilities. For more information, see [Reporting NDIS Selective Suspend Capabilities](reporting-ndis-selective-suspend-capabilities.md).

## \*SSIdleTimeout INF Keyword


The INF file for the miniport driver that supports NDIS selective suspend should specify the optional **\*SSIdleTimeout** standardized INF keyword. This keyword specifies the idle time-out period in units of seconds. If NDIS does not detect any activity on the network adapter for a period that exceeds the **\*SSIdleTimeout** value, NDIS starts a selective suspend operation by calling the miniport driver's [*MiniportIdleNotification*](https://msdn.microsoft.com/library/windows/hardware/hh464092) handler function.

After the driver is installed, administrators can update the **\*SSIdleTimeout** keyword value in the **Advanced** property page for the network adapter. For more information about advanced properties, see [Specifying Configuration Parameters for the Advanced Properties Page](specifying-configuration-parameters-for-the-advanced-properties-page.md).

**Note**   The miniport driver is automatically restarted after a change is made in the advanced property page for the adapter.

 

The **\*SSIdleTimeout** INF keyword is a numeric (**Int**) keyword. The following table describes the possible INF entries for the **\*SSIdleTimeout** INF keyword. The columns in the table describe the following attributes for an **Int** keyword:

<a href="" id="subkeyname"></a>SubkeyName  
The name of the keyword that you must specify in the INF file. This name also appears in the registry under the **NDI\\params\\** key for the network adapter.

<a href="" id="paramdesc"></a>ParamDesc  
The display text that is associated with SubkeyName.

**Note**  The independent hardware vendor (IHV) can define any descriptive text for the SubkeyName.

 

<a href="" id="default-value"></a>Default value  
The default value for the integer.

<a href="" id="minimum-value"></a>Minimum value  
The minimum value that is allowed for an integer.

<a href="" id="maximum-value"></a>Maximum value  
The maximum value that is allowed for an integer.

<table>
<colgroup>
<col width="20%" />
<col width="20%" />
<col width="20%" />
<col width="20%" />
<col width="20%" />
</colgroup>
<thead>
<tr class="header">
<th align="left">SubkeyName</th>
<th align="left">ParamDesc</th>
<th align="left">Default value</th>
<th align="left">Minimum value</th>
<th align="left">Maximum value</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td align="left"><p><strong>*SSIdleTimeout</strong></p></td>
<td align="left"><p>Selective suspend idle time-out in units of seconds</p></td>
<td align="left"><p>5</p></td>
<td align="left"><p>1</p></td>
<td align="left"><p>60</p></td>
</tr>
</tbody>
</table>

 

**Note**  NDIS reads the value of the **\*SSIdleTimeout** standardized INF keyword for every instance of the network adapter whose driver supports NDIS selective suspend. Miniport drivers should not read this keyword.

 

NDIS measures the idle time-out by using timers that are precise to within 30 percent of the **\*SSIdleTimeout** value. For example, if the **\*SSIdleTimeout** value is 10, the adapter is suspended between 10 to 13 seconds after NDIS first detects the adapter is idle.


## \*SSIdleTimeoutScreenOff INF Keyword


The INF file for the miniport driver that supports NDIS selective suspend should specify the optional **\*SSIdleTimeoutScreenOff** standardized INF keyword. This keyword specifies the idle time-out period in units of seconds and is only applicable when the screen is off. If NDIS does not detect any activity on the network adapter for a period that exceeds the **\*SSIdleTimeoutScreenOff** value after the screen is off, NDIS starts a selective suspend operation by calling the miniport driver's [*MiniportIdleNotification*](https://msdn.microsoft.com/library/windows/hardware/hh464092) handler function.

After the driver is installed, administrators can update the **\*SSIdleTimeoutScreenOff** keyword value in the **Advanced** property page for the network adapter. For more information about advanced properties, see [Specifying Configuration Parameters for the Advanced Properties Page](specifying-configuration-parameters-for-the-advanced-properties-page.md).

**Note**   The miniport driver is automatically restarted after a change is made in the advanced property page for the adapter.

 

The **\*SSIdleTimeoutScreenOff** INF keyword is a numeric (**Int**) keyword. The following table describes the possible INF entries for the **\*SSIdleTimeoutScreenOff** INF keyword. The columns in the table describe the following attributes for an **Int** keyword:

<a href="" id="subkeyname"></a>SubkeyName  
The name of the keyword that you must specify in the INF file. This name also appears in the registry under the **NDI\\params\\** key for the network adapter.

<a href="" id="paramdesc"></a>ParamDesc  
The display text that is associated with SubkeyName.

**Note**  The independent hardware vendor (IHV) can define any descriptive text for the SubkeyName.

 

<a href="" id="default-value"></a>Default value  
The default value for the integer.

<a href="" id="minimum-value"></a>Minimum value  
The minimum value that is allowed for an integer.

<a href="" id="maximum-value"></a>Maximum value  
The maximum value that is allowed for an integer.

<table>
<colgroup>
<col width="20%" />
<col width="20%" />
<col width="20%" />
<col width="20%" />
<col width="20%" />
</colgroup>
<thead>
<tr class="header">
<th align="left">SubkeyName</th>
<th align="left">ParamDesc</th>
<th align="left">Default value</th>
<th align="left">Minimum value</th>
<th align="left">Maximum value</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td align="left"><p><strong>*SSIdleTimeoutScreenOff</strong></p></td>
<td align="left"><p>Selective suspend idle time-out in units of seconds</p></td>
<td align="left"><p>3</p></td>
<td align="left"><p>1</p></td>
<td align="left"><p>60</p></td>
</tr>
</tbody>
</table>

 

**Note**  NDIS reads the value of the **\*SSIdleTimeoutScreenOff** standardized INF keyword for every instance of the network adapter whose driver supports NDIS selective suspend. Miniport drivers should not read this keyword.

**Note**  The maximum value is only for testing purposes. The HLK certification test will explicitly check and fail if the value is more than 5.

 
NDIS measures the idle time-out by using timers that are precise to within 30 percent of the **\*SSIdleTimeoutScreenOff** value. For example, if the **\*SSIdleTimeoutScreenOff** value is 5, the adapter is suspended between 5 to 6.5 seconds after NDIS first detects the adapter is idle.


 





