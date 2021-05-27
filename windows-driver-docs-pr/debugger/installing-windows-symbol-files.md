---
title: Installing Windows Symbol Files
description: Installing Windows Symbol Files
keywords: ["symbols, Windows", "symbols, user-mode"]
ms.date: 03/26/2017
ms.localizationpriority: medium
---

# Installing Windows Symbol Files

Before you debug the Windows kernel, a driver or app, you need access to the proper symbol files. The official way to get Windows symbols is to use the Microsoft Symbol Server. The symbol server makes symbols available to your debugging tools as needed. After a symbol file is downloaded from the symbol server it is cached on the local computer for quick access. 

You can connect to the Microsoft Symbol Server with one simple use of the [**.symfix (Set Symbol Store Path)**](-symfix--set-symbol-store-path-.md) command. For full details, see [Microsoft Public Symbols](microsoft-public-symbols.md).

> [!IMPORTANT]
> We are no longer publishing the offline symbol packages for Windows. The faster Windows update cadence means the Windows debugging symbols are quickly made out of  date. We have made significant improvements to the online [Microsoft Symbol Server](microsoft-public-symbols.md) where symbols for all Windows versions and updates are available. You can find more about this in this [blog entry](/archive/blogs/windbg/update-on-microsofts-symbol-server). 
>
> For information on how to retrieve symbols for a machine that is not connected to the Internet, see [Using a Manifest File with SymChk](using-a-manifest-file-with-symchk.md).

If you are going to debug a user-mode app, you need to install the symbols for this app as well.

You can debug an app if you have its symbols but not Windows symbols. However, your results will be much more limited. You will still be able to step through the app code, but any debugger activity which requires analysis of the kernel (such as getting a stack trace) is likely to fail.
