---
title: Creating and Starting a Parallel Port
description: Creating and Starting a Parallel Port
ms.assetid: 75c82353-6490-47e9-9278-ec0981af9ae9
keywords:
- parallel ports WDK , creating
- parallel ports WDK , starting
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Creating and Starting a Parallel Port





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

 

 




