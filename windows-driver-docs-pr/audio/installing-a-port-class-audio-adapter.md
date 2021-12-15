---
title: Installing a Port Class Audio Adapter
description: Installing a Port Class Audio Adapter
keywords:
- Port Class audio adapters WDK , installing
- audio miniport drivers WDK , adapter drivers
- miniport drivers WDK audio , adapter drivers
- adapter drivers WDK audio , installing
- audio adapter drivers WDK , installing
- port-class audio adapters WDK
- registry WDK audio
- add-registry-sections WDK audio
- audio adapter drivers WDK
ms.date: 04/20/2017
---

# Installing a Port Class Audio Adapter


## <span id="installing_a_port_class_audio_adapter"></span><span id="INSTALLING_A_PORT_CLASS_AUDIO_ADAPTER"></span>


This section describes the device-class-specific information that a vendor should include in an INF file to install a port-class audio adapter. For a description of the general INF file requirements and options for all device classes, see [Device Installation Overview](../install/overview-of-device-and-driver-installation.md).

The description of the required INF file entries in this section is based on a hypothetical XYZ Audio Device. The driver for this device is contained in a file named Xyzaudio.sys. Example **Manufacturer** and **Models** sections for the device are shown in the following:

```inf
  [VendorName]  ; Manufacturer section
  %XYZ-Audio-Device-Description%=XYZ-Audio-Device, <Plug and Play hardware ID>
  [XYZ-Audio-Device]  ; Models section
  AddReg=XYZ-Audio-Device.AddReg
```

For more information, see [**INF AddReg Directive**](../install/inf-addreg-directive.md).

For additional examples, see the INF files included in the SYVAD audio sample. For more information, see [Sample Audio Drivers](sample-audio-drivers.md) and [Universal Windows Drivers for Audio](audio-universal-drivers.md).

The following topics present examples of the key sections in the INF file that installs the device:

[Specifying Version Information for an Audio Adapter](specifying-version-information-for-an-audio-adapter.md)

[Installing Device Interfaces for an Audio Adapter](installing-device-interfaces-for-an-audio-adapter.md)

[Installing Core System Components for an Audio Adapter](installing-core-system-components-for-an-audio-adapter.md)

[Installing Windows Multimedia System Support for an Audio Adapter](installing-windows-multimedia-system-support-for-an-audio-adapter.md)

[Installing an Audio Adapter Service in Windows](installing-an-audio-adapter-service-in-windows.md)

[Customizing Control Panel](customizing-control-panel.md)

[Miscellaneous Installation Issues for an Audio Adapter](miscellaneous-installation-issues-for-an-audio-adapter.md)

 

