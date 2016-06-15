---
title: Network Redirector Design in Windows NT
author: windows-driver-content
description: Network Redirector Design in Windows NT
ms.assetid: 1feb43a3-ee65-4446-b38b-8b3f9188f43d
keywords: ["network redirectors WDK , Windows NT", "redirector drivers WDK , Windows NT", "kernel network redirectors WDK , Windows NT"]
---

# Network Redirector Design in Windows NT


## <span id="ddk_network_redirector_design_in_windows_nt_if"></span><span id="DDK_NETWORK_REDIRECTOR_DESIGN_IN_WINDOWS_NT_IF"></span>


The architecture that implements a kernel-mode driver for network redirectors has changed over time. The general model for network redirectors has typically been based on the architecture that implements the kernel driver for the Client for Microsoft Networks (LAN Manager Client). The original scheme introduced in Windows NT 3.0 used no shared components and was limited. This model is often called the original rdr driver model (rdr was an abbreviation for redirector). No special support from the operating system was provided to simplify the process of writing a network redirector. Each kernel-mode driver implemented all of the functions required for a network redirector. Consequently, each kernel driver would include a large amount of code for interactions with the I/O Manager, Cache Manager, and Memory Manager. Each network redirector (LAN Manager, NetWare, and NFS, for example) installed on Windows had to implement all of these functions themselves. This design model was used for drivers for network redirectors through Windows NT 4.0. The following is a diagram of this architecture, with multiple redirectors.

![diagram illustrating network redirector design in windows nt](images/redir-01.png)

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[ifsk\ifsk]:%20Network%20Redirector%20Design%20in%20Windows%20NT%20%20RELEASE:%20%285/9/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


