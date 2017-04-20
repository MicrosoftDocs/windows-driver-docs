---
title: Multiple Audio Subdevices
description: Multiple Audio Subdevices
ms.assetid: 1654a2b3-7bec-4438-8cb5-b3136c8e66cc
keywords:
- multifunction audio devices WDK , subdevices
- multiple subdevices WDK audio
ms.author: windows-driver-content
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Multiple Audio Subdevices


## <span id="multiple_audio_subdevices"></span><span id="MULTIPLE_AUDIO_SUBDEVICES"></span>


A multifunction device can contain two or more audio subdevices. For example, an adapter driver might allow an eight-channel audio device to be exposed to the system as four stereo channels. When writing an adapter driver to expose multiple subdevices in this way, you should incorporate information about the subdevices into your driver's [startup sequence](startup-sequence.md) and INF file.

First, your adapter driver should expose each stereo subdevice as a separate instance of a port/miniport driver pair during the startup sequence. Several of the sample adapters in the Microsoft Windows Driver Kit (WDK) implement an `InstallSubdevice` function that creates and registers a subdevice consisting of a system port driver, a miniport driver, and a set of resources that are to be bound to this pair. During startup, your driver should call its `InstallSubdevice` function once for each stereo subdevice and specify a unique name for each port/miniport driver pair.

In addition, the unique name you assign to this pair must match the KSNAME string that you specify in your driver's INF file. For example, your driver might assign the names "Wave1" and "Wave2" to two subdevices during startup, as shown below:

```
  InstallSubdevice(..., "Wave1",...);
  InstallSubdevice(..., "Wave2",...);
```

In this case, the same names should appear in the INF file:

```
  KSNAME_Wave1="Wave1"
  KSNAME_Wave2="Wave2"
```

Your INF file should add interfaces that contain these names:

```
  AddInterface=%KSCATEGORY_AUDIO%,%KSNAME_Wave1%,Test.Interface.Wave1
  AddInterface=%KSCATEGORY_AUDIO%,%KSNAME_Wave2%,Test.Interface.Wave2
```

The INF file should create **AddReg** sections (see [**INF AddReg Directive**](https://msdn.microsoft.com/library/windows/hardware/ff546320)) in order to add information about these interfaces to the registry:

```
  [Test.Interface.Wave1]
  AddReg=Test.I.Wave1.AddReg

  [Test.Interface.Wave2]
  AddReg=Test.I.Wave2.AddReg
```

The **AddReg** sections should also specify the registry entries for each subdevice:

```
  [Test.I.Wave1.AddReg]
  HKR,,CLSID,,%Proxy.CLSID%
  HKR,,FriendlyName,,%Test.Wave1.szName%

  [Test.I.Wave2.AddReg]
  HKR,,CLSID,,%Proxy.CLSID%
  HKR,,FriendlyName,,%Test.Wave2.szName%
```

Finally, the INF file should define the friendly names for these subdevices:

```
  Test.Wave1.szName="Punch"
  Test.Wave2.szName="Judy"
```

The friendly names show up in the audio control panel to identify the subdevices.

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[audio\audio]:%20Multiple%20Audio%20Subdevices%20%20RELEASE:%20%287/18/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


