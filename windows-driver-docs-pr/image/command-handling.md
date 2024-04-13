---
title: Command Handling
description: Command handling
ms.date: 03/29/2023
---

# Command handling

The WIA architecture enables a WIA application to send a specific command to the WIA minidriver. This command can be sent only to the root item in the WIA item tree. (Note that the minidriver reports all of the commands it supports in its capabilities table.)

The command issued by the WIA application does not go directly to the WIA minidriver. Instead, the application sends the command to the WIA service. The WIA service then forwards this command to the WIA minidriver. When the minidriver receives the command (as a parameter of the [**IWiaMiniDrv::drvDeviceCommand**](/windows-hardware/drivers/ddi/wiamindr_lh/nf-wiamindr_lh-iwiaminidrv-drvdevicecommand) method), the minidriver might need to access the device to satisfy the command.

In some cases, the command might require the minidriver to create a new child driver item. For example, a digital still camera device might support the **TakePicture** command. If the minidriver receives this command, it instructs the camera to take a picture. When the camera carries out the request to take a picture, the camera creates a new image on its media, and the WIA minidriver adds a new driver item to its item tree.
