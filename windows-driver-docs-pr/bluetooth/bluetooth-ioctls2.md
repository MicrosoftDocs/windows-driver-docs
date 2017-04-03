---
title: Bluetooth IOCTLs
description: Bluetooth IOCTLs
ms.assetid: 384ea4bb-863c-4da7-bf81-85d2de734ef7
keywords: ["Bluetooth WDK , IOCTLs", "IOCTLs WDK Bluetooth", "local Bluetooth WDK", "remote Bluetooth WDK"]
---

# Bluetooth IOCTLs


The Bluetooth driver stack provides profile drivers with several IOCTLs to gather information about:

-   The local Bluetooth radio and system.

-   Remote Bluetooth devices.

-   The device that caused the Plug and Play (PnP) Manager to load a profile driver.

To gather information about the local Bluetooth radio and system, a profile driver uses [**IOCTL\_BTH\_GET\_LOCAL\_INFO**](https://msdn.microsoft.com/library/windows/hardware/ff536684). After the IOCTL returns, its **AssociatedIrp.SystemBuffer** member contains a pointer to a [**BTH\_LOCAL\_RADIO\_INFO**](https://msdn.microsoft.com/library/windows/hardware/ff536644) structure that contains information about the local Bluetooth radio and system, including flags that indicate whether the local radio can be discovered and connected to. The returned BTH\_LOCAL\_RADIO\_INFO structure contains a [BTH\_DEVICE\_INFO](http://go.microsoft.com/fwlink/p/?linkid=50713) structure, which contains system-specific information, and a [**BTH\_RADIO\_INFO**](https://msdn.microsoft.com/library/windows/hardware/ff536646) structure, which contains local radio-specific information.

To gather information about a specific remote Bluetooth device, a profile driver uses [**IOCTL\_BTH\_GET\_RADIO\_INFO**](https://msdn.microsoft.com/library/windows/hardware/ff536685). After the IOCTL returns, its **AssociatedIrp.SystemBuffer** member contains a pointer to a BTH\_RADIO\_INFO structure that provides information about the specific remote radio, including whether the remote radio can be discovered and connected to.

To gather information about all remote radios that have been discovered, a profile driver uses [**IOCTL\_BTH\_GET\_DEVICE\_INFO**](https://msdn.microsoft.com/library/windows/hardware/ff536683). After the IOCTL returns, its **AssociatedIrp.SystemBuffer** member contains a pointer to a [**BTH\_DEVICE\_INFO\_LIST**](https://msdn.microsoft.com/library/windows/hardware/ff536642) structure that contains an array of BTH\_DEVICE\_INFO structures. The BTH\_DEVICE\_INFO\_LIST structure contains one array entry for each discovered remote radio. The user-mode [BluetoothGetDeviceInfo](http://go.microsoft.com/fwlink/p/?linkid=74493) API uses this functionality to return information about all remote radios.

To gather information about the remote device that caused the PnP Manager to load it, a profile driver uses [**IOCTL\_INTERNAL\_BTHENUM\_GET\_DEVINFO**](https://msdn.microsoft.com/library/windows/hardware/ff536748). After the IOCTL returns, its **AssociatedIrp.SystemBuffer** member contains a pointer to a BTH\_DEVICE\_INFO structure that contains information about the remote device, including its Bluetooth device address, device state, and its class-of-device (CoD) settings.

A profile driver uses [**IOCTL\_INTERNAL\_BTHENUM\_GET\_ENUMINFO**](https://msdn.microsoft.com/library/windows/hardware/ff536750) to obtain information about the underlying device and service that caused the PnP manager to load the profile driver. After the IOCTL returns, its **AssociatedIrp.SystemBuffer** member contains a pointer to a [**BTH\_ENUMERATOR\_INFO**](https://msdn.microsoft.com/library/windows/hardware/ff536643) structure that contains vendor-provided information about the device, including the port number, device flags, vendor ID, and product ID.

For more information about using Bluetooth IOCTLs and BRBs, see [Building and Sending a BRB](building-and-sending-a-brb.md).

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[bltooth\bltooth]:%20Bluetooth%20IOCTLs%20%20RELEASE:%20%283/20/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




