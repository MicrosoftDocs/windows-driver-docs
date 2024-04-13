---
title: IStiDeviceControl COM Interface
description: IStiDeviceControl COM Interface
ms.date: 04/20/2017
---

# IStiDeviceControl COM Interface





The **IStiDeviceControl** COM interface provides [User-Mode Still Image Minidrivers](overview-of-sti-components.md#ddk-user-mode-still-image-minidrivers-si) with access to information stored within the [Still Image Event Monitor](overview-of-sti-components.md#ddk-still-image-event-monitor-si). It also allows minidrivers to write information into the still image error log.

The methods defined by the **IStiDeviceControl** interface include the following:

<a href="" id="istidevicecontrol--addref"></a>[**IStiDeviceControl::AddRef**](/windows-hardware/drivers/ddi/stiusd/nf-stiusd-istidevicecontrol-addref)  
Increments the **IStiDeviceControl** interface's reference count.

<a href="" id="istidevicecontrol--getmydeviceopenmode"></a>[**IStiDeviceControl::GetMyDeviceOpenMode**](/windows-hardware/drivers/ddi/stiusd/nf-stiusd-istidevicecontrol-getmydeviceopenmode)  
Allows a still image minidriver to obtain the transfer mode that an application specified when it created an instance of a still image device.

<a href="" id="istidevicecontrol--getmydeviceportname"></a>[**IStiDeviceControl::GetMyDevicePortName**](/windows-hardware/drivers/ddi/stiusd/nf-stiusd-istidevicecontrol-getmydeviceportname)  
Allows a still image minidriver to obtain a device's port name.

<a href="" id="istidevicecontrol--release"></a>[**IStiDeviceControl::Release**](/windows-hardware/drivers/ddi/stiusd/nf-stiusd-istidevicecontrol-release)  
Closes an instance COM object that defines the **IStiDeviceControl** interface, and removes access to the interface.

<a href="" id="istidevicecontrol--writetoerrorlog"></a>[**IStiDeviceControl::WriteToErrorLog**](/windows-hardware/drivers/ddi/stiusd/nf-stiusd-istidevicecontrol-writetoerrorlog)  
Allows a still image minidriver to write a message into the still image error log.

 

