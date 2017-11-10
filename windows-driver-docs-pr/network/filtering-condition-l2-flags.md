---
title: Filtering condition L2 flags
author: windows-driver-content
description: This section describes filtering condition L2 flags.
ms.assetid: D24A261D-6324-43CC-BD2A-CDB9B024432C
keywords:
- Filtering condition L2 flags network drivers
ms.author: windowsdriverdev
ms.date: 11/08/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Filtering condition L2 flags

The filtering condition L2 flags are each represented by a bit field. These flags are defined as follows:

<table>
<tr>
<th>Filtering condition flag</th>
<th>Description</th>
</tr>
<tr>
<td>
<p>FWP_CONDITION_L2_IS_NATIVE_ETHERNET</p>
<p>0x00000001</p>
</td>
<td>
<p>Tests if the data passed to a callout driver describes a native Ethernet packet.</p>
<p>This flag is applicable at the following filtering layers in Windows 8,  Windows Server 2012, and later versions of Windows:</p>
<dl>
<dd>
FWPM_LAYER_INBOUND_MAC_FRAME_ETHERNET
</dd>
<dd>
FWPM_LAYER_OUTBOUND_MAC_FRAME_ETHERNET
</dd>
<dd>
FWPM_LAYER_INBOUND_MAC_FRAME_NATIVE
</dd>
<dd>
FWPM_LAYER_OUTBOUND_MAC_FRAME_NATIVE
</dd>
</dl>
<p>Tests if the data passed to a callout driver describes a  WIFI packet.</p>
<p>This flag is applicable at the following filtering layers in Windows 8,  Windows Server 2012, and later versions of Windows:</p>
<dl>
<dd>
FWPM_LAYER_INBOUND_MAC_FRAME_ETHERNET
</dd>
<dd>
FWPM_LAYER_OUTBOUND_MAC_FRAME_ETHERNET
</dd>
<dd>
FWPM_LAYER_INBOUND_MAC_FRAME_NATIVE
</dd>
<dd>
FWPM_LAYER_OUTBOUND_MAC_FRAME_NATIVE
</dd>
</dl>
</td>
</tr>
<tr>
<td>
<p>FWP_CONDITION_L2_IS_WIFI</p>
<p>0x00000002</p>
</td>
<td>
<p>Tests if the data passed to a callout driver describes a native Wi-Fi packet.</p>
<p>This flag is applicable at the following filtering layers in Windows 8,  Windows Server 2012, and later versions of Windows:</p>
<dl>
<dd>
FWPM_LAYER_INBOUND_MAC_FRAME_ETHERNET
</dd>
<dd>
FWPM_LAYER_OUTBOUND_MAC_FRAME_ETHERNET
</dd>
<dd>
FWPM_LAYER_INBOUND_MAC_FRAME_NATIVE
</dd>
<dd>
FWPM_LAYER_OUTBOUND_MAC_FRAME_NATIVE
</dd>
</dl>
</td>
</tr>
<tr>
<td>
<p>FWP_CONDITION_L2_IS_MOBILE_BROADBAND</p>
<p>0x00000004</p>
</td>
<td>
<p>Tests if the data passed to a callout driver describes a mobile broadband packet.</p>
<p>This flag is applicable at the following filtering layers in Windows 8,  Windows Server 2012, and later versions of Windows:</p>
<dl>
<dd>
FWPM_LAYER_INBOUND_MAC_FRAME_ETHERNET
</dd>
<dd>
FWPM_LAYER_OUTBOUND_MAC_FRAME_ETHERNET
</dd>
<dd>
FWPM_LAYER_INBOUND_MAC_FRAME_NATIVE
</dd>
<dd>
FWPM_LAYER_OUTBOUND_MAC_FRAME_NATIVE
</dd>
</dl>
</td>
</tr>
<tr>
<td>
<p>FWP_CONDITION_L2_IS_WIFI_DIRECT_DATA</p>
<p>0x00000008</p>
</td>
<td>
<p>Tests if the data passed to a callout driver describes a WIFI direct data packet.</p>
<p>This flag is applicable at the following filtering layers in Windows 8,  Windows Server 2012, and later versions of Windows:</p>
<dl>
<dd>
FWPM_LAYER_INBOUND_MAC_FRAME_ETHERNET
</dd>
<dd>
FWPM_LAYER_OUTBOUND_MAC_FRAME_ETHERNET
</dd>
<dd>
FWPM_LAYER_INBOUND_MAC_FRAME_NATIVE
</dd>
<dd>
FWPM_LAYER_OUTBOUND_MAC_FRAME_NATIVE
</dd>
</dl>
</td>
</tr>
<tr>
<td>
<p>FWP_CONDITION_L2_IS_VM2VM</p>
<p>0x00000010</p>
</td>
<td>
<p>Tests if the data passed to a callout driver describes a native virtual machine to virtual machine packet.</p>
<p>This flag is applicable at the following filtering layers in Windows 8,  Windows Server 2012, and later versions of Windows:</p>
<dl>
<dd>
FWPM_LAYER_INBOUND_MAC_FRAME_ETHERNET
</dd>
<dd>
FWPM_LAYER_OUTBOUND_MAC_FRAME_ETHERNET
</dd>
<dd>
FWPM_LAYER_INBOUND_MAC_FRAME_NATIVE
</dd>
<dd>
FWPM_LAYER_OUTBOUND_MAC_FRAME_NATIVE
</dd>
</dl>
</td>
</tr>
<tr>
<td>
<p>FWP_CONDITION_L2_IS_MALFORMED_PACKET</p>
<p>0x00000020</p>
</td>
<td>
<p>Tests if the data passed to a callout driver describes a malformed Ethernet packet.</p>
<p>This flag is applicable at the following filtering layers in Windows 8,  Windows Server 2012, and later versions of Windows:</p>
<dl>
<dd>
FWPM_LAYER_INBOUND_MAC_FRAME_ETHERNET
</dd>
<dd>
FWPM_LAYER_OUTBOUND_MAC_FRAME_ETHERNET
</dd>
<dd>
FWPM_LAYER_INBOUND_MAC_FRAME_NATIVE
</dd>
<dd>
FWPM_LAYER_OUTBOUND_MAC_FRAME_NATIVE
</dd>
</dl>
</td>
</tr>
<tr>
<td>
<p>FWP_CONDITION_L2_IS_IP_FRAGMENT_GROUP</p>
<p>0x00000040</p>
</td>
<td>
<p>Tests if the data passed to a callout driver describes a part of an IP fragment group.</p>
<p>This flag is applicable at the following filtering layers in Windows 8,  Windows Server 2012, and later versions of Windows:</p>
<dl>
<dd>
FWPM_LAYER_INBOUND_MAC_FRAME_ETHERNET
</dd>
<dd>
FWPM_LAYER_OUTBOUND_MAC_FRAME_ETHERNET
</dd>
<dd>
FWPM_LAYER_INBOUND_MAC_FRAME_NATIVE
</dd>
<dd>
FWPM_LAYER_OUTBOUND_MAC_FRAME_NATIVE
</dd>
</dl>
</td>
</tr>
<tr>
<td>
<p>FWP_CONDITION_L2_IF_CONNECTOR_PRESENT</p>
<p>0x00000080</p>
</td>
<td>
<p>Tests if a network interface connector is present on the underlying network adapter.</p>
<p>This flag should be set for a physical adapter.</p>
<p>This flag is applicable at the following filtering layers in Windows 8,  Windows Server 2012, and later versions of Windows:</p>
<dl>
<dd>
FWPM_LAYER_INBOUND_MAC_FRAME_ETHERNET
</dd>
<dd>
FWPM_LAYER_OUTBOUND_MAC_FRAME_ETHERNET
</dd>
<dd>
FWPM_LAYER_INBOUND_MAC_FRAME_NATIVE
</dd>
<dd>
FWPM_LAYER_OUTBOUND_MAC_FRAME_NATIVE
</dd>
</dl>
</td>
</tr>
</table>

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bp_mb\p_mb%5D:%20Planning%20your%20APN%20database%20submission%20%20RELEASE:%20%281/18/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")