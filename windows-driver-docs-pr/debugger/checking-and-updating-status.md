---
title: Checking and Updating Status
description: Checking and Updating Status
ms.assetid: 60b81369-e81b-4795-a729-a535c38a0999
keywords: ["SymProxy, status", "SymProxy, checking status", "SymProxy, updating status"]
ms.author: domars
ms.date: 05/23/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Checking and Updating Status


It is possible to see where SymProxy is configured to acquire symbols by using a web browser. Add *\\status* to the server URL get the status information. For example, if the symbols Web site is http://symbols.contoso.com, go to http://symbols.contoso.com/status. You can also use this to cause symproxy to re-read its configuration information after making a change to the registry. This changes the paths without having to restart the IIS service.

 

 





