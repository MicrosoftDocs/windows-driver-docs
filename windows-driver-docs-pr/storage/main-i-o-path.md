---
title: Main I/O Path
description: Main I/O Path
ms.assetid: 643842e4-a75e-4d86-a1f7-d1a4468b5e17
---

# Main I/O Path


One of the architectural improvements that Storport has to offer is the HwBuildIo routine. Although this Storport miniport driver entry point is optional, it is highly recommended. The LSI\_U3 driver takes advantage of this improvement by implementing the LsiU3BuildIo routine. This entry point is called before the HwStartIo routine with no locks held, and as long as no shared memory is modified, this routine may perform processing that was previously done in the HwStartIo routine in the case of a Scsiport-based miniport driver. This allows most of the processing required to start separate I/O requests to be done in parallel on multiprocessor systems.

The LsiU3StartIo routine assigns driver queue tags to I/O requests. This is needed since Storport assigns queue tags on a per-LUN basis, not a per-adapter basis. The adapter hardware is limited to a maximum of 256 outstanding I/Os.

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[storage\storage]:%20Main%20I/O%20Path%20%20RELEASE:%20%285/9/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




