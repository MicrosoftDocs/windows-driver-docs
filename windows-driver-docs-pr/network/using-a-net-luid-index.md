---
title: Using a NET_LUID Index
description: Using a NET_LUID Index
keywords:
- NDIS network interfaces WDK , NET_LUID
- network interfaces WDK , NET_LUID
- NET_LUID
- index operations WDK network interface
- locally unique identifier WDK network interface
ms.date: 04/20/2017
---

# Using a NET\_LUID Index





NDIS provides functions to allocate and free the [**NET\_LUID**](/windows/win32/api/ifdef/ns-ifdef-net_luid_lh) indexes that are required to create NET\_LUID values. An NDIS interface provider must allocate a NET\_LUID value to register an interface.

To allocate a NET\_LUID index, an interface provider calls the [**NdisIfAllocateNetLuidIndex**](/windows-hardware/drivers/ddi/ndis/nf-ndis-ndisifallocatenetluidindex) function. After allocating the index, the interface provider calls the [**NDIS\_MAKE\_NET\_LUID**](/windows-hardware/drivers/ddi/ntddndis/nf-ntddndis-ndis_make_net_luid) macro to build the NET\_LUID value. To free a NET\_LUID index, an interface provider calls the [**NdisIfFreeNetLuidIndex**](/windows-hardware/drivers/ddi/ndis/nf-ndis-ndisiffreenetluidindex) function.

**NdisIfAllocateNetLuidIndex** attempts to allocate a 24-bit value that is associated with the interface type that the caller specified at the *IfType* parameter and that is unique to the local computer. If the index allocation succeeds, **NdisIfAllocateNetLuidIndex** returns NDIS\_STATUS\_SUCCESS and provides a NET\_LUID index at the address that is provided in the *pNetLuidIndex* parameter. If NDIS is not able to find a free NET\_LUID index, **NdisIfAllocateNetLuidIndex** returns NDIS\_STATUS\_RESOURCES. **NdisIfAllocateNetLuidIndex** can return other NDIS status values to indicate internal errors within NDIS. NDIS records the allocation of this index for when the computer subsequently restarts. NDIS will not use a particular index for future callers, even after the computer restarts, until the interface provider that allocated that index calls the **NdisIfFreeNetLuidIndex** function for that index.

[**NdisIfFreeNetLuidIndex**](/windows-hardware/drivers/ddi/ndis/nf-ndis-ndisiffreenetluidindex) frees a previously allocated [**NET\_LUID**](/windows/win32/api/ifdef/ns-ifdef-net_luid_lh) index so that NDIS can possibly reallocate that index to another interface. The caller must pass in the same interface type at *IfType* that the caller used when it called [**NdisIfAllocateNetLuidIndex**](/windows-hardware/drivers/ddi/ndis/nf-ndis-ndisifallocatenetluidindex) to allocate the NET\_LUID index. If the free operation succeeds, **NdisIfFreeNetLuidIndex** returns NDIS\_STATUS\_SUCCESS. If the call to **NdisIfFreeNetLuidIndex** fails, the interface provider should remove any information that it saved in persistent storage that is related to the NET\_LUID index. Removing the information will ensure that the provider does not keep trying to free an index that is already freed after every computer restart. After calling **NdisIfFreeNetLuidIndex**, the caller must not use the NET\_LUID value again unless it calls **NdisIfAllocateNetLuidIndex** again for the same interface type and receives the same NET\_LUID index that it freed.

To register a network interface, an interface provider must pass a valid NET\_LUID value to the [**NdisIfRegisterInterface**](/windows-hardware/drivers/ddi/ndis/nf-ndis-ndisifregisterinterface) function. For more information about registering network interfaces, see [Registering a Network Interface](registering-a-network-interface.md).

 

