---
title: NET_RXQUEUE_CONFIG structure
description: Describes the configuration options for a NetAdapterCx client driver's receive queue.
ms.assetid: f5058263-4e48-42fc-bf8e-6a76276969f9
keywords: ["NET_RXQUEUE_CONFIG structure Network Drivers Starting with Windows Vista", "PNET_RXQUEUE_CONFIG structure pointer Network Drivers Starting with Windows Vista"]
topic_type:
- apiref
api_name:
- NET_RXQUEUE_CONFIG
api_location:
- netrxqueue.h
api_type:
- HeaderDef
---

# NET\_RXQUEUE\_CONFIG structure


[!include[NetAdapterCx Beta Prerelease](../netcx-beta-prerelease.md)]

Describes the configuration options for a NetAdapterCx client driver's receive queue.

Syntax
------

```ManagedCPlusPlus
typedef struct _NET_RXQUEUE_CONFIG {
  ULONG                                Size;
  PFN_RXQUEUE_CANCEL                   EvtRxQueueCancel;
  PFN_RXQUEUE_SET_NOTIFICATION_ENABLED EvtRxQueueSetNotificationEnabled;
  PFN_RXQUEUE_ADVANCE                  EvtRxQueueAdvance;
  PCNET_CONTEXT_TYPE_INFO              ContextTypeInfo;
  ULONG                                AllocationSize;
  ULONG                                AlignmentRequirement;
} NET_RXQUEUE_CONFIG, *PNET_RXQUEUE_CONFIG;
```

Members
-------

**Size**  
The size, in bytes, of this structure.

**EvtRxQueueCancel**  
A pointer to the client driver's [*EVT\_RXQUEUE\_CANCEL*](evt-rxqueue-cancel.md) event callback function. This callback function is required.

**EvtRxQueueSetNotificationEnabled**  
A pointer to the client driver's [*EVT\_RXQUEUE\_SET\_NOTIFICATION\_ENABLED*](evt-rxqueue-set-notification-enabled.md) event callback function. This callback function is required.

**EvtRxQueueAdvance**  
A pointer to the client driver's [*EVT\_RXQUEUE\_ADVANCE*](evt-rxqueue-advance.md) event callback function. This callback function is required.

**ContextTypeInfo**  
A pointer to a WDF\_OBJECT\_CONTEXT\_TYPE\_INFO structure.

**AllocationSize**  
Size of the DMA common buffer. If the driver provides a non-zero value, it must subsequently call [**NetRxQueueConfigureDmaAllocator**](netrxqueueconfiguredmaallocator.md). If this value is zero, the client must update the NET\_PACKET.Data.DmaLogicalAddress field manually to point to the memory it allocated.

**AlignmentRequirement**  
The alignment requirement for a data buffer. This value must be one less than the alignment boundary. For example, you can specify 15 for a 16-byte alignment boundary and 31 for a 32-byte alignment boundary. You can also use one of the FILE\_Xxxx\_ALIGNMENT constants that are defined in Wdm.h.

Remarks
-------

Call [**NET\_RXQUEUE\_CONFIG\_INIT**](net-rxqueue-config-init.md) to initialize this structure.

The **NET\_RXQUEUE\_CONFIG** structure is an input parameter to [**NetRxQueueCreate**](netrxqueuecreate.md). The client must use [**NET\_RXQUEUE\_CONFIG\_INIT**](net-rxqueue-config-init.md) to initialize this structure.

Requirements
------------

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<tbody>
<tr class="odd">
<td align="left"><p>Minimum KMDF version</p></td>
<td align="left"><p>1.21</p></td>
</tr>
<tr class="even">
<td align="left"><p>Minimum NetAdapterCx version</p></td>
<td align="left"><p>1.0</p></td>
</tr>
<tr class="odd">
<td align="left"><p>Header</p></td>
<td align="left">Netrxqueue.h</td>
</tr>
</tbody>
</table>

## See also


[**NetRxQueueConfigureDmaAllocator**](netrxqueueconfiguredmaallocator.md)

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bnetvista\netvista%5D:%20NET_RXQUEUE_CONFIG%20structure%20%20RELEASE:%20%281/19/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")





