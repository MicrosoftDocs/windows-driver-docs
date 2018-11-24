---
title: Hello World' Definition File
description: Hello World' Definition File
ms.assetid: 50c38eea-7826-44bb-9048-ce8e07ce3478
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# 'Hello World' Definition File

The definition file is used to export entry point functions. The *hellowld.def* file should contain the two following COM exports, **DllGetClassObject** and **DllCanUnloadNow**, which are described in the Microsoft Windows SDK documentation.

```make
LIBRARY HELLOWLD

EXPORTS
     DllGetClassObject   PRIVATE
     DllCanUnloadNow     PRIVATE
```
