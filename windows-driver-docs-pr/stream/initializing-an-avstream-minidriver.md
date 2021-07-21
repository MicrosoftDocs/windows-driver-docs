---
title: Initializing an AVStream Minidriver
description: Initializing an AVStream Minidriver
keywords:
- AVStream WDK , initializing minidrivers
- minidrivers WDK AVStream , initializing
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Initializing an AVStream Minidriver





An AVStream minidriver that does not handle device initialization on its own calls [**KsInitializeDriver**](/windows-hardware/drivers/ddi/ks/nf-ks-ksinitializedriver) from the minidriver's [**DriverEntry**](/previous-versions/ff554081(v=vs.85)) routine. **KsInitializeDriver** initializes the driver object of an AVStream driver, in addition to IRP dispatching, PnP add device messages, and unloading.

In calling **KsInitializeDriver**, the minidriver passes a pointer to the driver object to initialize a pointer to the registry path, and optionally, a device descriptor object. Note that passing the [**KSDEVICE\_DESCRIPTOR**](/windows-hardware/drivers/ddi/ks/ns-ks-_ksdevice_descriptor) object is not required. If the minidriver does pass a device descriptor, AVStream creates a device with the specified characteristics at AddDevice time.

The device descriptor object contains a pointer to a [**KSDEVICE\_DISPATCH**](/windows-hardware/drivers/ddi/ks/ns-ks-_ksdevice_dispatch) structure as well as an array of filter descriptors. Provide a [**KSFILTER\_DESCRIPTOR**](/windows-hardware/drivers/ddi/ks/ns-ks-_ksfilter_descriptor) for each filter type that your minidriver supports. When the minidriver calls [**KsInitializeDriver**](/windows-hardware/drivers/ddi/ks/nf-ks-ksinitializedriver), AVStream creates a filter factory object for each type of filter exposed by the minidriver. Individual filters are then instantiated by the filter factory upon receipt of a create IRP for the associated create item. Each filter descriptor contains a pointer to an array of [**KSPIN\_DESCRIPTOR\_EX**](/windows-hardware/drivers/ddi/ks/ns-ks-_kspin_descriptor_ex) objects. AVStream creates a pin factory on the relevant filter for each type of pin the minidriver exposes through that filter.

When a connection is made to a given pin type on a filter, the AVStream pin factory creates a pin object. Note that each filter must expose at least one pin. The minidriver uses the **InstancesNecessary** member of KSPIN\_DESCRIPTOR\_EX to identify the number of instances of this pin type that are necessary for the filter to function correctly. Similarly, the minidriver can impose a maximum on the number of pins that the pin factory can instantiate by using the **InstancesPossible** member of this structure.

AVStream supports two types of processing: [filter-centric processing](filter-centric-processing.md), and [pin-centric processing](pin-centric-processing.md). When laying out the descriptors, decide which type of processing each filter type will perform.

### Installing an AVStream Minidriver

An AVStream minidriver must have an INF file that the system uses to install the driver. An AVStream INF file is based on the common INF format, which is described in [Creating an INF File](../install/overview-of-inf-files.md). You can also refer to the INF files supplied with AVStream sample drivers in the Windows Driver Kit (WDK). Keep in mind the following AVStream-specific guidelines.

If you are writing a minidriver for a parent device, the **AddReg** section of your INF file should contain:

```INF
[ParentName.AddReg]
HKR,"ENUM\[DeviceName]",pnpid,,"[string]"
```

If you are writing a minidriver for a child device, the **AddReg** section should contain:

```INF
[Manufacturer]
...=ChildName
[ChildName]
...=ChildName.Device,AVStream\[string]
```

Note that "AVStream" would be "Stream" for a stream class driver.

For all AVStream minidrivers, the filter-specific reference string in the INF file must match the **ReferenceGuid** member of the [**KSFILTER\_DESCRIPTOR**](/windows-hardware/drivers/ddi/ks/ns-ks-_ksfilter_descriptor) structure.

For more information about descriptors, see [AVStream Descriptors](avstream-descriptors.md).
