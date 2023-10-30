---
title: IStiDevice COM Interface
description: IStiDevice COM Interface
ms.date: 04/28/2023
---

# IStiDevice COM Interface

The **IStiDevice** COM interface provides applications with the ability to communicate with still image devices. Interface methods allow applications to send and receive data and commands, to run diagnostic tests, to receive notifications of [Still Image Device Events](still-image-device-events.md), and to obtain device capabilities and status information.

Access to the **IStiDevice** interface is obtained by calling the **CreateDevice** method of the [IStillImage COM Interface](istillimage-com-interface.md). Many of the **IStiDevice** interface's methods are implemented by calling like-named methods defined by the [IStiUSD COM Interface](istiusd-com-interface.md).

The following table lists and describes all of the methods supplied by the **IStiDevice** interface. The table indicates the types of clients that typically must call each method.

| Method | Description | Typical Callers |
|--|--|--|
| [**IStiDevice::DeviceReset**](/windows-hardware/drivers/ddi/sti/nf-sti-istidevice-devicereset) | Resets a still image device to a known state. | Image Acquisition APIs |
| [**IStiDevice::Diagnostic**](/windows-hardware/drivers/ddi/sti/nf-sti-istidevice-diagnostic) | Executes diagnostic tests on a still image device. | Scanners and Cameras Control Panel |
| [**IStiDevice::Escape**](/windows-hardware/drivers/ddi/sti/nf-sti-istidevice-escape) | Sends a request for a vendor-specific I/O operation to a still image device. | Image Acquisition APIs |
| [**IStiDevice::GetCapabilities**](/windows-hardware/drivers/ddi/sti/nf-sti-istidevice-getcapabilities) | Returns a still image device's capabilities. | Still image event monitor |
| [**IStiDevice::GetLastError**](/windows-hardware/drivers/ddi/sti/nf-sti-istidevice-getlasterror) | Returns the last known error associated with a still image device. | Image Acquisition APIs |
| [**IStiDevice::GetLastErrorInfo**](/windows-hardware/drivers/ddi/sti/nf-sti-istidevice-getlasterrorinfo) | Returns information about the last known error associated with a still image device. | Image Acquisition APIs |
| [**IStiDevice::GetLastNotificationData**](/windows-hardware/drivers/ddi/sti/nf-sti-istidevice-getlastnotificationdata) | Returns a description of the most recent event that occurred on a still image device. | Image Acquisition APIs |
| [**IStiDevice::GetStatus**](/windows-hardware/drivers/ddi/sti/nf-sti-istidevice-getstatus) | Returns a still image device's status information. | Image acquisition APIs and still image event monitor |
| [**IStiDevice::Initialize**](/windows-hardware/drivers/ddi/sti/nf-sti-istidevice-initialize) | Initializes an object instance. | Not called directly |
| [**IStiDevice::LockDevice**](/windows-hardware/drivers/ddi/sti/nf-sti-istidevice-lockdevice) | Locks a device for exclusive use by the caller. | All **IStiDevice** interface clients |
| [**IStiDevice::RawReadCommand**](/windows-hardware/drivers/ddi/sti/nf-sti-istidevice-rawreadcommand) | Reads command information from a still image device. | Image Acquisition APIs |
| [**IStiDevice::RawReadData**](/windows-hardware/drivers/ddi/sti/nf-sti-istidevice-rawreaddata) | Reads data from a still image device. | Image Acquisition APIs |
| [**IStiDevice::RawWriteCommand**](/windows-hardware/drivers/ddi/sti/nf-sti-istidevice-rawwritecommand) | Sends command information to a still image device. | Image Acquisition APIs |
| [**IStiDevice::RawWriteData**](/windows-hardware/drivers/ddi/sti/nf-sti-istidevice-rawwritedata) | Writes data to a still image device. | Image Acquisition APIs |
| [**IStiDevice::Release**](/windows-hardware/drivers/ddi/sti/nf-sti-istidevice-release) | Closes an object instance and removes access to the **IStiDevice** interface. | All **IStiDevice** interface clients |
| [**IStiDevice::Subscribe**](/windows-hardware/drivers/ddi/sti/nf-sti-istidevice-subscribe) | Registers the caller to receive notifications of device events. | Image Acquisition APIs |
| [**IStiDevice::UnLockDevice**](/windows-hardware/drivers/ddi/sti/nf-sti-istidevice-unlockdevice) | Unlocks a device. | All **IStiDevice** interface clients |
| [**IStiDevice::UnSubscribe**](/windows-hardware/drivers/ddi/sti/nf-sti-istidevice-unsubscribe) | Removes the caller from the list of applications registered to receive notification of device events. | Image Acquisition APIs |
