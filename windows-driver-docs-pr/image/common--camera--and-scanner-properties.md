---
title: Common, camera, and scanner properties
description: Common, camera, and scanner properties
ms.date: 03/29/2023
---

# Common, camera, and scanner properties

WIA properties are attributes of either a device (the root) or an item (a child). Device properties contain information about the device, such as the manufacturer's name, a description of the device, and its type (scanner or camera). Item properties contain information about a particular item, such as the item's name, when it was captured, and so on. Device properties are identified by the WIA_D naming convention; item properties are identified by the WIA_I naming convention.

The three-letter acronym in the middle of a WIA property name contains information about the type of property: whether it is a generic device information property (DIP), a device property (DPA, DPC, or DPS), or an item property (IPA, IPC, or IPS). Device and item properties can be common to both types of devices (DPA and IPA), can be specific to cameras (DPC or IPC), or can be specific to scanners (DPS and IPS). The following table lists the various WIA property types and gives examples of each type.

| Property type | Meaning |
|--|--|
| WIA_DIP_*Xxx* | Device Information Property<br><br>Setup and installation information common to both scanner and camera devices. The WIA service provides these properties. A minidriver does not provide them. |
| WIA_DPA_*Xxx* | Device Property, All<br><br>Information that is common to both scanner and camera devices, such as connection status and device time. |
| WIA_IPA_*Xxx* | Item Property, All<br><br>Information that is common to both camera and scanner items, such as the item's name and the type of image. |
| WIA_DPC_*Xxx* | Device Property, Camera<br><br>Information that is specific to camera devices, such as the number of pictures taken. |
| WIA_IPC_*Xxx* | Item Property, Camera<br><br>Information that is specific to camera items, such as width and height of thumbnail images. |
| WIA_DPS_*Xxx* | Device Property, Scanner<br><br>Information that is specific to scanner devices, such as bed size. |
| WIA_IPS_*Xxx* | Item Property, Scanner<br><br>Information that it is specific to scanner items, such as horizontal and vertical resolution. |

See [WIA Properties](./wia-properties.md) for a complete list of WIA common, camera-specific, and scanner-specific properties.
