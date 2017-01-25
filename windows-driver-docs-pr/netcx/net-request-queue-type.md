---
title: NET_REQUEST_QUEUE_TYPE enumeration
description: .
ms.assetid: 34aa0f46-b86f-4ee3-82ff-7fd8e2f86f54
keywords: ["NET_REQUEST_QUEUE_TYPE enumeration Network Drivers Starting with Windows Vista"]
topic_type:
- apiref
api_name:
- NET_REQUEST_QUEUE_TYPE
api_location:
- netrequestqueue.h
api_type:
- HeaderDef
---

# NET\_REQUEST\_QUEUE\_TYPE enumeration


\[Some information relates to pre-released product which may be substantially modified before it's commercially released. Microsoft makes no warranties, express or implied, with respect to the information provided here.\]

Syntax
------

```ManagedCPlusPlus
typedef enum _NET_REQUEST_QUEUE_TYPE { 
  NetRequestQueueTypeInvalid        = ,
  NetRequestQueueDefaultSequential  = ,
  NetRequestQueueDefaultParallel    = 
} NET_REQUEST_QUEUE_TYPE;
```

Constants
---------

<a href="" id="netrequestqueuetypeinvalid"></a>**NetRequestQueueTypeInvalid**  

<a href="" id="netrequestqueuedefaultsequential"></a>**NetRequestQueueDefaultSequential**  

<a href="" id="netrequestqueuedefaultparallel"></a>**NetRequestQueueDefaultParallel**  

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
<td align="left">Netrequestqueue.h</td>
</tr>
</tbody>
</table>

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bnetvista\netvista%5D:%20NET_REQUEST_QUEUE_TYPE%20enumeration%20%20RELEASE:%20%281/19/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




