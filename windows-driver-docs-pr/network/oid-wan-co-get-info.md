---
title: OID_WAN_CO_GET_INFO
description: The OID_WAN_CO_GET_INFO OID requests the miniport driver to return information that applies to all virtual connections (VCs) on its NIC. This information is returned in an NDIS_WAN_CO_INFO structure, defined as follows.
ms.assetid: c97130a5-68e1-4c69-a5a5-9781ea59af0c
ms.date: 08/08/2017
keywords: 
 -OID_WAN_CO_GET_INFO Network Drivers Starting with Windows Vista
ms.localizationpriority: medium
---

# OID\_WAN\_CO\_GET\_INFO


The OID\_WAN\_CO\_GET\_INFO OID requests the miniport driver to return information that applies to all virtual connections (VCs) on its NIC. This information is returned in an NDIS\_WAN\_CO\_INFO structure, defined as follows.

```ManagedCPlusPlus
    typedef struct _NDIS_WAN_CO_INFO {
         OUT ULONG MaxFrameSize;
         OUT ULONG MaxSendWindow;
         OUT ULONG FramingBits;
         OUT ULONG DesiredACCM;
    } NDIS_WAN_CO_INFO, *PNDIS_WAN_CO_INFO;
```




The members of this structure contain the following information:

<a href="" id="maxframesize"></a>**MaxFrameSize**  
Specifies the maximum frame size for any net packet that the miniport driver can send and receive. This value should exclude the miniport driver's own framing overhead and/or the PPP HDLC overhead. Typically this value is around 1500.

However, all CoNDIS WAN miniport drivers should use an internal **MaxFrameSize** that is 32 bytes larger than the value they return for this OID. For example, a CoNDIS WAN miniport driver that returns 1500 for this OID should internally accept and send up to 1532. Such a miniport driver can readily support future bridging and additional protocols.

<a href="" id="maxsendwindow"></a>**MaxSendWindow**  
Specifies the maximum number of outstanding packets that the CoNDIS WAN miniport driver can handle on a VC. This member must be set to at least one.

The NDISWAN driver uses the value of this member as a limit on how many packets it submits in send requests to the miniport driver's *MiniportCoSendPackets* function before NDISWAN holds send packets. These packets are queued until the miniport driver completes an outstanding send. A miniport driver can adjust this value dynamically and on a per-VC basis using the **SendWindow** member in the [**WAN\_CO\_LINKPARAMS**](https://msdn.microsoft.com/library/windows/hardware/ff565819) structure that the miniport driver passes to [**NdisMCoIndicateStatus**](https://msdn.microsoft.com/library/windows/hardware/ff553458). NDISWAN uses the current **SendWindow** value as its limit on outstanding sends. If the miniport driver sets **SendWindow** to zero, NDISWAN must stop sending packets for the particular VC. That is, the miniport driver specifies that the send window is shut down, which, in effect, specifies that it cannot accept any packets from NDISWAN.

Because a CoNDIS WAN miniport driver must queue packets internally, the value of **MaxSendWindow** is theoretically **max**( ULONG). However, this driver-determined value should reflect the link speed or hardware capabilities of the NIC. For example, if a miniport driver's NIC always has room for at least four packets, the miniport driver sets **MaxSendWindow** to four so that any incoming packet to *MiniportCoSendPackets* can be placed on the hardware immediately.

<a href="" id="framingbits"></a>**FramingBits**  
A 32-bit value that specifies a bitmask specifying the types of framing the miniport driver supports. The miniport driver can specify a combination of the following values, using the binary OR operator:

<a href="" id="ras-framing"></a>RAS\_FRAMING  
Set only if the miniport driver can detect older RAS framing. Only legacy drivers that supported earlier RAS framing set this flag.

<a href="" id="ras-compression"></a>RAS\_COMPRESSION  
Set only if the miniport driver supports the older RAS compression scheme.

<a href="" id="ppp-framing"></a>PPP\_FRAMING  
Should always be set. Indicates the miniport driver can detect and support PPP framing for its medium type.

<a href="" id="ppp-compress-address-control"></a>PPP\_COMPRESS\_ADDRESS\_CONTROL  
Set if the miniport driver supports PPP address and control-field compression.

NDISWAN will remove the address and control field if this LCP option is negotiated. Some WAN medium types, such as X.25, do not support this option.

<a href="" id="ppp-compress-protocol-field"></a>PPP\_COMPRESS\_PROTOCOL\_FIELD  
Set if the miniport driver supports PPP protocol field compression.

NDISWAN will remove one byte from the protocol field when applicable if this LCP option is negotiated.

<a href="" id="ppp-accm-supported"></a>PPP\_ACCM\_SUPPORTED  
Set if the miniport driver supports Asynchronous Control Character Mapping. This bit is only valid for asynchronous media, such as modems. If this bit is set the **DesiredACCM** member should be valid.

<a href="" id="ppp-multilink-framing"></a>PPP\_MULTILINK\_FRAMING  
Set if the miniport driver supports multiple-link framing as specified in IETF RFC 1717.

<a href="" id="ppp-short-sequence-hdr-format"></a>PPP\_SHORT\_SEQUENCE\_HDR\_FORMAT  
Set if the miniport driver supports header format for multiple-link framing as specified in IETF RFC 1717.

<a href="" id="slip-framing"></a>SLIP\_FRAMING  
Set if the miniport driver can detect and support SLIP framing (asynchronous miniport drivers only).

<a href="" id="slip-vj-compression"></a>SLIP\_VJ\_COMPRESSION  
Set if the miniport driver can support Van Jacobsen TCP/IP header compression for SLIP. NDISWAN supports SLIP\_VJ\_COMPRESSION (with 16 slots). Asynchronous media (serial miniport drivers) that support SLIP framing should set this bit.

Asynchronous media need not write any code to support VJ header compression. NDISWAN will take care of it.

<a href="" id="slip-vj-autodetect"></a>SLIP\_VJ\_AUTODETECT  
Set if the miniport driver can auto-detect Van Jacobsen TCP/IP header compression for SLIP. NDISWAN will auto-detect VJ header compression. Asynchronous media (serial miniport drivers) should set this bit if they support SLIP framing.

<a href="" id="tapi-provider"></a>TAPI\_PROVIDER  
Set if the miniport driver supports the TAPI Service Provider OIDs. Unless this bit is set, TAPI OID calls will not be made to the miniport driver.

<a href="" id="media-nrz-encoding"></a>MEDIA\_NRZ\_ENCODING  
Set if the miniport driver supports NRZ encoding, the PPP default for some media types such as ISDN. This value is reserved for future use.

<a href="" id="media-nrzi-encoding"></a>MEDIA\_NRZI\_ENCODING  
Set if the miniport driver supports NRZI encoding. This value is reserved for future use.

<a href="" id="media-nlpid"></a>MEDIA\_NLPID  
Set if the miniport driver has and can set the NLPID in its frame. This value is reserved for future use.

<a href="" id="rfc-1356-framing"></a>RFC\_1356\_FRAMING  
Set if the miniport driver supports IETF RFC 1356 X.25 and ISDN framing. This value is reserved for future use.

<a href="" id="rfc-1483-framing"></a>RFC\_1483\_FRAMING  
Set if the miniport driver supports IETF RFC 1483 ATM adaptation layer-5 encapsulation. This value is reserved for future use.

<a href="" id="rfc-1490-framing"></a>RFC\_1490\_FRAMING  
Set if the miniport driver supports IETF RFC 1490 Frame Relay framing. This value is reserved for future use.

<a href="" id="nbf-preserve-mac-address"></a>NBF\_PRESERVE\_MAC\_ADDRESS  
Set if the miniport driver supports IETF framing as specified in the draft "The PPP NETBIOS Frames Control Protocol (NBFCP)."

<a href="" id="shiva-framing"></a>SHIVA\_FRAMING  
Superseded by NBF\_PRESERVE\_MAC\_ADDRESS.

<a href="" id="pass-through-mode"></a>PASS\_THROUGH\_MODE  
Set if the miniport driver does its own framing. If this flag is set, NDISWAN passes frames, uninterpreted and unmodified.

Miniport drivers must be in the default PPP framing mode until each miniport driver receives an [OID\_WAN\_CO\_SET\_LINK\_INFO](oid-wan-co-set-link-info.md) request. The miniport driver must auto-detect any framing that it claims to support.

For example, miniport drivers that support old RAS framing must auto-detect RAS framing from PPP framing. If a miniport driver detects a framing scheme other than the default, that miniport driver should automatically switch its framing into the newly detected framing.

A subsequent query with [OID\_WAN\_CO\_GET\_LINK\_INFO](oid-wan-co-get-link-info.md) should indicate the detected framing. If no framing is yet detected, the **FramingBits** should be zero in the returned NDIS\_WAN\_CO\_GET\_LINK\_INFO information.

If the WAN miniport driver is called subsequently with OID\_WAN\_CO\_SET\_LINK\_INFO in which the **FramingBits** member is zero, the miniport driver should attempt to auto-detect the framing upon reception of each frame.

<a href="" id="desiredaccm"></a>**DesiredACCM**  
The Asynchronous Control Character Map is negotiated. This member is relevant only for asynchronous media types.

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
<td><p>Supported for NDIS 6.0 and NDIS 5.1 drivers in Windows Vista. Supported for NDIS 5.1 drivers in Windows XP.</p></td>
</tr>
<tr class="even">
<td><p>Header</p></td>
<td>Ntddndis.h (include Ndis.h)</td>
</tr>
</tbody>
</table>

## See also


[**NdisMCoIndicateStatus**](https://msdn.microsoft.com/library/windows/hardware/ff553458)

[OID\_WAN\_CO\_GET\_LINK\_INFO](oid-wan-co-get-link-info.md)

[OID\_WAN\_CO\_SET\_LINK\_INFO](oid-wan-co-set-link-info.md)

[**WAN\_CO\_LINKPARAMS**](https://msdn.microsoft.com/library/windows/hardware/ff565819)








