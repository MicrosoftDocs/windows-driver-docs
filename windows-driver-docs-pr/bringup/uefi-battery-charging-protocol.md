---
title: UEFI battery charging protocol
description: The UEFI battery charging protocol is used by the Microsoft UEFI battery charging application to communicate with the UEFI battery charging driver. 
ms.date: 08/19/2021
---

# UEFI battery charging protocol

> [!NOTE]
> Some information in this section may apply only to Windows 10 Mobile and certain processor architectures.

The UEFI battery charging protocol is used by the Microsoft UEFI battery charging application to communicate with the UEFI battery charging driver. The UEFI battery charging driver must implement this protocol if the device uses the Microsoft UEFI battery charging application.

> [!IMPORTANT]
> If the device uses a custom UEFI battery charging application instead of the Microsoft-provided application, the UEFI battery charging driver must not implement this protocol. The Windows Boot Manager will load the Microsoft UEFI battery charging application if the driver implements this protocol.

For more information about the Microsoft UEFI battery charging application, see [Battery charging in the boot environment](battery-charging-in-the-boot-environment.md).

## Protocol Interface

- [EFI_BATTERY_CHARGING_PROTOCOL](efi-battery-charging-protocol.md)

- [EFI_BATTERY_CHARGING_PROTOCOL.GetBatteryInformation](efi-battery-charging-protocolgetbatteryinformation.md)

- [EFI_BATTERY_CHARGING_PROTOCOL.GetBatteryStatus](efi-battery-charging-protocolgetbatterystatus.md)

- [EFI_BATTERY_CHARGING_PROTOCOL.ChargeBattery](efi-battery-charging-protocolchargebattery.md)

The Windows boot flow requires the battery to be charged to a certain level before it can load the main OS. The UEFI specification version 2.3 lacks a standard battery charging protocol.

### Sequence diagram

![uefi battery charging sequence diagram.](images/uefibatterychargingsequencediagram.png)
