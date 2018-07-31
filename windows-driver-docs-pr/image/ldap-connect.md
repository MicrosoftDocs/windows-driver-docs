---
title: LDAP Connect
author: windows-driver-content
description: LDAP Connect
ms.assetid: 8a19e5fb-fec3-4fb6-9cca-1fba01e70958
ms.author: windowsdriverdev
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
ms.localizationpriority: medium
---

# LDAP Connect


The LDAP connect should use the fully qualified domain name as the parameter and connect to the LDAP Server using port 389.

A typical example would look like this:

```
ld = ldap_open("mydomain.corp.contoso.com", 389);
```

For more information about LDAP Connect, see [ldap\_connect Function](http://go.microsoft.com/fwlink/p/?linkid=154078).

 

 




