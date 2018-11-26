---
title: eHS_AUTHENTICATION_RESULT enumeration
description: The eHS_AUTHENTICATION_RESULT enumeration indicates the result of authentication by the plugin after the PostConnectAuth request.
ms.assetid: a61ddc7c-8df8-410c-83df-9058e88bce51
keywords: 
 - eHS_AUTHENTICATION_RESULT enumeration Network Drivers Starting with Windows Vista
ms.date: 07/31/2017
ms.localizationpriority: medium
---

# eHS\_AUTHENTICATION\_RESULT enumeration

[!include[Wi-Fi Hotspot Offloading deprecation](wi-fi-hotspot-offloading-deprecation.md)]


The **eHS\_AUTHENTICATION\_RESULT** enumeration indicates the result of authentication by the plugin after the PostConnectAuth request.

Syntax
------

```ManagedCPlusPlus
typedef enum _eHS_AUTHENTICATION_RESULT { 
  HS_AUTHENTICATION_RESULT_SUCCESS         = 0,
  HS_AUTHENTICATION_RESULT_FAILED_TIMEOUT  = 100,
  HS_AUTHENTICATION_RESULT_FAILED_AUTH,
  HS_AUTHENTICATION_RESULT_FAILED_CONNECT,
  HS_AUTHENTICATION_RESULT_FAILED_OTHER,
  HS_AUTHENTICATION_RESULT_MAX
} eHS_AUTHENTICATION_RESULT;
```

Constants
---------

<a href="" id="hs-authentication-result-success"></a>**HS\_AUTHENTICATION\_RESULT\_SUCCESS**  
Indicates the authentication was successful.

<a href="" id="hs-authentication-result-failed-timeout"></a>**HS\_AUTHENTICATION\_RESULT\_FAILED\_TIMEOUT**  
Indicates the authentication failed due to a timeout from the server/back end.

<a href="" id="hs-authentication-result-failed-auth"></a>**HS\_AUTHENTICATION\_RESULT\_FAILED\_AUTH**  
Indicates the authentication failed due to incorrect credentials.

<a href="" id="hs-authentication-result-failed-connect"></a>**HS\_AUTHENTICATION\_RESULT\_FAILED\_CONNECT**  
Indicates the authentication failed due to an inability to connect to the authentication server

<a href="" id="hs-authentication-result-failed-other"></a>**HS\_AUTHENTICATION\_RESULT\_FAILED\_OTHER**  
Indicates the authentication failed for some other reason.

<a href="" id="hs-authentication-result-max"></a>**HS\_AUTHENTICATION\_RESULT\_MAX**  
Indicates an out-of-range value.

Remarks
-------

The plugin passes this enumeration value to the hotspot plugin host through the [**HS\_HOST\_POST\_CONNECT\_AUTH\_COMPLETION**](hs-host-post-connect-auth-completion.md) function, which is used to inform the hotspot plugin host of the results of a call to [**HS\_PLUGIN\_START\_POST\_CONNECT\_AUTH**](hs-plugin-start-post-connect-auth.md).

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

 

 




