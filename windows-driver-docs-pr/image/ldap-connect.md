---
title: LDAP Connect
author: windows-driver-content
description: LDAP Connect
MS-HAID:
- 'dsm\_des\_tut\_13bb3f50-f6c3-4b2e-aa39-7516e32260dd.xml'
- 'image.ldap\_connect'
MSHAttr:
- 'PreferredSiteName:MSDN'
- 'PreferredLib:/library/windows/hardware'
ms.assetid: 8a19e5fb-fec3-4fb6-9cca-1fba01e70958
---

# LDAP Connect


The LDAP connect should use the fully qualified domain name as the parameter and connect to the LDAP Server using port 389.

A typical example would look like this:

```
ld = ldap_open("mydomain.corp.contoso.com", 389);
```

For more information about LDAP Connect, see [ldap\_connect Function](http://go.microsoft.com/fwlink/p/?linkid=154078).

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bimage\image%5D:%20LDAP%20Connect%20%20RELEASE:%20%288/17/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


