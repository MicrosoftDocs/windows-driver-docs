---
title: What's new in driver development for Windows 11
description: This section describes new features for driver development in Windows 11.
ms.date: 05/23/2022
---

# <a name="top"></a>What's new in driver development for Windows 11, version 21H2

This section describes new features and updates for driver development in Windows 11, version 21H2.

## Camera

- [Digital Window overview](./stream/digital-window-overview.md)
- [Privacy shutter notification](./stream/privacy-shutter-notification.md)
- [Create device property keys from the MS OS descriptor in USB Video Class (UVC) firmware](./stream/create-camera-device-property-keys-from-ms-os-descriptor.md)
- [Microsoft extensions to USB Video Class 1.5 specification](./stream/uvc-extensions-1-5.md) (Updated)
- [Network camera design guide](./stream/network-camera-design-guide.md) (Updated)

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

## Print devices

- [Print support app design guide](./devapps/print-support-app-design-guide.md)
- [Print support app association](./devapps/print-support-app-association.md)

[Back to Top](#top)
