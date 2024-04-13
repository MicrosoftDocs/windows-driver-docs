---
title: Identifying Device Functions in MFPs
description: Identifying Device Functions in MFPs
ms.date: 01/27/2023
---

# Identifying Device Functions in MFPs

[!include[Print Support Apps](../includes/print-support-apps.md)]

The Devices and Printers user interface uses a device container identifier (ContainerID) to identify the printer and scanner functions that belong to an MFP. A ContainerID is a GUID that all the functional device instances (devnodes) in an MFP or other multifunction device can use to identify themselves as part of the same multifunction device. For example, the printer functional device instance and the scanner functional device instance in an MFP should have the same ContainerID value.

A device may report the ContainerID.If a device does not report a ContainerID, Windows PnP assigns one for the device. Windows PnP performs this identification by taking advantage of the fact that many multifunction devices have a parent device, which represents the multifunction device as a whole, and child devices that represent the individual functions in the multifunction device. The PnP manager assumes that if two functional device instances have the same parent and if neither instance is labeled as a removable device, the two instances must be permanent members of the same multifunction device. By using this technique, Windows PnP can assign common ContainerIDs to the functional device instances.

For devices that may connect through more than one transport (that is, device connects through USB and WSD), it is recommended that the device reports a ContainerID to make the different device instances show as one device.

For more information about ContainerIDs, see [Container ID](../install/container-ids.md).
