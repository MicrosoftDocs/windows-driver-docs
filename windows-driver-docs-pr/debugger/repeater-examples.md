---
title: Repeater Examples
description: Repeater Examples
ms.assetid: 83aff647-65a7-409f-adce-254305395775
keywords: ["repeater, examples"]
ms.author: domars
ms.date: 05/23/2017
ms.localizationpriority: medium
---

# Repeater Examples


## <span id="ddk_repeater_examples_dbg"></span><span id="DDK_REPEATER_EXAMPLES_DBG"></span>


Let us suppose you have three computers, \\\\BOXA, \\\\BOXB, and \\\\BOXC, and you wish to use them as the server, the repeater, and the client, respectively.

You can start a debugging server on \\\\BOXA, using process 122 as the target, in the following manner:

```console
E:\Debugging Tools for Windows> cdb -server tcp:port=1025,password=wrought -p 122 
```

Then you can start a repeater on \\\\BOXB as follows:

```console
C:\Misc> dbengprx -c tcp:server=BOXA,port=1025 -s npipe:pipe=MyPipe 
```

Finally, start a debugging client on \\\\BOXC in the following manner:

```console
G:\Debugging Tools> windbg -remote npipe:server=BOXB,pipe=MyPipe,password=wrought 
```

Here is another example. Your symbols are at the remote location, 127.0.0.30. So you decide to use a process server on the computer where the target is, 127.0.0.10. You put a repeater at 127.0.0.20.

You also decide to use reverse connections. So you begin by starting the client on 127.0.0.30:

```console
G:\Debugging Tools> windbg -premote tcp:clicon=127.0.0.20,port=1033 notepad.exe 
```

Then start the repeater on 127.0.0.20:

```console
C:\Misc> dbengprx -c tcp:clicon=127.0.0.10,port=1025 -s tcp:port=1033,clicon=127.0.0.10 
```

And finally start the process server on 127.0.0.10:

```console
E:\Debugging Tools for Windows> dbgsrv -t tcp:port=1025,clicon=127.0.0.20 
```

For a more complicated example using repeaters, see [Two Firewalls](two-firewalls.md).

 

 





