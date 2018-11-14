---
title: Symbols in the Middle
description: Symbols in the Middle
ms.assetid: 0fbf47fc-1216-4eaa-b4b9-96e206194b54
keywords: ["remote debugging, symbols on third machine"]
ms.author: domars
ms.date: 05/23/2017
ms.localizationpriority: medium
---

# Symbols in the Middle


## <span id="ddk_symbols_in_the_middle_dbg"></span><span id="DDK_SYMBOLS_IN_THE_MIDDLE_DBG"></span>


In this scenario, you have three computers. The first has the target application, the second has the symbols, and the third has the technician.

Since the smart client behaves like a regular debugger in every way, it can be used as a debugging server at the same time. This allows you to link three machines together with the smart client in the middle.

First, you start a process server on the computer \\\\BOXA:

```console
dbgsrv -t npipe:pipe=FarPipe 
```

The middle machine, named \\\\BOXB, starts the debugger with both the **-premote** and **-server** parameters. Suppose the PID of the target application is 400 and the symbol path is G:\\MySymbols:

```console
cdb -server npipe:pipe=NearPipe -premote npipe:server=BOXA,pipe=FarPipe -v -y g:\mysymbols -p 400 
```

Then a debugging client on a third machine can be started as follows:

```console
windbg -remote npipe:server=BOXB,pipe=NearPipe 
```

The third machine is then used to control the debugging, while the second machine is where the actual processing is done and the symbols are accessed.

 

 





