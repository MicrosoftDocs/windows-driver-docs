---
title: UPS\\Status Registry Entries
description: UPS\\Status Registry Entries
ms.assetid: c24ef185-ba8d-4cfd-9d33-b70682905f00
keywords: ["UPS minidrivers WDK , registry entries", "UPS\Status registry key", "status registry entries WDK UPS", "UPS registry entries WDK", "registry WDK UPS"]
---

# UPS\\Status Registry Entries


## <span id="ddk_ups_status_registry_entries_kg"></span><span id="DDK_UPS_STATUS_REGISTRY_ENTRIES_KG"></span>


The following registry entries, under the **UPS**\\**Status** key, must be set by UPS minidrivers.

### <span id="BatteryCapacity"></span><span id="batterycapacity"></span><span id="BATTERYCAPACITY"></span>BatteryCapacity

<span id="Value_Name"></span><span id="value_name"></span><span id="VALUE_NAME"></span>Value Name  
**BatteryCapacity**

<span id="Value_Type"></span><span id="value_type"></span><span id="VALUE_TYPE"></span>Value Type  
REG\_DWORD

<span id="Value"></span><span id="value"></span><span id="VALUE"></span>Value  
The percent of battery capacity remaining in the UPS. This percent is represented as a value in the range of 0 through 100. (The displayed value is rounded to the nearest integer.)

<span id="Default_Value"></span><span id="default_value"></span><span id="DEFAULT_VALUE"></span>Default Value  
0

### <span id="BatteryStatus"></span><span id="batterystatus"></span><span id="BATTERYSTATUS"></span>BatteryStatus

<span id="Value_Name"></span><span id="value_name"></span><span id="VALUE_NAME"></span>Value Name  
**BatteryStatus**

<span id="Value_Type"></span><span id="value_type"></span><span id="VALUE_TYPE"></span>Value Type  
REG\_DWORD

<span id="Value"></span><span id="value"></span><span id="VALUE"></span>Value  
The current status of the UPS batteries. Values are listed in the following table.

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<thead>
<tr class="header">
<th align="left">Value</th>
<th align="left">Meaning</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td align="left"><p>0</p></td>
<td align="left"><p>The battery status is unknown.</p></td>
</tr>
<tr class="even">
<td align="left"><p>1</p></td>
<td align="left"><p>The batteries are OK.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>2</p></td>
<td align="left"><p>The batteries need to be replaced.</p></td>
</tr>
</tbody>
</table>

 

<span id="Default_Value"></span><span id="default_value"></span><span id="DEFAULT_VALUE"></span>Default Value  
0

### <span id="CommStatus"></span><span id="commstatus"></span><span id="COMMSTATUS"></span>CommStatus

<span id="Value_Name"></span><span id="value_name"></span><span id="VALUE_NAME"></span>Value Name  
**CommStatus**

<span id="Value_Type"></span><span id="value_type"></span><span id="VALUE_TYPE"></span>Value Type  
REG\_DWORD

<span id="Value"></span><span id="value"></span><span id="VALUE"></span>Value  
The status of the communication path to the UPS. Values are listed in the following table.

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<thead>
<tr class="header">
<th align="left">Value</th>
<th align="left">Meaning</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td align="left"><p>0</p></td>
<td align="left"><p>The communication path to the UPS is unknown.</p></td>
</tr>
<tr class="even">
<td align="left"><p>1</p></td>
<td align="left"><p>The communication path to the UPS is OK.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>2</p></td>
<td align="left"><p>The communication path to the UPS has been lost.</p></td>
</tr>
</tbody>
</table>

 

<span id="Default_Value"></span><span id="default_value"></span><span id="DEFAULT_VALUE"></span>Default Value  
1

### <span id="FirmwareRev"></span><span id="firmwarerev"></span><span id="FIRMWAREREV"></span>FirmwareRev

<span id="Value_Name"></span><span id="value_name"></span><span id="VALUE_NAME"></span>Value Name  
**FirmwareRev**

<span id="Value_Type"></span><span id="value_type"></span><span id="VALUE_TYPE"></span>Value Type  
REG\_SZ

<span id="Value"></span><span id="value"></span><span id="VALUE"></span>Value  
Reports the UPS firmware revision as a displayable string.

<span id="Default_Value_"></span><span id="default_value_"></span><span id="DEFAULT_VALUE_"></span>Default Value:  
""

### <span id="SerialNumber"></span><span id="serialnumber"></span><span id="SERIALNUMBER"></span>SerialNumber

<span id="Value_Name"></span><span id="value_name"></span><span id="VALUE_NAME"></span>Value Name  
**SerialNumber**

<span id="Value_Type"></span><span id="value_type"></span><span id="VALUE_TYPE"></span>Value Type  
REG\_SZ

<span id="Value"></span><span id="value"></span><span id="VALUE"></span>Value  
Reports the UPS serial number as a displayable string.

<span id="Default_Value_"></span><span id="default_value_"></span><span id="DEFAULT_VALUE_"></span>Default Value:  
""

### <span id="TotalUPSRuntime"></span><span id="totalupsruntime"></span><span id="TOTALUPSRUNTIME"></span>TotalUPSRuntime

<span id="Value_Name"></span><span id="value_name"></span><span id="VALUE_NAME"></span>Value Name  
**TotalUPSRuntime**

<span id="Value_Type"></span><span id="value_type"></span><span id="VALUE_TYPE"></span>Value Type  
REG\_DWORD

<span id="Value"></span><span id="value"></span><span id="VALUE"></span>Value  
The amount of remaining UPS run time, in minutes.

<span id="Default_Value"></span><span id="default_value"></span><span id="DEFAULT_VALUE"></span>Default Value  
0

### <span id="UtilityPowerStatus"></span><span id="utilitypowerstatus"></span><span id="UTILITYPOWERSTATUS"></span>UtilityPowerStatus

<span id="Value_Name"></span><span id="value_name"></span><span id="VALUE_NAME"></span>Value Name  
**UtilityPowerStatus**

<span id="Value_Type"></span><span id="value_type"></span><span id="VALUE_TYPE"></span>Value Type  
REG\_DWORD

<span id="Value_"></span><span id="value_"></span><span id="VALUE_"></span>Value:  
Reports the status of utility-supplied power into the UPS. Values are listed in the following table.

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<thead>
<tr class="header">
<th align="left">Value</th>
<th align="left">Meaning</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td align="left"><p>0</p></td>
<td align="left"><p>The status of utility-supplied power is unknown.</p></td>
</tr>
<tr class="even">
<td align="left"><p>1</p></td>
<td align="left"><p>Utility-supplied power is OK.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>2</p></td>
<td align="left"><p>A power failure has occurred.</p></td>
</tr>
</tbody>
</table>

 

<span id="Default_Value"></span><span id="default_value"></span><span id="DEFAULT_VALUE"></span>Default Value  
0

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[battery\battery]:%20UPS\Status%20Registry%20Entries%20%20RELEASE:%20%286/7/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


