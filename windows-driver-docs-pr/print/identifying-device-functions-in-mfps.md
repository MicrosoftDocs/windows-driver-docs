---
title: Identifying Device Functions in MFPs
author: windows-driver-content
description: Identifying Device Functions in MFPs
MS-HAID:
- 'prn\_dxpui\_4b644a84-be1f-4a0d-a5eb-972faf3d56ec.xml'
- 'print.identifying\_device\_functions\_in\_mfps'
MSHAttr:
- 'PreferredSiteName:MSDN'
- 'PreferredLib:/library/windows/hardware'
ms.assetid: 14016c43-b93a-4009-848b-1bcf3f1d94b6
---

# Identifying Device Functions in MFPs


The Devices and Printers user interface uses a device container identifier (ContainerID) to identify the printer and scanner functions that belong to an MFP. A ContainerID is a GUID that all the functional device instances (devnodes) in an MFP or other multifunction device can use to identify themselves as part of the same multifunction device. For example, the printer functional device instance and the scanner functional device instance in an MFP should have the same ContainerID value.

A device may report the ContainerID.If a device does not report a ContainerID, Windows PnP assigns one for the device. Windows PnP performs this identification by taking advantage of the fact that many multifunction devices have a parent device, which represents the multifunction device as a whole, and child devices that represent the individual functions in the multifunction device. The PnP manager assumes that if two functional device instances have the same parent and if neither instance is labeled as a removable device, the two instances must be permanent members of the same multifunction device. By using this technique, Windows PnP can assign common ContainerIDs to the functional device instances.

For devices that may connect through more than one transport (that is, device connects through USB and WSD), it is recommended that the device reports a ContainerID to make the different device instances show as one device.

For more information about ContainerIDs, see [Windows Device Experience](http://go.microsoft.com/fwlink/p/?linkid=145535).

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bprint\print%5D:%20Identifying%20Device%20Functions%20in%20MFPs%20%20RELEASE:%20%289/1/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


