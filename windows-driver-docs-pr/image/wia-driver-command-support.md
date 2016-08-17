---
title: WIA Driver Command Support
description: WIA Driver Command Support
MS-HAID:
- 'WIA\_db\_event\_18c13021-bb6f-4a97-a312-e2c0122f4d97.xml'
- 'image.wia\_driver\_command\_support'
MSHAttr:
- 'PreferredSiteName:MSDN'
- 'PreferredLib:/library/windows/hardware'
ms.assetid: 9c552316-7dd6-4102-88d3-fab9732d1e5d
---

# WIA Driver Command Support


## <a href="" id="ddk-wia-driver-command-support-si"></a>


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

```

```

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bimage\image%5D:%20WIA%20Driver%20Command%20Support%20%20RELEASE:%20%288/17/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




