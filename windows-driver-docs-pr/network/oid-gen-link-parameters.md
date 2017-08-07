---
title: OID\_GEN\_LINK\_PARAMETERS
author: windows-driver-content
description: As a set, NDIS and overlying drivers use the OID\_GEN\_LINK\_PARAMETERS OID to set the current link state of a miniport adapter. The miniport driver receives the duplex state, link speeds, and pause functions in an NDIS\_LINK\_PARAMETERS structure.
ms.assetid: 6a8ee5b1-ac68-424f-b749-45b085ca1d75
ms.author: windowsdriverdev
ms.date: 08/08/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
keywords:
 - OID_GEN_LINK_PARAMETERS Network Drivers Starting with Windows Vista
---

# OID\_GEN\_LINK\_PARAMETERS


As a set, NDIS and overlying drivers use the OID\_GEN\_LINK\_PARAMETERS OID to set the current link state of a miniport adapter. The miniport driver receives the duplex state, link speeds, and pause functions in an NDIS\_LINK\_PARAMETERS structure.

**Version Information**

<a href="" id="windows-vista-and-later-versions-of-windows"></a>Windows Vista and later versions of Windows  
Supported.

<a href="" id="ndis-6-0-and-later-miniport-drivers"></a>NDIS 6.0 and later miniport drivers  
Mandatory.

The NDIS\_LINK\_PARAMETERS structure is defined as follows:

```ManagedCPlusPlus
    typedef struct _NDIS_LINK_PARAMETERS {
         NDIS_OBJECT_HEADER Header;
         NDIS_MEDIA_DUPLEX_STATE MediaDuplexState;
         ULONG64 XmitLinkSpeed;
         ULONG64 RcvLinkSpeed;
         NDIS_SUPPORTED_PAUSE_FUNCTIONS PauseFunctions;
         ULONG AutoNegotiationFlags;
    } NDIS_LINK_PARAMETERS, *PNDIS_LINK_PARAMETERS;
  
```

## <a href="" id="ddk-oid-gen-link-parameters--nr"></a>


This structure contains the following members:

<a href="" id="header"></a>**Header**  
The [**NDIS\_OBJECT\_HEADER**](ndis-object-header.md) structure for the NDIS\_LINK\_PARAMETERS structure. Set the **Type** member of the structure that **Header** specifies to NDIS\_OBJECT\_TYPE\_DEFAULT, the **Revision** member to NDIS\_LINK\_PARAMETERS\_REVISION\_1, and the **Size** member to NDIS\_SIZEOF\_LINK\_PARAMETERS\_REVISION\_1.

<a href="" id="mediaduplexstate"></a>**MediaDuplexState**  
The media duplex state. This value is the same as the value that is returned by the [OID\_GEN\_MEDIA\_DUPLEX\_STATE](oid-gen-media-duplex-state.md) OID.

<a href="" id="xmitlinkspeed"></a>**XmitLinkSpeed**  
The transmit link speed in bits per second.

<a href="" id="rcvlinkspeed"></a>**RcvLinkSpeed**  
The receive link speed in bits per second.

<a href="" id="pausefunctions"></a>**PauseFunctions**  
The type of support for the IEEE 802.3 pause frames. This member must be one of the following pause functions:

<a href="" id="ndispausefunctionsunsupported"></a>**NdisPauseFunctionsUnsupported**  
The adapter or link partner does not support pause frames.

<a href="" id="ndispausefunctionssendonly"></a>**NdisPauseFunctionsSendOnly**  
The adapter and link partner support only sending pause frames from the adapter to the link partner.

<a href="" id="ndispausefunctionsreceiveonly"></a>**NdisPauseFunctionsReceiveOnly**  
The adapter and link partner support only sending pause frames from the link partner to the adapter

<a href="" id="ndispausefunctionssendandreceive"></a>**NdisPauseFunctionsSendAndReceive**  
The adapter and link partner support sending and receiving pause frames in both transmit and receive directions.

<a href="" id="autonegotiationflags"></a>**AutoNegotiationFlags**  
The auto-negotiation settings for the miniport adapter. This member is created from a bitwise OR of the following flags:

<a href="" id="ndis-link-state-xmit-link-speed-auto-negotiated"></a>NDIS\_LINK\_STATE\_XMIT\_LINK\_SPEED\_AUTO\_NEGOTIATED  
The adapter should auto-negotiate the transmit link speed with the link partner. If this flag is not set, the miniport driver should set the transmit link speed to the value that is specified in the **XmitLinkSpeed** member.

<a href="" id="ndis-link-state-rcv-link-speed-auto-negotiated"></a>NDIS\_LINK\_STATE\_RCV\_LINK\_SPEED\_AUTO\_NEGOTIATED  
The adapter should auto-negotiate the receive link speed with the link partner. If this flag is not set, the miniport driver should set the receive link speed to the value that is specified in the **RcvLinkSpeed** member.

<a href="" id="ndis-link-state-duplex-auto-negotiated"></a>NDIS\_LINK\_STATE\_DUPLEX\_AUTO\_NEGOTIATED  
The adapter should auto-negotiate the duplex state with the link partner. If this flag is not set, the miniport driver should set the duplex state to the value that is specified in the **MediaDuplexState** member.

<a href="" id="ndis-link-state-pause-functions-auto-negotiated"></a>NDIS\_LINK\_STATE\_PAUSE\_FUNCTIONS\_AUTO\_NEGOTIATED  
The miniport driver should auto-negotiate the support for pause frames with the other end. If this flag is not set, the miniport driver should use the pause frame support that is specified in the **PauseFunctions** member.

Remarks
-------

**Note**  Setting OID\_GEN\_LINK\_PARAMETERS can cause a loss of connectivity. Miniport drivers must reconfigure the miniport adapter when this OID is set. For example, the miniport driver can reset the miniport adapter with the resulting loss of existing connections. The specific mechanism for reconfiguration is application dependent.

 

If the link state of the miniport adapter changes because of the OID\_GEN\_LINK\_PARAMETERS set request, the miniport driver should generate an [**NDIS\_STATUS\_LINK\_STATE**](https://msdn.microsoft.com/library/windows/hardware/ff567391) status indication to notify NDIS and overlying drivers of the new link state.

Requirements
------------

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<tbody>
<tr class="odd">
<td><p>Header</p></td>
<td>Ntddndis.h (include Ndis.h)</td>
</tr>
</tbody>
</table>

## See also


[**NDIS\_OBJECT\_HEADER**](ndis-object-header.md)

[**NDIS\_STATUS\_LINK\_STATE**](https://msdn.microsoft.com/library/windows/hardware/ff567391)

[OID\_GEN\_MEDIA\_DUPLEX\_STATE](oid-gen-media-duplex-state.md)

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bnetvista\netvista%5D:%20OID_GEN_LINK_PARAMETERS%20%20RELEASE:%20%288/3/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


