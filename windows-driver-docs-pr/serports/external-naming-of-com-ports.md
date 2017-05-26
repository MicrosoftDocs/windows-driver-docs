---
title: External Naming of COM Ports
author: windows-driver-content
description: External Naming of COM Ports
ms.assetid: d517bc73-9687-45f8-a5f8-837ffe868fae
keywords:
- Serial driver WDK , COM ports
- COM ports WDK serial devices
- serial devices WDK , COM ports
- names WDL serial devices
- external naming WDK serial devices
- symbolic links WDK serial devices
ms.author: windowsdriverdev
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# External Naming of COM Ports


## <a href="" id="ddk-external-naming-of-com-ports-kg"></a>


By default, the Serial function driver creates a symbolic link name for a serial port and registers a GUID\_DEVINTERFACE\_COMPORT [*device interface*](https://msdn.microsoft.com/library/windows/hardware/ff556277#wdkgloss-device-interface) for the port. By definition, a serial port is a [COM port](configuration-of-com-ports.md) only if it has a COM port device interface associated with it.

For a Plug and Play serial device, external naming is controlled by a **SerialSkipExternalNaming** entry value under the hardware key of the device. If the **SerialSkipExternalNaming** entry value does not exist, or its value is zero, Serial creates a COM port device interface; otherwise, Serial does not create a COM port interface. Serial does not support this entry value for a legacy COM port and always creates a COM port device interface for a legacy COM port.

Serial performs the following tasks to create a COM port device interface:

-   Creates a symbolic link between **\\DosDevices\\**&lt;*PortName*&gt; and the internal device object name for a COM port.

    &lt;*PortName*&gt; is the value of the **PortName** (or **Identifier**) entry value for the COM port. The Ports class installer sets **PortName** to COM*&lt;n&gt;*, where &lt;*n&gt;* is a COM port number that the installer obtains from the [COM port database](com-port-database.md). Serial uses this name to create a symbolic link to the port. There is no limit to the number of COM ports that Windows supports. User-mode clients use the symbolic link name to open a COM port.

-   Writes an entry value under the **\\Registry\\Machine\\Hardware\\DeviceMap\\SERIALCOMM** key.

    The name of the entry value is **\\Device\\Serial**&lt;*m&gt;,* where *&lt;m&gt;* is a number assigned to the device by Serial. Note that the serial device number *&lt;m&gt;* is the not the same as a COM port number *&lt;n&gt;*. The value of **\\Device\\Serial**&lt;*m*&gt; is set to the value of **PortName**.

-   Registers a device interface of type GUID\_DEVINTERFACE\_COMPORT for the COM port.

    Clients can register for notification of the arrival of a COM port interface, or can obtain the symbolic link names of all registered COM port interfaces.

For more information about how Serial uses registry entry values, see [Registry Settings for Serial](registry-settings-for-serial.md).

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bserports\serports%5D:%20External%20Naming%20of%20COM%20Ports%20%20RELEASE:%20%288/4/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


