---
title: EFI\_BATTERY\_CHARGING\_COMPLETION\_TOKEN
author: windows-driver-content
description: EFI\_BATTERY\_CHARGING\_COMPLETION\_TOKEN
MSHAttr:
- 'PreferredSiteName:MSDN'
- 'PreferredLib:/library/windows/hardware'
ms.assetid: 1151643e-8b22-4034-b043-ac4d44c01082
---

# EFI\_BATTERY\_CHARGING\_COMPLETION\_TOKEN


This structure defines the completion token used by [EFI\_BATTERY\_CHARGING\_PROTOCOL.ChargeBattery](efi-battery-charging-protocolchargebattery.md).

## Syntax


``` syntax
typedef struct _EFI_BATTERY_CHARGING_COMPLETION_TOKEN {
  EFI_EVENT Event;
  EFI_BATTERY_CHARGING_STATUS Status;
} EFI_BATTERY_CHARGING_COMPLETION_TOKEN;
```

## Members


<a href="" id="event"></a>**Event**  
The event to signal after charge request is finished. The type of event must be EVT\_NOTIFY\_SIGNAL.

<a href="" id="status"></a>**Status**  
The result of the completed operation.

## Remarks


EFI\_BATTERY\_CHARGING\_COMPLETION\_TOKEN is returned in the *CompletionToken* parameter of [EFI\_BATTERY\_CHARGING\_PROTOCOL.ChargeBattery](efi-battery-charging-protocolchargebattery.md).

## Requirements


**Header:** User generated

## Related topics
[EFI\_BATTERY\_CHARGING\_PROTOCOL.ChargeBattery](efi-battery-charging-protocolchargebattery.md)  
[EFI\_BATTERY\_CHARGING\_STATUS](efi-battery-charging-status.md)  

--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bp_OEMBringUp\p_oembringup%5D:%20EFI_BATTERY_CHARGING_COMPLETION_TOKEN%20%20RELEASE:%20%284/22/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


