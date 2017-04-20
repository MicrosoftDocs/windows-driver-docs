---
title: Registry Settings for a Plug and Play Serial Device
author: windows-driver-content
description: Registry Settings for a Plug and Play Serial Device
ms.assetid: 57bd090a-20fe-41c6-b730-0479f6ae0982
keywords:
- Serial driver WDK , Plug and Play devices
- Plug and Play serial devices WDK
- serial devices WDK , Plug and Play
ms.author: windows-driver-content
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Registry Settings for a Plug and Play Serial Device


## <a href="" id="ddk-registry-settings-for-a-plug-and-play-serial-device-kg"></a>


This topic describes the registry settings that Serial uses as a function driver for a Plug and Play serial device. Serial also uses these settings as a lower-level device filter driver for a device that requires a 16550 UART-compatible interface.

Serial queries these registry entry values when it adds the device. If a device-specific entry value is not present, Serial uses a Serial service value.

The following registry settings are under the Plug and Play registry key for a device.

<a href="" id="portname--reg-sz-"></a>**PortName** (REG\_SZ)  
Specifies the name of the device. The name of a device is typically COM*&lt;n&gt;,* where *&lt;n&gt;* is a COM port number that the installer obtains from the [COM port database](com-port-database.md). However, the device can be set to any non-NULL string. If the device is configured as a [COM port](configuration-of-com-ports.md), Serial uses the port name to create a symbolic link name for the device. The default value of **PortName** is an empty string.

<a href="" id="identifier--reg-sz-"></a>**Identifier** (REG\_SZ)  
Specifies the name of the device. The support for an **Identifier** entry value is provided for compatibility with some legacy PCMCIA devices. The use of **Identifier** is obsolete and should not be used with Microsoft Windows 2000 and later drivers. For a description, see the **PortName** entry value.

<a href="" id="multiportdevice--reg-dword-"></a>**MultiportDevice** (REG\_DWORD)  
Specifies a Boolean flag that indicates whether a serial port is a device on a multiport device. If **MultiportDevice** is 0x00000000, the serial port is a stand-alone device; otherwise, the serial port is on a multiport device. The default value of **MultiportDevice** is 0x00000000.

<a href="" id="portindex--reg-dword-"></a>**PortIndex** (REG\_DWORD)  
Specifies the index number of a serial port on a multiport device. The **Indexed** entry value specifies whether a port is bitmapped or indexed. The default value of **PortIndex** is 0x00000000.

<a href="" id="clockrate--reg-dword-"></a>**ClockRate** (REG\_DWORD)  
Specifies the UART clock rate. The default value of **ClockRate** is 1,843,200 Hertz.

<a href="" id="indexed--reg-dword-"></a>**Indexed** (REG\_DWORD)  
Specifies a Boolean flag that indicates whether a port on a multiport device is *bitmapped* or *indexed*. If **Indexed** is nonzero, the port is indexed; otherwise, the port is bitmapped. **Indexed** is used in conjunction with the **PortIndex** entry value. The default value of **Indexed** is 0x00000000.

<a href="" id="disableport--reg-dword-"></a>**DisablePort** (REG\_DWORD)  
Boolean flag that specifies whether to disable the device. If **DisablePort** is nonzero, Serial disables the device; otherwise, the device is enabled. Use of the **DisablePort** entry value is obsolete and should not be used with Windows 2000 and later drivers. Windows 2000 provides a generic manual method through the GUI of Device Manager to enable and disable devices. The default value of **DisablePort** is 0x00000000. Note that flagging a device as disabled does not mean that the device does not exist. Serial still attempts to detect the presence of a disabled device. If the device is specified as disabled, Serial returns STATUS\_NO\_SUCH\_DEVICE in response to an **IRP\_MN\_START\_DEVICE** request. After the start request fails, the Plug and Play manager sends a remove request.

<a href="" id="forcefifoenable--reg-dword-"></a>**ForceFifoEnable** (REG\_DWORD)  
Specifies a Boolean flag that indicates whether to force Serial to use FIFOs. If **ForceFifoEnable** is nonzero, FIFOs are used, regardless of whether Serial can detect the presence of FIFOs. Otherwise, FIFOs are only used if Serial can detect them. The default value of **ForceFifoEnable** is the value set for the Serial service. (The default value for the Serial service is 0x00000001.)

<a href="" id="rxfifo--reg-dword-"></a>**RxFIFO** (REG\_DWORD)  
Specifies the number of bytes in the receive FIFO that triggers a serial port interrupt. For valid values, see the constants defined in the Serial.h header file in the [Serial driver sample](http://go.microsoft.com/fwlink/p/?LinkId=617962) on GitHub. The default value of **RxFIFO** is the value set for the Serial service. (The default value for the Serial service is eight bytes.)

<a href="" id="txfifo--reg-dword-"></a>**TxFIFO** (REG\_DWORD)  
Specifies the number of bytes in the transmit FIFO that triggers a serial device interrupt. For valid values, see the constants defined in the Serial.h header file in the [Serial driver sample](http://go.microsoft.com/fwlink/p/?LinkId=617962) on GitHub. The default value of **TxFIFO** is the value set for the Serial service. (The default value for the Serial service is fourteen bytes.)

<a href="" id="maskinverted--reg-dword-"></a>**MaskInverted** (REG\_DWORD)  
Specifies a Boolean flag that indicates whether the serial device hardware inverts the contents of the interrupt status register. If **MaskInverted** is nonzero, the interrupt status register is inverted; otherwise, the interrupt status register is not inverted. The default value of **MaskInverted** is 0x00000000.

<a href="" id="serialskipexternalnaming--reg-dword-"></a>**SerialSkipExternalNaming** (REG\_DWORD)  
Specifies a Boolean flag that indicates whether Serial configures the device as a [COM port](configuration-of-com-ports.md). If **SerialSkipExternalNaming** is set to 0x00000000, Serial configures the device as a COM port; otherwise, Serial does not configure the device as a COM port. The default value of **SerialSkipExternalNaming** is 0x00000000. For more information about how Serial configures a device as a COM port, see [External Naming of COM Ports](external-naming-of-com-ports.md).

<a href="" id="serialrelinquishpowerpolicy--reg-dword-"></a>**SerialRelinquishPowerPolicy** (REG\_DWORD)  
Specifies a Boolean flag that indicates whether Serial is the power policy owner for a serial device stack. If **SerialRelinquishPowerPolicy** is zero, Serial is the power policy owner; otherwise, Serial is not the power policy owner. The default value of **SerialRelinquishPowerPolicy** is 0x00000000.

<a href="" id="share-system-interrupt--reg-dword-"></a>**Share System Interrupt** (REG\_DWORD)  
Boolean flag that specifies whether to permit the system to share the interrupt that the device uses. If **Share System Interrupt** is nonzero, the interrupt can be shared; otherwise, the interrupt cannot be shared. The default value of **Share System Interrupt** is the value set for the **PermitShare** entry value for the Serial service. (The default service value for **PermitShare** is 0x00000000.)

<a href="" id="serialioresourcesindex--reg-dword-"></a>**SerialIoResourcesIndex** (REG\_DWORD)  
Specifies the index of the partial resource descriptor that Serial uses to determine the I/O addresses of the serial register set for the device. The default value of **SerialIoResourceIndex** is 0x00000000.

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bserports\serports%5D:%20Registry%20Settings%20for%20a%20Plug%20and%20Play%20Serial%20Device%20%20RELEASE:%20%288/4/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


