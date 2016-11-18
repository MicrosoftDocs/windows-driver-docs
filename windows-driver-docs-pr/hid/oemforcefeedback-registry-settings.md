---
title: OEMForceFeedback Registry Settings
author: windows-driver-content
description: OEMForceFeedback Registry Settings
MS-HAID:
- 'di\_10d0818a-5feb-4ae9-8c53-2a554051465c.xml'
- 'hid.oemforcefeedback\_registry\_settings'
MSHAttr:
- 'PreferredSiteName:MSDN'
- 'PreferredLib:/library/windows/hardware'
ms.assetid: c29fe1e8-1cd9-4b32-96d7-1afae5a49d42
keywords: ["force feedback drivers WDK HID , OEMForceFeedback settiings", "OEMForceFeedback key WDK HID", "registry WDK force feedback", "Effects subkey WDK force feedback"]
---

# OEMForceFeedback Registry Settings


## <a href="" id="ddk-oemforcefeedback-registry-settings-di"></a>


New joystick registry entries are found under an OEM-specific key that is installed for each joystick device type under the key with the registry path **HKEY\_LOCAL\_MACHINE\\System\\CurrentControlSet\\Control\\MediaProperties\\PrivateProperties\\Joystick\\OEM**. The data stored under this OEM-specific key is initialized when the device is first installed and then used for reference purposes only. In addition to the values defined for existing joystick devices, two new optional generic values and a set of force feedback specific values have been defined.

The two generic values are a binary value containing version information and a **Manufacturer** string value (REGSTR\_VAL\_MANUFACTURER in regstr.h ) containing a string for the manufacturer's name. The latter complements the existing **OEMName** value that holds the name of the device.

A new **OEMForceFeedback** key has been defined to hold force feedback specific keys and values. Under this key is an **Effects** subkey that contains two values for each effect.

Under the **Effects** subkey is a list of subkeys, one for each effect. The name of each subkey is a globally unique identifier (GUID) in the form "{12345678-1234-1234-1234-123456789012}". Beneath the key named "{...}" are two values. The default value is the string friendly name for the effect. The **Attributes** value is the [**DIEFFECTATTRIBUTES**](https://msdn.microsoft.com/library/windows/hardware/ff538456) structure.

```
"{guid1}"
    Default value = friendly name for effect {guid1} (string)
    "Attributes" = DIEFFECTATTRIBUTES structure (binary)
"{guid2}"
    Default value = friendly name for effect {guid2} (string)
    "Attributes" = DIEFFECTATTRIBUTES structure (binary)
```

The **OEMForceFeedback** key also includes a value that contains the device attributes and one of two optional values. Of the optional values, use **CLSID** if you are using a ring 3 driver (DLL), and **VJoyD** if you are using a ring 0 driver (VxD).

```
"Attributes" = DIFFDEVICEATTRIBUTES structure (binary)
"CLSID" = {GUID} for force feedback effect driver (string)(optional)
"VJoyD" = zero-length binary (optional)
```

The name of the optional values indicate which form of interface is used. If the **CLSID** value is present, it should be a string value containing the GUID in the form "{12345678-1234-1234-1234-123456789012}" for the COM object that provides the driver interface. If the **VJoyD** value is present, it should be a zero-length binary value, which indicates that the VJoyD minidriver associated with the device to be used should provide extra callbacks for the driver interface. A value is added to indicate that the Human Interface Device (HID) provides the driver interface when that is implemented.

If a device supports a hardware effect that does not fall into any of the predefined categories (DIEFT\_CONSTANTFORCE, DIEFT\_RAMPFORCE, DIEFT\_PERIODIC, DIEFT\_CONDITION, or DIEFT\_CUSTOMFORCE), then the [**DIEFFECTATTRIBUTES**](https://msdn.microsoft.com/library/windows/hardware/ff538456) structure for the effect should specify DIEFT\_HARDWARE as the effect type.

A device can support a hardware effect that falls into one of the predefined categories (listed in the preceding paragraph) but also receive additional parameters that are not part of the standard type-specific data structures (DICONSTANTFORCE, DIRAMPFORCE, DIPERIODIC, DICONDITION, or DICUSTOMFORCE). For information about these structures, see the DirectInput section of the DirectX Software Development Kit (SDK). In these cases, the effect should be listed twice as follows:

-   List the effect under the predefined category. If an application creates the effect in the predefined category, the driver should provide suitable defaults for the specified parameters that are not part of the standard type-specific data structure.

-   List the effect under the DIEFT\_HARDWARE category. Create a special type-specific structure (such as DIPERIODICFORCEWITHDECAY) that contains the extra parameters.

In this manner, an application designed for your hardware can use the second effect descriptor to access the full capabilities of the effect, whereas an application designed for generic hardware can use the first effect descriptor to access basic capabilities of the effect.

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bhid\hid%5D:%20OEMForceFeedback%20Registry%20Settings%20%20RELEASE:%20%287/18/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


