---
title: Accessing SDP Service Information
description: Accessing SDP service information
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
ms.date: 01/10/2024
---

# Accessing SDP service information

After a profile driver submits a Service Discovery Protocol (SDP) record to advertise its services with SDP, other devices can discover these services by either searching specifically for the record or by browsing to find it.

To search for SDP records, a client profile driver must first use [**IOCTL_BTH_SDP_CONNECT**](/windows-hardware/drivers/ddi/bthioctl/ni-bthioctl-ioctl_bth_sdp_connect) to connect to the SDP service of the remote device.

A profile driver can then use one of the following IOCTLs to perform the actual SDP record search:

- [**IOCTL_BTH_SDP_ATTRIBUTE_SEARCH**](/windows-hardware/drivers/ddi/bthioctl/ni-bthioctl-ioctl_bth_sdp_attribute_search) obtains all components of a remote SDP record that fall into a specified SDP attribute range.

- [**IOCTL_BTH_SDP_SERVICE_SEARCH**](/windows-hardware/drivers/ddi/bthioctl/ni-bthioctl-ioctl_bth_sdp_service_search) issues an SDP request to the remote device, requesting handles to SDP records of a particular service class or classes.

- [**IOCTL_BTH_SDP_SERVICE_ATTRIBUTE_SEARCH**](/windows-hardware/drivers/ddi/bthioctl/ni-bthioctl-ioctl_bth_sdp_service_attribute_search) combines IOCTL_BTH_SDP_ATTRIBUTE_SEARCH and IOCTL_BTH_SDP_SERVICE_ATTRIBUTE_SEARCH and returns a usable SDP record stream in a single operation.

Profile drivers can use IOCTL_BTH_SDP_SERVICE_SEARCH and IOCTL_BTH_SDP_ATTRIBUTE_SEARCH to reduce the amount of SDP traffic transmitted across a Bluetooth link and can extract necessary information by using a small number of maximum transfer units (MTUs). If neither of these issues is of great concern, it can be more convenient for profile drivers to call IOCTL_BTH_SDP_SERVICE_ATTRIBUTE_SEARCH.

After the profile driver has obtained the *dynamic* protocol/service multiplexer (PSM) for the desired service, it can connect to the remote service by using the **BRB_L2CA_OPEN_CHANNEL** BRB.

> [!NOTE]
> If the service has a fixed PSM, which many do, L2CAP client profile drivers do not need to use SDP to obtain the PSM. However, L2CAP client profile drivers can still use SDP to get the SDP server attributes.

When the profile driver finishes searching, it should use [**IOCTL_BTH_SDP_DISCONNECT**](/windows-hardware/drivers/ddi/bthioctl/ni-bthioctl-ioctl_bth_sdp_disconnect) to disconnect from the remote SDP server.
