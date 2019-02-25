---
title: Using Avcstrm.sys
description: Using Avcstrm.sys
ms.assetid: 53430526-ee24-4081-b220-4089d60aec94
keywords:
- filter drivers WDK AV/C streaming
- AV/C WDK , Stream filter driver
- Stream filter driver WDK AV/C
- Avcstrm.sys streaming filter driver WDK , about Avcstrm.sys streaming filter driver
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Using Avcstrm.sys





The AV/C Streaming filter driver, *Avcstrm.sys*, provides services after its client subunit driver creates a data stream. A data stream can be categorized to perform three functions: data streaming, clock provider, and getting and setting of stream properties or events. These three functions are inter-related, and the stream state (stop, pause, or run) controls the data stream's behavior.

A subunit driver first requests that *Avcstrm.sys* create a stream with a given data format. This data format contains definitions of the signal format used in IEC 61883-*x* protocol specifications. The data format can be either SDDV or MPEG2TS. The 61883 protocol defines how data is transmitted on the 1394 bus. The AV/C Streaming filter driver validates and caches the data format, queries the available isochronous resources from the target device, such as plug information, and allocates the necessary resources for queuing data streaming requests.

**Note**  : Prior to Windows XP Service Pack 2 (SP2), *Avcstrm.sys* could only use the target device's first (index 0) isochronous plug handle to establish a connection. This limitation restricted AV/C devices (and consequently their drivers) with more than one subunit from supporting more than one stream simultaneously. In Windows XP SP2 and later, however, *Avcstrm.sys* has been changed to automatically select an AV/C device's isochronous plug handle, starting from the lowest index and up, to enable devices to support more than one stream simultaneously.
Since connections are made from the lowest index and up, the internal connection of a subunit plug to the AV/C unit's isochronous plug must follow the same order. AV/C devices with only one subunit, or devices that have only one isochronous plug, are not affected.

 

Upon successful creation of a stream, a stream context is returned. This context is a pointer to an opaque structure that contains information about the current stream, such as data format and stream state.

After a stream is created, a subunit driver can start to send down the stream data request. This request will be queued and a separate IRP will be allocated and submitted to *61883.sys* for receiving data or data transmission. Upon completion of the data request, the completion routine will be called. This request is asynchronous because data transfer is controlled by the stream state and availability of the data.

The stream can be in either paused or run states when stream data requests arrive. The isochronous connection is made in the paused stream-state. *Avcstrm.sys* then requests *61883.sys* to allocate bandwidth and isochronous channel, if needed, and then transition into the run stream-state.

A data stream will be stopped when transitioning into the stop state. The AV/C Streaming filter driver will reclaim ownership of the data buffer by requesting 61883 to detach the data buffers. These data buffers will be completed with STATUS\_CANCELLED.

A stream might need to be aborted during events, such as surprise device removal or data IRP cancellation, if the thread that dispatched the IOCTL was terminated. When transitioning to a stop state, the AV/C Streaming filter driver will stop isochronous data transfer but will not change the stream state.

As a filter driver, *Avcstrm.sys* filters and processes only the I/O request packet (IRP) with **MajorFunction** of IRP\_MJ\_INTERNAL\_DEVICE\_CONTROL and the I/O control (IOCTL) code of IOCTL\_AVCSTRM\_CLASS, and passes through other IRPs to the lower stack. Depending on the request, the AV/C Streaming filter driver processes an IRP from its client and then creates one or more locally allocated IRPs to request service from its lower stack, either the 61883 or AV/C protocol drivers. Even though the IRP from a subunit driver can send a request to the lower stack, it is safer to create a different IRP in case a class driver claims ownership of an IRP.

The AV/C Streaming filter driver is designed to work with kernel streaming interface on the 61883 and AV/C stack. A subunit driver can use either the AVStream or Stream class interfaces.

In the following sections, each AV/C Streaming command function is discussed (some with code samples). The code sample is from a Stream class-based subunit driver.

 

 




