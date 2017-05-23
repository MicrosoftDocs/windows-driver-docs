---
title: Repeater Examples
description: Repeater Examples
ms.assetid: 83aff647-65a7-409f-adce-254305395775
keywords: ["repeater, examples"]
ms.author: windowsdriverdev
ms.date: 05/23/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Repeater Examples


## <span id="ddk_repeater_examples_dbg"></span><span id="DDK_REPEATER_EXAMPLES_DBG"></span>


Let us suppose you have three computers, \\\\BOXA, \\\\BOXB, and \\\\BOXC, and you wish to use them as the server, the repeater, and the client, respectively.

You can start a debugging server on \\\\BOXA, using process 122 as the target, in the following manner:

```
E:\Debugging Tools for Windows> cdb -server tcp:port=1025,password=wrought -p 122 
```

Then you can start a repeater on \\\\BOXB as follows:

```
C:\Misc> dbengprx -c tcp:server=BOXA,port=1025 -s npipe:pipe=MyPipe 
```

Finally, start a debugging client on \\\\BOXC in the following manner:

```
G:\Debugging Tools> windbg -remote npipe:server=BOXB,pipe=MyPipe,password=wrought 
```

Here is another example. Your symbols are at the remote location, 127.0.0.30. So you decide to use a process server on the computer where the target is, 127.0.0.10. You put a repeater at 127.0.0.20.

You also decide to use reverse connections. So you begin by starting the client on 127.0.0.30:

```
G:\Debugging Tools> windbg -premote tcp:clicon=127.0.0.20,port=1033 notepad.exe 
```

Then start the repeater on 127.0.0.20:

```
C:\Misc> dbengprx -c tcp:clicon=127.0.0.10,port=1025 -s tcp:port=1033,clicon=127.0.0.10 
```

And finally start the process server on 127.0.0.10:

```
E:\Debugging Tools for Windows> dbgsrv -t tcp:port=1025,clicon=127.0.0.20 
```

For a more complicated example using repeaters, see [Two Firewalls](two-firewalls.md).

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[debugger\debugger]:%20Repeater%20Examples%20%20RELEASE:%20%285/15/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




