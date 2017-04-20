---
title: Registering with the Stream Class Interface
author: windows-driver-content
description: Registering with the Stream Class Interface
ms.assetid: dfc94f8d-0c0a-44ed-a4f8-791ce49aba2d
keywords:
- video capture WDK AVStream , registering Stream class interface
- capturing video WDK AVStream , registering Stream class interface
- registering Stream class interface WDK AVStream
- initializing stream data WDK AVStream
ms.author: windows-driver-content
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Registering with the Stream Class Interface


Stream class minidrivers use the following steps to initialize and prepare to stream data:

1.  The hardware adapter supported by the minidriver is detected by the Plug and Play manager.

2.  The Plug and Play manager loads the minidriver and calls the minidriver's [*DriverEntry*](https://msdn.microsoft.com/library/windows/hardware/ff544113) routine. A file object is created from the information in the **DriverEntry** routine.

3.  The minidriver calls the Stream class interface's [**StreamClassRegisterMinidriver**](https://msdn.microsoft.com/library/windows/hardware/ff568263) function from its **DriverEntry** routine and passes a properly initialized [**HW\_INITIALIZATION\_DATA**](https://msdn.microsoft.com/library/windows/hardware/ff559682) structure as a parameter. The HW\_INITIALIZATION\_DATA structure includes the addresses of minidriver functions that handle stream request block (SRB) command codes. This allows the minidriver to respond to SRB codes sent by the Stream class interface. A complete list of SRB command codes supported by the stream class is documented in the [Stream Class SRB Reference](https://msdn.microsoft.com/library/windows/hardware/ff568295).

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstream\stream%5D:%20Registering%20with%20the%20Stream%20Class%20Interface%20%20RELEASE:%20%288/23/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


