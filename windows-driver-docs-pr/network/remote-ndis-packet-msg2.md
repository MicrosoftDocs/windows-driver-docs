---
title: REMOTE_NDIS_PACKET_MSG
description: REMOTE_NDIS_PACKET_MSG
ms.assetid: 334b0f74-7cc2-466b-9e12-5fac60911606
ms.author: windowsdriverdev
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# REMOTE\_NDIS\_PACKET\_MSG


## <a href="" id="ddk-remote-ndis-packet-msg-ng"></a>


A Remote NDIS device must send and receive data through NDIS data packets. The bus used by the device determines how these packets are passed from host to device and device to host. It could be shared memory, or, in the case of USB for example, Isoch and Bulk pipes. NDIS packets may also contain out-of-band (OOB) data as well as the data that goes across the network.

A Remote NDIS device transfers NDIS packets, encapsulated as [**REMOTE\_NDIS\_PACKET\_MSG**](https://msdn.microsoft.com/library/windows/hardware/ff570635) across the data channel. Both connectionless (for example, 802.3) and connection-oriented (for example, ATM) devices use the same packet message structure, in order to facilitate common code for packet processing. Each **REMOTE\_NDIS\_PACKET\_MSG** message contains information about a single network data unit (for example, an Ethernet 802.3 frame).

Any out-of-band data records must appear in sequence. If there are multiple out-of-band data blocks attached to a [**REMOTE\_NDIS\_PACKET\_MSG**](https://msdn.microsoft.com/library/windows/hardware/ff570635), then each subsequent out-of-band data record must immediately follow the previous out-of-band record's data. There is no out-of-band information currently defined for Ethernet 802.3 devices.

For more information about out-of-band packet data, see the [Windows 2000 and Windows XP Networking Design Guide](https://msdn.microsoft.com/library/windows/hardware/ff565849) section.

Each [**REMOTE\_NDIS\_PACKET\_MSG**](https://msdn.microsoft.com/library/windows/hardware/ff570635) may contain one or more per-packet-info data records. Per-packet-info is used to convey packet metadata such as TCP checksum. If there are multiple per-packet-info data blocks, then each subsequent per-packet-info data record must immediately follow the previous per-packet-info record's data.

For more information about per-packet-info data, see the [Windows 2000 and Windows XP Networking Design Guide](https://msdn.microsoft.com/library/windows/hardware/ff565849) section.

 

 





