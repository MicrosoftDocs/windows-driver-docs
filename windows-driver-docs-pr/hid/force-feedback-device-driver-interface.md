---
title: Force Feedback Device Driver Interface
author: windows-driver-content
description: Force Feedback Device Driver Interface
MS-HAID:
- 'di\_31ea3fc5-27cb-4a0d-a5ad-66c15b18da60.xml'
- 'hid.force\_feedback\_device\_driver\_interface'
MSHAttr:
- 'PreferredSiteName:MSDN'
- 'PreferredLib:/library/windows/hardware'
ms.assetid: 59668521-84b9-4a1a-980b-6de57422a2c5
keywords: ["force feedback drivers WDK HID", "virtual joystick drivers WDK HID , force feedback", "VJoyD WDK HID , force feedback", "joysticks WDK HID , force feedback", "effect drivers WDK force feedback"]
---

# Force Feedback Device Driver Interface


## <a href="" id="ddk-force-feedback-device-driver-interface-di"></a>


This section covers the interface between DirectInput and the device-specific force feedback driver. The following topics are covered:

## OEMForceFeedback Registry Settings


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

 
## Driver Interface


## <a href="" id="ddk-driver-interface-di"></a>


If the force-feedback driver is COM-based, an instance of the driver is created by DirectInput. If the interface specified is "VJoyD", then the VJoyD minidriver is loaded by VJoyD. Both driver paths support the following exported methods:

[*DestroyEffect*](https://msdn.microsoft.com/library/windows/hardware/ff538410)

[*Initialize*](https://msdn.microsoft.com/library/windows/hardware/ff541025)

[*DownloadEffect*](https://msdn.microsoft.com/library/windows/hardware/ff538601)

[*GetEffectStatus*](https://msdn.microsoft.com/library/windows/hardware/ff538772)

[*GetForceFeedbackState*](https://msdn.microsoft.com/library/windows/hardware/ff538776)

[*Escape*](https://msdn.microsoft.com/library/windows/hardware/ff538680)

[*SendForceFeedbackCommand*](https://msdn.microsoft.com/library/windows/hardware/ff543387)

[*SetGain*](https://msdn.microsoft.com/library/windows/hardware/ff543406)

[*StartEffect*](https://msdn.microsoft.com/library/windows/hardware/ff543458)

[*StopEffect*](https://msdn.microsoft.com/library/windows/hardware/ff543460)

This functionality is supported by all force feedback devices.

## User-Mode Functions


## <a href="" id="ddk-user-mode-functions-di"></a>


DirectInput creates an instance of the force-feedback effect driver by creating the object named by the CLSID that is stored in the **OEMForceFeedback** registry subkey of the joystick type subkey.

Because applications using DirectInput need not load OLE, the effect driver should be careful not to rely on OLE-specific behavior. For example, applications using DirectInput cannot be relied upon to call the **CoFreeUnusedLibraries** method. DirectInput performs the standard COM operations to create an instance of the effect driver object. The only visible effect this should have on the implementation of the effect driver is described following.

After DirectInput releases the last effect driver object, it manually performs a FreeLibrary of the effect driver DLL. Consequently, if the effect driver DLL creates additional resources that are not associated with the effect driver object, it should manually LoadLibrary itself to artificially increase its DLL reference count, thereby preventing the FreeLibrary from DirectInput from unloading the DLL prematurely.

In particular, if the effect driver DLL creates a worker thread, the effect driver must perform this artificial LoadLibrary operation for as long as the worker thread exists. When the worker thread is no longer needed (for example, upon notification from the last effect driver object as it is being destroyed), the worker thread should call the FreeLibraryAndExitThread method to decrement the DLL reference count and terminate the thread.

All magnitude and gain values used by DirectInput are uniform and linear across the range. Any nonlinearity in the physical device must be handled by the device driver so that the application sees a linear device.

The user-mode force feedback functions that are exposed by the [IDirectInputEffectDriver](https://msdn.microsoft.com/library/windows/hardware/ff540050)interface must be implemented by a force-feedback effect driver DLL. For more information about these functions, see IDirectInputEffectDriver.

 

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bhid\hid%5D:%20Force%20Feedback%20Device%20Driver%20Interface%20%20RELEASE:%20%287/18/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


