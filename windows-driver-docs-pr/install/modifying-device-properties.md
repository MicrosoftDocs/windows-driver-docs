---
title: Rules for Modifying Device Properties
description: Provides information about rules for modifying device properties.
keywords:
- device properties WDK device installations , rules for modifying
- device properties WDK device installations , modifying
- modifying device properties WDK device installations
ms.date: 08/15/2022
---

# Rules for modifying device properties

Many [device properties](device-properties.md) have complex dependencies on other properties or device state. For example, the values of [**DEVPKEY_Device_Class**](./devpkey-device-class.md) and [**DEVPKEY_Device_ClassGuid**](./devpkey-device-classguid.md) must be consistent with one another.

Direct modification of reserved properties could invalidate device installation state. For example, if the [**DEVPKEY_Device_DeviceDesc**](./devpkey-device-devicedesc.md) is changed, system functionality (such as backup, driver rollback, and Windows Update) could break.

The following properties are read-only and can never be set with [**CM_Set_DevNode_Property**](/windows/win32/api/cfgmgr32/nf-cfgmgr32-cm_set_devnode_propertyw) or [**SetupDiSetDeviceProperty**](/windows/win32/api/setupapi/nf-setupapi-setupdisetdevicepropertyw):

- [**DEVPKEY_Device_Address**](./devpkey-device-address.md)

- [**DEVPKEY_Device_BusNumber**](./devpkey-device-busnumber.md)

- [**DEVPKEY_Device_BusTypeGuid**](./devpkey-device-bustypeguid.md)

- [**DEVPKEY_Device_Capabilities**](./devpkey-device-capabilities.md)

- [**DEVPKEY_Device_CompatibleIds**](./devpkey-device-compatibleids.md)

- [**DEVPKEY_Device_DevNodeStatus**](./devpkey-device-devnodestatus.md)

- [**DEVPKEY_Device_EnumeratorName**](./devpkey-device-enumeratorname.md)

- [**DEVPKEY_Device_HardwareIds**](./devpkey-device-hardwareids.md)

- [**DEVPKEY_Device_InstallState**](./devpkey-device-installstate.md)

- [**DEVPKEY_Device_InstanceId**](./devpkey-device-instanceid.md)

- [**DEVPKEY_Device_LegacyBusType**](./devpkey-device-legacybustype.md)

- [**DEVPKEY_Device_LocationPaths**](./devpkey-device-locationpaths.md)

- [**DEVPKEY_Device_PDOName**](./devpkey-device-pdoname.md)

- [**DEVPKEY_Device_PowerData**](./devpkey-device-powerdata.md)

- [**DEVPKEY_Device_ProblemCode**](./devpkey-device-problemcode.md)

- [**DEVPKEY_Device_RemovalPolicy**](./devpkey-device-removalpolicy.md)

- [**DEVPKEY_Device_RemovalPolicyDefault**](./devpkey-device-removalpolicydefault.md)

- [**DEVPKEY_Device_UINumber**](./devpkey-device-uinumber.md)

- [**DEVPKEY_NAME**](./devpkey-name--device-instance-.md)

The following properties are writable. However, they are reserved for use by the operating system and must not be set directly:

- [**DEVPKEY_Device_Class**](./devpkey-device-class.md)

- [**DEVPKEY_Device_ClassGuid**](./devpkey-device-classguid.md)

- [**DEVPKEY_Device_DeviceDesc**](./devpkey-device-devicedesc.md)

- [**DEVPKEY_Device_Driver**](./devpkey-device-driver.md)

- [**DEVPKEY_Device_DriverDesc**](./devpkey-device-driverdesc.md)

- [**DEVPKEY_Device_InstallDate**](./devpkey-device-installdate.md)

- [**DEVPKEY_Device_LowerFilters**](./devpkey-device-lowerfilters.md)

- [**DEVPKEY_Device_Manufacturer**](./devpkey-device-manufacturer.md)

- [**DEVPKEY_Device_Service**](./devpkey-device-service.md)

- [**DEVPKEY_Device_UpperFilters**](./devpkey-device-upperfilters.md)

> [!NOTE]
> *Class installers* and *co-installers* must not change device properties except for the friendly name ([**DEVPKEY_Device_FriendlyName**](./devpkey-device-friendlyname.md)). For more information, see [Accessing Device Instance Properties](accessing-device-instance-properties--windows-vista-and-later-.md).
