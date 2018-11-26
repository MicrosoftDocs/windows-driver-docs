---
title: Accessing PCI Device Configuration Space
description: Accessing PCI Device Configuration Space
ms.assetid: 05e0ada9-d465-4787-abc5-469a75352ee0
keywords:
- PCI configuration space WDK buses
- configuration space WDK buses
- IRP_MN_READ_CONFIG
- IRP_MN_WRITE_CONFIG
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Accessing PCI Device Configuration Space


Some operations on a peripheral component interconnect (PCI) device are reserved for the device's function driver. Such operations include, for example, accessing the device-specific configuration space of a bus and programming a direct memory access (DMA) controller. Microsoft provides system support for accessing the configuration space of PCI devices by two methods:

-   The [**BUS\_INTERFACE\_STANDARD**](https://msdn.microsoft.com/library/windows/hardware/ff540707) bus interface

-   The configuration I/O request packets (IRPs), [**IRP\_MN\_READ\_CONFIG**](https://msdn.microsoft.com/library/windows/hardware/ff551727) and [**IRP\_MN\_WRITE\_CONFIG**](https://msdn.microsoft.com/library/windows/hardware/ff551769)

The Windows XP and Windows Server 2003 and later operating systems have exclusive control over the configuration space header, as defined by the *PCI Local Bus* specification, as well as all of the capabilities in the capabilities linked list. Drivers must not attempt to modify these registers.

However, drivers can write to the configuration space that does not belong to the header or the capabilities list that is vendor-defined, using the IRP\_MN\_WRITE\_CONFIG request or the **SetBusData** method of BUS\_INTERFACE\_STANDARD. Drivers can also read a device's capabilities, using the IRP\_MN\_READ\_CONFIG request or the **GetBusData** method of BUS\_INTERFACE\_STANDARD. To use IRP\_MN\_READ\_CONFIG or IRP\_MN\_WRITE\_CONFIG, drivers must be running at PASSIVE\_LEVEL. For a list of capabilities and the corresponding structures that drivers can query for, see the [PCI Structures](https://msdn.microsoft.com/library/windows/hardware/ff537590) section.

Drivers can read from the extended PCI device configuration space (that is, more than 256 bytes of configuration data) using the IRP\_MN\_READ\_CONFIG request or the **GetBusData** method of BUS\_INTERFACE\_STANDARD. Likewise, drivers can write to the extended PCI device configuration space using the IRP\_MN\_WRITE\_CONFIG request or the **SetBusData** method of BUS\_INTERFACE\_STANDARD. If a device does not have an extended configuration space or the platform does not define a path for an extended configuration space on a device, the read requests will return 0xFFFF and the write requests will have no effect. To determine if the operation succeeded, drivers can examine the number of bytes read or written.

PCI Express and PCI-X mode 2 support an extended PCI device configuration space of greater than 256 bytes. Drivers can read and write to this configuration space, but only with the appropriate hardware and BIOS support. Within the ACPI BIOS, the root bus must have a PNP ID of either PNP0A08 or PNP0A03. For root buses with PNP ID of PNP0A03, the \_DSM method with function 4 should indicate that the current mode is PCI-X mode 2. All the bridges and devices should either be PCI express or operate in PCI-X mode 2.

In addition, the system should support memory-mapped configuration space accesses. This is by defining an MCFG table in the system BIOS/firmware. Windows Vista and Windows Server 2008 and later operating systems automatically support memory-mapped configuration space accesses.

The following code example shows how to query for the power management capability data of a device:

```cpp
#define LSZ sizeof(ULONG)
#define HEADERSIZE (FIELD_OFFSET (PCI_COMMON_CONFIG, DeviceSpecific)) / LSZ

 // The PCI_COMMON_CONFIG structure includes 
// device specific data. The following
// structure is used to retrieve the
// 64 bytes of data that precedes the
// device-specific data.

typedef struct {
    ULONG  Reserved[HEADERSIZE];
} PCI_COMMON_HEADER, *PPCI_COMMON_HEADER;

PCI_COMMON_HEADER Header;
PCI_COMMON_CONFIG *pPciConfig = (PCI_COMMON_CONFIG *)&Header;
// declare power management capabilities header
 PCI_PM_CAPABILITY  PowerMgmtCapability;
PCI_PM_CAPABILITY  *pPowerMgmtCapability = &Capability; 
UCHAR CapabilityOffset;

// Read the first part of the header
// to get the status register and
// the capabilities pointer.
// The "capabilities pointer" is
// actually an offset from the
// beginning of the header to a
// linked list of capabilities.
BusInterface.GetBusData(Context,
    PCI_WHICHSPACE_CONFIG,
    pPciConfig, // output buffer
    0, // offset of the capability to read
 sizeof(PCI_COMMON_HEADER)); // just 64 bytes

// Check the Status register to see if 
// this device supports capability lists.
 
if ((pPciConfig->Status &
   PCI_STATUS_CAPABILITIES_LIST) == 0) {
   // does not support capabilities list
   return(STATUS_NOT_IMPLEMENTED);
}

// The device supports capability lists.
// Find the capabilities.

// The position of the capabilities pointer
// in the header depends on whether this is 
// a bridge type device. Check the type.

if ((pPciConfig->HeaderType & 
   (~PCI_MULTIFUNCTION)) == PCI_BRIDGE_TYPE) {
   CapabilityOffset = 
       pPciConfig->u.type1.CapabilitiesPtr;
} else if ((pPciConfig->HeaderType & 
   (~PCI_MULTIFUNCTION)) == PCI_CARDBUS_TYPE) {
   CapabilityOffset = 
       pPciConfig->u.type2.CapabilitiesPtr;
} else {
   CapabilityOffset = 
       pPciConfig->u.type0.CapabilitiesPtr;
}

// Loop through the capabilities in search
// of the power management capability. The
// list is NULL-terminated, so the last 
// offset will always be zero.

while (CapabilityOffset != 0) {

    // Read the header of the capability at 
    // this offset.

    // If the retrieved capability is not
    // the power management capability that
    // we are looking for, follow the
    // link to the next capability and
    // continue looping.

    BusInterface.GetBusData(Context,
        PCI_WHICHSPACE_CONFIG,
        pPowerMgmtCapability,
        CapabilityOffset,
        sizeof(PCI_CAPABILITIES_HEADER));

    if (Capability->Header.CapabilityID ==
 PCI_CAPABILITY_ID_POWER_MANAGEMENT) {
        // Found the power management capability
        break;
    } else {
        // This is some other capability.
        // Keep looking for the power 
        // management capability.
        CapabilityOffset = Capability->Header.Next;
    }
}

if (CapabilityOffset == 0) {
    // We didn&#39;t find a power management
    // capability. Return an error.
    return(STATUS_NOT_IMPLEMENTED);
}

// Skip past the capabilities header and read
// the rest of the power management capability

BusInterface.GetBusData(Context,
   PCI_WHICHSPACE_CONFIG,
   // write to location immediately following header
   & (pPowerMgmtCapability->Header) + 1, 
   CapabilityOffset + 
       sizeof(PCI_CAPABILITIES_HEADER),
   sizeof(PCI_PM_CAPABILITY) - 
       sizeof(PCI_CAPABILITIES_HEADER)
);
```

 

 




