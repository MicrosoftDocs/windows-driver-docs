---
title: No Header Information Available
description: No Header Information Available
ms.assetid: cafc98c0-cae7-4140-8be7-6a535523f0e3
keywords: ["No header information available (warning)", "header information not available (warning)"]
ms.author: domars
ms.date: 05/23/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# No Header Information Available


## <span id="ddk_no_header_information_available_dbg"></span><span id="DDK_NO_HEADER_INFORMATION_AVAILABLE_DBG"></span>


The debugger identifies the proper symbols by examining the headers of the relevant modules. If these module headers are paged out, the debugger (and the symbol server) are unable to find the proper symbols. When this occurs, "No Header Information Available" is displayed within the symbol error message.

For information about how to debug a target when module headers are paged out, see [Reading Symbols from Paged-Out Headers](reading-symbols-from-paged-out-headers.md).

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[debugger\debugger]:%20No%20Header%20Information%20Available%20%20RELEASE:%20%285/15/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




