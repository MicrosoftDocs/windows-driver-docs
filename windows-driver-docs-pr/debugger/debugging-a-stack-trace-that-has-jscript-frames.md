---
title: Debugging a Stack Trace that has JScript Frames
description: The JScript Stack Dump Creation and Consumption feature works by collecting JScript frames and stitching them against debugger physical frames. 
ms.assetid: A470809F-55AA-4A49-B181-EC8D22C84F31
keywords: ["JScript", "jscript9diagdump.dll"]
ms.author: domars
ms.date: 05/23/2017
ms.localizationpriority: medium
---

# Debugging a Stack Trace that has JScript Frames


The JScript Stack Dump Creation and Consumption feature works by collecting JScript frames and stitching them against debugger physical frames. Sometimes on x86 platforms, the debugger constructs the stack trace incorrectly.

If your stack includes JScript frames that you think might be incorrect, enter the following command in the debugger.

**.stkwalk\_force\_frame\_pointer 1**

 

 





