---
title: Using the Registry in UMDF 1.x Drivers
description: Using the Registry in UMDF 1.x Drivers
keywords:
- registry WDK UMDF
- property store objects WDK UMDF
- UMDF drivers WDK UMDF , registry
- user-mode drivers WDK UMDF , registry
- UMDF WDK , registry
- User-Mode Driver Framework WDK , registry
- keys WDK UMDF
ms.date: 04/20/2017
---

# Using the Registry in UMDF 1.x Drivers


[!include[UMDF 1 Deprecation](../includes/umdf-1-deprecation.md)]

UMDF-based drivers can read and write values in the registry by using interfaces of the property store object.

UMDF-based drivers can access four types of registry keys. Drivers can create, read, and write subkeys and values under these keys. The following types of registry keys are available to UMDF-based drivers:

- Hardware keys

  The PnP manager creates a hardware key, or *device key*, for each device, in which it stores the device's unique identification information.

  Your driver can retrieve and modify some of the property values under the hardware key. The location of the stored values depends on the method that you use to access them.

  Property values that were created using PropertyStore methods are stored in the **\\Device Parameters** subkey, under the hardware key. To access these properties, your driver calls one of the following methods to obtain a property store interface.

  <a href="" id="iwdfdevice--retrievedevicepropertystore"></a>[**IWDFDevice::RetrieveDevicePropertyStore**](/windows-hardware/drivers/ddi/wudfddi/nf-wudfddi-iwdfdevice-retrievedevicepropertystore)  
  Obtains a pointer to an [**IWDFNamedPropertyStore**](/windows-hardware/drivers/ddi/wudfddi/nn-wudfddi-iwdfnamedpropertystore) interface.

  <a href="" id="iwdfdeviceinitialize--retrievedevicepropertystore"></a>[**IWDFDeviceInitialize::RetrieveDevicePropertyStore**](/windows-hardware/drivers/ddi/wudfddi/nf-wudfddi-iwdfdeviceinitialize-retrievedevicepropertystore)  
  Obtains a pointer to an [**IWDFNamedPropertyStore**](/windows-hardware/drivers/ddi/wudfddi/nn-wudfddi-iwdfnamedpropertystore) interface.

  <a href="" id="iwdfpropertystorefactory--retrievedevicepropertystore"></a>[**IWDFPropertyStoreFactory::RetrieveDevicePropertyStore**](/windows-hardware/drivers/ddi/wudfddi/nf-wudfddi-iwdfpropertystorefactory-retrievedevicepropertystore)  
  Obtains a pointer to an [**IWDFNamedPropertyStore2**](/windows-hardware/drivers/ddi/wudfddi/nn-wudfddi-iwdfnamedpropertystore2) interface. You can use the *SubkeyPath* parameter to specify values under a driver-created subkey, such as **\\Device Parameters\\**<em>DriverServiceName\\subkey</em>.

  Drivers have read-only access to values within the **\\Device Parameters** subkey, and cannot access **\\Device Parameters\\WDF** or **\\Device Parameters\\WUDF**.

  Property values that were created using the Unified Device Property model are stored in the **\\Properties** subkey, under the hardware key.

  To access these properties, your driver calls [**IWDFUnifiedPropertyStoreFactory::RetrieveUnifiedDevicePropertyStore**](/windows-hardware/drivers/ddi/wudfddi/nf-wudfddi-iwdfunifiedpropertystorefactory-retrieveunifieddevicepropertystore) to obtain a property store interface. Then the driver can use the [**IWDFUnifiedPropertyStore**](/windows-hardware/drivers/ddi/wudfddi/nn-wudfddi-iwdfunifiedpropertystore) interface to modify and retrieve current settings of device properties.

- Software keys

  A driver's software key is also called its *driver key* because the registry contains a software key for each driver. The registry contains a list of all of the device classes, and each driver's software key resides under its device class entry. The system stores information about each driver under its software key.

  Your driver can call [**IWDFPropertyStoreFactory::RetrieveDevicePropertyStore**](/windows-hardware/drivers/ddi/wudfddi/nf-wudfddi-iwdfpropertystorefactory-retrievedevicepropertystore) to obtain read or write access to values under its software key. The driver can read and write driver-specific information that is not associated with specific devices.

- Device interface keys

  The registry contains keys for all of the [device interface classes](../install/overview-of-device-interface-classes.md) that drivers have created. Under each of these keys is an entry for each instance of the device interface class that a driver has registered.

  If your driver has registered an instance of a device interface class, it can read and write values under the registry's entry for that instance by calling [**IWDFPropertyStoreFactory::RetrieveDevicePropertyStore**](/windows-hardware/drivers/ddi/wudfddi/nf-wudfddi-iwdfpropertystorefactory-retrievedevicepropertystore). The driver can read and write instance-specific information about the device interface.

- The **DEVICEMAP** key

  The registry contains a **HKEY\_LOCAL\_MACHINE\\HARDWARE\\DEVICEMAP** key that some drivers for older technologies, such as serial and parallel ports, use. If your driver supports a technology that uses the **DEVICEMAP** key, the driver can access subkeys and values under the key by calling [**IWDFPropertyStoreFactory::RetrieveDevicePropertyStore**](/windows-hardware/drivers/ddi/wudfddi/nf-wudfddi-iwdfpropertystorefactory-retrievedevicepropertystore).

After a driver has called one of the **RetrieveDevicePropertyStore** methods to open a registry subkey, the driver can use methods exposed by [**IWDFNamedPropertyStore**](/windows-hardware/drivers/ddi/wudfddi/nn-wudfddi-iwdfnamedpropertystore), [**IWDFNamedPropertyStore2**](/windows-hardware/drivers/ddi/wudfddi/nn-wudfddi-iwdfnamedpropertystore2), or [**IWDFUnifiedPropertyStore**](/windows-hardware/drivers/ddi/wudfddi/nn-wudfddi-iwdfunifiedpropertystore) to create, read, and write values under a subkey. The **IWDFNamedPropertyStore2** interface also enables drivers to delete values.

For more information about registry keys for drivers, see [Overview of Registry Trees and Keys](../install/overview-of-registry-trees-and-keys.md).

 

