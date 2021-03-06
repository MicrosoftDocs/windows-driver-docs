---
title: Indicating RSS Receive Data
description: Indicating RSS Receive Data
keywords:
- receive-side scaling WDK networking , indicating receive data
- RSS WDK networking , indicating receive data
- indicating receive data WDK RSS
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Indicating RSS Receive Data





A miniport driver indicates received data by calling the [**NdisMIndicateReceiveNetBufferLists**](/windows-hardware/drivers/ddi/ndis/nf-ndis-ndismindicatereceivenetbufferlists) function from its [*MiniportInterruptDPC*](/windows-hardware/drivers/ddi/ndis/nc-ndis-miniport_interrupt_dpc) function.

After the NIC computes the RSS hash value successfully, the driver should store the hash type, hashing function, and hash value in the [**NET\_BUFFER\_LIST**](/windows-hardware/drivers/ddi/nbl/ns-nbl-net_buffer_list) structure with the following macros:

[**NET\_BUFFER\_LIST\_SET\_HASH\_TYPE**](/windows-hardware/drivers/ddi/nblhash/nf-nblhash-net_buffer_list_set_hash_type)

[**NET\_BUFFER\_LIST\_SET\_HASH\_FUNCTION**](/windows-hardware/drivers/ddi/nblhash/nf-nblhash-net_buffer_list_set_hash_function)

[**NET\_BUFFER\_LIST\_SET\_HASH\_VALUE**](/windows-hardware/drivers/ddi/nblhash/nf-nblhash-net_buffer_list_set_hash_value)

The hash type identifies the area of the received packet that the hash should be calculated over. For more information about the hash type, see [RSS Hashing Types](rss-hashing-types.md). The hashing function identifies the function that is used to calculate the hash value. For more information about hashing functions, see [RSS Hashing Functions](rss-hashing-functions.md). The protocol driver selects the hash type and function at initialization. For more information, see [RSS Configuration](rss-configuration.md).

If the NIC fails to identify the area of the packet that the hash type specifies, then it should not do any hash computation or scaling. In this case, the miniport driver or NIC should assign the received data to the default CPU.

If the NIC runs out of receive buffers, each buffer must be returned as soon as the original receive DPC returns. The miniport driver can indicate the received data with a status of NDIS\_STATUS\_RESOURCES. In this case, the overlying driver has to go through a slow path of copying the buffer descriptors and relinquishing ownership of the original one immediately.

For more information about receiving network data, see [Receiving Network Data](receiving-network-data.md).

 

