---
title: SDV environment variable is not set
description: SDV environment variable is not set
ms.assetid: 608a103b-333c-4692-b64b-4c1508f37b94
ms.author: windowsdriverdev
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# %SDV% environment variable is not set


SDV reports the following error when the %SDV% environment variable is not set.

```
Staticdv has detected that %SDV% environment variable is not set on the system.
Please reinstall Static Driver Verifier to fix this issue.
```

SDV creates the %SDV% system environment variable during installation to store the path to the SDV installation directory. If you delete this environment variable, SDV does not operate properly.

To resolve this error, uninstall and then reinstall SDV.

 

 





