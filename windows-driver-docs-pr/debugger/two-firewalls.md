---
title: Two Firewalls
description: Two Firewalls
ms.assetid: e6192cf8-02a4-4dbe-8ed7-a64f8efc24f6
keywords: ["remote debugging, two firewalls", "firewalls and remote debugging"]
ms.author: domars
ms.date: 05/23/2017
ms.localizationpriority: medium
---

# Two Firewalls


## <span id="ddk_two_firewalls_dbg"></span><span id="DDK_TWO_FIREWALLS_DBG"></span>


In this scenario, you need to perform kernel debugging on a computer in Building A. Your technician is located in Building C, and he or she has access to symbols there. However, both buildings have firewalls that will not allow incoming connections.

You need to set up a repeater at a neutral site -- say, Building B. Then you can connect A outward to B, and connect C outward to B.

There will be four computers involved in this scenario:

-   The target computer, located in Building A.

-   The local host computer, located in Building A. This computer will run a KD connection server. It will be connected to the target computer by a debug cable or 1394 cable, and will connect outward to the repeater. Let this computer's IP address be 127.0.10.10.

-   The computer in Building B. This will run the repeater. Let its IP address be 127.0.20.20.

-   The computer in Building C where the technician is located. This computer will run WinDbg as a smart client. Let its IP address be 127.0.30.30.

First, make sure the target computer is configured for debugging and is attached to the local host computer. In this example, a 1394 cable is used.

Second, start the repeater on 127.0.20.20:

```console
dbengprx -p -s tcp:port=9001 -c tcp:port=9000,clicon=127.0.10.10 
```

Third, start the KD connection server on 127.0.10.10 in Building A as follows:

```console
kdsrv -t tcp:port=9000,clicon=127.0.20.20,password=longjump 
```

Finally, start the smart client on 127.0.30.30 in Building C. (This can actually be done before or after starting the server in Building A.)

```console
windbg -k kdsrv:server=@{tcp:server=127.0.20.20,port=9001,password=longjump},trans=@{1394:channel=9} -y SymbolPath
```

### <span id="five_computer_scenario"></span><span id="FIVE_COMPUTER_SCENARIO"></span>Five-Computer Scenario

This scenario can be made even more complicated if you suppose that the symbols are on one computer in Building C, but the technician is at a different computer.

Suppose that 127.0.30.30 has the symbols, as before, and that its local name is \\\\BOXC. The smart client can be started with the same command as above but with an additional **-server** parameter. Since no one will be using this machine, it will take less processing time if you use KD instead of WinDbg:

```console
kd -server npipe:pipe=randomname -k kdsrv:server=@{tcp:server=127.0.20.20,port=9001,password=longjump},trans=@{1394:channel=9} -y SymbolPath
```

Then the technician, elsewhere in the building, can start a debugging client as follows:

```console
windbg -remote npipe:server=\\BOXC,pipe=randomname 
```

Notice that the password must be supplied by the first non-repeater in the chain (the smart client on \\\\BOXC), not by the final debugger in the chain.

 

 





