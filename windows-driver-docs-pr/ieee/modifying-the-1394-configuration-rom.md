---
title: Modifying the 1394 Configuration ROM
description: Modifying the 1394 Configuration ROM
MS-HAID:
- '1394-configrom\_80b59cac-0599-4d82-b46b-94e6fcde850a.xml'
- 'IEEE.modifying\_the\_1394\_configuration\_rom'
MSHAttr:
- 'PreferredSiteName:MSDN'
- 'PreferredLib:/library/windows/hardware'
ms.assetid: 3dc4fe53-a26b-44c7-96ef-e7bb6181c958
keywords: ["IEEE 1394 WDK buses , modifying Configuration ROMs", "1394 WDK buses , modifying Configuration ROMs", "Configuration ROMs WDK IEEE 1394 bus"]
---

# Modifying the 1394 Configuration ROM


## <a href="" id="ddk-modifying-the-1394-configuration-rom-kg"></a>


A Microsoft Windows system connected to the 1394 bus exposes a Configuration ROM that describes the functional units supported by the node. For further information about 1394 Configuration ROMs, see the IEEE 1394-1995 and IEEE-1212-2000 specifications. In Windows XP and later operating systems, the contents of the Configuration ROM can be dynamically defined in two ways:

1.  Drivers can dynamically modify the Configuration ROM to expose hardware designed for non-1394 buses on the 1394 bus.

    For example, consider a general purpose system that has an internal DVD drive connected to the system's IDE bus. A driver that maps 1394 requests into the protocol used by the DVD drive could expose the DVD drive on the 1394 bus to other 1394 nodes. To do this, it would have to add a new unit directory to the 1394 Configuration ROM of the system. Other systems connected on the 1394 bus will then be able to enumerate the general purpose system as though it were a 1394 DVD device.

2.  Drivers can use virtual physical device objects (PDOs) to emulate hardware in ways that facilitate the testing of device drivers.

    Device emulation allows developers to test drivers for devices that they have not yet received. Hardware emulation drivers can expose a virtual 1394 device on the 1394 bus. Developers can then debug a driver for the new hardware on another system. For more information about device emulations, see [IEEE 1394 Hardware Emulation Drivers](https://msdn.microsoft.com/library/windows/hardware/ff537214).

## Related topics


[Retrieving the Contents of a IEEE 1394 Node's Configuration ROM](https://msdn.microsoft.com/library/windows/hardware/gg266408)

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5BIEEE\buses%5D:%20Modifying%20the%201394%20Configuration%20ROM%20%20RELEASE:%20%287/14/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")





