---
title: UEFI battery charging protocol
description: UEFI battery charging protocol
MSHAttr:
- 'PreferredSiteName:MSDN'
- 'PreferredLib:/library/windows/hardware'
ms.assetid: 5e9ef620-2ca1-4579-a715-19eec8933d57
---

# UEFI battery charging protocol


**Note**  Some information in this section may apply only to Windows 10 Mobile and certain processor architectures.

 

The UEFI battery charging protocol is used by the Microsoft UEFI battery charging application to communicate with the UEFI battery charging driver. The UEFI battery charging driver must implement this protocol if the device uses the Microsoft UEFI battery charging application.

**Important**  If the device uses a custom UEFI battery charging application instead of the Microsoft-provided application, the UEFI battery charging driver must not implement this protocol. The Windows Boot Manager will load the Microsoft UEFI battery charging application if the driver implements this protocol.

 

For more information about the Microsoft UEFI battery charging application, see [Battery charging in the boot environment](battery-charging-in-the-boot-environment.md).

## Protocol Interface


-   [EFI\_BATTERY\_CHARGING\_PROTOCOL](efi-battery-charging-protocol.md)

-   [EFI\_BATTERY\_CHARGING\_PROTOCOL.GetBatteryInformation](efi-battery-charging-protocolgetbatteryinformation.md)

-   [EFI\_BATTERY\_CHARGING\_PROTOCOL.GetBatteryStatus](efi-battery-charging-protocolgetbatterystatus.md)

-   [EFI\_BATTERY\_CHARGING\_PROTOCOL.ChargeBattery](efi-battery-charging-protocolchargebattery.md)

The Windows boot flow requires the battery to be charged to a certain level before it can load the main OS. The UEFI specification version 2.3 lacks a standard battery charging protocol.

### Sequence diagram

![uefi battery charging sequence diagram](images/uefibatterychargingsequencediagram.png)

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bp_OEMBringUp\p_oembringup%5D:%20UEFI%20battery%20charging%20protocol%20%20RELEASE:%20%284/22/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




