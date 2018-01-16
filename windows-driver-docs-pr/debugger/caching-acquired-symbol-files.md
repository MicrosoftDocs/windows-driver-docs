---
title: Caching Acquired Symbol Files
description: Caching Acquired Symbol Files
ms.assetid: 2aedc67f-27f3-46f4-8369-504e525b8c18
keywords: ["SymProxy, caching"]
ms.author: domars
ms.date: 05/23/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Caching Acquired Symbol Files


Typically, SymProxy caches the files that it acquires in the directory designated within Internet Information Services (IIS) as the virtual root for the associated Web site. Then IIS makes the file available to the client debugger. Because the debugger cannot open a file directly from HTTP, it copies the file to a local cache, specified by the symbol path:

```
srv*c:\localcache*http://server/symbols
```

In this example, the client debugger copies the file to c:\\localcache. In a situation such as this, the file is copied twice - once by SymProxy to the virtual root of the Web site, and again by the debugger to its local cache.

It is possible to avoid the second copy operation and speed up processing. To do this, you must first share the virtual root of the Web site as a UNC path that can be accessed by the debuggers. For sake of example, this path is named \\\\server\\symbols. You must then remove the IIS configuration for MIME types:

**To remove the IIS configuration for MIME types**

1.  From **Administrative Tools** open **Internet Information Services (IIS) Manager**.

2.  Expand **Web Sites**.

3.  Right-click **Default Web Site**.

4.  Right-click the **Symbols** virtual directory and select **Properties**.

5.  Click the **HTTP Headers** tab.

6.  Click **MIME Types** .

7.  Select all types in the list box labeled **Registered MIME Types**.

8.  Click **Remove** .

9.  To exit the **MIME Types** dialog, click **OK**.

10. To exit **Symbols Properties**, click **OK**.

This causes IIS to return **file not found** to the debugging client for all transactions on the Web site. However, it does not prevent SymProxy from populating the virtual root with the file.

After you remove the IIS configuration for MIME types, configure the debugger clients to look for symbols first in the HTTP store and in the share that maps to the virtual root of the store with the command:

```
srv**http://server/symbols;srv*\\server\symbols
```

In the preceding example, the first element of the symbol path (srv\*\*http://server/symbols) says to get files from the HTTP store and copy them to the default symbol store as a local cache. The specified cache is of no importance because no file is ever received from the HTTP store. After this failure, it attempts to obtain the file from the actual location of the virtual root of the store (srv\*\\\\server\\symbols). This attempt succeeds because the file is copied to that location as a side effect of the previous path processing.

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[debugger\debugger]:%20Caching%20Acquired%20Symbol%20Files%20%20RELEASE:%20%285/15/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




