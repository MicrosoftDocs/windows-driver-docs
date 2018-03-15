---
title: LDAP Bind
author: windows-driver-content
description: LDAP Bind
ms.assetid: c45a3273-d571-4e56-987e-929fb12159a6
ms.author: windowsdriverdev
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
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

 

 




