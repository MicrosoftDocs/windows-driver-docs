---
title: dbgerr002 Bad Pointer
description: dbgerr002 Bad Pointer
ms.assetid: d5f2404e-3e7d-4de2-a772-0d42169eb9ad
keywords: ["dbgerr002", "Bad pointer (dbgerr002)"]
ms.author: windowsdriverdev
ms.date: 05/23/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# dbgerr002: Bad Pointer


## <span id="ddk_dbgerr002_dbg"></span><span id="DDK_DBGERR002_DBG"></span>


Debugger error **dbgerr002** displays the message "Bad pointer." This error indicates a problem retrieving a symbol file.

The symbol server has the file indexed, but is being redirected to another location to find the file. No file is accessible at this other location.

Two common causes of this problem are:

-   The path is a UNC path, and the computer containing this server is not available.

-   The path indicates a directory or file that has been deleted.

If your symbol store was created by using SymStore, you can find the full path to this file by examining file.ptr. For details, see [Using SymStore](symstore.md).

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[debugger\debugger]:%20dbgerr002:%20Bad%20Pointer%20%20RELEASE:%20%285/15/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




