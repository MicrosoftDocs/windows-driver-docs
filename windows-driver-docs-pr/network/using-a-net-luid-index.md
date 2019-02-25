---
title: Using a NET_LUID Index
description: Using a NET_LUID Index
ms.assetid: 21e0a73b-a02c-4ab4-b7c2-efcb8bfc806d
keywords:
- NDIS network interfaces WDK , NET_LUID
- network interfaces WDK , NET_LUID
- NET_LUID
- index operations WDK network interface
- locally unique identifier WDK network interface
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Using a NET\_LUID Index





NDIS provides functions to allocate and free the [**NET\_LUID**](https://msdn.microsoft.com/library/windows/hardware/ff568747) indexes that are required to create NET\_LUID values. An NDIS interface provider must allocate a NET\_LUID value to register an interface.

To allocate a NET\_LUID index, an interface provider calls the [**NdisIfAllocateNetLuidIndex**](https://msdn.microsoft.com/library/windows/hardware/ff562695) function. After allocating the index, the interface provider calls the [**NDIS\_MAKE\_NET\_LUID**](https://msdn.microsoft.com/library/windows/hardware/ff565890) macro to build the NET\_LUID value. To free a NET\_LUID index, an interface provider calls the [**NdisIfFreeNetLuidIndex**](https://msdn.microsoft.com/library/windows/hardware/ff562706) function.

**NdisIfAllocateNetLuidIndex** attempts to allocate a 24-bit value that is associated with the interface type that the caller specified at the *IfType* parameter and that is unique to the local computer. If the index allocation succeeds, **NdisIfAllocateNetLuidIndex** returns NDIS\_STATUS\_SUCCESS and provides a NET\_LUID index at the address that is provided in the *pNetLuidIndex* parameter. If NDIS is not able to find a free NET\_LUID index, **NdisIfAllocateNetLuidIndex** returns NDIS\_STATUS\_RESOURCES. **NdisIfAllocateNetLuidIndex** can return other NDIS status values to indicate internal errors within NDIS. NDIS records the allocation of this index for when the computer subsequently restarts. NDIS will not use a particular index for future callers, even after the computer restarts, until the interface provider that allocated that index calls the **NdisIfFreeNetLuidIndex** function for that index.

[**NdisIfFreeNetLuidIndex**](https://msdn.microsoft.com/library/windows/hardware/ff562706) frees a previously allocated [**NET\_LUID**](https://msdn.microsoft.com/library/windows/hardware/ff568747) index so that NDIS can possibly reallocate that index to another interface. The caller must pass in the same interface type at *IfType* that the caller used when it called [**NdisIfAllocateNetLuidIndex**](https://msdn.microsoft.com/library/windows/hardware/ff562695) to allocate the NET\_LUID index. If the free operation succeeds, **NdisIfFreeNetLuidIndex** returns NDIS\_STATUS\_SUCCESS. If the call to **NdisIfFreeNetLuidIndex** fails, the interface provider should remove any information that it saved in persistent storage that is related to the NET\_LUID index. Removing the information will ensure that the provider does not keep trying to free an index that is already freed after every computer restart. After calling **NdisIfFreeNetLuidIndex**, the caller must not use the NET\_LUID value again unless it calls **NdisIfAllocateNetLuidIndex** again for the same interface type and receives the same NET\_LUID index that it freed.

To register a network interface, an interface provider must pass a valid NET\_LUID value to the [**NdisIfRegisterInterface**](https://msdn.microsoft.com/library/windows/hardware/ff562715) function. For more information about registering network interfaces, see [Registering a Network Interface](registering-a-network-interface.md).

 

 





