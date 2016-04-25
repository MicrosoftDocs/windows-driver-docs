---
title: EFI\_BATTERY\_CHARGING\_PROTOCOL
description: EFI\_BATTERY\_CHARGING\_PROTOCOL
MSHAttr:
- 'PreferredSiteName:MSDN'
- 'PreferredLib:/library/windows/hardware'
ms.assetid: 978d063e-f864-44be-9f58-4e4c6b2193b8
---

# EFI\_BATTERY\_CHARGING\_PROTOCOL


This protocol allows a UEFI driver to support charging of the main battery.

## Syntax


``` syntax
// {840CB643-8198-428a-A8B3-A072CE57CDB9}
#define EFI_BATTERY_CHARGING_PROTOCOL_GUID \
  {0x840cb643, 0x8198, 0x428a, 0xa8, 0xb3, 0xa0, 0x72, 0xce, 0x57, 0xcd, 0xb9};

typedef struct _EFI_BATTERY_CHARGING_PROTOCOL {
  EFI_BATTERY_CHARGING_GET_BATTERY_STATUS         GetBatteryStatus;
  EFI_BATTERY_CHARGING_CHARGE_BATTERY             ChargeBattery; 
  UINT32                                          Revision;
  EFI_BATTERY_CHARGING_GET_BATTERY_INFORMATION    GetBatteryInformation;
} EFI_BATTERY_CHARGING_PROTOCOL;
```

## Members


<a href="" id="getbatterystatus"></a>**GetBatteryStatus**  
Returns information about the current state of the main battery.

<a href="" id="chargebattery"></a>**ChargeBattery**  
Charges the main battery to the specified level using the specified maximum current.

<a href="" id="revision"></a>**Revision**  
The revision to which the EFI\_BATTERY\_CHARGING\_PROTOCOL adheres. All future revisions must be backward compatible. If a future version is not backward compatible, a different GUID must be used.

The current revision is 0x00010002, although revision 0x00010001 is also supported. For more information about which functions are supported in each version of the protocol, see the remarks section below.

<a href="" id="getbatteryinformation"></a>**GetBatteryInformation**  
Returns information about the current state of the main battery. This function is similar to **GetBatteryStatus**, but it provides more information than **GetBatteryStatus**.

## Remarks


The following table lists the functions that are supported in each version of the EFI\_BATTERY\_CHARGING\_PROTOCOL protocol.

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<thead>
<tr class="header">
<th>Revision 0x00010002</th>
<th>Revision 0x00010001</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p><strong>GetBatteryInformation</strong></p>
<p><strong>GetBatteryStatus</strong></p>
<p><strong>ChargeBattery</strong></p></td>
<td><p><strong>GetBatteryStatus</strong></p>
<p><strong>ChargeBattery</strong></p></td>
</tr>
</tbody>
</table>

 

## Requirements


**Header:** User generated

## Related topics


[UEFI battery charging protocol](uefi-battery-charging-protocol.md)

[EFI\_BATTERY\_CHARGING\_PROTOCOL.GetBatteryInformation](efi-battery-charging-protocolgetbatteryinformation.md)

[EFI\_BATTERY\_CHARGING\_PROTOCOL.GetBatteryStatus](efi-battery-charging-protocolgetbatterystatus.md)

[EFI\_BATTERY\_CHARGING\_PROTOCOL.ChargeBattery](efi-battery-charging-protocolchargebattery.md)

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bp_OEMBringUp\p_oembringup%5D:%20EFI_BATTERY_CHARGING_PROTOCOL%20%20RELEASE:%20%284/22/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")





