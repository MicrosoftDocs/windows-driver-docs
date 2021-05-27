---
title: Communicating with SDP Servers Overview
description: Communicating with SDP Servers Overview
keywords:
- Bluetooth WDK , SDP server communication
- SDP WDK Bluetooth
- Service Discovery Protocol WDK Bluetooth
- profile drivers WDK Bluetooth
- browsing services WDK Bluetooth
- searching services WDK Bluetooth
- services browsing WDK Bluetooth
- advertising services WDK Bluetooth
- services advertising WDK Bluetooth
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Communicating with SDP Servers Overview


The Bluetooth driver stack supports the Service Discovery Protocol (SDP). This protocol allows profile drivers to search or browse for services that are offered by Bluetooth devices that are in range of the local radio. SDP uses the Logical Link Control and Adaptation Protocol (L2CAP) as its transport protocol and follows a client-server model.

A service is any entity that can provide information, perform an action, or control a resource on behalf of another entity. A service might be implemented as software, hardware, or a combination of hardware and software. The service record consists entirely of a list of service attributes.

After a L2CAP server profile driver registers itself to accept incoming L2CAP connection requests, it can advertise its services with the SDP protocol by using [**IOCTL\_BTH\_SDP\_SUBMIT\_RECORD**](/windows-hardware/drivers/ddi/bthioctl/ni-bthioctl-ioctl_bth_sdp_submit_record) or [**IOCTL\_BTH\_SDP\_SUBMIT\_RECORD\_WITH\_INFO**](/windows-hardware/drivers/ddi/bthioctl/ni-bthioctl-ioctl_bth_sdp_submit_record_with_info). Each SDP record is submitted as a stream. If the profile driver uses IOCTL\_BTH\_SDP\_SUBMIT\_RECORD\_WITH\_INFO, the profile driver prepends a [**BTH\_SDP\_RECORD**](/windows-hardware/drivers/ddi/bthioctl/ns-bthioctl-_bth_sdp_record) structure to the raw stream, which contains extra attributes that are not part of the SDP record itself. These include security requirements for a requesting client, publication options for the SDP record, class-of-device (CoD) information, the length of the record, and the record itself.

After the profile driver has advertised its services, other Bluetooth devices can search or browse for these services. For more information about SDP services, see [Accessing SDP Service Information](accessing-sdp-service-information.md).

To stop advertising services with SDP, a profile driver uses [**IOCTL\_BTH\_SDP\_REMOVE\_RECORD**](/windows-hardware/drivers/ddi/bthioctl/ni-bthioctl-ioctl_bth_sdp_remove_record).

 

