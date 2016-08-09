---
title: Installing Plug and Play Serial Ports and COM Ports
author: windows-driver-content
description: Installing Plug and Play Serial Ports and COM Ports
MS-HAID:
- 'sseovr\_741c56d5-b702-43c3-a1cb-2b69348d634d.xml'
- 'serports.installing\_plug\_and\_play\_serial\_ports\_and\_com\_ports'
MSHAttr:
- 'PreferredSiteName:MSDN'
- 'PreferredLib:/library/windows/hardware'
ms.assetid: 48a489a1-6ed9-4e17-a7b5-0f2325486ab6
keywords: ["Serial driver WDK , Plug and Play devices", "Plug and Play serial devices WDK", "serial devices WDK , Plug and Play"]
---

# Installing Plug and Play Serial Ports and COM Ports


## <a href="" id="ddk-installing-plug-and-play-serial-ports-and-com-ports-kg"></a>


By default, the combined operation of the Ports class installer and the Serial function driver configure a serial port as a COM port. Serial creates a COM port device interface for a serial port if the **SerialSkipExternalNaming** entry value for a device does not exist or is set to zero. For more information about how Serial creates a COM port device interface for a COM port and how to override this operation, see [External Naming of COM Ports](external-naming-of-com-ports.md).

The Ports class installer performs the following tasks when it installs a serial port:

1.  Selects a COM port number and sets a port name in the **PortName** entry value under the device's hardware key. The port name has the format COM*&lt;n&gt;*, where *&lt;n&gt;* is the port number. If Serial creates a COM port interface for the serial port, Serial uses the value of **PortName** as the symbolic link name for the COM port.

2.  Displays a default property page dialog box, which allows a user to select settings for the port. For information about how to install a custom properties page, see [Installing an Advanced Properties Page for a COM Port](installing-an-advanced-properties-page-for-a-com-port.md).

3.  Sets the device friendly name for the device. You obtain the name using the SPDRP\_FRIENDLYNAME flag with **SetupDiGetDeviceRegistryProperty**.

You can supply a co-installer to set [registry settings for a Plug and Play serial device](registry-settings-for-a-plug-and-play-serial-device.md). If an entry value is not present in the registry, Serial uses a default value for the port.

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bserports\serports%5D:%20Installing%20Plug%20and%20Play%20Serial%20Ports%20and%20COM%20Ports%20%20RELEASE:%20%288/4/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


