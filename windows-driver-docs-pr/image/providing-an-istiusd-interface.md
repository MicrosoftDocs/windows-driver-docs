---
title: Provide an IStiUSD Interface
description: Provide an IStiUSD interface
ms.date: 05/03/2023
---

# Provide an IStiUSD interface

WIA builds on STI. In order to ensure the integration of a WIA minidriver with STI, the minidriver must implement an interface derived from the [IStiUSD interface methods](/windows-hardware/drivers/ddi/_image/index). This interface must be present in a WIA minidriver. The **IStiUSD** interface is used for managing devices (such as loading a driver), and is the means by which the [IStiDevice interface methods](/windows-hardware/drivers/ddi/_image/index) communicates with still image devices. A minidriver must fully implement an interface derived from the [**IStiUSD::Initialize**](/windows-hardware/drivers/ddi/stiusd/nf-stiusd-istiusd-initialize) method in order to be loaded by the WIA service.

Typically, **IStiUSD** interface methods are called by similarly named methods defined by the **IStiDevice** interface. Minidrivers typically implement **IStiUSD** interface methods by calling the appropriate kernel-mode driver. Each minidriver must define all interface methods, but if a method is not needed it can simply return STIERR\_UNSUPPORTED.

See the *wiacam* camera sample minidriver file, *IStiUSD.cpp*, for an example of how a minidriver implements the **IStiUSD** interface.

The following table lists and describes all of the methods defined by the **IStiUSD** interface. Methods that must be implemented or conditionally implemented by WIA minidrivers are identified.

| Method | Description |
|--|--|
| [**IStiUSD::DeviceReset**](/windows-hardware/drivers/ddi/stiusd/nf-stiusd-istiusd-devicereset) | Resets a still image device to a known initialized state. |
| [**IStiUSD::Diagnostic**](/windows-hardware/drivers/ddi/stiusd/nf-stiusd-istiusd-diagnostic) | Runs diagnostic tests on a still image device. A WIA minidriver must implement this method. |
| [**IStiUSD::Escape**](/windows-hardware/drivers/ddi/stiusd/nf-stiusd-istiusd-escape) | Performs a vendor-specific I/O operation on a still image device. |
| [**IStiUSD::GetCapabilities**](/windows-hardware/drivers/ddi/stiusd/nf-stiusd-istiusd-getcapabilities) | Returns a still image device's capabilities. |
| [**IStiUSD::GetLastErrorInfo**](/windows-hardware/drivers/ddi/stiusd/nf-stiusd-istiusd-getlasterrorinfo) | Returns information about the last known error associated with a still image device. |
| [**IStiUSD::GetNotificationData**](/windows-hardware/drivers/ddi/stiusd/nf-stiusd-istiusd-getnotificationdata) | Returns a description of the most recent event that occurred on a still image device. |
| [**IStiUSD::GetStatus**](/windows-hardware/drivers/ddi/stiusd/nf-stiusd-istiusd-getstatus) | Returns the status of a still image device. A WIA minidriver must implement this method if its device has objects, such as buttons, that can generate events. |
| [**IStiUSD::Initialize**](/windows-hardware/drivers/ddi/stiusd/nf-stiusd-istiusd-initialize) | Initializes an instance of the COM object that defines the [IStiUSD interface](/windows-hardware/drivers/ddi/_image/index). A WIA minidriver must implement this method. |
| [**IStiUSD::LockDevice**](/windows-hardware/drivers/ddi/stiusd/nf-stiusd-istiusd-lockdevice) | Locks a device for exclusive use by the caller. A WIA minidriver must implement this method. |
| [**IStiUSD::RawReadCommand**](/windows-hardware/drivers/ddi/stiusd/nf-stiusd-istiusd-rawreadcommand) | Reads command information from a still image device. |
| [**IStiUSD::RawReadData**](/windows-hardware/drivers/ddi/stiusd/nf-stiusd-istiusd-rawreaddata) | Reads data from a still image device. |
| [**IStiUSD::RawWriteCommand**](/windows-hardware/drivers/ddi/stiusd/nf-stiusd-istiusd-rawwritecommand) | Writes command information to a still image device. |
| [**IStiUSD::RawWriteData**](/windows-hardware/drivers/ddi/stiusd/nf-stiusd-istiusd-rawwritedata) | Writes data to a still image device. |
| [**IStiUSD::SetNotificationHandle**](/windows-hardware/drivers/ddi/stiusd/nf-stiusd-istiusd-setnotificationhandle) | Specifies an event handle that the minidriver should use to inform the caller of device events. A WIA minidriver must implement this method if its device has objects, such as buttons, that can generate events. |
| [**IStiUSD::UnLockDevice**](/windows-hardware/drivers/ddi/stiusd/nf-stiusd-istiusd-unlockdevice) | Closes the device port. A WIA minidriver must implement this method. |
