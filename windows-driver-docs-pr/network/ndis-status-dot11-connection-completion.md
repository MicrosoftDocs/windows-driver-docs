---
title: NDIS_STATUS_DOT11_CONNECTION_COMPLETION
author: windows-driver-content
description: A miniport driver must make an NDIS\_STATUS\_DOT11\_CONNECTION\_COMPLETION indication after a connection operation completes.
ms.assetid: 85656517-28b4-4905-8f80-f83a0fde9028
ms.author: windowsdriverdev
ms.date: 08/08/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
keywords: 
 -NDIS_STATUS_DOT11_CONNECTION_COMPLETION Network Drivers Starting with Windows Vista
---

# NDIS\_STATUS\_DOT11\_CONNECTION\_COMPLETION


**Important**  The [Native 802.11 Wireless LAN](https://msdn.microsoft.com/library/windows/hardware/ff560690) interface is deprecated in Windows 10 and later. Please use the WLAN Device Driver Interface (WDI) instead. For more information about WDI, see [WLAN Universal Windows driver model](https://msdn.microsoft.com/library/windows/hardware/dn897672).

 

A miniport driver must make an NDIS\_STATUS\_DOT11\_CONNECTION\_COMPLETION indication after a connection operation completes.

The miniport driver indicates the start of the connection operation through the [NDIS\_STATUS\_DOT11\_CONNECTION\_START](ndis-status-dot11-connection-start.md) indication. Every NDIS\_STATUS\_DOT11\_CONNECTION\_START indication made by the driver must have a corresponding NDIS\_STATUS\_DOT11\_CONNECTION\_COMPLETION indication.

For more information about the connection operation, see [Connection Operations](https://msdn.microsoft.com/library/windows/hardware/ff545185).

The data type for this indication is the DOT11\_CONNECTION\_COMPLETION\_PARAMETERS structure:

```ManagedCPlusPlus
    typedef struct DOT11_CONNECTION_COMPLETION_PARAMETERS {
         NDIS_OBJECT_HEADER Header;
         DOT11_ASSOC_STATUS uStatus;
    } DOT11_CONNECTION_COMPLETION_PARAMETERS,   *PDOT11_CONNECTION_COMPLETION_PARAMETERS;
  
```

The DOT11\_CONNECTION\_COMPLETION\_PARAMETERS structure contains the following members:

<a href="" id="header"></a>**Header**  
The type, revision, and size of the DOT11\_CONNECTION\_COMPLETION\_PARAMETERS structure. This member is formatted as an [**NDIS\_OBJECT\_HEADER**](https://msdn.microsoft.com/library/windows/hardware/ff566588) structure.

The miniport driver must set the members of **Header** to the following values:

<a href="" id="type"></a>**Type**  
This member must be set to NDIS\_OBJECT\_TYPE\_DEFAULT.

<a href="" id="revision"></a>**Revision**  
This member must be set to DOT11\_CONNECTION\_COMPLETION\_PARAMETERS\_REVISION\_1.

<a href="" id="size"></a>**Size**  
This member must be set to sizeof(DOT11\_CONNECTION\_COMPLETION\_PARAMETER).

For more information about these members, see [**NDIS\_OBJECT\_HEADER**](https://msdn.microsoft.com/library/windows/hardware/ff566588).

<a href="" id="ustatus"></a>**uStatus**  
The completion status of the connection operation, as specified by a value defined for [**DOT11\_ASSOC\_STATUS**](https://msdn.microsoft.com/library/windows/hardware/ff547652).

The miniport driver calls [**NdisMIndicateStatusEx**](https://msdn.microsoft.com/library/windows/hardware/ff563600) to make an NDIS\_STATUS\_DOT11\_CONNECTION\_COMPLETION indication, and must pass a pointer to an [**NDIS\_STATUS\_INDICATION**](https://msdn.microsoft.com/library/windows/hardware/ff567373) structure through the *StatusIndication* parameter. When making this indication, the miniport driver must set the following members of the NDIS\_STATUS\_INDICATION structure:

-   **StatusCode** must be set to NDIS\_STATUS\_DOT11\_CONNECTION\_COMPLETION.

-   **StatusBuffer** must be set to the address of a DOT11\_CONNECTION\_COMPLETION\_PARAMETERS structure.

-   **StatusBufferSize** must be set to sizeof(DOT11\_CONNECTION\_COMPLETION\_PARAMETERS).

The [NDIS\_STATUS\_DOT11\_CONNECTION\_START](ndis-status-dot11-connection-start.md) and NDIS\_STATUS\_DOT11\_CONNECTION\_COMPLETION indications define a connection operation that is performed by the 802.11 station. The miniport driver cannot make the NDIS\_STATUS\_DOT11\_CONNECTION\_COMPLETION indication unless it has made an NDIS\_STATUS\_DOT11\_CONNECTION\_START indication at the beginning of the connection operation.

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
<td><p>Available in Windows Vista and later versions of the Windows operating systemss.</p></td>
</tr>
<tr class="even">
<td><p>Header</p></td>
<td>Windot11.h (include Ndis.h)</td>
</tr>
</tbody>
</table>

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bnetvista\netvista%5D:%20NDIS_STATUS_DOT11_CONNECTION_COMPLETION%20%20RELEASE:%20%288/8/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


