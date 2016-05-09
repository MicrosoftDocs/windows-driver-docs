---
title: Porting from ScsiPort to StorPort
description: Porting from ScsiPort to StorPort
ms.assetid: 2a14051d-dc23-4420-a3e5-0827b16b1e42
---

# Porting from ScsiPort to StorPort


The following is a summary of the porting activities that were necessary in order to port the sample code from a Scsiport-based miniport driver to a Storport-based miniport driver:

-   Remove all NextRequest and NextLuRequest calls

-   Rename all ScsiPortXxx calls to StorPortXxx

-   Add BuildIo routine (moved about 75% of code from StartIo)

-   Convert driver to full-duplex operation

-   Add queue management routines (error handling, adapter restart)

-   Add LUN and target reset support

-   Add code to assign queue tags internally (hardware limitation)

-   Add synchronization routines for bus reset and full adapter restart

-   Add support for SRB\_FUNCTION\_POWER (adapter shutdown through SRB)

-   Add StorPortSetDeviceQueueDepth call -- LUN queue depth set to 31

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[storage\storage]:%20Porting%20from%20ScsiPort%20to%20StorPort%20%20RELEASE:%20%285/9/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




