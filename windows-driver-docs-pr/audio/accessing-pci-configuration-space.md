---
title: Accessing PCI Configuration Space
description: Accessing PCI Configuration Space
ms.assetid: 4ec520db-7976-40e8-8336-f9056dc024b1
keywords: ["PCI configuration space WDK audio", "audio adapter drivers WDK , PCI configuration space", "adapter drivers WDK audio , PCI configuration space"]
---

# Accessing PCI Configuration Space


## <span id="accessing_pci_configuration_space"></span><span id="ACCESSING_PCI_CONFIGURATION_SPACE"></span>


In Windows Me/98, and Windows 2000 and later, an adapter driver can access its adapter card's PCI configuration space at IRQL PASSIVE\_LEVEL by using the [**IRP\_MN\_READ\_CONFIG**](https://msdn.microsoft.com/library/windows/hardware/ff551727) and [**IRP\_MN\_WRITE\_CONFIG**](https://msdn.microsoft.com/library/windows/hardware/ff551769) requests.

In Windows 2000 and later, PCI driver stacks export the [**BUS\_INTERFACE\_STANDARD**](https://msdn.microsoft.com/library/windows/hardware/ff540707) interface, which provides access to the PCI configuration space at IRQL DISPATCH\_LEVEL.

For more information, see [Accessing Device Configuration Space](https://msdn.microsoft.com/library/windows/hardware/ff540450).

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[audio\audio]:%20Accessing%20PCI%20Configuration%20Space%20%20RELEASE:%20%287/18/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




