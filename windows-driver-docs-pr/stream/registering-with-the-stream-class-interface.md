---
title: Registering with the Stream Class Interface
description: Registering with the Stream Class Interface
ms.assetid: dfc94f8d-0c0a-44ed-a4f8-791ce49aba2d
keywords:
- video capture WDK AVStream , registering Stream class interface
- capturing video WDK AVStream , registering Stream class interface
- registering Stream class interface WDK AVStream
- initializing stream data WDK AVStream
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Registering with the Stream Class Interface


Stream class minidrivers use the following steps to initialize and prepare to stream data:

1.  The hardware adapter supported by the minidriver is detected by the Plug and Play manager.

2.  The Plug and Play manager loads the minidriver and calls the minidriver's [*DriverEntry*](https://docs.microsoft.com/windows-hardware/drivers/ddi/wdm/nc-wdm-driver_initialize) routine. A file object is created from the information in the **DriverEntry** routine.

3.  The minidriver calls the Stream class interface's [**StreamClassRegisterMinidriver**](https://docs.microsoft.com/windows-hardware/drivers/ddi/strmini/nf-strmini-streamclassregisteradapter) function from its **DriverEntry** routine and passes a properly initialized [**HW\_INITIALIZATION\_DATA**](https://docs.microsoft.com/windows-hardware/drivers/ddi/strmini/ns-strmini-_hw_initialization_data) structure as a parameter. The HW\_INITIALIZATION\_DATA structure includes the addresses of minidriver functions that handle stream request block (SRB) command codes. This allows the minidriver to respond to SRB codes sent by the Stream class interface. A complete list of SRB command codes supported by the stream class is documented in the [Stream Class SRB Reference](https://docs.microsoft.com/windows-hardware/drivers/stream/stream-class-srb-reference).

 

 




