---
title: What's new in driver development
description: This section describes new features for driver development in WIN10_NEXT.
ms.date: 06/21/2021
ms.localizationpriority: medium
---

# <a name="top"></a>What's new in driver development

This section describes new features and updates for driver development in WIN10_NEXT.

## HID

Use Human Interface Device (HID) class devices over a Serial Peripheral Interface (SPI) bus.

- [Introduction to HID over SPI](./hid/hid-over-spi.md)
- [Architecture and overview for HID over the SPI transport](./hid/architecture-and-overview-for-spi.md)
- [Plug and Play support for HID over SPI](./hid/plug-and-play-for-spi.md)
- [HID over SPI power management](./hid/power-management-over-spi.md)
- [Error handling for HID over SPI](./hid/error-handling-for-spi.md)

New API pages:

- [hidspicx.h header](/windows-hardware/drivers/ddi/hidspicx)
- [**EVT_HIDSPICX_NOTIFY_POWERDOWN**](/windows-hardware/drivers/ddi/hidspicx/nc-hidspicx-evt_hidspicx_notify_powerdown)
- [**EVT_HIDSPICX_RESETDEVICE**](/windows-hardware/drivers/ddi/hidspicx/nc-hidspicx-evt_hidspicx_resetdevice)
- [**HIDSPICX_DEVICE_CONFIG**](/windows-hardware/drivers/ddi/hidspicx/ns-hidspicx-hidspicx_device_config)
- [**HIDSPICX_REPORT**](/windows-hardware/drivers/ddi/hidspicx/ns-hidspicx-hidspicx_report)
- [**HidSpiCxDeviceConfigure**](/windows-hardware/drivers/ddi/hidspicx/nf-hidspicx-hidspicxdeviceconfigure)
- [**HidSpiCxDeviceInitConfig**](/windows-hardware/drivers/ddi/hidspicx/nf-hidspicx-hidspicxdeviceinitconfig)
- [**HidSpiCxNotifyDeviceReset**](/windows-hardware/drivers/ddi/hidspicx/nf-hidspicx-hidspicxnotifydevicereset)

## Related Topics

For information on what was new for drivers in past Windows releases, see the following pages:

- [Driver development changes for Windows Server 2022](driver-changes-for-windows-server-2022.md)
- [Driver development changes for Windows 10, version 2004](driver-changes-for-windows-10-version-2004.md)
- [Driver development changes for Windows 10, version 1903](driver-changes-for-windows-10-version-1903.md)
- [Driver development changes for Windows 10, version 1809](driver-changes-for-windows-10-version-1809.md)

[Back to Top](#top)
