---
title: Setting Friendly Names, Registering APOs
description: The Setting Friendly Names, Registering APOs topic describes how a Port Class Bluetooth sideband audio driver can set the friendly name for a device interface, and register any audio processing object (APO) that is used by the Bluetooth device.
ms.assetid: A3C4E04C-8F3B-49B4-8E46-CF37E1A4F5AF
---

# Setting Friendly Names, Registering APOs


The Setting Friendly Names, Registering APOs topic describes how a Port Class Bluetooth sideband audio driver can set the friendly name for a device interface, and register any audio processing object (APO) that is used by the Bluetooth device.

For each enabled GUID\_DEVINTERFACE\_BLUETOOTH\_HFP\_SCO\_HCIBYPASS interface, the Port Class audio driver (PortCls) normally calls the PcRegisterSubdevice function, which registers PnP device interfaces that represent a sub-device on an audio adapter. In typical audio driver designs, the audio driver calls PcRegisterSubdevice for “wave” and “topology” sub-devices, which are then connected by calling other Port Class functions.

Before calling PcRegisterSubdevice for the “topology” sub-device, the driver follows the procedure described in [Setting Properties and Registry Values](setting-properties-and-registry-values.md) to set properties and registry values on the interface in the KSCATEGORY\_AUDIO interface class. The specific properties and registry values are described in the following sections.

## <span id="DEVPKEY_DeviceInterface_FriendlyName"></span><span id="devpkey_deviceinterface_friendlyname"></span><span id="DEVPKEY_DEVICEINTERFACE_FRIENDLYNAME"></span>DEVPKEY\_DeviceInterface\_FriendlyName


The audio driver sends an [**IOCTL\_BTHHFP\_DEVICE\_GET\_DESCRIPTOR**](https://msdn.microsoft.com/library/windows/hardware/dn265108) request to the Hands-free profile (HFP) audio driver. The requested information is returned in the form of a [**BTHHFP\_DESCRIPTOR**](https://msdn.microsoft.com/library/windows/hardware/dn302030) structure, plus an other data referenced by the structure. The audio driver then calls IoSetDeviceInterfacePropertyData to set DEVPKEY\_DeviceInterface\_FriendlyName to the value in the *FriendlyName* field of the **BTHHFP\_DESCRIPTOR** structure.

The audio driver sets the parameters to IoSetDeviceInterfacePropertyData as follows:

-   SymbolicLinkName = the string returned from IoRegisterDeviceInterface

-   PropertyKey = DEVPKEY\_DeviceInterface\_FriendlyName

-   Lcid = LOCALE\_NEUTRAL

-   Flags = PLUGPLAY\_PROPERTY\_PERSISTENT

-   Type = DEVPROP\_TYPE\_STRING\_INDIRECT

-   Size = BTHHFP\_DESCRIPTOR.FriendlyName.Length + sizeof(UNICODE\_NULL)

-   Data = BTHHFP\_DESCRIPTOR.FriendlyName.Buffer

## <span id="APO_registration"></span><span id="apo_registration"></span><span id="APO_REGISTRATION"></span>APO registration


As described in [Setting Properties and Registry Values](setting-properties-and-registry-values.md), the driver can set registry values for a device interface. To register an APO, the audio driver sets several values on the device interface. These values are the same as those that are often set for APO registration in an INF, and the specific values will change from one audio driver to the next.

Here is an example of INF file syntax for registering an APO:

``` syntax
HKR,"EPFX\\0",%PKEY_FX_Association%,,%KSNODETYPE_ANY%
HKR,"EPFX\\0",%PKEY_FX_EndpointEffectClsid%,,%FX_DISCOVER_EFFECTS_APO_CLSID%
```

**Note**  The syntax shown in the preceding snippet doesn't include instructions for registering the COM server of the APO.

 

## <span id="related_topics"></span>Related topics
[Related Design Guidelines](related-design-guidelines.md)  

--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[audio\audio]:%20Setting%20Friendly%20Names,%20Registering%20APOs%20%20RELEASE:%20%287/18/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


