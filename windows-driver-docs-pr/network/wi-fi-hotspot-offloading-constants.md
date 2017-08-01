---
title: Wi-Fi Hotspot Offloading Constants
author: windows-driver-content
description: This section describes the constants that are defined for the Wi-Fi Hotspot Offloading framework.
ms.assetid: F09DCB81-C9FF-493B-AE8F-97DE441A4BC3
ms.author: windowsdriverdev
ms.date: 07/31/2017 
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Wi-Fi Hotspot Offloading Constants

[!include[Wi-Fi Hotspot Offloading deprecation](wi-fi-hotspot-offloading-deprecation.md)]

This section describes the constants that are defined for the Wi-Fi Hotspot Offloading framework.

<a href="" id="hs-const-host-current-api-version"></a>**HS\_CONST\_HOST\_CURRENT\_API\_VERSION**  
1  
Current API version number.

<a href="" id="hs-const-max-network-display-name-length"></a>**HS\_CONST\_MAX\_NETWORK\_DISPLAY\_NAME\_LENGTH**  
32  
Maximum length of the network display name string.

<a href="" id="hs-const-max-realm-length"></a>**HS\_CONST\_MAX\_REALM\_LENGTH**  
255  
Maximum length of the realm value string.

<a href="" id="hs-const-min-conn-keepalive-time-in-mins"></a>**HS\_CONST\_MIN\_CONN\_KEEPALIVE\_TIME\_IN\_MINS**  
5  
Minimum time between keep-alive message transmissions

<a href="" id="hs-const-profile-update-time-in-days"></a>**HS\_CONST\_PROFILE\_UPDATE\_TIME\_IN\_DAYS**  
7  
Minimum time between checks for profile updates.

<a href="" id="hs-const-min-network-priority-value"></a>**HS\_CONST\_MIN\_NETWORK\_PRIORITY\_VALUE**  
1  
Minimum network priority value.

<a href="" id="hs-const-max-network-priority-value"></a>**HS\_CONST\_MAX\_NETWORK\_PRIORITY\_VALUE**  
65000  
Maximum network priority value.

<a href="" id="hs-max-phone-number-length"></a>**HS\_MAX\_PHONE\_NUMBER\_LENGTH**  
32  
Maximum length of the phone number string.

<a href="" id="hs-const-max-host-name-length"></a>**HS\_CONST\_MAX\_HOST\_NAME\_LENGTH**  
255  
Maximum length of the host name string.

<a href="" id="hs-const-plugin-min-rank-value"></a>**HS\_CONST\_PLUGIN\_MIN\_RANK\_VALUE**  
1  
Minimum Rank value. Must be greater than 0.

<a href="" id="hs-const-plugin-max-rank-value"></a>**HS\_CONST\_PLUGIN\_MAX\_RANK\_VALUE**  
250  
Maximum rank value. Must be less than or equal to 250.

<a href="" id="hs-const-max-provider-name-length"></a>**HS\_CONST\_MAX\_PROVIDER\_NAME\_LENGTH**  
63  
Maximum length of provider name string.

<a href="" id="hs-const-max-advanced-page-string-length"></a>**HS\_CONST\_MAX\_ADVANCED\_PAGE\_STRING\_LENGTH**  
255  
Maximum length of the advanced page string.

<a href="" id="hs-const-max-phone-number-length"></a>**HS\_CONST\_MAX\_PHONE\_NUMBER\_LENGTH**  
32  
Maximum length of the phone number string.

<a href="" id="hs-const-max-supported-sims"></a>**HS\_CONST\_MAX\_SUPPORTED\_SIMS**  
1000  
Maximum size of the list of supported SIM configurations.

<a href="" id="hs-const-max-cellular-exception-hosts"></a>**HS\_CONST\_MAX\_CELLULAR\_EXCEPTION\_HOSTS**  
5  
Maximum size of the list of cellular bearers.

<a href="" id="hs-const-max-auth-error-msg-length"></a>**HS\_CONST\_MAX\_AUTH\_ERROR\_MSG\_LENGTH**  
512  
Maximum length of an authentication error message.

<a href="" id="hs-const-max-user-messages-in-minutes"></a>**HS\_CONST\_MAX\_USER\_MESSAGES\_IN\_MINUTES**  
7\*24\*60  
Maximum user messages, in minutes (7 days).

The following flags are defined for the plug-in and the host to indicate their requirements and capabilities respectively.

<a href="" id="hs-flag-capability-network-type-visible"></a>**HS\_FLAG\_CAPABILITY\_NETWORK\_TYPE\_VISIBLE**  
0x00000001  
Specifies visible network.

<a href="" id="hs-flag-capability-network-type-hidden"></a>**HS\_FLAG\_CAPABILITY\_NETWORK\_TYPE\_HIDDEN**  
0x00000002  
Specifies hidden network.

<a href="" id="hs-flag-capability-network-display-name"></a>**HS\_FLAG\_CAPABILITY\_NETWORK\_DISPLAY\_NAME**  
0x00000010  
Specifies use of display name for EAP-SIM or EAP-AKA authentication.

<a href="" id="hs-flag-capability-network-auth-no-sim"></a>**HS\_FLAG\_CAPABILITY\_NETWORK\_AUTH\_NO\_SIM**  
0x00000100  
Specifies no-SIM authentication.

<a href="" id="hs-flag-capability-network-auth-http"></a>**HS\_FLAG\_CAPABILITY\_NETWORK\_AUTH\_HTTP**  
0x00000200  
Specifies HTTP authentication.

<a href="" id="hs-flag-capability-network-auth-eap-sim"></a>**HS\_FLAG\_CAPABILITY\_NETWORK\_AUTH\_EAP\_SIM**  
0x00001000  
Specifies EAP-SIM authentication.

<a href="" id="hs-flag-capability-network-auth-eap-aka"></a>**HS\_FLAG\_CAPABILITY\_NETWORK\_AUTH\_EAP\_AKA**  
0x00002000  
Specifies EAP-AKA authentication.

<a href="" id="hs-flag-capability-network-auth-eap-aka-prime"></a>**HS\_FLAG\_CAPABILITY\_NETWORK\_AUTH\_EAP\_AKA\_PRIME**  
0x00004000  
Specifies EAP-AKA’ (AKA Prime) authentication.

<a href="" id="hs-flag-capability-network-custom-realm"></a>**HS\_FLAG\_CAPABILITY\_NETWORK\_CUSTOM\_REALM**  
0x00010000  
Specifies use of custom realm value for network authentication.

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
<td><p>Windows 10 Mobile</p></td>
</tr>
<tr class="even">
<td><p>Header</p></td>
<td>Hotspotoffloadplugin.h (include Hotspotoffloadplugin.h)</td>
</tr>
</tbody>
</table>

## See also


[Wi-Fi Hotspot Offloading Reference](wi-fi-hotspot-offloading-reference.md)

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bnetvista\netvista%5D:%20Wi-Fi%20Hotspot%20Offloading%20Constants%20%20RELEASE:%20%287/31/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


