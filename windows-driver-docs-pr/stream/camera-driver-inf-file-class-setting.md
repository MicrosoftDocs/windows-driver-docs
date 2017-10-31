---
title: Camera class INF file setting for camera drivers
description: Describes how to add the camera class setting to a Universal camera driver INF file.
ms.author: windowsdriverdev
ms.date: 10/26/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Camera class INF file setting for Universal camera drivers

Starting with Windows 10, version 1709, you should add **Class=Camera** settings to your Universal camera driver INF file to ensure future compatability with camera driver HLK tests.

Add the following **Class** and **ClassGuid** entries to the **Version** section of your Universal camera driver INF file (as shown below) to ensure your driver will pass future camera driver HLK tests:

```
[Version]

...

Class=Camera
ClassGuid={ca3e7ab9-b4c3-4ae6-8251-579ef933890f}

...

```


For more information on the HLK requirements for the Camera class INF file setting, see the **Device.Streaming.Camera.Base.AVStreamClassInterfaceAndWDM** section in [Device.Streaming.Camera](https://docs.microsoft.com/en-us/windows-hardware/design/compatibility/device-streaming-camera).

--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bprint\print%5D:%20Slicer%20settings%20%20RELEASE:%20%289/2/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")

