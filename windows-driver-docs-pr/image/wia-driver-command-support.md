---
title: WIA Driver Command Support
description: WIA Driver Command Support
ms.assetid: 9c552316-7dd6-4102-88d3-fab9732d1e5d
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# WIA Driver Command Support





A WIA device command is a request sent by the WIA service (on behalf of the imaging application) to the WIA minidriver, instructing it to perform a particular action.

The following is a list of WIA device commands that can be issued to a minidriver:

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<thead>
<tr class="header">
<th>Command</th>
<th>Meaning</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p>WIA_CMD_CHANGE_DOCUMENT</p></td>
<td><p>Change to the next document (issued to multidocument scanners only).</p></td>
</tr>
<tr class="even">
<td><p>WIA_CMD_DELETE_ALL_ITEMS</p></td>
<td><p>Delete the driver item tree.</p></td>
</tr>
<tr class="odd">
<td><p>WIA_CMD_DIAGNOSTIC</p></td>
<td><p>Reserved by Microsoft.</p></td>
</tr>
<tr class="even">
<td><p>WIA_CMD_SYNCHRONIZE</p></td>
<td><p>Rebuild the driver item tree. All minidrivers must support this command.</p></td>
</tr>
<tr class="odd">
<td><p>WIA_CMD_TAKE_PICTURE</p></td>
<td><p>Take a picture (issued to cameras only).</p></td>
</tr>
<tr class="even">
<td><p>WIA_CMD_UNLOAD_DOCUMENT</p></td>
<td><p>Unload the current document (issued to multidocument scanners only).</p></td>
</tr>
</tbody>
</table>

 

The WIA\_CMD\_XXX commands are described in the Microsoft Windows SDK documentation. You can include your own custom list of commands.

### Adding Device Command Support

To properly set up your WIA minidriver to report device commands, report an array of supported commands in the [**IWiaMiniDrv::drvGetCapabilities**](https://msdn.microsoft.com/library/windows/hardware/ff543977) method. For an example implementation of the **IWiaMiniDrv::drvGetCapabilities** method, see [Adding Interrupt Event Support](adding-interrupt-event-support.md).

### Implementing the IWiaMiniDrv::drvDeviceCommand Method

The WIA service calls the [**IWiaMiniDrv::drvDeviceCommand**](https://msdn.microsoft.com/library/windows/hardware/ff543967) method in response to the application's call to the **IWiaItem::DeviceCommand** method (described in the Microsoft Windows SDK documentation). The **IWiaMiniDrv::drvDeviceCommand** method should perform the following tasks:

1.  Determine whether the command sent is a supported command.

2.  Process the command request.

The WIA driver should determine the WIA item that is to receive the device command by using the *pWiasContext* pointer. The WIA driver should then process the received device command targeted to the incoming WIA item. Any command sent to the WIA driver that is not supported should be failed with an E\_INVALIDARG error code.

For an example implementation of the **IWiaMiniDrv::drvDeviceCommand** method, see [Informing an Application of Item Tree Changes](informing-an-application-of-item-tree-changes.md).
