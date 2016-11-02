---
title: Installing a Port Class Audio Adapter
description: Installing a Port Class Audio Adapter
ms.assetid: 02cea7c1-cf9a-4f4b-9d35-d565fac731ec
keywords: ["Port Class audio adapters WDK , installing", "audio miniport drivers WDK , adapter drivers", "miniport drivers WDK audio , adapter drivers", "adapter drivers WDK audio , installing", "audio adapter drivers WDK , installing", "port-class audio adapters WDK", "registry WDK audio", "add-registry-sections WDK audio", "audio adapter drivers WDK"]
---

# Installing a Port Class Audio Adapter


## <span id="installing_a_port_class_audio_adapter"></span><span id="INSTALLING_A_PORT_CLASS_AUDIO_ADAPTER"></span>


This section describes the device-class-specific information that a vendor should include in an INF file to install a port-class audio adapter. For a description of the general INF file requirements and options for all device classes, see [Device Installation Overview](https://msdn.microsoft.com/library/windows/hardware/ff549455).

The description of the required INF file entries in this section is based on a hypothetical XYZ Audio Device. The driver for this device is contained in a file named Xyzaudio.sys. Example **Manufacturer** and **Models** sections for the device are shown in the following:

```
  [VendorName]  ; Manufacturer section
  %XYZ-Audio-Device-Description%=XYZ-Audio-Device, <Plug and Play hardware ID>
  [XYZ-Audio-Device]  ; Models section
  AddReg=XYZ-Audio-Device.AddReg
```

For more information, see [**INF AddReg Directive**](https://msdn.microsoft.com/library/windows/hardware/ff546320).

For additional examples, see the INF files included in the SYVAD audio sample. For more information, see [Sample Audio Drivers](sample-audio-drivers.md) and [Universal Windows Drivers for Audio](audio-universal-drivers.md).

The following topics present examples of the key sections in the INF file that installs the device:

[Specifying Version Information for an Audio Adapter](specifying-version-information-for-an-audio-adapter.md)

[Installing Device Interfaces for an Audio Adapter](installing-device-interfaces-for-an-audio-adapter.md)

[Installing Core System Components for an Audio Adapter](installing-core-system-components-for-an-audio-adapter.md)

[Installing Windows Multimedia System Support for an Audio Adapter](installing-windows-multimedia-system-support-for-an-audio-adapter.md)

[Installing an Audio Adapter Service](installing-an-audio-adapter-service.md)

[Customizing Control Panel](customizing-control-panel.md)

[Miscellaneous Installation Issues for an Audio Adapter](miscellaneous-installation-issues-for-an-audio-adapter.md)

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[audio\audio]:%20Installing%20a%20Port%20Class%20Audio%20Adapter%20%20RELEASE:%20%287/18/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


