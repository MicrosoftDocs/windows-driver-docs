---
title: Registering as a WMI Data Provider
author: windows-driver-content
description: Registering as a WMI Data Provider
MS-HAID:
- 'WMI\_c8542b58-a729-4d9f-a405-eaa017b1db42.xml'
- 'kernel.registering\_as\_a\_wmi\_data\_provider'
MSHAttr:
- 'PreferredSiteName:MSDN'
- 'PreferredLib:/library/windows/hardware'
ms.assetid: a08fed24-20b6-46aa-9a52-7a22f0e89ce4
keywords: ["WMI WDK kernel , registering with WMI", "registering WMI data providers", "data providers WDK WMI", "driver registrations WDK WMI", "event blocks WDK WMI", "blocks WDK WMI"]
---

# Registering as a WMI Data Provider


## <a href="" id="ddk-registering-as-a-wmi-data-provider-kg"></a>


A driver that supports WMI must register as a WMI data provider to make its data and event blocks available to WMI clients. A driver typically registers with WMI when starting its device, after the device has been initialized to the point that the driver can handle WMI IRPs. During the registration process, the driver passes WMI a pointer to its device object and information about the data and event blocks it supports.

A driver registers with WMI in two phases:

1.  The driver calls [**IoWMIRegistrationControl**](https://msdn.microsoft.com/library/windows/hardware/ff550480) with the action WMIREG\_ACTION\_REGISTER and a pointer to the device object passed to the driver's [*AddDevice*](https://msdn.microsoft.com/library/windows/hardware/ff540521) routine.

2.  The driver handles the [**IRP\_MN\_REGINFO**](https://msdn.microsoft.com/library/windows/hardware/ff551731) or [**IRP\_MN\_REGINFO\_EX**](https://msdn.microsoft.com/library/windows/hardware/ff551734) request that WMI sends in response to the driver's **IoWMIRegistrationControl** call. The **Parameters.WMI.DataPath** member of the IRP is set to WMIREGISTER and **Parameters.WMI.ProviderId** is set to the driver's device object pointer. The driver supplies WMI with registration information about its data and event blocks, either by using the WMI Library as described in [Using the WMI Library to Register Blocks](using-the-wmi-library-to-register-blocks.md), or by handling the **IRP\_MN\_REGINFO** or **IRP\_MN\_REGINFO\_EX** requests as described in [Handling IRP\_MN\_REGINFO and IRP\_MN\_REGINFO\_EX to Register Blocks](handling-irp-mn-reginfo-and-irp-mn-reginfo-ex-to-register-blocks.md).

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bkernel\kernel%5D:%20Registering%20as%20a%20WMI%20Data%20Provider%20%20RELEASE:%20%286/14/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


