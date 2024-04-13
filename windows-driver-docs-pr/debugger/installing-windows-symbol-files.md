---
title: Installing Windows Symbol Files
description: Installing Windows Symbol Files
keywords: ["symbols, Windows", "symbols, user-mode"]
ms.date: 09/29/2021
---

# Installing Windows Symbol Files in Older Versions of Windows

Before you debug the Windows kernel, a driver or app, you need access to the proper symbol files. The official way to get Windows symbols is to use the Microsoft Symbol Server. The symbol server makes symbols available to your debugging tools as needed. After a symbol file is downloaded from the symbol server it is cached on the local computer for quick access. 

You can connect to the Microsoft Symbol Server with one simple use of the [**.symfix (Set Symbol Store Path)**](../debuggercmds/-symfix--set-symbol-store-path-.md) command. For full details, see [Microsoft Public Symbols](microsoft-public-symbols.md).

> [!IMPORTANT]
> We are no longer publishing the offline symbol packages for Windows. The faster Windows update cadence means the Windows debugging symbols are quickly made out of  date. We have made significant improvements to the online [Microsoft Symbol Server](microsoft-public-symbols.md) where symbols for all Windows versions and updates are available. You can find more about this in this [blog entry](/archive/blogs/windbg/update-on-microsofts-symbol-server). 
>
> For information on how to retrieve symbols for a machine that is not connected to the Internet, see [Using a Manifest File with SymChk](using-a-manifest-file-with-symchk.md).

