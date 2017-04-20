---
title: Initializing an AVStream Minidriver
author: windows-driver-content
description: Initializing an AVStream Minidriver
ms.assetid: 666d6efb-93ec-43f3-87c5-ea1a3983bfd0
keywords:
- AVStream WDK , initializing minidrivers
- minidrivers WDK AVStream , initializing
ms.author: windows-driver-content
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Initializing an AVStream Minidriver


## <a href="" id="ddk-initializing-an-avstream-minidriver-ksg"></a>


An AVStream minidriver that does not handle device initialization on its own calls [**KsInitializeDriver**](https://msdn.microsoft.com/library/windows/hardware/ff562683) from the minidriver's [**DriverEntry**](https://msdn.microsoft.com/library/windows/hardware/ff554081) routine. **KsInitializeDriver** initializes the driver object of an AVStream driver, in addition to IRP dispatching, PnP add device messages, and unloading.

In calling **KsInitializeDriver**, the minidriver passes a pointer to the driver object to initialize a pointer to the registry path, and optionally, a device descriptor object. Note that passing the [**KSDEVICE\_DESCRIPTOR**](https://msdn.microsoft.com/library/windows/hardware/ff561691) object is not required. If the minidriver does pass a device descriptor, AVStream creates a device with the specified characteristics at AddDevice time.

The device descriptor object contains a pointer to a [**KSDEVICE\_DISPATCH**](https://msdn.microsoft.com/library/windows/hardware/ff561693) structure as well as an array of filter descriptors. Provide a [**KSFILTER\_DESCRIPTOR**](https://msdn.microsoft.com/library/windows/hardware/ff562553) for each filter type that your minidriver supports. When the minidriver calls [**KsInitializeDriver**](https://msdn.microsoft.com/library/windows/hardware/ff562683), AVStream creates a filter factory object for each type of filter exposed by the minidriver. Individual filters are then instantiated by the filter factory upon receipt of a create IRP for the associated create item. Each filter descriptor contains a pointer to an array of [**KSPIN\_DESCRIPTOR\_EX**](https://msdn.microsoft.com/library/windows/hardware/ff563534) objects. AVStream creates a pin factory on the relevant filter for each type of pin the minidriver exposes through that filter.

When a connection is made to a given pin type on a filter, the AVStream pin factory creates a pin object. Note that each filter must expose at least one pin. The minidriver uses the **InstancesNecessary** member of KSPIN\_DESCRIPTOR\_EX to identify the number of instances of this pin type that are necessary for the filter to function correctly. Similarly, the minidriver can impose a maximum on the number of pins that the pin factory can instantiate by using the **InstancesPossible** member of this structure.

AVStream supports two types of processing: [filter-centric processing](filter-centric-processing.md), and [pin-centric processing](pin-centric-processing.md). When laying out the descriptors, decide which type of processing each filter type will perform.

### Installing an AVStream Minidriver

An AVStream minidriver must have an INF file that the system uses to install the driver. An AVStream INF file is based on the common INF format, which is described in [Creating an INF File](https://msdn.microsoft.com/library/windows/hardware/ff549520). You can also refer to the INF files supplied with AVStream sample drivers in the Windows Driver Kit (WDK). Keep in mind the following AVStream-specific guidelines.

If you are writing a minidriver for a parent device, the **AddReg** section of your INF file should contain:

```
[ParentName.AddReg]
HKR,"ENUM\[DeviceName]",pnpid,,"[string]"
```

If you are writing a minidriver for a child device, the **AddReg** section should contain:

```
[Manufacturer]
...=ChildName
[ChildName]
...=ChildName.Device,AVStream\[string]
```

Note that "AVStream" would be "Stream" for a stream class driver.

For all AVStream minidrivers, the filter-specific reference string in the INF file must match the **ReferenceGuid** member of the [**KSFILTER\_DESCRIPTOR**](https://msdn.microsoft.com/library/windows/hardware/ff562553) structure.

For more information about descriptors, see [AVStream Descriptors](avstream-descriptors.md).

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstream\stream%5D:%20Initializing%20an%20AVStream%20Minidriver%20%20RELEASE:%20%288/23/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


