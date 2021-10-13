---
title: Retrieving Device Setup Information
description: Retrieving Device Setup Information
keywords:
- audio adapters WDK , retrieving setup information
- adapter drivers WDK audio , retrieving setup information
- Port Class audio adapters WDK , retrieving setup information
- retrieving device setup information
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Retrieving Device Setup Information


## <span id="retrieving_device_setup_information"></span><span id="RETRIEVING_DEVICE_SETUP_INFORMATION"></span>


To retrieve setup information from the registry, an adapter driver can call the [**PcGetDeviceProperty**](/windows-hardware/drivers/ddi/portcls/nf-portcls-pcgetdeviceproperty) function, and a miniport driver can call the port driver's [**IPort::GetDeviceProperty**](/windows-hardware/drivers/ddi/portcls/nf-portcls-iport-getdeviceproperty) method.

For either of these calls, the caller selects the type of setup information to request by setting the device-property parameter to one of the following DEVICE\_REGISTRY\_PROPERTY enumeration values from header file Wdm.h:

-   **DevicePropertyAddress**

-   **DevicePropertyBootConfiguration**

-   **DevicePropertyBootConfigurationTranslated**

-   **DevicePropertyBusNumber**

-   **DevicePropertyBusTypeGuid**

-   **DevicePropertyClassGuid**

-   **DevicePropertyClassName**

-   **DevicePropertyCompatibleIDs**

-   **DevicePropertyDetachability**

-   **DevicePropertyDeviceDescription**

-   **DevicePropertyDriverKeyName**

-   **DevicePropertyEnumeratorName**

-   **DevicePropertyFriendlyName**

-   **DevicePropertyHardwareID**

-   **DevicePropertyInstallState**

-   **DevicePropertyLegacyBusType**

-   **DevicePropertyLocationInformation**

-   **DevicePropertyManufacturer**

-   **DevicePropertyPhysicalDeviceObjectName**

-   **DevicePropertyUINumber**

For a description of the DeviceProperty*Xxx* values above, see [**IoGetDeviceProperty**](/windows-hardware/drivers/ddi/wdm/nf-wdm-iogetdeviceproperty).

 

