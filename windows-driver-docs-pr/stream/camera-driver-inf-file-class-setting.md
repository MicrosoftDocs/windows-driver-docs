---
title: Camera class INF file setting for camera drivers
description: Describes how to add the camera class setting to a Universal camera driver INF file.
ms.date: 01/30/2018
ms.localizationpriority: medium
---

# Camera class INF file setting for Universal camera drivers

Starting with Windows 10, version 1709, you should add the following Camera class settings to your Universal camera driver INF file.

Add these **Class** and **ClassGuid** entries to the **Version** section of your Universal camera driver INF file to ensure your driver will pass future camera driver HLK tests:

```INF
[Version]

...

Class=Camera
ClassGuid={ca3e7ab9-b4c3-4ae6-8251-579ef933890f}

...
```


For more information on the HLK requirements for the Camera class INF file setting, see the **Device.Streaming.Camera.Base.AVStreamClassInterfaceAndWDM** section in [Device.Streaming.Camera](https://docs.microsoft.com/windows-hardware/design/compatibility/device-streaming-camera).




