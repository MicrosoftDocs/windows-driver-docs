---
title: EFI_BATTERY_CHARGING_PROTOCOL
description: This protocol allows a UEFI driver to support charging of the main battery.
ms.date: 02/24/2023
ms.topic: reference
---

# EFI_BATTERY_CHARGING_PROTOCOL

This protocol allows a UEFI driver to support charging of the main battery.

## Syntax

```cpp
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

**GetBatteryStatus**  
Returns information about the current state of the main battery.

**ChargeBattery**  
Charges the main battery to the specified level using the specified maximum current.

**Revision**  
The revision to which the EFI_BATTERY_CHARGING_PROTOCOL adheres. All future revisions must be backward compatible. If a future version is not backward compatible, a different GUID must be used.

The current revision is 0x00010002, although revision 0x00010001 is also supported. For more information about which functions are supported in each version of the protocol, see the remarks section below.

**GetBatteryInformation**  
Returns information about the current state of the main battery. This function is similar to **GetBatteryStatus**, but it provides more information than **GetBatteryStatus**.

## Remarks

The following table lists the functions that are supported in each version of the EFI_BATTERY_CHARGING_PROTOCOL protocol.

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

[EFI_BATTERY_CHARGING_PROTOCOL.GetBatteryInformation](efi-battery-charging-protocolgetbatteryinformation.md)  

[EFI_BATTERY_CHARGING_PROTOCOL.GetBatteryStatus](efi-battery-charging-protocolgetbatterystatus.md)  

[EFI_BATTERY_CHARGING_PROTOCOL.ChargeBattery](efi-battery-charging-protocolchargebattery.md)  
