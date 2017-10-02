---
title: eHS_AUTHENTICATION_RESULT enumeration
author: windows-driver-content
description: The eHS\_AUTHENTICATION\_RESULT enumeration indicates the result of authentication by the plugin after the PostConnectAuth request.
ms.assetid: a61ddc7c-8df8-410c-83df-9058e88bce51
keywords: 
 - eHS_AUTHENTICATION_RESULT enumeration Network Drivers Starting with Windows Vista
ms.author: windowsdriverdev
ms.date: 07/31/2017 
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# eHS\_AUTHENTICATION\_RESULT enumeration


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

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bnetvista\netvista%5D:%20eHS_AUTHENTICATION_RESULT%20enumeration%20%20RELEASE:%20%287/31/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


