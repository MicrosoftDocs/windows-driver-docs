---
title: Creating and Starting a Parallel Port
author: windows-driver-content
description: Creating and Starting a Parallel Port
MS-HAID:
- 'vspd\_dacad28c-06f7-43c4-af04-60461ddf2bd6.xml'
- 'parports.creating\_and\_starting\_a\_parallel\_port'
MSHAttr:
- 'PreferredSiteName:MSDN'
- 'PreferredLib:/library/windows/hardware'
ms.assetid: 75c82353-6490-47e9-9278-ec0981af9ae9
keywords: ["parallel ports WDK , creating", "parallel ports WDK , starting"]
---

# Creating and Starting a Parallel Port


## <a href="" id="ddk-creating-and-starting-a-parallel-port-kg"></a>


The Plug and Play manager uses the Plug and Play support of the system-supplied function driver for parallel ports to create and start a function device object ([*FDO*](https://msdn.microsoft.com/library/windows/hardware/ff556280#wdkgloss-fdo)) that represents a parallel port.

The parallel port function driver does the following:

-   Creates a named FDO

    The format of the device name for the parallel port is "\\Device\\ParallelPortx", where x is an integer value for the port number. The parallel port function driver uses the PortName entry value (REG\_SZ) under the Plug and Play registry key for the parallel port to determine the port number. Note that if PortName has the format "LPTn", where n is the number of the port, then x in "ParallePortx" is set to the value of (n -1). For example, "ParallelPort0" is associated with "LPT1". If PortName does not have the correct format, a device object is not created.

    Note that a "ParallelPortx" device name is not guaranteed. Microsoft recommends using [**IoRegisterPlugPlayNotification**](https://msdn.microsoft.com/library/windows/hardware/ff549526) to be notified of the arrival of a GUID\_PARALLEL\_DEVICE device interface.

-   Registers and enables a GUID\_PARALLEL\_DEVICE interface for the parallel port

-   Validates the resources sent by the Plug and Play manager

-   Initializes 1284.3 devices attached to the parallel port

    The parallel port function driver counts the number of daisy chain devices, and assigns a daisy chain ID to each device. In Microsoft Windows 2000, the driver assigns IDs from 0 to 3. In Windows XP, the driver assigns an ID of 0 or 1. The device IDs are assigned to the devices in ascending order, beginning with the device that is physically closest to the parallel port.

-   Registers the FDO and the associated WMI data blocks and callbacks with the WDM provider

    The parallel port function driver logs the number of times a parallel port is allocated and freed.

-   Determines the communication modes that are supported by the parallel port hardware

    The hardware must be at least IEEE 1284-compatible. The parallel port function driver checks to determine if the hardware supports BYTE, EPP, and ECP modes. Note that EPP is only supported on a small subset of machines.

-   Creates a work queue (FIFO) for the parallel port

    Each parallel port has its own work queue. The parallel port function driver queues only allocate and select device requests. If the port is already allocated when the parallel port function driver receives a new allocate request or select request, it queues the request.

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bparports\parports%5D:%20Creating%20and%20Starting%20a%20Parallel%20Port%20%20RELEASE:%20%287/25/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


