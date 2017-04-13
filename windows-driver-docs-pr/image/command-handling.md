---
title: Command Handling
author: windows-driver-content
description: Command Handling
ms.assetid: 1b940585-8228-4857-92bf-c77c789f6ad5
---

# Command Handling


## <a href="" id="ddk-command-handling-si"></a>


The WIA architecture enables a WIA application to send a specific command to the WIA minidriver. This command can be sent only to the root item in the WIA item tree. (Note that the minidriver reports all of the commands it supports in its capabilities table.)

The command issued by the WIA application does not go directly to the WIA minidriver. Instead, the application sends the command to the WIA service. The WIA service then forwards this command to the WIA minidriver. When the minidriver receives the command (as a parameter of the [**IWiaMiniDrv::drvDeviceCommand**](https://msdn.microsoft.com/library/windows/hardware/ff543967) method), the minidriver might need to access the device to satisfy the command.

In some cases, the command might require the minidriver to create a new child driver item. For example, a digital still camera device might support the **TakePicture** command. If the minidriver receives this command, it instructs the camera to take a picture. When the camera carries out the request to take a picture, the camera creates a new image on its media, and the WIA minidriver adds a new driver item to its item tree.

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bimage\image%5D:%20Command%20Handling%20%20RELEASE:%20%288/17/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


