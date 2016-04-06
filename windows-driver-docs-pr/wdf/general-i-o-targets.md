---
title: General I/O Targets
description: General I/O Targets
ms.assetid: e5527aa2-a63f-49d8-aa9a-f91efd2ae9ad
keywords: ["general I/O targets WDK KMDF", "I/O targets WDK KMDF , general", "local I/O targets WDK KMDF", "remote I/O targets WDK KMDF", "general I/O targets WDK KMDF , about general I/O targets"]
---

# General I/O Targets


## <a href="" id="ddk-general-i-o-targets-df"></a>


General I/O targets do not support special, device-specific data formats, such as USB request blocks. Before drivers send data to a general I/O target, they must put data into a write buffer in a format that the I/O target can interpret. Likewise, when drivers read data from a general I/O target, the drivers must be able interpret the contents of data buffers that they receive from the target.

General I/O targets are either local or remote:

<a href="" id="local-i-o-targets"></a>Local I/O Targets  
Each framework-based function driver, filter driver, and miniport driver has a local I/O target for each of the driver's devices. A device's local I/O target is always the next-lower driver in the driver stack.

<a href="" id="remote-i-o-targets"></a>Remote I/O Targets  
Remote I/O targets represent the top of a different driver stack or (rarely) a different driver in the current driver's stack.

This section includes:

-   [Initializing a General I/O Target](initializing-a-general-i-o-target.md)

-   [Sending I/O Requests to General I/O Targets](sending-i-o-requests-to-general-i-o-targets.md)

-   [Controlling a General I/O Target's State](controlling-a-general-i-o-target-s-state.md)

-   [Obtaining Information About a General I/O Target](obtaining-information-about-a-general-i-o-target.md)

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bwdf\wdf%5D:%20General%20I/O%20Targets%20%20RELEASE:%20%284/5/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




