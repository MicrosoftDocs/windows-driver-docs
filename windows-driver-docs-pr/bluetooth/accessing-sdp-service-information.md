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
ms.date: 04/20/2017
ms.localizationpriority: medium
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

 

 





