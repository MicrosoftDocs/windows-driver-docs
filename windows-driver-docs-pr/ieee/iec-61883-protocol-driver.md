---
title: IEC-61883 Protocol Driver
description: IEC-61883 Protocol Driver
keywords:
- IEC-61883 client drivers WDK IEEE 1394 bus
- 61883 WDK IEEE 1394 bus
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# IEC-61883 Protocol Driver





The IEC-61883 protocol driver, *61883.sys*, supports function control protocol (FCP), common isochronous packet (CIP) format, and connection management procedures (CMP), as defined in the IEC 61883-1 specification. The protocol driver strips stream packet headers from requests, supports scatter/gather, and limits buffer copies to move large amounts of data efficiently.

To issue IEC-61883 commands to devices connected to the IEEE 1394 bus, IEC-61883 client drivers include *61883.h* and issue the [**IRP\_MJ\_INTERNAL\_DEVICE\_CONTROL**](../kernel/irp-mj-internal-device-control.md) IRP with the I/O control code [**IOCTL\_61883\_CLASS**](/windows-hardware/drivers/ddi/61883/ni-61883-ioctl_61883_class). The client driver packages the parameters in an [**AV\_61883\_REQUEST**](/windows-hardware/drivers/ddi/61883/ns-61883-_av_61883_request) structure and passes a pointer to it in the **Parameters.Others.Argument1** member of the IRP. The **Function** member of the AV\_61883\_REQUEST structure determines the type of operation. The AV\_61883\_REQUEST structure contains request-specific parameters in a union of data structures, one per request type.

 

