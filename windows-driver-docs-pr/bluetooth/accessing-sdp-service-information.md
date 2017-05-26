---
title: Accessing SDP Service Information
description: Accessing SDP Service Information
ms.assetid: 0b327fbd-1101-4566-ac2f-3d039eed6835
keywords:
- Bluetooth WDK , SDP server communication
- SDP WDK Bluetooth
- Service Discovery Protocol WDK Bluetooth
- browsing services WDK Bluetooth
- searching services WDK Bluetooth
- services browsing WDK Bluetooth
- IOCTL_BTH_SDP_CONNECT
- searching SDP records WDK Bluetooth
- IOCTL_BTH_SDP_SERVICE_SEARCH
ms.author: windowsdriverdev
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Accessing SDP Service Information


After a profile driver submits a Service Discovery Protocol (SDP) record to advertise its services with SDP, other devices can discover these services by either searching specifically for the record or by browsing to find it.

To search for SDP records, a client profile driver must first use [**IOCTL\_BTH\_SDP\_CONNECT**](https://msdn.microsoft.com/library/windows/hardware/ff536688) to connect to the SDP service of the remote device.

A profile driver can then use one of the following IOCTLs to perform the actual SDP record search:

-   [**IOCTL\_BTH\_SDP\_ATTRIBUTE\_SEARCH**](https://msdn.microsoft.com/library/windows/hardware/ff536687) obtains all components of a remote SDP record that fall into a specified SDP attribute range.

-   [**IOCTL\_BTH\_SDP\_SERVICE\_SEARCH**](https://msdn.microsoft.com/library/windows/hardware/ff536692) issues an SDP request to the remote device, requesting handles to SDP records of a particular service class or classes.

-   [**IOCTL\_BTH\_SDP\_SERVICE\_ATTRIBUTE\_SEARCH**](https://msdn.microsoft.com/library/windows/hardware/ff536691) combines IOCTL\_BTH\_SDP\_ATTRIBUTE\_SEARCH and IOCTL\_BTH\_SDP\_SERVICE\_ATTRIBUTE\_SEARCH and returns a usable SDP record stream in a single operation.

Profile drivers can use IOCTL\_BTH\_SDP\_SERVICE\_SEARCH and IOCTL\_BTH\_SDP\_ATTRIBUTE\_SEARCH to reduce the amount of SDP traffic transmitted across a Bluetooth link and can extract necessary information by using a small number of maximum transfer units (MTUs). If neither of these issues is of great concern, it can be more convenient for profile drivers to call IOCTL\_BTH\_SDP\_SERVICE\_ATTRIBUTE\_SEARCH.

After the profile driver has obtained the *dynamic* protocol/service multiplexer (PSM) for the desired service, it can connect to the remote service by using the **BRB\_L2CA\_OPEN\_CHANNEL** BRB.

**Note**  If the service has a fixed PSM, which many do, L2CAP client profile drivers do not need to use SDP to obtain the PSM. However, L2CAP client profile drivers can still use SDP to get the SDP server attributes.

 

When the profile driver finishes searching, it should use [**IOCTL\_BTH\_SDP\_DISCONNECT**](https://msdn.microsoft.com/library/windows/hardware/ff536689) to disconnect from the remote SDP server.

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[bltooth\bltooth]:%20Accessing%20SDP%20Service%20Information%20%20RELEASE:%20%283/20/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




