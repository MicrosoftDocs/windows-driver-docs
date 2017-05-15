---
title: Symbols in the Middle
description: Symbols in the Middle
ms.assetid: 0fbf47fc-1216-4eaa-b4b9-96e206194b54
keywords: ["remote debugging, symbols on third machine"]
---

# Symbols in the Middle


## <span id="ddk_symbols_in_the_middle_dbg"></span><span id="DDK_SYMBOLS_IN_THE_MIDDLE_DBG"></span>


In this scenario, you have three computers. The first has the target application, the second has the symbols, and the third has the technician.

Since the smart client behaves like a regular debugger in every way, it can be used as a debugging server at the same time. This allows you to link three machines together with the smart client in the middle.

First, you start a process server on the computer \\\\BOXA:

```
dbgsrv -t npipe:pipe=FarPipe 
```

The middle machine, named \\\\BOXB, starts the debugger with both the **-premote** and **-server** parameters. Suppose the PID of the target application is 400 and the symbol path is G:\\MySymbols:

```
cdb -server npipe:pipe=NearPipe -premote npipe:server=BOXA,pipe=FarPipe -v -y g:\mysymbols -p 400 
```

Then a debugging client on a third machine can be started as follows:

```
windbg -remote npipe:server=BOXB,pipe=NearPipe 
```

The third machine is then used to control the debugging, while the second machine is where the actual processing is done and the symbols are accessed.

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[debugger\debugger]:%20Symbols%20in%20the%20Middle%20%20RELEASE:%20%285/15/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




