---
title: Setting Properties and Registry Values
description: The Setting Properties and Registry Values topic describes how a Port Class audio driver can set properties and registry values for a PnP device interface.
ms.assetid: EB6E9673-4A87-45D9-A334-8C2AE33A7581
ms.author: windows-driver-content
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Setting Properties and Registry Values


The Setting Properties and Registry Values topic describes how a Port Class audio driver can set properties and registry values for a PnP device interface.

The port class audio driver, Portcls must perform the following steps to properly register the device interface and set required values.

## <span id="1._register_the_device_interface"></span><span id="1._REGISTER_THE_DEVICE_INTERFACE"></span>1. Register the device interface


Before calling PcRegisterSubdevice for the sub-device, the driver can directly call IoRegisterDeviceInterface to register the KSCATEGORY\_AUDIO interface. This gives the driver a chance to set interface properties and registry values on the device interfaces before PcRegisterSubdevice registers and enables the interfaces.

The audio driver sets the parameters for IoRegisterDeviceInterface as follows.

-   The PhysicalDeviceObject parameter is the PDEVICE\_OBJECT that the audio driver can retrieve from the PcGetPhysicalDeviceObject function.

-   The InterfaceClassGuid is set to the interface’s class GUID.

-   The ReferenceString is the same as the Name parameter that the audio driver passes to PcRegisterSubdevice.

After the preceding tasks are completed successfully, IoRegisterDeviceInterface returns a SymbolicLinkName for the registered interface.

## <span id="2._set_registry_values"></span><span id="2._SET_REGISTRY_VALUES"></span>2. Set registry values


The audio driver calls IoOpenDeviceInterfaceRegistryKey to obtain a handle to the device interface registry key. The audio driver sets the parameters to IoOpenDeviceInterfaceRegistryKey as follows.

The SymbolicLinkName is the string returned from IoRegisterDeviceInterface in the previous step.

The DesiredAccess is set to KEY\_WRITE (or other values if needed by the driver).

After the preceding steps are completed successfully, DeviceInterfaceKey returns the opened registry key handle. The audio driver:

-   Calls ZwSetValueKey to set registry values

-   Closes the registry key handle by calling ZwClose

**Note**  If the driver needs to set values in a registry subkey, then the driver calls ZwCreateKey to create the subkey. When preparing to call ZwCreateKey, the driver:
-   Calls InitializeObjectAttributes, and sets the ObjectName to the subkey path

-   Sets Attributes to OBJ\_CASE\_INSENSITIVE | OBJ\_KERNEL\_HANDLE

-   Sets RootDirectory to the handle returned by IoOpenDeviceInterfaceRegistryKey

-   Calls ZwClose to close any handle created by calling ZwCreateKey

 

## <span id="3._set_properties"></span><span id="3._SET_PROPERTIES"></span>3. Set properties


The audio driver calls IoSetDeviceInterfacePropertyData to set properties. The audio driver sets the parameters to IoSetDeviceInterfacePropertyData as follows: The SymbolicLinkName is the string returned from IoRegisterDeviceInterface. The remaining parameters depend on the specific property being set.

## <span id="related_topics"></span>Related topics
[Related Design Guidelines](related-design-guidelines.md)  

--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[audio\audio]:%20Setting%20Properties%20and%20Registry%20Values%20%20RELEASE:%20%287/18/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


