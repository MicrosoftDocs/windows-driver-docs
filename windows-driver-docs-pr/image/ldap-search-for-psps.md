---
title: LDAP Search for PSPs
author: windows-driver-content
description: LDAP Search for PSPs
ms.assetid: c93b0c0f-eb46-4740-a5af-6a1ccaa6ccf9
ms.author: windowsdriverdev
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
ms.localizationpriority: medium
---

# LDAP Search for PSPs


Use LDAP Search to complete the search for PSPs.

The following shows a typical LDAP Search:

```
     LDAP Search Request
     Scope : SingleLevel
     baseObject : CN=PSPs,CN=System,[defaultNamingContext]
     filter: (objectClass = msImagingPostScanProcess)
     attributes:
          Item: displayName 
          Etc....
```

For more information about LDAP Search, see [ldap\_search Function](http://go.microsoft.com/fwlink/p/?linkid=154081).

 

 




