---
title: Setting Friendly Names, Sideband SCO Transport and Registering APOs
description: This topic describes how a Port Class Bluetooth sideband audio driver can set the friendly name for a device interface, and register any APO that is used by the Bluetooth device.
ms.date: 10/05/2022
---

# Setting Friendly Names, Sideband SCO Transport, and Registering APOs

The Setting Friendly Names, Sideband SCO Transport, and Registering APOs topic describes how a Port Class Bluetooth sideband audio driver can set the friendly name for a device interface, identify itself as having sideband SCO transport, and register any audio processing object (APO) that is used by the Bluetooth device.

For each enabled GUID_DEVINTERFACE_BLUETOOTH_HFP_SCO_HCIBYPASS interface, the Port Class audio driver (PortCls) normally calls the PcRegisterSubdevice function, which registers PnP device interfaces that represent a sub-device on an audio adapter. In typical audio driver designs, the audio driver calls PcRegisterSubdevice for "wave" and "topology" sub-devices, which are then connected by calling other Port Class functions.

Before calling PcRegisterSubdevice for the "topology" sub-device, the driver follows the procedure described in [Setting Properties and Registry Values](setting-properties-and-registry-values.md) to set properties and registry values on the interface in the KSCATEGORY_AUDIO interface class. The specific properties and registry values are described in the following sections.

## DEVPKEY_DeviceInterface_FriendlyName

The audio driver sends an [**IOCTL_BTHHFP_DEVICE_GET_DESCRIPTOR**](/windows-hardware/drivers/ddi/bthhfpddi/ni-bthhfpddi-ioctl_bthhfp_device_get_descriptor) request to the Hands-free profile (HFP) audio driver. The requested information is returned in the form of a [**BTHHFP_DESCRIPTOR**](/windows-hardware/drivers/ddi/bthhfpddi/ns-bthhfpddi-_bthhfp_descriptor) structure, plus an other data referenced by the structure. The audio driver then calls IoSetDeviceInterfacePropertyData to set DEVPKEY_DeviceInterface_FriendlyName to the value in the *FriendlyName* field of the **BTHHFP_DESCRIPTOR** structure.

The audio driver sets the parameters to IoSetDeviceInterfacePropertyData as follows:

- SymbolicLinkName = the string returned from IoRegisterDeviceInterface
- PropertyKey = DEVPKEY_DeviceInterface_FriendlyName
- Lcid = LOCALE_NEUTRAL
- Flags = PLUGPLAY_PROPERTY_PERSISTENT
- Type = DEVPROP_TYPE_STRING_INDIRECT
- Size = BTHHFP_DESCRIPTOR.FriendlyName.Length + sizeof(UNICODE_NULL)
- Data = BTHHFP_DESCRIPTOR.FriendlyName.Buffer

## USB Bluetooth controller sideband SCO transport

To have the USB Bluetooth controller identify itself as having sideband SCO transport, specify BthUsb_SidebandSco.NT, instead of BthUsb.NT that is normally used in the controller INF file.

```inf
Needs=BthUsb_SidebandSco.NT 
```

Setting this value means that a dedicated audio interface will be used to transfer audio in and out of the controller rather than USB endpoints.

For more information about the INF *Needs* directive, see [INF DDInstall section](/windows-hardware/drivers/install/inf-ddinstall-section).

## APO registration

As described in [Setting Properties and Registry Values](setting-properties-and-registry-values.md), the driver can set registry values for a device interface. To register an APO, the audio driver sets several values on the device interface. These values are the same as those that are often set for APO registration in an INF, and the specific values will change from one audio driver to the next.

Here is an example of INF file syntax for registering an APO:

``` syntax
HKR,"EPFX\\0",%PKEY_FX_Association%,,%KSNODETYPE_ANY%
HKR,"EPFX\\0",%PKEY_FX_EndpointEffectClsid%,,%FX_DISCOVER_EFFECTS_APO_CLSID%
```

> [!NOTE]
> The syntax shown in the preceding snippet doesn't include instructions for registering the COM server of the APO.

## Related topics

[Audio Processing Object Architecture](audio-processing-object-architecture.md)

[Implementing Audio Processing Objects](implementing-audio-processing-objects.md)