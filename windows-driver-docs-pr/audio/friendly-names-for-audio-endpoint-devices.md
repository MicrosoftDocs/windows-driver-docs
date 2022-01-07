---
title: Friendly Names for Audio Endpoint Devices
description: Friendly Names for Audio Endpoint Devices
ms.date: 04/20/2017
---

# Friendly Names for Audio Endpoint Devices


In Windows Vista, Windows Server 2008 and later versions of Windows, the audio subsystem supports the notion of an audio endpoint device, for example, speakers, headphones, microphones, and CD players. This concept of audio endpoints helps create user-friendly audio applications that have user interfaces that refer to the endpoint devices that users directly manipulate. These endpoints have friendly names such as "speakers", "headphones", "microphone", and "CD player" that applications can display in their user interfaces. For more information about endpoint devices, see [Audio Endpoint Devices](/windows/win32/coreaudio/audio-endpoint-devices).

The audio subsystem models a Plug and Play (PnP) device on an audio adapter as a KS filter. Data streams enter and exit the filter through KS pins. A bridge pin is a KS pin through which an audio endpoint device connects to a KS filter. For more information about bridge pins, see [Audio Filter Graphs](audio-filter-graphs.md).

The audio subsystem obtains information about an audio endpoint device by examining the properties of the bridge pin that the endpoint device connects to. One such property is the [pin category property](pin-category-property.md) ([**KSPROPERTY\_PIN\_CATEGORY**](../stream/ksproperty-pin-category.md)). 

For each KS filter, the adapter driver supplies a table of [**PCPIN\_DESCRIPTOR**](/windows-hardware/drivers/ddi/portcls/ns-portcls-pcpin_descriptor) structures that describe the properties of the KS pins on the filter. The pin category GUID is stored in the **KsPinDescriptor.Category** member of the PCPIN\_DESCRIPTOR structure. For a bridge pin, the value of the pin category GUID indicates the type of endpoint that connects to the bridge pin. For example, the pin-category GUID KSNODETYPE\_MICROPHONE indicates that the bridge pin connects to a microphone, the GUID KSNODETYPE\_SPEAKER indicates that the bridge pin connects to speakers, and so on. The KSNODETYPE\_*XXX* GUIDs are defined in the Ksmedia.h header file.

In addition the **PCPIN\_DESCRIPTOR** includes a GUID that can be used to identify the pin by a unique name.  This pin name GUID is stored in the **KsPinDescriptor.Name** member of the PCPIN\_DESCRIPTOR structure. This name GUID is used by the ([**KSPROPERTY\_PIN\_NAME**](../stream/ksproperty-pin-name.md)) property to associate a friendly name found in the registry with the pin. 

The audio subsystem invokes the **KSPROPERTY\_PIN\_NAME** property to associate a friendly name with an audio endpoint. KS handles this request by first searching for a unicode string in the registry describing the **KsPinDescriptor.Name** GUID.  If KS does not find an entry, it searches the registry for a unicode string describing the **KsPinDescriptor.Category** GUID.  

Starting with **Windows 10 REDSTONE 5** when searching the registry, KS first looks for an entry in the device's software key.  This is created by the INF through an AddReg section referenced by the [Models] section of the device driver's INF.  The AddReg section constructs these entries using the HKR\\MediaCategories key. This allows the driver developer to create device-specific friendly names for both Name and Category GUIDs, whether the GUID is unique to the device or not.

If an entry has not been installed in the device's software key or the driver is running on an operating system prior to **Windows 10 REDSTONE 5**, KS looks under HKLM\\SYSTEM\\CurrentControlSet\\Control\\MediaCategories registry key. This second key is treated as a global name space.  Starting with **Windows 10 REDSTONE 5** this space is reserved for global definitions and should not be modified by new drivers.  Modification of entries under this key will not be supported in a future OS release.

Audio devices that expose pins with standard categories GUIDs should include / needs the inbox KS.INF or KSCAPTUR.INF name registration in your device INF.  These inbox INFs contain default friendly name definitions for pre-defined category GUIDs that your driver may wish to populate. These are the same GUIDs found in the **KsPinDescriptor.Category** member of the PCPIN\_DESCRIPTOR structure. For example, the category GUID KSNODETYPE\_MICROPHONE entry has the associated friendly name "microphone" and the category GUID KSNODETYPE\_SPEAKER entry has the associated friendly name "speakers," and so on.

The GUIDs and friendly names for both Category and Name GUIDs are stored under the HKR\\MediaCategories while global definitions HKLM\\SYSTEM\\CurrentControlSet\\Control\\MediaCategories paths. For each GUID-name pair in the registry, the GUID string is used as a sub-key under the MediaCategories key.  Under the GUID key the friendly name a Unicode string value under the "Name" variable. 

If none of the friendly names and pin categories defined by the audio subsystem adequately describes your device, you can define your own pin category and name GUIDs and associate friendly names with them in your INF. To ensure that your pin-category GUID is unique, use a utility such as Uuidgen.exe to generate the GUID. Next, modify the INF file that installs your audio adapter to write the pin-category GUID and friendly name to the registry path HKR\\MediaCategories. The following code example shows a fragment of an INF file that adds two pin-category GUIDs and their associated friendly names to the registry:

```inf
[Manufacturer]
MyOEMName=Unicorn,NTamd64

[Unicorn.NTamd64]
MyDeviceName=MyDevice,Root\MyDevice

[MyDevice.NT]
Include=ks.inf, kscaptur.inf
Needs=KS.Registration, KSCAPTUR.Registration.NT
CopyFiles=MyDevice.CopyFiles
AddReg=PinNameRegistration

...

[PinNameRegistration]
HKR,%MediaCategories%\%GUID.MyNewEndpointCategory%,Name,,%Name.MyNewEndpointCategory%
HKR,%MediaCategories%\%GUID.MyNewEndpointName%,Name,,%Name.MyNewEndpointName%

...

[Strings]
MyOEMName="Unicorns Inc."
MyDeviceName="Sparkly Unicorn"
MediaCategories="MediaCategories"

GUID.MyNewEndpointCategory="{B72FBD1A-4634-4240-B207-0E6B52F3701C}"
GUID.MyNewEndpoint_2="{71DD3A5D-E303-49A0-ACEE-908634AA9520}"

Name.MyNewEndpointCategory="Unicorn"
Name.MyNewEndpointName="Fred the Unicorn"
```

Both GUID strings were generated by Uuidgen.exe.

Applications can access the properties of an audio endpoint device by using the device's **IPropertyStore** interface. The interface uses the property keys defined in the Functiondiscoverykeys\_devpkey.h and Mmdeviceapi.h header files to identify the properties. An application can use the **PKEY\_Device\_FriendlyName** property key to retrieve the friendly name of an endpoint device. For space-constrained user interfaces, a shorter version of the friendly name can be retrieved by using the **PKEY\_Device\_DeviceDesc** property key. For more information about these property keys, see [IMMDevice::OpenPropertyStore](/windows/win32/api/mmdeviceapi/nf-mmdeviceapi-immdevice-openpropertystore).

An **IPropertyStore** interface instance maintains a persistent property store for an audio endpoint device. The property store copies its initial value for the **PKEY\_Device\_DeviceDesc** property key from the friendly name string that is associated with the KS pin category GUID in the registry path HKLM\\SYSTEM\\CurrentControlSet\\Control\\MediaCategories. Applications can read the **PKEY\_Device\_DeviceDesc** property value (the name string) from the property store, but they cannot change the value. However, users can modify the name by using the Windows multimedia control panel, Mmsys.cpl. For example, in Windows Vista, you can use the following steps to modify the name of a rendering endpoint device:

1.  To run Mmsys.cpl, open a Command Prompt window and enter the following command:

    ```console
    mmsys.cpl
    ```

    (Alternatively, you can run Mmsys.cpl by right-clicking the speaker icon in the notification area, which is located on the right side of the taskbar, and clicking **Playback Devices**.)

2.  Click the name of a rendering device, and then click **Properties**.

3.  In the Properties window, click the **General** tab. The friendly name should appear in a text box at the top of the property sheet. You can edit the friendly name, and then save your changes by clicking **OK**.

The preceding steps change the friendly name that is stored in the property store for the audio endpoint device. These steps have no effect on the friendly names associated with other audio endpoint devices that belong to the same KS pin category. They also have no effect on any component that might query KS directly for a name.
