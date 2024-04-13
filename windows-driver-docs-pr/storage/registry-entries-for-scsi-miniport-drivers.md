---
title: Registry Entries for SCSI Miniport Drivers
description: Registry Entries for SCSI Miniport Drivers
keywords:
- SCSI miniport drivers WDK storage , registry entries
- registry WDK SCSI
- TimeoutValue
- TotalSenseDataBytes
- MaximumSGList
- BusType
- CreateInitiatorLU
- pseudo-LUNs WDK SCSI
ms.date: 10/27/2021
---

# Registry Entries for SCSI Miniport Drivers

The following registry entries allow you to configure the behavior of the port driver/SCSI miniport driver pair. For information about the **PnpInterface** registry entry required for all Plug and Play (PnP) devices, see [Registry Entries for Plug and Play SCSI Miniport Drivers](registry-entries-for-plug-and-play-scsi-miniport-drivers.md).

- **TimeoutValue**
  - Location: HKLM\\System\\CurrentControlSet\\Services\\Disk\\TimeoutValue
  - Values: 1 - 255 seconds
  - Meaning: Time in units of seconds before an SRB request initiated by the disk class driver will time out. If this registry value is not set, a default value of 10 seconds is used. Time-out values for requests that are initiated by class drivers vary according to the class driver.

  > [!NOTE]
  > If the miniport sets a value, that timeout will be honored preferentially. The timeout selection logic is as follows:
  >
  > - Starting in Windows 8, if the miniport sets a timeout value (in HKLM … \\Services\\<*miniport*>\\Parameters\\IoTimeoutValue), this value is honored by the storage class driver.
   > - Otherwise, if the disk global timeout registry (this key) is set, this value is honored by the storage class driver.
  > - Otherwise, a default value of 10 seconds is used by the storage class driver.
  > - Operating system (OS) version: Available in all versions of the Windows operating systems.

- **TotalSenseDataBytes**
  - Location: HKLM\\System\\CurrentControlSet\\Enum\\<*Bus*>\\<*DeviceID*>\\<*Device*>\\DeviceParameters\\ScsiPort\\TotalSenseDataBytes
  - Values: Between 18 and 255 for SCSI Port. Storport always uses 255.
  - Meaning: If set, this value designates the size in bytes of the buffer that the SCSI Port driver allocates for request sense data. If the value is not set, SCSI port uses a default size of 18. The Storport driver always allows 255. Warning: filter drivers that insert between the class driver and the port driver must respect this value and not attempt to manage the size of the sense data buffer.
  - OS version: Available starting in Windows 2000 Server.

- **MaximumSGList**
  - Location: HKLM\\System\\CurrentControlSet\\Services\\<*ServiceName*>\\Parameters\\Device\\MaximumSGList, where <*ServiceName*> = the miniport driver name specified with the **AddServices** directive in the INF file.
  - Values: Between 16 and 255.
  - Meaning: Indicates the number of scatter/gather list elements supported by the adapter.
  - OS version: This feature is available in Windows NT 4.0 SP4 and later operating systems.
- **BusType**
  - Location: HKLM\\System\\CurrentControlSet\\Services\\<*ServiceName*>\\Parameters\\BusType, where <*ServiceName*> = the miniport driver name specified with the **AddServices** directive in the INF file.
  - Values: The same as [**STORAGE\_BUS\_TYPE**](/previous-versions/windows/hardware/drivers/ff566356(v=vs.85)) enumerator:
  - Meaning: Indicates the type of bus that the adapter is connected to.
  - OS version: Available starting in Windows 2000.

- **CreateInitiatorLU**
  - Location: <*ServiceName*>\\Parameters\\Device\\CreateInitiatorLU, where <*ServiceName*> = the miniport driver name specified with the **AddServices** directive in the INF file.
  - Values: Either 0 or 1.
  - Meaning: A value of 1 indicates that the port driver will create an "initiator logical unit," so that higher-level drivers can send certain requests to the port driver even though there is no actual hardware device connected to the adapter or the connected device is not visible to the system. Sometimes it is necessary to configure a device's operating parameters or update its firmware before it will be visible to the system. Prior to Windows Server 2003, it was not possible to instruct the port driver to update firmware for a device unless the port driver had at least one logical unit in its device stack. Some vendors attempted to remedy this deficiency by adding so-called "pseudo-LUNs" to the adapter's stack, but this created problems for setup and disk management, and occasionally such solutions would cause the configuration manager to prompt the user for a driver for a non-existent device. With the new "initiator logical unit" feature, it is no longer necessary to use these work-around techniques. By setting **CreateInitiatorLU** to 1 in the registry, you can send IOCTLs and WMI requests to the port driver whether it has devices attached that are visible to the operating system. Another use of the "initiator logical unit" feature is to allow communication with fibre channel adapters that have a purely administrative function and no attached devices.
  - OS version: Available starting in Windows Server 2003. The value of this registry value only affects the functionality of the SCSI Port miniport drivers. Storport miniport driver always permit access to adapter objects, even when no device is attached to the adapter.
