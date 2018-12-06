---
title: External Naming of COM Ports
description: External Naming of COM Ports
ms.assetid: d517bc73-9687-45f8-a5f8-837ffe868fae
keywords:
- Serial driver WDK , COM ports
- COM ports WDK serial devices
- serial devices WDK , COM ports
- names WDL serial devices
- external naming WDK serial devices
- symbolic links WDK serial devices
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# External Naming of COM Ports





By default, the Serial function driver creates a symbolic link name for a serial port and registers a GUID\_DEVINTERFACE\_COMPORT [*device interface*](https://msdn.microsoft.com/library/windows/hardware/ff556277#wdkgloss-device-interface) for the port. By definition, a serial port is a [COM port](configuration-of-com-ports.md) only if it has a COM port device interface associated with it.

For a Plug and Play serial device, external naming is controlled by a **SerialSkipExternalNaming** entry value under the hardware key of the device. If the **SerialSkipExternalNaming** entry value does not exist, or its value is zero, Serial creates a COM port device interface; otherwise, Serial does not create a COM port interface. Serial does not support this entry value for a legacy COM port and always creates a COM port device interface for a legacy COM port.

Serial performs the following tasks to create a COM port device interface:

- Creates a symbolic link between **\\DosDevices\\**&lt;*PortName*&gt; and the internal device object name for a COM port.

  &lt;*PortName*&gt; is the value of the **PortName** (or **Identifier**) entry value for the COM port. The Ports class installer sets **PortName** to COM<em>&lt;n&gt;</em>, where &lt;*n&gt;* is a COM port number that the installer obtains from the [COM port database](com-port-database.md). Serial uses this name to create a symbolic link to the port. There is no limit to the number of COM ports that Windows supports. User-mode clients use the symbolic link name to open a COM port.

- Writes an entry value under the **\\Registry\\Machine\\Hardware\\DeviceMap\\SERIALCOMM** key.

  The name of the entry value is **\\Device\\Serial**&lt;*m&gt;,* where *&lt;m&gt;* is a number assigned to the device by Serial. Note that the serial device number *&lt;m&gt;* is the not the same as a COM port number *&lt;n&gt;*. The value of **\\Device\\Serial**&lt;*m*&gt; is set to the value of **PortName**.

- Registers a device interface of type GUID\_DEVINTERFACE\_COMPORT for the COM port.

  Clients can register for notification of the arrival of a COM port interface, or can obtain the symbolic link names of all registered COM port interfaces.

For more information about how Serial uses registry entry values, see [Registry Settings for Serial](registry-settings-for-serial.md).

 

 




