---
title: Hotspot 2.0
description: Hotspot 2.0
ms.assetid: 4dbd242d-8745-4ab2-b1dc-9f9dd9a73b42
---

# Hotspot 2.0


Hotspot 2.0 is a standard for seamless authentication to hotspots. Hotspot 2.0 offers an encrypted connection between the client and the access point. It uses IEEE 802.11u to communicate with the provider before it establishes a connection. Authentication and encryption are provided by using WPA2-Enterprise together with one of several EAP methods.

The following table describes common credential types that are defined by Hotspot 2.0:

<table>
<colgroup>
<col width="20%" />
<col width="20%" />
<col width="20%" />
<col width="20%" />
<col width="20%" />
</colgroup>
<thead>
<tr class="header">
<th>Credential</th>
<th>EAP method</th>
<th>EAP method supported</th>
<th>User can enter credentials</th>
<th>Operator can provision credentials</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p>Username and password</p></td>
<td><p>EAP-TTLS</p></td>
<td><p>Yes</p></td>
<td><p>Yes</p></td>
<td><p>No</p></td>
</tr>
<tr class="even">
<td><p>Certificate</p></td>
<td><p>EAP-TTLS</p></td>
<td><p>Yes</p></td>
<td><p>Yes*</p></td>
<td><p>No</p></td>
</tr>
<tr class="odd">
<td><p>SIM</p></td>
<td><p>EAP-SIM or EAP-AKA</p></td>
<td><p>Yes</p></td>
<td><p>Yes*</p></td>
<td><p>Yes</p></td>
</tr>
</tbody>
</table>

 

\*User can select from certificates or the SIM is already present on the system.

Windows 8 and Windows 8.1 do not support the discovery or online sign-up portions of Hotspot 2.0, but they do support WPA2-Enterprise and all EAP methods that are required by the Hotspot 2.0 specification. Therefore, Windows 8 and Windows 8.1 can connect to a Hotspot 2.0 network when the user already has credentials.

Because Windows 8 and Windows 8.1 do not support 802.11u discovery, operators must provision Windows 8 or Windows 8.1 with wireless profiles that contain the applicable SSIDs for their networks.

Windows 10 fully supports Hotspot 2.0 Release 1, including discovery and profile creation.

## <span id="related_topics"></span>Related topics


[Hotspot authentication methods](hotspot-authentication-methods.md)

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bp_mb\p_mb%5D:%20Hotspot%202.0%20%20RELEASE:%20%281/18/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")





