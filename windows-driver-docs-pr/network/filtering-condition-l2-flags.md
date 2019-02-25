---
title: Filtering condition L2 flags
description: This section describes filtering condition L2 flags.
ms.assetid: D24A261D-6324-43CC-BD2A-CDB9B024432C
keywords:
- Filtering condition L2 flags network drivers
ms.date: 11/08/2017
ms.localizationpriority: medium
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

