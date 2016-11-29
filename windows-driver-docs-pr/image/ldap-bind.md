---
title: LDAP Bind
author: windows-driver-content
description: LDAP Bind
MS-HAID:
- 'dsm\_des\_tut\_08305556-e176-4a2b-8f04-124f6cda7c0d.xml'
- 'image.ldap\_bind'
MSHAttr:
- 'PreferredSiteName:MSDN'
- 'PreferredLib:/library/windows/hardware'
ms.assetid: c45a3273-d571-4e56-987e-929fb12159a6
---

# LDAP Bind


The LDAP Bind should use either NTLM/Kerberos authentication to bind with the supplied user credentials.

A typical example would look like this:

```
ldap_bind_s(ld, NULL, &NtAuthIdentity, 4230);
```

The above example assumes that NTAuthIdentity has the user credentials.

In order to get the objectSid of the user, the LDAP Search query for the user record should not assume a specific structure of the DN for users. It is advisable to search from the root of the directory instead.

For example, to search for the SID of user "Joe" in the directory the search query should be

```
scope: SubTree
baseObject: [defaultNamingContext of the domain]
filter: (&(objectclass=*)(sAMAccountName=Joe))
attributes: 
     Item: cn
     Item: objectSid
```

For more information about LDAP Bind, see [ldap\_bind\_s Function](http://go.microsoft.com/fwlink/p/?linkid=154080).

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bimage\image%5D:%20LDAP%20Bind%20%20RELEASE:%20%288/17/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


