---
title: OID_DOT11_WFD_SEND_GO_NEGOTIATION_REQUEST
author: windows-driver-content
description: When set, the OID_DOT11_WFD_SEND_GO_NEGOTIATION_REQUEST object identifier (OID) requests that the Wi-Fi Direct (WFD) miniport driver send a Group Owner (GO) negotiation request to a WFD peer currently in device mode.
ms.assetid: B23D8381-1331-4DCD-B63A-7514A38970C6
ms.author: windowsdriverdev
ms.date: 08/08/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
keywords: 
 -OID_DOT11_WFD_SEND_GO_NEGOTIATION_REQUEST Network Drivers Starting with Windows Vista
---

# OID\_DOT11\_WFD\_SEND\_GO\_NEGOTIATION\_REQUEST


**Important**  The [Native 802.11 Wireless LAN](https://msdn.microsoft.com/library/windows/hardware/ff560690) interface is deprecated in Windows 10 and later. Please use the WLAN Device Driver Interface (WDI) instead. For more information about WDI, see [WLAN Universal Windows driver model](https://msdn.microsoft.com/library/windows/hardware/dn897672).

 

When set, the OID\_DOT11\_WFD\_SEND\_GO\_NEGOTIATION\_REQUEST object identifier (OID) requests that the Wi-Fi Direct (WFD) miniport driver send a Group Owner (GO) negotiation request to a WFD peer currently in device mode.

The data type for OID\_DOT11\_WFD\_SEND\_GO\_NEGOTIATION\_REQUEST is the **DOT11\_SEND\_GO\_NEGOTIATION\_REQUEST\_PARAMETERS** structure.

```ManagedCPlusPlus
    typedef struct _DOT11_SEND_GO_NEGOTIATION_REQUEST_PARAMETERS {
        NDIS_OBJECT_HEADER Header;
        DOT11_MAC_ADDRESS PeerDeviceAddress;
        DOT11_DIALOG_TOKEN DialogToken;
        ULONG uSendTimeout;
        DOT11_WFD_GO_INTENT GroupOwnerIntent;
        DOT11_WFD_CONFIGURATION_TIMEOUT MinimumConfigTimeout;
        DOT11_MAC_ADDRESS IntendedInterfaceAddress;
        DOT11_WFD_GROUP_CAPABILITY GroupCapability;
        ULONG uIEsOffset;
        ULONG uIEsLength;
    } DOT11_SEND_GO_NEGOTIATION_REQUEST_PARAMETERS, * PDOT11_SEND_GO_NEGOTIATION_REQUEST_PARAMETERS;
  
```

This structure includes the following members:

<a href="" id="header"></a>**Header**  
The type, revision, and size of the **DOT11\_SEND\_GO\_NEGOTIATION\_REQUEST\_PARAMETERS** structure. This member is formatted as an [**NDIS\_OBJECT\_HEADER**](https://msdn.microsoft.com/library/windows/hardware/ff566588) structure.

The miniport driver must set the members of **Header** to the following values:

<a href="" id="type"></a>**Type**  
This member must be set to NDIS\_OBJECT\_TYPE\_DEFAULT.

<a href="" id="revision"></a>**Revision**  
This member must be set to DOT11\_SEND\_GO\_NEGOTIATION\_REQUEST\_PARAMETERS\_REVISION\_1.

<a href="" id="size"></a>**Size**  
This member must be set to DOT11\_SIZEOF\_SEND\_GO\_NEGOTIATION\_REQUEST\_PARAMETERS\_REVISION\_1.

For more information about these members, see [**NDIS\_OBJECT\_HEADER**](https://msdn.microsoft.com/library/windows/hardware/ff566588).

<a href="" id="--------peerdeviceaddress"></a> **PeerDeviceAddress**  
The Peer-to-Peer (P2P) address of the Wi-Fi Direct (WFD) device where the GO negotiation request will be sent.

<a href="" id="--------dialogtoken"></a> **DialogToken**  
The dialog token to insert in the GO negotiation request packet.

<a href="" id="--------usendtimeout"></a> **uSendTimeout**  
The maximum time, in milliseconds, allowed to send the GO negotiation request. If the time-out expires before the miniport has successfully transmitted the GO negotiation request, it should indicate the [**NDIS\_STATUS\_DOT11\_WFD\_GO\_NEGOTIATION\_REQUEST\_SEND\_COMPLETE**](https://msdn.microsoft.com/library/windows/hardware/hh439774) with a failure status.

<a href="" id="--------groupownerintent"></a> **GroupOwnerIntent**  
The GO intent value. This value is included in the Group Owner Intent attribute of the GO negotiation request packet.

<a href="" id="--------minimumconfigtimeout"></a> **MinimumConfigTimeout**  
The configuration time-out, in milliseconds, required by the system to change its mode of operation to Peer-to-Peer (P2P) GO or P2P Client. The miniport driver can overwrite this value with a longer time-out.

<a href="" id="--------intendedinterfaceaddress"></a> **IntendedInterfaceAddress**  
The Intended Interface address to be used for generation of the GO negotiation request.

<a href="" id="--------groupcapability"></a> **GroupCapability**  
The values to set in the Group Capability bitmask of the P2P Capability Information Element (IE) in the GO negotiation request.

<a href="" id="--------uiesoffset"></a> **uIEsOffset**  
The offset, in bytes, of the array of additional IEs the Wi-Fi Direct (WFD) port must add to the GO negotiation request packet. This offset is from the start of the buffer that contains this structure.

<a href="" id="--------uieslength"></a> **uIEsLength**  
The length, in bytes, of the array of IEs provided at **uIEsOffset**.

When receiving this OID, the miniport must create and populate all the required P2P attributes in the P2P IE prior to sending the GO negotiation request packet.

This OID is sent to the miniport with **NdisRequestSetInformation** as the OID request type. After creating the packet for transmission, the miniport must complete the OID with **NDIS\_STATUS\_INDICATION\_REQUIRED**. The completion of the attempt to send the GO negotiation request must be indicated back to the system with an [**NDIS\_STATUS\_DOT11\_WFD\_GO\_NEGOTIATION\_REQUEST\_SEND\_COMPLETE**](https://msdn.microsoft.com/library/windows/hardware/hh439774) indication. The miniport driver must send the **NDIS\_STATUS\_DOT11\_WFD\_GO\_NEGOTIATION\_REQUEST\_SEND\_COMPLETE** after stopping the attempt to send the GO negotiation request. This must occur in either case of success or failure.

Miniport drivers should periodically attempt sending the GO Negotiation Request frame at intervals no longer than 50ms because a remote device may not be constantly available on its listen channel.

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
<td><p>Supported starting with Windows 8.</p></td>
</tr>
<tr class="even">
<td><p>Header</p></td>
<td>Windot11.h (include Windot11.h)</td>
</tr>
</tbody>
</table>

## See also


[**NDIS\_OBJECT\_HEADER**](https://msdn.microsoft.com/library/windows/hardware/ff566588)

[**NDIS\_STATUS\_DOT11\_WFD\_GO\_NEGOTIATION\_REQUEST\_SEND\_COMPLETE**](https://msdn.microsoft.com/library/windows/hardware/hh439774)

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bnetvista\netvista%5D:%20OID_DOT11_WFD_SEND_GO_NEGOTIATION_REQUEST%20%20RELEASE:%20%288/8/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


