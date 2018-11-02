---
title: Setting Properties and Registry Values
description: The Setting Properties and Registry Values topic describes how a Port Class audio driver can set properties and registry values for a PnP device interface.
ms.assetid: EB6E9673-4A87-45D9-A334-8C2AE33A7581
ms.date: 04/20/2017
ms.localizationpriority: medium
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


The audio driver calls IoSetDeviceInterfacePropertyData to set properties. The audio driver sets the parameters to IoSetDeviceInterfacePropertyData as follows: 
- The SymbolicLinkName is the string returned from IoRegisterDeviceInterface. 
- The remaining parameters depend on the specific property being set.

## <span id="related_topics"></span>Related topics
[Related Design Guidelines](related-design-guidelines.md)  



