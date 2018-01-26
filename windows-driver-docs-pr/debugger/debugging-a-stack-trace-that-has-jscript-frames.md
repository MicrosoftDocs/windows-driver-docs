---
title: Debugging a Stack Trace that has JScript Frames
description: The JScript Stack Dump Creation and Consumption feature works by collecting JScript frames and stitching them against debugger physical frames. 
ms.assetid: A470809F-55AA-4A49-B181-EC8D22C84F31
keywords: ["JScript", "jscript9diagdump.dll"]
ms.author: domars
ms.date: 05/23/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Debugging a Stack Trace that has JScript Frames


The JScript Stack Dump Creation and Consumption feature works by collecting JScript frames and stitching them against debugger physical frames. Sometimes on x86 platforms, the debugger constructs the stack trace incorrectly.

If your stack includes JScript frames that you think might be incorrect, enter the following command in the debugger.

**.stkwalk\_force\_frame\_pointer 1**

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[debugger\debugger]:%20Debugging%20a%20Stack%20Trace%20that%20has%20JScript%20Frames%20%20RELEASE:%20%285/15/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




