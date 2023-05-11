---
title: WIA driver command support
description: WIA driver command support
ms.date: 05/10/2023
---

# WIA driver command support

A WIA device command is a request sent by the WIA service (on behalf of the imaging application) to the WIA minidriver, instructing it to perform a particular action.

The following is a list of WIA device commands that can be issued to a minidriver:

| Command | Meaning |
|--|--|
| WIA_CMD_CHANGE_DOCUMENT | Change to the next document (issued to multidocument scanners only). |
| WIA_CMD_DELETE_ALL_ITEMS | Delete the driver item tree. |
| WIA_CMD_DIAGNOSTIC | Reserved by Microsoft. |
| WIA_CMD_SYNCHRONIZE | Rebuild the driver item tree. All minidrivers must support this command. |
| WIA_CMD_TAKE_PICTURE | Take a picture (issued to cameras only). |
| WIA_CMD_UNLOAD_DOCUMENT | Unload the current document (issued to multidocument scanners only). |

The WIA\_CMD\_XXX commands are described in the Microsoft Windows SDK documentation. You can include your own custom list of commands.

## Add Device Command Support

To properly set up your WIA minidriver to report device commands, report an array of supported commands in the [**IWiaMiniDrv::drvGetCapabilities**](/windows-hardware/drivers/ddi/wiamindr_lh/nf-wiamindr_lh-iwiaminidrv-drvgetcapabilities) method. For an example implementation of the **IWiaMiniDrv::drvGetCapabilities** method, see [Adding Interrupt Event Support](adding-interrupt-event-support.md).

### Implement the IWiaMiniDrv::drvDeviceCommand Method

The WIA service calls the [**IWiaMiniDrv::drvDeviceCommand**](/windows-hardware/drivers/ddi/wiamindr_lh/nf-wiamindr_lh-iwiaminidrv-drvdevicecommand) method in response to the application's call to the **IWiaItem::DeviceCommand** method (described in the Microsoft Windows SDK documentation). The **IWiaMiniDrv::drvDeviceCommand** method should perform the following tasks:

1. Determine whether the command sent is a supported command.

1. Process the command request.

The WIA driver should determine the WIA item that is to receive the device command by using the *pWiasContext* pointer. The WIA driver should then process the received device command targeted to the incoming WIA item. Any command sent to the WIA driver that is not supported should be failed with an E\_INVALIDARG error code.

For an example implementation of the **IWiaMiniDrv::drvDeviceCommand** method, see [Informing an Application of Item Tree Changes](informing-an-application-of-item-tree-changes.md).
