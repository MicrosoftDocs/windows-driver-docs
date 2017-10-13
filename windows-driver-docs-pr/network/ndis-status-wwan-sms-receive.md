---
title: NDIS_STATUS_WWAN_SMS_RECEIVE
author: windows-driver-content
description: Miniport drivers use the NDIS\_STATUS\_WWAN\_SMS\_RECEIVE notification to inform the MB Service about either the completion of a previous read request through a OID\_WWAN\_SMS\_READ \ 160;query request, or the arrival of a new class-0 (flash/alert) message from the network provider as an event notification. Miniport drivers can also send unsolicited events with this notification.This notification uses the NDIS\_WWAN\_SMS\_RECEIVE structure.
ms.assetid: fc1c3587-8bba-4ffd-9561-4140c307c705
ms.author: windowsdriverdev
ms.date: 08/08/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
keywords: 
 -NDIS_STATUS_WWAN_SMS_RECEIVE Network Drivers Starting with Windows Vista
---

# NDIS\_STATUS\_WWAN\_SMS\_RECEIVE


Miniport drivers use the NDIS\_STATUS\_WWAN\_SMS\_RECEIVE notification to inform the MB Service about either the completion of a previous read request through a [OID\_WWAN\_SMS\_READ](oid-wwan-sms-read.md) query request, or the arrival of a new class-0 (flash/alert) message from the network provider as an event notification.

Miniport drivers can also send unsolicited events with this notification.

This notification uses the [**NDIS\_WWAN\_SMS\_RECEIVE**](https://msdn.microsoft.com/library/windows/hardware/ff567942) structure.

Remarks
-------

RequestId is set to "0" by the miniport driver to indicate the arrival of the new class-0 (flash/alert) message. Arrival of new class-0 (flash/alert) messages is dependent on the current network registration state.

If the request for read results in retrieval of large number of SMS records that can't be accommodated in a pre-allocated buffer of miniport driver, then the SMS records can be sent to the MB Service in multiple indications. The uStatus in this case must be set to WWAN\_STATUS\_SMS\_MORE\_DATA for the intermediate transactions and the final transaction must end with WWAN\_STATUS\_SUCCESS.

The following diagram represents the usage of the multiple indication method for large number of SMS record retrieval:

![diagram illustrating the usage of the multiple indication method for a large number of sms record retrieval](images/wwansmsrecordretrieval.png)

Requirements
------------

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<tbody>
<tr class="odd">
<td><p>Version</p></td>
<td><p>Available in Windows 7 and later versions of Windows.</p></td>
</tr>
<tr class="even">
<td><p>Header</p></td>
<td>Ntddndis.h (include Ndis.h)</td>
</tr>
</tbody>
</table>

## See also


[OID\_WWAN\_SMS\_READ](oid-wwan-sms-read.md)

[**NDIS\_WWAN\_SMS\_RECEIVE**](https://msdn.microsoft.com/library/windows/hardware/ff567942)

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bnetvista\netvista%5D:%20NDIS_STATUS_WWAN_SMS_RECEIVE%20%20RELEASE:%20%288/8/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


