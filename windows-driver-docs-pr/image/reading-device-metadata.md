---
title: Reading Device Metadata
author: windows-driver-content
description: Reading Device Metadata
ms.assetid: 402de9de-8bfe-4cc2-9b8e-06e0ad925eb1
---

# Reading Device Metadata


WIA minidrivers for web services scanners must read the following device metadata properties at run time:

<a href="" id="pkey-pnpx-serviceid"></a>**PKEY\_PNPX\_ServiceId**  
This property is needed to initialize the [**WIA\_DPS\_SERVICE\_ID**](https://msdn.microsoft.com/library/windows/hardware/ff551428) WIA property.

<a href="" id="pkey-pnpx-globalidentity"></a>**PKEY\_PNPX\_GlobalIdentity**  
This property initializes the [**WIA\_DPS\_GLOBAL\_IDENTITY**](https://msdn.microsoft.com/library/windows/hardware/ff551395) WIA property.

<a href="" id="pkey-pnpx-id--directly-or-indirectly-by-using-istidevicecontrol--getmydeviceportname-"></a>**PKEY\_PNPX\_ID** (directly or indirectly by using [**IStiDeviceControl::GetMyDevicePortName**](https://msdn.microsoft.com/library/windows/hardware/ff542944))  
This property initializes the [**WIA\_DPS\_DEVICE\_ID**](https://msdn.microsoft.com/library/windows/hardware/ff551374) device property.

The minidrivers might also read other properties, including the following:

<a href="" id="pkey-pnpx-firmware-version"></a>**PKEY\_PNPX\_FIRMWARE\_VERSION**  
This property initializes the [**WIA\_DPA\_FIRMWARE\_VERSION**](https://msdn.microsoft.com/library/windows/hardware/ff550309) WIA property.

**Note**   Minidrivers that use *WSDScan.sys* can also retrieve the PNPX ID value by calling [**IStiDeviceControl::GetMyDevicePortName**](https://msdn.microsoft.com/library/windows/hardware/ff542944); the returned device path is the current PKEY\_PNPX\_ID.

 

For a description of these PKEY\_PNPX\_*Xxx* properties, see the [PNP-X Implementer's Guide](http://go.microsoft.com/fwlink/p/?linkid=242570).

The following code examples show how to open a Property Store for the current Function Instance object that is obtained as described in the previous section and how to read device properties from the store:

[Code Example for Opening a Property Store](code-example-for-opening-a-property-store.md)

[Code Example for Reading Device Properties](code-example-for-reading-device-properties.md)

[Code Example for Initializing Device Properties](code-example-for-initializing-device-properties.md)

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bimage\image%5D:%20Reading%20Device%20Metadata%20%20RELEASE:%20%288/17/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


